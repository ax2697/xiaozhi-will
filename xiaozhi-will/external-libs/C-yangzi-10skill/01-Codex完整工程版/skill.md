# 01-Codex完整工程版

Codex 专用工程安装包：由 Codex 自动安装 10 个电影 Skill、项目模板与维护脚本，学员无需手工解压复制。

## 本目录文件

- **AGENTS.md**（7KB）：课程包安装总控。规定用户说"安装课程包 / 配置本地知识库 / 更新本地知识库 / 整理新剧本并更新知识库 / 新建电影项目 / 升级已有电影工程规则"时分别执行哪些脚本与流程；Windows 执行 .ps1、macOS/Linux 执行 python3 install_course.py；强调知识桥默认未调用、原 9 个 Skill 照常工作、安装只更新全局 Skill 不碰项目创作文件。
- **_索引.md**：本目录索引，列出 project-template、scripts、skills 三个子目录与 AGENTS.md。

## 子目录

- **project-template**：AI 影视项目弹性总控模板（00_inbox 至 08_delivery 十个阶段目录 + AGENTS.md）。
- **scripts**：安装课程包、新建项目、配置/更新知识库、升级旧项目等 PowerShell / Python / Shell 脚本。
- **skills**：10 个 Skill 安装源（ai-film-router 路由 + film-synopsis / film-characters / film-worldbuilding / film-treatment / film-screenplay / film-lira-assets / film-acting / film-cinedance 九个创作 Skill + film-knowledge-bridge 知识桥）。
