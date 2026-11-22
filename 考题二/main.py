from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3
from datetime import date
from fastapi.openapi.docs import get_swagger_ui_html

app = FastAPI(title="简易记账接口", docs_url=None)

@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url="/openapi.json",
        title=app.title + " - Swagger UI",
        swagger_js_url="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui-bundle.js",
        swagger_css_url="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui.css",
    )

DB_NAME = "account.db"

# 初始化数据库表
def init_db():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS records (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        amount REAL NOT NULL,
        rtype TEXT NOT NULL,
        category TEXT NOT NULL,
        record_date TEXT NOT NULL
    )
    ''')
    conn.commit()
    conn.close()

init_db()

# 数据模型校验
class RecordIn(BaseModel):
    amount: float
    rtype: str
    category: str
    record_date: str

@app.post("/records")
def add_record(rec: RecordIn):
    if rec.amount <= 0:
        raise HTTPException(status_code=400, detail="金额必须大于0")
    if rec.rtype not in ["收入", "支出"]:
        raise HTTPException(status_code=400, detail="类型只能是【收入/支出】")
    try:
        date.fromisoformat(rec.record_date)
    except:
        raise HTTPException(status_code=400, detail="日期格式错误，请使用 yyyy-MM-dd")

    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO records(amount, rtype, category, record_date) VALUES (?,?,?,?)",
        (rec.amount, rec.rtype, rec.category, rec.record_date)
    )
    conn.commit()
    rid = cur.lastrowid
    conn.close()
    return {"id": rid, "msg": "添加成功"}

@app.get("/records")
def get_records(rtype=None, category=None, start_date=None, end_date=None, page:int=1, page_size:int=10):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    sql = "SELECT * FROM records WHERE 1=1"
    params = []
    if rtype:
        sql += " AND rtype=?"
        params.append(rtype)
    if category:
        sql += " AND category=?"
        params.append(category)
    if start_date:
        sql += " AND record_date >= ?"
        params.append(start_date)
    if end_date:
        sql += " AND record_date <= ?"
        params.append(end_date)
    offset = (page - 1) * page_size
    sql += " LIMIT ? OFFSET ?"
    params.extend([page_size, offset])
    rows = cur.execute(sql, params).fetchall()
    conn.close()
    res = []
    for r in rows:
        res.append({
            "id": r[0],
            "amount": r[1],
            "rtype": r[2],
            "category": r[3],
            "record_date": r[4]
        })
    return {"data": res, "page": page, "page_size": page_size}

@app.get("/summary")
def summary(start_date:str, end_date:str):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    income = cur.execute("SELECT SUM(amount) FROM records WHERE rtype='收入' AND record_date BETWEEN ? AND ?", (start_date, end_date)).fetchone()[0] or 0
    expend = cur.execute("SELECT SUM(amount) FROM records WHERE rtype='支出' AND record_date BETWEEN ? AND ?", (start_date, end_date)).fetchone()[0] or 0
    conn.close()
    balance = income - expend
    return {"收入合计": income, "支出合计": expend, "结余": balance}