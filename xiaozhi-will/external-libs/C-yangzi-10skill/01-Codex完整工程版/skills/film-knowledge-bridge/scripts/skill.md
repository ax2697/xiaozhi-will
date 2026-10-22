# scripts

film-knowledge-bridge（本地知识库外挂）的脚本目录：知识库配置、阶段参考检索与增量索引。

## 本目录文件

- **configure_knowledge_base.py**（4KB）：配置脚本。接收知识库根目录或 curated-screenplay-methods.sqlite 文件，自动查找 `99-索引与检索规则` 下的数据库与 CSV 目录，校验 SQLite 完整性并统计文档数/片段数，写出 knowledge-base.json。
- **configure_knowledge_base.ps1**（535B）：Windows 包装脚本，优先用 Codex 自带 Python 执行 configure_knowledge_base.py。
- **configure_knowledge_base.command**（130B）：macOS/Linux 快捷脚本，调用 `python3 configure_knowledge_base.py`。
- **retrieve_stage_sources.py**（18KB）：阶段参考检索脚本。读取知识库配置与阶段检索画像（profile.json），对 SQLite 执行 FTS5 + trigram 中文全文检索（不支持时自动走兼容检索）；第一轮给 3-5 部候选，用户确认后按 selected_documents 定向精读，输出带路径/页码/片段证据的知识卡。
- **retrieve_stage_sources.ps1**（433B）：Windows 包装脚本，转发参数到 retrieve_stage_sources.py。
- **update_knowledge_index.py**（18KB）：增量索引脚本。扫描知识库根目录下新增/修改的 PDF/TXT/MD/DOCX，跳过 99-索引与检索规则、90-隔离与待审、待精筛等目录；支持 PDF 文本提取与 DOCX 解析，更新 SQLite 索引并输出新增/更新/未变化/失败/OCR 报告。
- **update_knowledge_index.ps1**（942B）：Windows 包装脚本，支持 Root/Config/Database/IncludeIsolated/DryRun 参数并转发到 update_knowledge_index.py。
- **update_knowledge_index.command**（132B）：macOS/Linux 快捷脚本，调用 update_knowledge_index.py。
- **_索引.md**：本目录索引，列出以上脚本。
