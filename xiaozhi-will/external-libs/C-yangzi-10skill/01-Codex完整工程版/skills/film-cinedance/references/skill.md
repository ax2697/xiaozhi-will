# references

film-cinedance（08 CINEDANCE 视频提示词）的参考文档目录。

## 本目录文件

- **source.md**（38KB）：CINEDANCE V5 Seedance 2.0 提示词适配器。内部 4-D 智能体方法论（拆解 / 诊断 / 开发 / 交付）、镜头规划门、连续性编译、参考一致性、起幅画面、角色站位调度、视线与身体朝向、轴线、光学镜头物理、对白时间轴、无语境泄露等；最终 Seedance 提示词必须使用清晰电影级纯中文。
- **continuity-compiler.md**（4KB）：跨镜头连续性编译器。定义连续性状态表（`05_shots/<场次ID>-continuity-ledger-vNN.md`）须记录的字段；最终提示词禁止"上一镜头 / 刚才 / 继续 / 同上 / 照旧 / 保持原样"等指代；世界位置与画面位置分离；三种连续模式（纯文字 / Lira 资产 / 首尾帧）；对白跨切（Dxxx-A/B 分段）与连续性校验。
- **h3-prompt-format.md**（4KB）：MiniMax H3 提示词适配器。按用户实际参考自动选择模式（T2VA / I2VA / FL2VA / L2VA / Ref2VA）；小白默认中文直投；进阶可选官方结构兼容（integrated_multimodal_description / overall_soundscape / non_diegetic_music 三段或 Ref2VA 六段英文字段）；与 Seedance 隔离、双版本不混写。
- **shot-planning.md**（4KB）：场景拆镜与时长规划。两次计时（场次初估 / 镜头终估）；时长计算方法（顺序相加、同时取长、3-10 秒节奏建议）；中文对白安全预算（每秒约 2.5-3.2 个有效汉字，5 秒约 10-14 字等）；专业覆盖设计（主镜头 / 正反打 / 反应 / 插入等）；镜头清单字段；输出后停止等待用户确认。
- **_索引.md**：本目录索引，列出以上四个文件。
