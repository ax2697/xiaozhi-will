# project-rules

ai-film-router 内置的 V3 项目规则模板：升级旧电影工程时用来覆盖项目控制文件的规则源。

## 本目录文件

- **AGENTS.md**（5KB）：AI 影视项目弹性总控（与 project-template/AGENTS.md 同源）。入口 A/B/C/D 只问一次、一次一个 Skill、08 两步（镜头规划门→提示词）、每条提示词独立写全连续性、知识桥默认未调用、跨阶段参考记忆规则、01 与 05 强制检查。
- **routing.md**（2KB）：当前路由模板（与 project-template/00_project/routing.md 同源）。运行模式、项目入口、当前阶段、知识桥状态、A/B/C/D 可选入口与路由原则。
- **reference-memory.md**（3KB）：本地知识库跨阶段参考记忆模板（与 project-template/00_project/reference-memory.md 同源）。权威顺序、使用规则、参考方法编号、使用范围、已确认参考条目字段、变更记录与阶段应用记录。
- **_索引.md**：本目录索引，列出以上三个文件。
