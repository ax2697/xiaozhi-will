# 本地知识库外挂

通用版的可选本地知识桥：从本地剧本/编剧方法书库检索可追溯参考，默认关闭、只有用户主动调用才启用。

## 本目录文件

- **00-系统指令-本地知识库外挂.txt**（4KB）：知识桥系统指令。只读取用户本轮指定的项目资料、默认不提示不检索；知识库B 第一轮匹配 3-5 部候选，用户确认 1-3 部后定向精读；每条命中必须显示真实路径/页码/命中词；组合参考必须分工、禁止拼接剧情；知识卡确认后才交给创作模块。
- **01-中文口令.txt**（2KB）：知识桥中文口令示例（调用 / 知识库A/B/C / 确认后定向精读 / 只查方法书 / ACTING / Lira / CINEDANCE 可选增强 / 查看与修改项目参考）。
- **AGENTS.md**（5KB）：知识库外挂 AGENTS 规则。配置方式（Windows 运行 tools/configure_knowledge_base.ps1，macOS/Linux 运行 python3 tools/configure_knowledge_base.py）；两轮检索流程（候选 → 精读，retrieve_stage_sources.py）；精度规则（参考剧本优先 05/06/07 目录，方法书优先 08）；与项目参考记忆的衔接；增量索引与"整理新剧本并更新知识库"口令边界。
- **knowledge-base.json**（308B）：知识库配置文件（占位模板，root/database 等字段待首次配置时自动写入）。
- **新剧本自动整理规则.md**（4KB）：新剧本自动整理流程（与 Codex 版 film-knowledge-bridge/references/inbox-workflow.md 同源）。触发词、只整理"新加入待分类"、安全解压去重分类、待人工确认隔离、运行增量索引并报告。
- **_索引.md**：本目录索引。

## 子目录

- **tools**：知识库工具脚本（configure / retrieve / update 三套 PowerShell / Python / Shell 脚本）。
