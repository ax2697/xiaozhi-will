# references

ai-film-router（项目路由总控）的参考文档目录：本地知识库精准调用、作者剧本接管规则与项目规则模板。

## 本目录文件

- **knowledge-base-template.json**（182B）：知识库配置模板，含 name、database（占位）、catalog（占位）、enabled 字段，首次配置后写入本机真实路径。
- **local-knowledge.md**（4KB）：本地知识库精准调用规则。规定配置查找顺序（项目 00_project/knowledge-base.json → 环境变量 AI_FILM_KNOWLEDGE_CONFIG → Skill 内 knowledge-base.json）、阶段检索命令与参数（query_local_knowledge.ps1，每阶段 2-4 次检索、单次最多 6 条、总引用不超 12 条）、9 个知识库分类选择、阶段隔离（每阶段只读自己的知识卡）、用户主动调用后 01-08 各阶段检索重点。
- **screenplay-intake.md**（3KB）：已有作者剧本接管规则。第一轮只生成检查报告（00_project/screenplay-intake-report.md）并询问是否保持原文；第二轮用户确认后才生成 02_script/production-breakdown-vNN.md，补角色与状态表、场次制片表、场次时长初估、资产需求表、信息缺口等生产资料；不改作者剧本正文。
- **_索引.md**：本目录索引。

## 子目录

- **project-rules**：V3 项目规则模板（AGENTS.md、routing.md、reference-memory.md），供"升级当前电影工程到新版规则"时覆盖项目控制文件。
