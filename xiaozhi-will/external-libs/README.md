# external-libs/ 外部四库原文（深挖层，按需取用）

`references/09A–09E`、`17`、`18` 是**要点与路由**（先读它，够用就不必往下翻）；本目录放的是**原库原文**（要细则、要完整规则条文时再进）。

> **边界（仲裁⑦）**：原库一律"只补方法、不覆盖参数"。它们的默认值（竖屏 9:16 / R2 商业高燃 / 21:9 / Higgsfield 模型 / Seedance 2.0）**不得覆盖本剧锁定值**（`【画幅】` / `【出图模型】` / `【视频模型】` / `【帧率】` / `【风格】`）。原库也**不提供剧情**——剧情唯一来源是剧情源（第十章）。

## A 库 · short-drama-director（已自带 ✅）

路径：`A-short-drama-director/`，36 个文件 / 303 KB，含 `README.md`（索引）、`references/`（28 份规则库）、`seedance-fight-sequence/`（打戏子库，含自检脚本）、`scripts/build_board_lite.py`。

**怎么用**：按 `references/09A-domestic-gate-lib.md` 的 **9.2 表** → "查 references\ 哪份"列给出的**文件名** → 到 `A-short-drama-director/references/<文件名>.md` 打开。常用几份：

| 你要解决什么 | 打开 |
|---|---|
| 资产 16 项锁定 / 分批出图 | `asset-spatial-ledger.md` |
| 空间顶视图 / CAM1~4 / 180°轴线 | `spatial-topview-camera.md` |
| P4 投喂六步细则（★权威） | `★ prompt-feeding-checklist.md` |
| 台词语速（3.5~5 字/s、单句>24 字拆镜） | `dialogue-speed-check.md` |
| 台词诊断七维 / 文戏微表情 | `dialogue-doctor-7d.md`、`wenxi-micro-expression.md`、`★ facs-micro-expression.md` |
| 镜头规格 15 条 / 转场六式 | `camera-specs-15rules.md`、`camera-transitions-6types.md` |
| 真实光线防棚拍假 | `lighting-and-antifake.md` |
| 打戏 15 格 / 玄幻 / 武学库 | `action-previs-15grid.md`、`xuanhuan-magic-combat.md`、`martial-arts-*.md` |
| 打戏专项（首帧/时长/安全口径/自检） | `seedance-fight-sequence/`（脚本 `scripts/check_fight_prompt.py`） |

## B 库 · 国外三库 LIRA / CINEDANCE / ACTING（已自带 ✅ 中文全本）

路径：`B-overseas-three-libs/`

| 文件 | 对应要点 | 什么时候翻原文 |
|---|---|---|
| `LIRA-SKILL-图像提示词优化.md`（29.7KB） | 09B 的 LIRA 段 | 写出图/改图提示词，要完整的模型路由、10 反失败、模板与 pre-send 清单 |
| `CINEDANCE-HIGGSFIELD-提示词导演系统.md`（32.2KB） | 09B 的 CINEDANCE 段 | 写视频提示词，要 12 段架构逐段写法、六把锁、FOV°库、静默 QA 20 问原文 |
| `ACTING-SKILL-角色表演系统.md`（25.0KB） | 09B 的 ACTING 段 | 写表演层，要五支柱细则、Master Profile 写法、15 种坏表演图谱、0–5 量表 |

## C 库 · 洋子 10-Skill 完整工程 V3（✅ 已入包 · ⚠ 索引骨架版）

路径：`C-yangzi-10skill/`，91 个文件 / 100.8 KB。来源：`汇总文件\02_方法文档与提示词\_外部方法论库_10步`，原样复制未改动。

**先读这份**：`C-yangzi-10skill/00-先看这里.md`（11KB，V3 新增点 / 安装方式 / 知识桥开关规则 / 重要限制）。

```
C-yangzi-10skill\
├─ 00-先看这里.md          ← 全库说明书，第一次进先看它
├─ AGENTS.md / _索引.md / skill.md
├─ 01-Codex完整工程版\
│  ├─ AGENTS.md            ← 安装总控（6.6KB）：安装 / 配置知识库 / 升级旧工程 的中文口令
│  ├─ project-template\    00_inbox · 00_project · 01_story · 02_script · 03_assets ·
│  │                       04_performance · 05_shots(keyframes) · 06_prompts ·
│  │                       07_generations · 08_delivery   ← 九段目录映射（对应 09E）
│  ├─ scripts\             安装/升级/建项目/配知识库（.ps1 ×5 + .command ×3 + install_course.py）
│  └─ skills\              ai-film-router · film-synopsis · film-characters · film-worldbuilding ·
│                          film-treatment · film-screenplay · film-lira-assets · film-acting ·
│                          film-cinedance · film-knowledge-bridge   ← 10 个 Skill
└─ 02-千问豆包OpenCode通用版\  专业模块\ + 本地知识库外挂\(tools\)
```

| 你要解决什么 | 打开 |
|---|---|
| 工程目录怎么分、九段怎么落盘 | `01-Codex完整工程版/project-template/_索引.md` + 各段 `_索引.md` |
| 10 个 Skill 各自的职责边界 | `01-Codex完整工程版/skills/_索引.md`（1.2KB） |
| 单个 Skill 的参考文档清单 | `skills/<name>/references/skill.md` |
| 安装 / 升级 / 配知识库的口令 | `01-Codex完整工程版/AGENTS.md` |
| 知识桥（第 10 个能力）怎么用 | `00-先看这里.md` 的"知识桥如何出现"一节 |

