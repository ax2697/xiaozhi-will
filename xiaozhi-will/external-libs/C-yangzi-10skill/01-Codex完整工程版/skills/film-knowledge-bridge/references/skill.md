# references

film-knowledge-bridge（本地知识库外挂）的参考文档目录。

## 本目录文件

- **inbox-workflow.md**（4KB）：新剧本自动整理流程（触发词"整理新剧本并更新知识库"）。只整理知识库根目录下 `90-隔离与待审/新加入待分类` 入口的文件；支持 PDF/DOCX/TXT/MD，ZIP/RAR/7Z 先安全检查再解压（拒绝可执行文件）；按文件哈希去重、按内容分类到 01-08 目录、无法判断的留"待人工确认"；最后运行增量索引并在聊天中报告分类/重复/待确认/OCR 等结果。
- **knowledge-base-template.json**（286B）：知识库配置模板，含 name、root（占位）、database（占位）、catalog、festival_catalog、indexed_documents、indexed_chunks、generated_at 字段。
- **profile-example.json**（1010B）：阶段检索画像示例（05-screenplay 阶段）。含 stage、selected_documents、deep_read_selected、problem、queries（"参考剧本候选"与"编剧方法候选"三组检索词，含 path_contains、mode、weight）、lane_limits（每通道最多 5 条）。
- **_索引.md**：本目录索引，列出以上三个文件。
