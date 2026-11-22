# test1

#### \# Python课程实验作业1

本仓库包含两道Python实验考题代码以及对应的实验报告文档。



📁 文件说明

\- 考题1：销售数据清洗与统计

&#x20; - sales\_report.py：数据清洗主程序

&#x20; - sales\_raw.xlsx：原始销售数据

&#x20; - report.xlsx：清洗后输出报表

\- 考题2：FastAPI记账接口开发

&#x20; - main.py：接口服务主代码

&#x20; - test\_api.py：接口测试代码

\- test-python\_vibe\_coding(1).docx、test-python\_vibe\_coding(2).docx：两道题完整实验报告



📌 环境依赖

pip install pandas openpyxl fastapi uvicorn httpx



▶️ 运行方式

考题 1

运行：python sales\_report.py

功能：读取 Excel 原始数据，完成数据清洗，生成统计报表。

考题 2

启动接口服务：uvicorn main:app --reload

访问接口文档：http://127.0.0.1:8000/docs

运行测试用例：pytest test\_api.py -v



📖 考察知识点

考题 1：pandas 库读取、清洗 Excel 数据；缺失值、异常数据处理；多工作表写入；数据分组统计。

考题 2：FastAPI 框架搭建 Web 接口；GET/POST 请求；接口自动文档；pytest 单元测试；本地服务启动调试。



🧠 解题思路

考题 1：先读取原始 Excel 数据，检查脏数据，完成清洗；再按需求分组汇总统计，最后新建多个工作表保存结果文件。

考题 2：先设计记账记录的数据结构，编写新增、查询、汇总接口；借助自带的 swagger 文档测试接口；编写 pytest 代码自动化验证接口功能。



❗ 遇到的难题与解决方法

Excel 列宽异常、日期格式错乱：在代码里增加格式处理逻辑，或者生成后手动调整表格列宽。

FastAPI 文档页面白屏：是 CDN 加载问题，替换为国内源，改用/redoc地址访问文档。

运行 pytest 提示缺少 httpx：使用 pip 命令安装对应依赖包后再执行测试。

GitHub 文档无法在线预览：GitHub 限制 docx 预览，只能下载到本地用 WPS/Word 打开查看。

💡 心得体会

这次实验让我熟悉了 Python 数据处理和 Web 接口开发两个方向。写代码的时候经常遇到各种报错，一开始不知道从哪里下手，慢慢学会看报错信息、定位问题。同时也学会了用 GitHub 管理代码，懂得整理项目文件。我意识到写程序不只是写出能运行的代码，还要做好注释、整理文档，方便别人看懂。后续我会继续练习调试能力，巩固 Python 和接口开发相关知识。

