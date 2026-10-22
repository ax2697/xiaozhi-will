# 给别人用：安装与前置条件（DISTRIBUTE.md）

> 这份说明是给**拿到本技能包的人**看的。技能本体自包含，但要真正跑起来，还需要三件事：装对位置、建项目文件、替换占位符。

## 一、安装（1 步）

把 `xiaozhi-will` **整个文件夹**复制到技能目录：

| 系统 | 路径 |
|---|---|
| Windows | `C:\Users\<你的用户名>\.workbuddy\skills\xiaozhi-will\` |
| macOS / Linux | `~/.workbuddy/skills/xiaozhi-will/` |

复制后不需要重启、不需要配置；在对话里说「按路由卡执行」「这条指令该读哪些文件」「第 N 集开工」「新剧立项」即可触发。

目录内结构（不要拆散、不要改名）：

```
xiaozhi-will/
├─ SKILL.md                 主入口：六步流程 / 路由总表 / 仲裁 / 自检 / 加载表
├─ DISTRIBUTE.md            本文件：安装与前置条件
├─ references/              第八章~第十一章原文转写（要点层）+ 索引 + 原版 HTML 备份
├─ external-libs/           A 库 short-drama-director（28 份规则库）+ B 库三库中文全本
│                           + C 库 洋子 10-Skill 工程（索引骨架版）+ 三库索引 README
├─ templates/               8 份空白项目模板（总索引/三资产包/分镜/机位图/SOP/剧本核对表）
└─ scripts/
   ├─ new_project_scaffold.py   建目录骨架（只新建目录，绝不删除或覆盖）
   └─ init_project_docs.py      复制模板到项目 + 批量替换占位符（默认不覆盖已有文件）
```

## 二、必须自带的项目文件（技能包里没有，也**不该**有）

本技能是**路由卡**：它规定"每条指令去读哪个文件的哪一节"，真正的执行事实源在你自己的项目磁盘。开工前至少要有：

| # | 文件 | 落盘位置 |
|---|---|---|
| 1 | 项目总索引（含 **P0 参数卡**：画幅 / 风格 / 平台 / 时长 / 出图·视频模型 / 帧率） | `总控\` 或 `剧集\{季}\{第N集}\` |
| 2 | 剧情源（原著 / 用户剧本）+ `参考\00_参考索引.md` | `参考\` |
| 3 | 总纲（全剧主纲：分季 / 阶段 / 章→集映射 / 能力体系 / 人物弧光） | `剧集\总纲\` |
| 4 | 分集大纲 + 剧本包 | `剧集\{季}\{第N集}\` |
| 5 | 三大资产包（角色 / 场景 / 道具）+ 已锁图 | `各个资产包汇总\角色\|场景\|道具\` |
| 6 | 10 字段分镜表 + 空间顶视图与机位调度图 | `各个资产包汇总\分镜\` |
| 7 | 图片视频生成执行规范 SOP | `工作流程\` |

目录骨架可一键生成（**只新建缺失目录，不动任何已有文件**）：

```bash
python scripts/new_project_scaffold.py "<项目根目录>" --season 第一季 --episode 第1集
# 先看看会建什么、不实际创建：加 --dry-run
```

## 三、必须替换的占位符（新剧只做一次）

正文中所有 `【方括号】` 都要换成本剧实际值，否则第 2 步会卡住（找不到就问用户，**不许用外部 skill 默认值填空**）。完整清单见 `references/11-new-drama-bootstrap.md` 的「11.2 占位符替换总表」，至少包括：

- 【新剧名】【第N集】【题材】【主角】【常驻角色】
- 【剧情源】/【剧情源文件】【项目根目录】【A 类授权】
- 【画幅】【出图模型】【视频模型】【帧率】【风格】【空间权威口径】【场景编号】【片段N】

替换后，把值写进**项目总索引参数卡**——它才是全项目"本剧锁定值"的唯一权威（仲裁⑦：本剧 `.md` ＞ 任何外部 skill 默认值）。

## 四、外部三库：A、B、C 全部随包自带

| 库 | 状态 | 位置 | 说明 |
|---|---|---|---|
| A 库 short-drama-director（28 份规则库 ＋ 打戏子库，303KB） | ✅ 完整 | `external-libs/A-short-drama-director\` | 打开 `references\09A` 的 9.2 表 → 按文件名取 |
| B 库 LIRA / CINEDANCE / ACTING（中文全本，87KB） | ✅ 完整 | `external-libs/B-overseas-three-libs\` | 三份全本，可直接通读 |
| C 库 洋子 10-Skill 工程 V3（91 文件 / 101KB） | ⚠ **索引骨架版** | `external-libs/C-yangzi-10skill\` | 结构、总控、目录映射齐全；10 个 Skill 的正文 `references/source.md` 等**缺失**。缺细则时先翻 B 库，覆盖度更高 |

C 库的骨架版说明：每个 Skill 的 `references\` 里只有 `_索引.md` + `skill.md` 两份**目录说明**，被它们描述的正文（如 `film-cinedance/references/source.md` 38KB）不在包内。若你从洋子原厂拿到 V3 完整 ZIP，把 `source.md`、`continuity-compiler.md`、`h3-prompt-format.md`、`shot-planning.md` 等覆盖进对应 `skills\<name>\references\` 即可升级为全本，本索引无需改动。

取用分两层：**先读 `references/09A–09E` 的要点定位方向**，需要完整条文/细则再进 `external-libs/` 的原库（详见 `external-libs/README.md`，内有"要解决什么→打开哪份"对照表）。

**注意**：外部库一律"只补方法、不覆盖参数"——它的默认值（竖屏 9:16 / R2 商业高燃 / 21:9 / Higgsfield 模型 / Seedance 2.0）不得覆盖你锁定的本剧参数；原库也**不提供剧情**，剧情唯一来源是你的剧情源。

## 五、安全说明

- **本技能自带的两个脚本**：`scripts/new_project_scaffold.py`（只用 `os.makedirs` 新建目录，不删除/不移动/不覆盖/不联网/不读凭据，支持 `--dry-run`）与 `scripts/init_project_docs.py`（复制模板到项目并替换占位符，默认不覆盖已有文件，支持 `--dry-run`）。
- **external-libs 内带的第三方脚本**（均**不会被本技能执行**，仅作资料保留，运行与否由你自己决定）：
  - A 库 2 个 Python：`build_board_lite.py`、`check_fight_prompt.py` —— 本地文本检查。
  - C 库 8 个安装脚本：`scripts\安装课程包.ps1` / `新建AI影视项目.ps1` / `配置本地知识库.ps1` / `更新本地知识库.ps1` / `升级旧电影工程规则.ps1` + 3 个 `.command` + `install_course.py`。它们是**洋子课程包的安装器**，会把 10 个 Skill 装进 Codex 的 `~/.codex/skills` 并写入知识库路径。**运行前请先自己读一遍脚本内容。**
- 其余全是 Markdown 与一份原版 HTML 备份，无可执行代码。

## 六、来源与保真

来源：《_AI指令文件路由卡_万能模板_新短剧用(1).html》（工作流 ＋ 方法论骨架，已剥离任何单剧剧本内容）。原版 HTML 完整备份在 `references/route-card-full-source.html`，需要按原始版式回看或核对是否漏转时直接读它。
