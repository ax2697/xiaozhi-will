# scripts

ai-film-router 的脚本目录：本地知识库查询与旧电影工程升级。

## 本目录文件

- **query_local_knowledge.ps1**（431B）：包装脚本，优先调用 Codex 自带 Python（`~/.cache/codex-runtimes/.../python.exe`）执行 query_local_knowledge.py，不存在时回退系统 python。
- **query_local_knowledge.py**（4KB）：本地知识库查询脚本。按项目/环境变量/Skill 顺序读取 knowledge-base.json，对 SQLite 执行 FTS5 + bm25 全文检索（支持 AND/OR 匹配、path-contains 过滤、limit 限制），把结果写成阶段知识卡（含页码、路径、检索片段、可迁移结论），并向 stdout 输出 JSON。
- **升级当前电影工程规则.ps1**（3KB）：ai-film-router 自带的旧项目升级能力。备份项目 AGENTS.md 与 00_project/routing.md 到 `rule-backup-*`，用 project-rules 模板覆盖，缺 00_project/reference-memory.md 时新增空白模板，写 rule-upgrade-log.md；不修改任何创作成果。
- **_索引.md**：本目录索引，列出以上脚本。