**⚠ 两个必须知道的事实**

1. **这是索引骨架版，不是全文本。** 每个 Skill 的 `references/` 里只有 `_索引.md` + `skill.md` 两份**目录说明**，被它们描述的正文（例如 `film-cinedance/references/source.md` 38KB、`continuity-compiler.md`、`h3-prompt-format.md`、`shot-planning.md`）在本机不存在。已在同一父目录下全盘检索确认无 `source.md` / `continuity-compiler.md` / `h3-prompt-format.md`。
   → 需要细则时，**优先翻 B 库**（`CINEDANCE-HIGGSFIELD-提示词导演系统.md` 32.2KB 是同族 CINEDANCE 中文全本，实际覆盖度更高）；真要洋子 V3 正文，需从洋子原厂 V3 ZIP 取回 `source.md` 等文件，覆盖进对应 `references/` 目录即可，本索引无需改。
2. **包内 `scripts\` 含 5 个 `.ps1` / 3 个 `.command` 安装脚本**（会把 10 个 Skill 装进 Codex 的 `~/.codex/skills`，并写知识库路径）。本技能**不会执行**它们，仅作资料保留。**别在没读完之前运行**；要用请自己先过一遍脚本内容。

**没有完整正文也不影响主流程**——`references/09E-yangzi-10skill-engineering.md` 已内嵌八阶段映射、入口门禁 A/B/C/D、目录映射、08 两步门、工程纪律六条。C 库补的是"洋子那套工程组织与阶段门禁"的原始说法。

## D 库 · 漫剧老李 V7.4.26 多技能套装（✅ 完整原文 · 新增 v2.3.0）

路径：`D-laoli-suite/`，171 个文件。来源：`github.com/lixiaoxiao9888-create/manju-laoli-skill`（**MIT License**，版权声明已保留在 `D-laoli-suite/LICENSE`）。

**结构**：1 总控 + 12 子技能。**六阶归位见 `references/17-laoli-engines-map.md`**（说清每个引擎在哪一阶用）。

```
D-laoli-suite/
├─ short-drama-director/     总控（183KB SKILL.md）+ 41 份 references + style-bible（8 份）
├─ sd-recon-engine/          素材采风 · 对标情报卡             → 一阶 立鼎
├─ sd-script-engine/         剧本六阶段链（250KB 细则）        → 二阶 采药
├─ sd-jieshuo-engine/        解说叙事赛道（旁白稿）            → 二阶 采药
├─ sd-overseas-engine/       海外剧赛道（语言契约）            → 二阶 采药
├─ sd-asset-engine/          资产三包模板（125KB）             → 三阶 炼精
├─ sd-decision-engine/       ★ 分镜选型依据（E01~E15）         → 四阶 炼气
├─ sd-storyboard-engine/     分镜（机位系统 54KB + 镜头经济）  → 四阶 炼气
├─ sd-feed-engine/           投喂七段式 + 六道闸门             → 五阶 炼神
├─ sd-combat-engine/         打戏（铁律 69KB + 招式库 81KB）   → 五阶 炼神
├─ sd-xuanhuan-engine/       玄幻（兵器参数库 36KB）           → 五阶 炼神
├─ sd-real-engine/           写实武打（运动链 11 环）          → 五阶 炼神
└─ sd-qc-engine/             机检 C1~C33 / H1~H12（74KB）      → 六阶 还虚
```

**最值得先看的三份**

| 你要解决什么 | 打开 |
|---|---|
| 分镜选型没依据（这场戏该用什么镜头） | `sd-decision-engine/references/context-mapping.md`（E01~E15 + 80/15/5）；我们的精简版见 `references/18-decision-engine.md` |
| 机检到底查哪些项 | `sd-qc-engine/references/machine-check-manual.md`（74KB，C1~C33 / H1~H12 逐条） |
| 老李的六道前置锁 | `short-drama-director/SKILL.md` 〇节（赛道 / 来源 / 模型 / 画幅 / 交付 / 段缝） |

**⚠ 三条使用边界**

1. **原包未做任何修改**。我们的道教化归类写在 `references/17` 与 `18`，不侵入 D 库原文。MIT 允许修改，但保留原文更便于日后与上游同步。
2. **术语冲突时用我们的**：老李用「图N」编号，我们用 `@CHR/@SCN/@PRP`（见 `references/14-anchor-coding.md`）。
3. **老李的默认值同样不得覆盖本剧锁定值**（仲裁⑦）。他默认 9:16 / Seedance 2.5，本剧以参数卡为准。

## 体积与来源

- 本目录合计约 492 KB（A 303 + B 87 + C 101），绝大多数是 Markdown/纯文本。
  - A 库含 2 个 Python 脚本（`build_board_lite.py`、`check_fight_prompt.py`），只做本地文本检查，不联网、不删改文件。
  - C 库含 5 个 `.ps1` / 3 个 `.command` / 1 个 `.py` 安装脚本（Codex 课程包安装用）。**本技能不会执行它们**，仅作资料保留，需要时请自行审阅后再决定是否运行。
- 来源：A、B 库来自本机已安装技能 `xiao-zhi-aoyi` 内的 `references/modules/short-drama-director` 与 `references/modules/legacy-methodology` 副本；C 库来自你提供的 `汇总文件\02_方法文档与提示词\_外部方法论库_10步`。三库均**原样复制未改动**。版本若与你的原库有差异，以你手上的原库为准，覆盖本目录同名文件即可。
