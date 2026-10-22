# scripts

Codex 工程版安装与维护脚本集：安装课程包、新建项目、配置/更新本地知识库、升级旧电影工程规则。

## 本目录文件

- **install_course.py**（4KB）：跨平台安装脚本（macOS/Linux 用）。校验 10 个 Skill 的 SKILL.md 是否齐全，将 skills/ 复制到 `~/.codex/skills`；发现同名旧 Skill 先移动到带时间戳的 `skills-backup-*` 备份目录；保留原有知识库配置（knowledge-base.json）；安装后校验并输出安装位置、备份与知识库配置结果。
- **安装课程包.ps1**（3KB）：Windows 版安装脚本，逻辑与 install_course.py 一致：校验、备份冲突 Skill、复制 10 个 Skill、保留知识库配置、安装后校验。
- **安装课程包.command**（120B）：macOS 快捷脚本，调用 `python3 install_course.py`。
- **新建AI影视项目.ps1**（1KB）：复制 project-template 生成新电影项目，默认放在"文档\AI STUDIO洋子AI电影工作流\电影项目\项目标题"；把项目名称写入 project-status.md 与 brief.md；同名项目已存在时报错拒绝覆盖。
- **配置本地知识库.ps1**（756B）：转发用户选择的知识库根目录，调用已安装或包内的 configure_knowledge_base.ps1 完成知识库配置。
- **配置本地知识库.command**（555B）：macOS 快捷脚本，优先调用已安装的 configure_knowledge_base.py，否则用包内版本。
- **更新本地知识库.ps1**（668B）：转发 Root/Config/Database/IncludeIsolated/DryRun 参数，调用 film-knowledge-bridge 的 update_knowledge_index.ps1 执行增量索引。
- **更新本地知识库.command**（178B）：macOS 快捷脚本，调用 film-knowledge-bridge 的 update_knowledge_index.command。
- **升级旧电影工程规则.ps1**（4KB）：把旧电影项目升级到 V3 规则。校验项目存在 00_project，备份旧 AGENTS.md / routing.md / project-status.md 到 `rule-backup-*`，补齐 V3 状态字段、新增 05_shots\keyframes 目录，写 rule-upgrade-log.md；明确不修改任何创作成果。
- **_索引.md**：本目录索引，列出以上脚本。
