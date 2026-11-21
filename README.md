# test1

\# Python综合实验1

本次项目包含两个考题：Excel销售数据清洗统计、FastAPI记账接口开发。



\## 项目内容

1\. 考题一：基于pandas实现销售原始数据清洗，自动生成多工作表统计Excel报表，处理脏数据、规范日期格式，自动调整列宽。

2\. 考题二：使用FastAPI开发简易记账后端接口，实现记账记录新增、查询、统计摘要，修复Swagger文档CDN问题，搭配pytest完成接口单元测试。



\## 环境依赖

\- Python 3.x

\- pandas

\- fastapi

\- uvicorn

\- httpx

\- openpyxl



\## 文件说明

\- sales\_report.py：考题一数据清洗代码

\- main.py：考题二FastAPI记账接口代码

\- test\_api.py：接口pytest测试脚本

\- sales\_raw.xlsx：原始销售数据

\- report.xlsx：清洗后输出报表

\- \*.docx：实验报告文档



\## 运行方式

\### 考题一（数据清洗）

终端运行：python sales\_report.py

运行后自动生成清洗统计后的 Excel 文件。



\###考题二（FastAPI 接口）

终端运行：uvicorn main:app --reload

启动后访问：

http://127.0.0.1:8000/docs

http://127.0.0.1:8000/redoc

接口测试：pytest test\_api.py -v



实验心得体会

通过本次实验，我练习了 Python 数据分析与 Web 接口开发。一开始安装依赖时遇到metadata-generation-failed报错，反复调试才找到使用预编译包的解决办法；FastAPI 文档白屏的问题，也让我了解到 Swagger 静态资源 CDN 的坑。

在处理 Excel 时，熟悉了 pandas 数据清洗、空值处理、格式转换；写接口和单元测试时，理解了后端接口的编写、调试思路。

同时学习了 Git 与 GitHub Desktop 的使用，学会把代码、实验文档统一托管到仓库，养成版本管理的习惯。过程中踩了很多小 bug，也意识到写代码要仔细核对文件路径、区分不同考题的代码，不要混淆。整体收获很大，对 Python 工程化开发有了更直观的认识。

