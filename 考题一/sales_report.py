import pandas as pd
import os
from openpyxl import load_workbook
from openpyxl.utils.dataframe import dataframe_to_rows

input_file = "sales_raw.xlsx"
output_file = "report.xlsx"

# 判断原始文件是否存在
if not os.path.exists(input_file):
    print(f"【错误】未找到原始文件：{input_file}")
    exit()

try:
    df = pd.read_excel(input_file)
except Exception as err:
    print(f"【错误】读取文件失败：{err}")
    exit()

# 定义关键字段
key_columns = ["日期", "销售员", "产品", "数量", "单价", "地区"]

# 1. 删除关键字段缺失的行
df = df.dropna(subset=key_columns)
# 2. 剔除数量 <= 0 的异常行
df = df[df["数量"] > 0]
# 3. 全字段去重
df = df.drop_duplicates()

# 清洗后无有效数据提示
if df.empty:
    print("【提示】清洗完成后没有有效销售数据！")
    exit()

# 计算销售额：销售额 = 数量 × 单价
df["销售额"] = df["数量"] * df["单价"]
# 日期只保留年月日
df["日期"] = pd.to_datetime(df["日期"]).dt.date

# 各个统计工作表
df_clean_detail = df.copy()
df_by_salesman = df.groupby("销售员")["销售额"].sum().reset_index()
df_by_area = df.groupby("地区")["销售额"].sum().reset_index()
month_total = df["销售额"].sum()
df_overview = pd.DataFrame([["月度销售总额", month_total]], columns=["项目", "金额"])

# 先写入文件
with pd.ExcelWriter(output_file, engine="openpyxl") as writer:
    df_clean_detail.to_excel(writer, sheet_name="明细清洗后", index=False)
    df_by_salesman.to_excel(writer, sheet_name="按销售员", index=False)
    df_by_area.to_excel(writer, sheet_name="按地区", index=False)
    df_overview.to_excel(writer, sheet_name="总览", index=False)

# 自动调整所有工作表列宽
wb = load_workbook(output_file)
for sheet_name in wb.sheetnames:
    ws = wb[sheet_name]
    for column in ws.columns:
        max_len = 0
        col = column[0].column_letter
        for cell in column:
            try:
                if len(str(cell.value)) > max_len:
                    max_len = len(str(cell.value))
            except:
                pass
        ws.column_dimensions[col].width = max_len + 2
wb.save(output_file)

print(f"✅ 报表生成成功，输出文件：{output_file}")
print(f"📊 月度销售总额：{month_total:.2f}")