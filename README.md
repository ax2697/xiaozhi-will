
<div align="center">

<img src="assets/banner.svg?v=2" alt="晓之意志 · AI 短剧指令路由卡 / Xiaozhi Will · Short-Drama Route Card" width="1200" />

# 🧭 晓之意志 · AI 短剧指令路由卡

### Xiaozhi Will · Short-Drama Route Card

**v2.3.0** · 中文 / English 双语

> 一条「指令 → 文件」的存取约定。
> 不生产内容，只负责让 AI 在动手之前，读对文件、读对章节。
>
> *A routing convention between «instruction» and «file».*
> *It produces no content — it only makes sure the AI reads the right file, at the right section, before it starts.*

![Version](https://img.shields.io/badge/version-v2.3.0-6a5acd?style=flat-square)
![Files](https://img.shields.io/badge/files-397-2ec4b6?style=flat-square)
![Templates](https://img.shields.io/badge/templates-17-00b4d8?style=flat-square)
![Libs](https://img.shields.io/badge/libs-A%2FB%2FC%2FD-8e44ad?style=flat-square)
![Models](https://img.shields.io/badge/models-Seedance%202.5%20%7C%20SeedAudio%201.0-9d4edd?style=flat-square)
![Platform](https://img.shields.io/badge/platform-WorkBuddy%20%7C%20OpenClaw%20%7C%20Coze%20%7C%20Dify-ff9f43?style=flat-square)
![License](https://img.shields.io/badge/license-MIT-ffca3a?style=flat-square)
![Stars](https://img.shields.io/github/stars/ax2697/xiaozhi-will?style=social)

[这是什么](#-这是在解决什么问题) · [道教体系](#️-道教体系v200-新增) · [三条铁律](#️-三条铁律v110-新增) · [开工四项确认](#-开工前四项确认) · [四层模块](#-四层模块职责) · [核心能力](#-核心能力逐阶段) · [常用指令](#-常用指令) · [快速开始](#-快速开始) · [目录结构](#-目录结构) · [赞助](#-赞助与合作) · [更新记录](#-更新记录) · [English](#english)

</div>

---

## 🎯 这是在解决什么问题

带 AI 做过短剧的人，大概率都踩过这三个坑。

### 坑一：AI 不记得该读什么

每次开工都要重新交代：资产包在哪、SOP 在哪、机位图叫什么、分镜表是第几版。这次交代完，下次换个会话又得重来。**AI 不是不聪明，是它手上没有地图。**

### 坑二：两个文件冲突时，不知道该听谁

总索引参数卡写 16:9，外部 skill 默认 9:16，那你到底按哪个做？没有仲裁规则，AI 就会自己挑一个——而且不告诉你它挑了哪个。

### 坑三：改了一处，下游全崩

改了剧本台词，忘了回头同步分镜；改了分镜机位，忘了同步机位图。等到出图才发现全对不上，返工成本已经付出去了。

---

**晓之意志用三样东西回答这三个问题：**

| 回答 | 用什么 | 在哪 |
|:---|:---|:---|
| 该读什么 | **一张路由总表**：10 类指令 → 第一依据 / 必读捆绑（精确到节）/ 产出归位 | `SKILL.md` §四 |
| 听谁的 | **一套仲裁优先级 ⑧ 条**：磁盘 > 记忆、本剧 `.md` > 外部 skill | `SKILL.md` §八 |
| 回改谁 | **一张改动联动表**：6 类改动各自的下游同步链路 | `SKILL.md` §七 |

> 🔑 **核心立场**：**本卡不是读物，是路由。**
> 不要凭对话记忆动手——对话记忆一律视为过期，一切以磁盘当前 `.md` 为准。

> 📦 **本卡不持有你的剧**：它只带工作流与方法论骨架。角色 / 场景 / 道具 / 剧本 / 分镜，全部在你自己的项目目录里，由 `templates/` 里的 13 份空白模板起步。

---

## ☯️ 道教体系（v2.0.0 新增）

> **道生一，一生二，二生三，三生万物。** ——《道德经》第四十二章
>
> 创作者从意志走向像素，验收者从像素回溯意志。
> 本卡的全部路由、仲裁、门禁，皆在这一顺一逆之间。

短剧生产与道教讲的是同一条秩序：**无形的意图，按序落成有形的成片。**
道是剧情源，气是分镜机位，形是资产与成片，自然是「不替用户做决定」。

这么编排不是为了好看，是为了**定位**——出问题时能一句话说出「坏在第几阶、过没过那一关、是气散了还是形虚了」。

### 道生万物 —— 三层事实源，顺行生、逆行验

| 层 | 道教对应 | 事实源 | 顺行（生 · 创作） | 逆行（验 · 自检） |
|:---:|:---|:---|:---|:---|
| **道** | 无极 · 本源 | 剧情源 · 剧本 · 人设 · 情绪曲线 | 定因果意志：谁为何做何事 | 是否忠于原文，有无增删改 |
| **气** | 太极 · 阴阳 | 分镜 · 机位 · 时间码 · 轴线 | 定时空运行：何时何地如何发生 | 镜与镜接不接得上，轴线守没守 |
| **形** | 三才 · 万物 | 角色/场景/道具资产图 · 成片 | 定形质外观：长什么样、锁没锁死 | 基准脸锁住了吗，图真打开看过没 |

> **AI 干活走顺行（道→气→形）；AI 自检必须走逆行（形→气→道）。**
> 只会顺行不会逆行的 AI，产出越快，错得越远——因为它从不回头看自己造了什么。

### 三丹田 —— P0–P5 的第二身份

工序号 P0–P5 **原样保留**，所有路由表、门禁、模板编号继续用 P 号。道教名是第二身份，不是替身。

道教内丹以**上丹田（神）、中丹田（气）、下丹田（精）**为三田，六阶分别落在三田的「立」与「成」上。

| 阶 | 道教名 | 工序 | 落在哪一田 | 这一段到底在干什么 | 不过关的样子 |
|:--:|:---|:--:|:---|:---|:---|
| **一** | **筑基** | P0 立项 | 下丹田 · 精 | 安炉立鼎、锁炉温（锁参数）、辨药（认剧情源） | 参数靠默认值填的，一开工就偏 |
| **二** | **炼己** | P1 剧本 | 下丹田 · 精 | 采真药：三不铁律即"不掺假" | 擅自"优化"原著，为后面所有环节埋雷 |
| **三** | **炼精化气** | P2 资产 | 下丹田 → 中丹田 | 精化气：文字锁成图 | 图没锁死，基准脸每张都不同 |
| **四** | **炼气化神** | P3 分镜 | 中丹田 | 气成序：图编排成时空 | 分镜写得漂亮，但接不上、站不住 |
| **五** | **炼神还虚** | P4 生成 | 中丹田 → 上丹田 | 气化神：编排落成画面 | 方案是方案，出片是出片，两回事 |
| **六** | **还虚合道** | P5 交付 | 上丹田 · 神 | 神还虚：开炉验丹，真打开看，签字 | 没验就交，让用户替你把关 |

> **火候总则：前慢中快后慢。** 越靠前的错，修起来越便宜；越靠后的错，只能重炼。

### 五行 —— 六阶六关，相生闭环（缺一即退回）

道教五行相生是**完整五环**：木生火 → 火生土 → 土生金 → 金生水 → 水生木。六阶之间正好六道关。

| 关 | 五行 | 位置 | 关名 | 判据 |
|:--:|:--:|:---|:---|:---|
| **一关** | 水生木 | 一阶 → 二阶 | **鼎关** | 占位符全替换（无 `【】`）＋ 12 类目录齐 ＋ 参数卡有值 |
| **二关** | 木生火 | 二阶 → 三阶 | **药关** | 剧本过检 95 分制全过、三不逐字核完、剧情源可追溯 |
| **三关** | 火生土 | 三阶 → 四阶 | **形关** | 三包已出图并锁定基准（角色脸 / 场景朝向 / 道具材质有唯一权威图） |
| **四关** | 土生金 | 四阶 → 五阶 | **序关** | 10 字段齐、时间码连续、机位站位可核、第四章连续性锚点已继承 |
| **五关** | 金生水 | 五阶 → 六阶 | **验关** | SOP 核验 ＋ 方法论自检（A 库 P0/P1/P2、LIRA pre-send、CINEDANCE 静默 QA、ACTING 量表 ≥4）全过 |
| **六关** | 水生木 | 六阶 → 下一集 | **收关** | 成片真打开看过、资产归位、总索引回填、旧版保留 |

> **相克 = 越级的账单**：木克土（剧本未定做资产 → 形象反复推翻）、土克水（图未锁做分镜 → 整表重排）、水克火（分镜未定投喂视频 → 整段重生成）。
> **上游未定，下游不动。**

### 八卦 —— 文件归哪儿（八类性质）

《说卦传》八卦之德：**乾健、坤顺、震动、巽入、坎陷、离丽、艮止、兑说**。不建八个文件夹，是八个归类问句。

| 卦 | 德 | 收什么 | 目录 |
|:--:|:--:|:---|:---|
| **乾** ☰ | 健 · 君 | 总索引、参数卡、路由卡（唯一权威） | `总控/` |
| **坤** ☷ | 顺 · 母 | 剧本、分集大纲、总纲（母体） | `剧集/{季}/{第N集}/` |
| **震** ☳ | 动 | 剧情源、原著章节、参考资料 | `参考/` |
| **巽** ☴ | 入 | SOP、工作流程、执行规范 | `工作流程/` |
| **坎** ☵ | 陷 | 角色 / 场景 / 道具三包文字资产 | `各个资产包汇总/` |
| **离** ☲ | 丽 · 明 | 所有图片与音频资产 | `资产图片音频汇总/` |
| **艮** ☶ | 止 | 已锁定、不再改的定稿与旧版 | `_锁定/` · 旧版 |
| **兑** ☱ | 说 | 成片、质检报告、交付件 | 交付区 |

> **拿不准就归坤，别在根目录乱放。** 散落根目录的文件，等于没有归档。

### 五气朝元 —— 质检五维（每维 0–5，任一 ≤2 退回）

内丹五气朝元：心肝脾肺肾各归其元。借到质检上，**一份产物要过五个维度**。

| 脏 | 五行 | 维度 | 在问什么 | 不合格 |
|:--:|:--:|:---|:---|:---|
| 肝 | 木 | **生化**（有没有） | 元素齐不齐 | 画面空、缺件 |
| 心 | 火 | **明丽**（亮不亮） | 光影色彩构图 | 灰暗、主体不清 |
| 脾 | 土 | **笃实**（稳不稳） | 结构比例材质可信 | 手崩、穿模 |
| 肺 | 金 | **肃杀**（净不净） | 有无多余物脏点错字 | 异物、乱入、字错 |
| 肾 | 水 | **藏精**（连不连） | 与前后镜与原著一致 | 跳戏、脸变、走样 |

> **好看但接不上（肾亏），比不好看更贵。**

### 三宝 —— 亏一件就废

道教三宝：**精、气、神**（《心印妙经》"上药三品，神与气精"）。它们不是别人的毛病，是 AI 最容易亏的三种省事。

| 宝 | 道教原义 | 亏了的样子 | 守则 |
|:--:|:---|:---|:---|
| **精不亏** | 形质之本，亏则形虚 | 拿外部 skill 默认值（9:16 / R2 高燃 / 21:9 / Higgsfield）顶包；凭对话记忆动手 | **参数卡唯一权威**（仲裁⑦）＋ 第 0 步强制 Read |
| **气不散** | 运化之力，散则序乱 | 一口气跑完 P0→P5；没过门禁就进下一阶 | **三关不跳** ＋ 前慢中快后慢 |
| **神不昏** | 主宰之明，昏则失察 | 改台词不改分镜，改机位不改机位图 | **改动联动表强制走**（§七） |

> 三宝的共同点：**亏了都不吭声，等出片才暴露。**
> 守法则只有一个共同点：**把决定权交回参数卡和磁盘文件。**

### 全图

```
                    道生万物（三层事实源）
        ┌──────────────────────────────────────────┐
        │  道：剧情源 · 剧本 · 人设 · 情绪曲线        │
        │        ↓ 顺行（生）      ↑ 逆行（验）      │
        │  气：分镜 · 机位 · 时间码 · 轴线            │
        │        ↓ 顺行（生）      ↑ 逆行（验）      │
        │  形：角色 / 场景 / 道具资产图 · 成片         │
        └──────────────────────────────────────────┘

  六阶                      六关（五行）                    三宝
  ──────────────────────────────────────────────────────────────
  一 · 筑基    P0 立项
                              │
  二 · 炼己    P1 剧本  ─ 一关 · 水生木 · 鼎关 ─┬─ 精不亏
                              │                 │
  三 · 炼精化气    P2 资产  ─ 二关 · 木生火 · 药关 ─┼─ 精不亏
                              │                 │
  四 · 炼气化神    P3 分镜  ─ 三关 · 火生土 · 形关 ─┼─ 气不散
                              │                 │
  五 · 炼神还虚    P4 生成  ─ 四关 · 土生金 · 序关 ─┼─ 气不散
                              │                 │
  六 · 还虚合道    P5 交付  ─ 五关 · 金生水 · 验关 ─┴─ 神不昏
                              │
                  ─ 六关 · 水生木 · 收关 → 下一集

  八卦：乾总控 · 坤剧集 · 震参考 · 巽流程 · 坎文字包 · 离像素包 · 艮锁定 · 兑交付
  五气朝元：肝生化 · 心明丽 · 脾笃实 · 肺肃杀 · 肾藏精
```

> **道法自然，顺逆相成；五行既生，三宝不亏。**
>
> 全文（含典籍对照表）见 [`references/12-daoxue-cosmology.md`](xiaozhi-will/references/12-daoxue-cosmology.md)。

---

## ⚖️ 三条铁律（v1.1.0 新增）

**规则管不住 AI，铁律才管得住。** 这三条优先于本卡其余一切内容，违反任何一条都停下补做。

| # | 铁律 | 一句话 | 怎么算做到 |
|:--:|:---|:---|:---|
| **1** | **留痕可逆** | 每次改动建 Git commit（白名单 add，禁 `git add .`），一步一提交 | 有 commit，能单独 revert |
| **2** | **跑过才算** | 验收脚本跑绿，贴真实命令输出与退出码；失败修根因，禁改测试让它变绿 | 有输出、有退出码 |
| **3** | **人认才算** | AI 不得自判合格。三级递进不得跳级：AI 自检 → AI 独立验证 → 你终审 | 三级都有回执 |

### 由铁律展开的 AI 执行六条

1. **先读再答** — 没读 `项目状态.md` 或本阶段点名的文件，不许回答
2. **一问一停** — 一轮只推进一个确认点，禁止一趟跑完 P0→P5
3. **不猜不默认** — 缺信息就停；假设标 `[假设]`＋后果，影响生成的升级为 `[待确认·阻塞]`
4. **不重复失败 + 先采集后创作** — 同处连续 3 次停手回退；有参照物先实读并留书面拆解记录
5. **状态明确 + 上下文治理** — 开工复述目标，跨会话先读记忆；临时产物入「AI工作区」；收尾三态 ✅/❌/🔄
6. **找规则别通读 + 开工三问** — ① 我读制度了吗 ② 我建清单了吗 ③ 我复述状态了吗。任一为否，不许开工

> 另守两条实操纪律：**唯一真相源**（只有 `项目状态.md`，不另建第二套记录）＋ **门禁不跳级**（上一阶段没验收不进下一阶段）。

> 完整版见 [`templates/A0-铁律卡.md`](xiaozhi-will/templates/A0-铁律卡.md)。

---

## 🚦 开工前四项确认

参考站用「六道前置锁」管住开工前的参数。我们是单技能路由卡，对应的是**四项确认**——任何一项没指定，**停下问，不许替用户推断**。

| # | 确认项 | 选项 / 说明 | 未指定时 |
|:--:|:---|:---|:---|
| **①** | **本剧名与集号** | 写进项目总索引参数卡，它是全项目「本剧锁定值」唯一权威 | ⛔ 停下询问 |
| **②** | **剧情源** | 原著 / 用户剧本的磁盘路径。剧情唯一来源，三库均不得供剧情 | ⛔ 停下询问 |
| **③** | **画幅 + 出图 / 视频模型** | 如 16:9 + seedream 出图 / seedance 出视频 + 帧率 | ⛔ 停下询问，**禁止拿外部 skill 默认值填空** |
| **④** | **本次产物类型** | 静态图 / 改图 / 视频 / 剧本 / 分镜 / 剪辑 / 质检 | 决定加载哪份方法论、走路由表哪一行 |

> ⚠️ 这四项是**硬门，不是建议**。参考站的做法是「必须弹出让用户勾选」，我们沿用这个精神：**未指定 = 停工询问**，而不是默默用默认值往前跑。

---

## 🧩 四层模块职责

参考站是「1 总控 + 12 子技能」的四层纵深。我们是**单技能 + 四层模块**——不是拆成 13 个目录，而是把职责在同一个包内分层，靠 `SKILL.md` 的路由把四层串起来。

| 层 | 落在哪 | 职责 | 对应道教层 | 你什么时候会用到 |
|:---:|:---|:---|:---:|:---|
| **L0 路由层** | `SKILL.md` | 六步流程 · 路由总表 · 仲裁 ⑧ 条 · 改动联动 · 交付自检 · 开工四项确认 | **道**（定序） | 每次开工都读，是唯一入口 |
| **L1 方法层** | `references/` | 9 份方法论要点：道教体系、诺兰手法、A/B/C 三库、Seedance / SeedAudio 官方规则、剧情三不铁律、立项清单 | **气**（运化） | 第 2 步「方法论先行」按产物类型定向加载 |
| **L2 原库层** | `external-libs/` | A/B/C 三库原库原文（130 个文件），要点不够时深挖 | **气**（运化 · 深源） | 需要完整条文 / 细则时进这一层 |
| **L3 执行层** | `templates/` + `scripts/` | 13 份空白项目模板 + 2 个本地脚本（建骨架 / 落盘模板） | **形**（落形） | 新剧立项、日常建文件 |

**两层取用法**：先用 `references/09A–09E` 的**要点层**定位方向 → 需要完整条文再进 `external-libs/` 的**原库原文**。

**三库分工一句话**：A 库（short-drama-director）**定流程门**、B 库（LIRA / CINEDANCE / ACTING）**定提示词写法**、C 库（洋子 10-Skill）**定工程组织与阶段门禁**。三库都**只补方法**，任何冲突按仲裁⑦回落到本项目磁盘 `.md`。

---

## 🔄 六步响应流程

每条制作指令进来，都按同一个顺序走。**每一步都对应三宝中的一件**——守不住，就退回去补。

| 步 | 动作 | 关键点 | 守哪一宝 |
|:---:|:---|:---|:--:|
| **0** | **先 Read 磁盘最新稿** | 最高门禁：项目 `.md` 与外部 SKILL/references 都以磁盘当前文件为准，旧记忆 / 摘要一律过期 | **精** |
| **1** | 解析指令 | 动作 ＋ 对象 ＋ 产物类型；同时定位落在哪一阶 | — |
| **2** | **方法论先行** | 按产物类型先读 `references/` 命中章节；剧情类同步通读剧情源 | **神** |
| **3** | 再读总索引 | 参数卡 · 最新状态 / 缺口 · 双编号 · 定稿门禁（参数卡唯一权威） | **精** |
| **4** | **第一依据 ＋ 捆绑取齐到节** | 路由表第一依据 ＋ SOP ＋ 固定前缀**逐字复制** ＋ 上游 / 已锁资产 ＋ 机位图 | **气** |
| **5** | 执行 · 双自检 · 归位 | SOP 核验 ＋ 方法论自检 ＋ 下游联动 ＋ 报用户确认 | **神** |

> **顺序原则：先图纸，后盖楼。**
> 方法论先于项目文件读取——先知道「该怎么做、有哪些坑、查哪些维度」，再去看「这次要做什么、锁了什么」。方法论**只定向加载本次命中章节**，不全量通读。

```
📥 磁盘最新稿 → 🧩 解析指令 → 📚 方法论先行 → 📇 总索引 → 🎯 第一依据·捆绑到节 → ✅ 执行·双自检·归位
  守精            定位阶位         守神            守精              守气                    守神
```

> **逆行验形**：第 5 步的自检不是顺行末尾的收尾，是**换方向重走一遍**——从成片回溯到道（忠于原文吗）→ 气（接得上吗）→ 形（图锁死了吗）。只顺不逆，等于没验。

---

## 📇 指令 → 文件 路由总表

**第一依据**是执行的事实源，**必读捆绑**必须精确到「第几节」，**产出归位**决定文件落到哪。**阶 / 关列**标出这条指令落在哪一阶、跨越哪一关——跨关意味着必须先确认上一关判据已过。

| 指令 | 阶 | 关 | 第一依据 | 必读捆绑（精确到节） | 产出归位 |
|---|:--:|:--:|---|---|---|
| 生成**角色** | 三 · 炼精化气 | 三关·形 | 角色包 · 该角色 x.1 设定图 | SOP；0.1 基底 / 0.2 负向 / 0.3 四张分图 / 5.3 门禁；x.2 表情 x.3 姿态 x.4 服装 x.5 锚点；剧本包人设；已锁基准脸 | `资产图片音频汇总/角色设定图/{角色}/` |
| 生成**场景 / 空间** | 三 · 炼精化气 | 三关·形 | 场景包 · 该 S 分节 | SOP；0.1–0.3 ＋ 该 S 的 -1 六视图 / -2 光影 / -3 空间锚点 / -4 粒子 / -5 陈设 ＋ 8.2 门禁；机位图 x.1 坐标 / x.3 轴线；10 字段分镜对应片段 | `资产图片音频汇总/场景设计图/` |
| 生成**道具**特写 | 三 · 炼精化气 | 三关·形 | 道具包 · 该 P 分节 | SOP；0.1–0.3 ＋ 该件 -1 六视图 / -2 光影 / -3 空间锚点 / -4 材质 / -5 陈设 ＋ 10.2 门禁；场景包承托面 | `资产图片音频汇总/道具设计图/{道具}/` |
| 生成**关键帧** | 五 · 炼神还虚 | 五关·验 | 10 字段分镜 · 该镜 ＋ 对应资产包 | SOP 静态流水线；**分镜第四章连续性锚点（必继承）**；关键帧公式（角色 5.4 / 场景 8.3 / 道具 10.3）；模板库 2 / 3 / 5 / 6；机位图站位朝向 | `资产图片音频汇总/关键帧/` |
| 生成**视频片段**（每段 ≤15s） | 五 · 炼神还虚 | 五关·验 | 10 字段分镜 · 逐镜 | SOP 三；剪辑包 G-PRE / G-NEG(1) V(2) R(3) T(4) BGM(5)；模板库 3.3 / 6.4；分镜第四章锚点；机位图 x.2 机位部署表 / x.3 轴线；关键帧 ＋ 三包（图生 ≤10） | `资产图片音频汇总/视频片段/` |
| 改剧情 / 台词 / 人设 | 二 · 炼己 | 二关·药 | 项目剧本包（最权威） | 本集剧本分场；剧情源原文；按改动联动表向下回改 | 更新 `.md` 重生成 docx |
| 切镜头 / 改时间码 / 机位 | 四 · 炼气化神 | 四关·序 | 10 字段分镜（★唯一依据） | 模板库 7.2 书写格式 / 7.3 切分 / 7.4 质检 / 6.4 轴线 | 同步机位图 x.2 与分镜第四章锚点 |
| 剪辑 / 转场 / 配乐 / 调色 | 六 · 还虚合道 | 六关·收 | 剪辑资产包 | 剪辑包 7 九步 SOP / 10 质检；10 字段分镜音效 / BGM / 衔接列 | 母版出 16:9，遮幅 / 竖裁后期再做 |
| 查原著依据 / 核对剧本忠于剧情源 | 二 · 炼己 | 二关·药 | 剧情源查章路由 | `00_参考索引`；剧情源结构地图（先定位第几章） | — |

### 走一遍看看

假设你说：**「生成主角的设定图」**

```
① 解析：动作=生成 · 对象=主角 · 产物类型=静态图 → 定位【三阶·炼精化气 · 三关·形】
② 方法论先行：读 references/09A 的 A 库流程门（Asset-First 六阶段）        · 守神
③ 读总索引：确认画幅 16:9、出图模型已锁定、该角色是否有缺口                  · 守精
④ 取件：角色包「主角 x.1」＋ SOP 0.1 基底 / 0.2 负向 / 0.3 四张分图
        ＋ 5.3 门禁 ＋ x.2~x.5 ＋ 剧本包人设 ＋ 已锁基准脸                    · 守气
⑤ 执行：按 SOP 核验 → 方法论自检 → 回改总索引状态 → 报你确认                 · 守神
   落盘：资产图片音频汇总/角色设定图/主角/
   逆行验：形（图打开看了吗）→ 气（脸锁住了吗）→ 道（还是原著那个人吗）
```

> 注意第 ④ 步：**没有读机位图**。因为这是纯角色白底单品图，不涉场景。一旦人物落进场景、两人同框，机位图立刻变成必读——这就是「四类必读时机」的判据。

---

## 🎥 机位图四类必读时机

| 必读 | 为什么 |
|:---|:---|
| ① **场景六视图** | 朝向 / 画左画右 / 门窗家具灯具方位，以最新定稿六视图为准 |
| ② **关键帧** | 角色站位、面朝、视线、画左画右 |
| ③ **视频片段** | 引 CAM1~CAM4、守 180° 轴线、跳段衔接、同机位回环 |
| ④ **道具放回场景 / 改镜头 / 剪辑** | 道具方位、机位方向、轴线连贯 |

**不需读**：纯角色 / 纯道具的白底单品图（无场景、无第二者）。一旦人物落进场景、两人同框、或道具「放回环境」，立即回到必读四类。

> **空间权威口径**：场景布局 / 画左画右 / 朝向 / 轴线，以**机位图最高**，并在机位图里逐字登记。

---

## 🖼️ 关键帧专用取件清单（跳三包，最易漏）

| 来源 | 必须取哪些 |
|:---|:---|
| **分镜** | 该镜 10 字段 ＋ 第四章连续性锚点（造型 / 关键道具 / 光影母题 / 声音母题 / 构图 / 轴线，整张必继承） |
| **角色关键帧** | 角色包 5.4 公式 ＋ 0.4 用法 ＋ x.6 专属基底 ＋ x.2~x.5；多人加 0.5 / 5.1 / 5.2 |
| **场景关键帧** | 场景包 8.3 公式 ＋ 该 S 的 -2 光影 / -3 空间锚点 |
| **道具关键帧** | 道具包 10.3 公式 ＋ 该件 -3 空间锚点 / -5 叙事陈设；10.4 边界登记防越界 |
| **语法 / 空间** | 模板库 2 景别、3 运镜、5 光影、6 安全区与 6.4 轴线；机位图定站位朝向 |

---

## 🔗 改动联动表

上游一改，下游必须同步。

| 你改了什么 | 必须回头同步谁 |
|:---|:---|
| 剧本 / 台词 / 情节 | 10 字段分镜 →（涉站位机位）机位图 →（涉形象陈设）三包 → 情绪曲线量化 |
| 分镜镜头号 / 机位 / 时长 | 机位图 x.2 部署表（逐条对照核准）、分镜第四章锚点、模板库 7.4 质检、受影响关键帧 / 视频 |
| 场景坐标 / 轴线 / 陈设 | 机位图、场景包该 S、已出场景图与关键帧、道具包该件叙事陈设 |
| 角色形象锚点 / 基准脸 | 重锁基准脸、角色包、已出设定图与关键帧（锁定后不轻易改） |
| 固定前缀 / 负向 / 全局参数 | 以资产包原文 ＋ 总索引参数卡为准，回改 SOP，**不反向用 SOP 覆盖资产包** |
| 任一 `.md` 改稿 / 重生成 `.docx` | 立即回填《项目总索引》该文件大小与最新状态，并重生成总索引 docx；**旧版保留不覆盖** |

---

## ⚖️ 冲突仲裁优先级

两个文件打架时，按这个顺序判。

| 序 | 规则 |
|:---:|:---|
| ⓪ | 磁盘当前 `.md` ＞ 对话记忆 / 摘要（旧记忆视为过期） |
| ① | `.md` ＞ `.docx` |
| ② | 10 字段分镜 ＞ 基础分镜 |
| ③ | 资产包原文 ＋ 总索引参数卡 ＞ SOP / 路由卡 |
| ④ | 场景 / 资产双编号查总索引映射表（剧本场景号＝资产包场景号） |
| ⑤ | 最新拍板日期优先（总索引第六章） |
| ⑥ | 门禁不跳级；剧情对原著不添加 / 不更改 / 不删除 |
| ⑦ | **本集 `.md` ＞ 外部 skill 方法论**（skill 只补方法不覆盖参数） |
| ⑧ | **剧情源原文 ＞ 总纲 ＞ 分集大纲 / 剧本 / 分镜** |

---

## 🔥 核心能力（逐阶段）

| 阶段 | 能力 | 具体做什么 |
|:---:|:---|:---|
| 🧭 **立项** | 新剧立项清单 | **一阶·筑基**：8 类必建文件 + 占位符替换总表，新剧第一次开工只做一次 |
| 📇 **路由** | 指令 → 文件路由 | 10 类指令各自的第一依据、必读捆绑（精确到节）、产出归位；**每条标出所属阶与所跨关** |
| 🎬 **呈现** | 诺兰电影化手法基石 | 非线性时间、闪前闪回、交叉蒙太奇、片尾双钩、集首冷开场——**一阶·筑基级**，创作任何一集前必读 |
| ✍️ **剧本** | A 库六阶段编剧链 | **二阶·炼己**：来源登记 → IP 与角色开发 → 开发圣经 → 分集规划 → 正式剧本 → 圆桌审核 |
| 📜 **剧情** | 三不铁律 + 改编白名单 | **守神**：不添加 / 不更改 / 不删除；有判定标准与统一边界 |
| 🖼️ **资产** | Asset-First 资产包 | **三阶·炼精化气**：角色资产板 / 场景空间图三件套 / 道具图；先锁定再进分镜 |
| 🎥 **空间** | 机位图四类必读时机 | **四阶·炼气化神**：哪四种必须读，哪两种可以跳过 |
| 🎬 **分镜** | 10 字段分镜 + 连续性锚点 | **四阶·炼气化神 · 四关·序**：每一镜的字段定义与第四章锚点，保证跳镜不漂移 |
| 🖼️ **关键帧** | 跳三包取件清单 | **五阶·炼神还虚**：分镜锚点 + 三包各自公式，一张清单取齐 |
| 🚀 **投喂** | Seedance 2.5 七条铁律 | **五阶·炼神还虚 · 五关·验**：三层解耦框架、标准投喂模板、P4 投喂六步序列过检 |
| 🎵 **音频** | SeedAudio 1.0 官方约束 | **五阶·炼神还虚**：T2A / A2A prompt 形态与硬约束 |
| 🔗 **联动** | 改动联动表 | **守神**：6 类改动各自的下游回改链路 |
| ⚖️ **仲裁** | 冲突仲裁 ⑧ 条 | **守精气**：⓪③⑦ 守精、⑥ 守气、⑧ 守神；文件打架时有据可依 |
| ✅ **自检** | 交付前防遗漏清单 | **逆行验形**：形（精）→ 气（关）→ 道（神）三段打勾 |
| ⚖️ **铁律** | 三条顶层铁律 | 全阶：留痕可逆 / 跑过才算 / 人认才算；违反任一条停下补做 |
| 📋 **状态** | 唯一真相源骨架 | **一阶·筑基**：70+ 字段参数卡 + P0–P5 阶段状态 |
| 🔍 **门禁** | 剧本过检 95 分制 | **二阶·炼己**：7 大项逐项签字，9 项评分任一 <95 不得提交 |
| 🎭 **情绪** | 情绪关键帧库 | **三阶·炼精化气 · 三关·形**：4 模块（恐怖/动作/情感/爽感）+ 8 种情绪速查 |
| ⏱️ **单元** | 30 秒分镜硬约束 | **四阶·炼气化神 · 四关·序**：时间码 0.0–30.0 连续校验，站位交接开关 |
| 📚 **三库** | A/B/C 三库路由 | 全阶：A 定流程门、B 定提示词写法、C 定工程组织 |
| 🎭 **表演** | Master Acting Profile | **三阶·炼精化气**：常驻角色 150–220 词行为说明书（八块结构）+ Voice 声学参数，让角色不是念台词机器 |
| 🔖 **锚点** | @CHR/@SCN/@PRP 编码 | **一阶·筑基**：三包统一主键，名字会变码不变，断链从源头杜绝 |
| 🔐 **六把锁** | CINEDANCE 六锁英文短句 | **五阶·炼神还虚**：首帧占用 / 空间调度 / 视线分离 / 地标邻近 / 多镜连续 / 上下文隔离，填空即用 |
| 🎨 **调色** | 60/30/10 调色板 | **三阶·炼精化气**：每场景一套色配比 + 光影四要素 + 全剧五色系收敛 |
| 🧭 **选型** | 情境映射 E01–E15 | **四阶·炼气化神**：这场戏该用什么镜头——80/15/5 权重 + 构图雷区双态，解决"全靠临场发挥" |
| 🎬 **赛道** | 四赛道分流 | **一阶·筑基**：国内剧 / 海外剧 / 解说类 / 其他——选错赛道，全套规则错配 |
| 🔍 **采风** | 对标情报卡 | **一阶·筑基**：对标爆款的公开信息采集 + 十三项字段 + 六条证据纪律 |
| 🥋 **打戏** | 三套打戏引擎 | **五阶·炼神还虚**：写实 / 玄幻 / 漫剧打斗是三套物理，不是一套 |
| 🔧 **机检** | C1~C33 + H1~H12 | **六阶·还虚合道**：把"看着行"变成逐条可判定（74KB 手册） |
| ⚓ **锚形** | 视觉资产对账单 | **三阶·炼精化气**：每场景定穴 + 每镜挂锚 + 覆率 100%——九成崩坏的源头 |
| 🫁 **调息** | 声音三段呼吸 | **六阶·还虚合道**：蓄息 → 屏息（≤0.8s）→ 吐息，屏息那半秒最贵 |
| ☯️ **交济** | 双轨错峰排期 | **二阶·炼己**：爽点与甜点永不同集到顶——水火既济，轮流旺 |
| 💰 **还债** | 承负账本 | **二阶·炼己**：打脸能量 ≥ 2 × 憋屈时长 × 见证人数，利息必须给足 |
| 🌏 **易地** | 出海换皮存神 | **二阶·炼己**：换一层文化皮，内核一点不动；台词 ≤10 词 |
| 📝 **立骨** | 剧本四骨 | **二阶·炼己**：开篇三式钩子 / 冲突见证链 / 反转三格 / 卡点三式 |
| 🥋 **炼形** | 打戏十一环 | **五阶·炼神还虚**：力从腰起不在手，十一环缺一环力就断 |
| 🪶 **画符** | 投喂七段六闸 | **五阶·炼神还虚**：七段是符的七位，六闸是画符六手续——格式错一个字整段返工 |
| 🔬 **九转** | 机检 C1~C33 | **六阶·还虚合道**：M/S/H 三类分开验，不得互相冒充；FAIL 清零才交付 |
| 🧪 **三单** | 资产三单提取 | **三阶·炼精化气**：角色 4 格 / 道具 4 格 / 场景 9 格，格数写死不许第 5 格第 10 格 |
| 📜 **六候** | 剧本六阶段 | **二阶·炼己**：一候来源登记 → 六候五席圆桌，候候有门禁 |
| 🗣️ **台词** | 自然化与七维诊断 | **二阶·炼己**：单句 ≤24 字，遮挡名认不出谁说的就是不合格 |
| ☯️ **体系** | 道教体系总纲 | 全阶：道生万物 / 六阶 / 五行六关 / 精气神三宝；出问题先定位在第几阶 |
| 📿 **八支** | 道教全体系 | 全阶：哲学 / 内丹 / 易学 / 风水 / 符箓 / 戒律 / 择日 / 宫观——**不止内丹** |
| ⚖️ **哲学** | 道德经 · 庄子 | 全阶：道法自然 / 无为 / 反者道之动；齐物论多视角、庖丁解牛顺结构切 |
| ☯️ **易学** | 阴阳 · 六爻 · 变卦 | **二阶·炼己**：一场戏要有"反"；六爻即六段；一爻即一个分支点 |
| 🏔️ **风水** | 藏风聚气 · 四象 | **三阶·炼精化气 / 四阶·炼气化神**：有遮挡、有纵深、有界限；左主右客 |
| 🔯 **符箓** | 符三部位 · 科仪四段 | **三阶 / 五阶**：头 / 胆 / 脚三层立住；请神→上香→诵经→送神四段一场戏 |
| 🚫 **戒律** | 五戒十善 | **一阶·筑基 / 六阶·还虚合道**：五戒是红线，十善是底线 |
| 📅 **择日** | 十二建除 · 二十八宿 | **一阶·筑基**：一季要有"平"与"定"呼吸；一剧只主打一象 |
| 🏛️ **宫观** | 三都五主十八头 | 全阶：谁知道资产在哪（知库）；一日不作一日不食 |

---

## 🧮 常用指令

在对话里直接这样说，路由卡会自己走对应那一行：

| 指令 | 对应路由 | 阶 | 说明 |
|:---|:---|:--:|:---|
| `/新剧立项` | 第十一章 | 一 · 筑基 | 建项目骨架 + 替换全部占位符 |
| `/角色` | 生成角色 | 三 · 炼精化气 | 读取角色包 x.1~x.5 与 SOP 门禁（过三关·形） |
| `/场景` | 生成场景 | 三 · 炼精化气 | 读取场景包该 S 分节 + 机位图轴线（过三关·形） |
| `/道具` | 生成道具 | 三 · 炼精化气 | 读取道具包该 P 分节 + 承托面（过三关·形） |
| `/关键帧` | 生成关键帧 | 五 · 炼神还虚 | 跳三包取件清单 |
| `/视频` | 生成视频片段 | 五 · 炼神还虚 | 10 字段分镜逐镜 + 投喂六步 |
| `/改剧本` | 改剧情 / 台词 / 人设 | 二 · 炼己 | 剧情三不铁律核对 |
| `/切镜头` | 切镜头 / 改机位 | 四 · 炼气化神 | 同步机位图与分镜锚点（过四关·序） |
| `/剪辑` | 剪辑 / 转场 / 配乐 | 六 · 还虚合道 | 剪辑包九步 SOP |
| `/查原著` | 查原著依据 | 二 · 炼己 | 剧情源查章路由 |
| `/自检` | 交付前自检 | 六 · 还虚合道 | 形 → 气 → 道 逆行三段打勾 |
| `/铁律` | 三条铁律 | 全阶 | 查当前该守的硬规则与执行六条 |
| `/状态` | 项目状态 | 一 · 筑基 | 看 P0–P5 做到哪一步、缺口在哪里 |
| `/过检` | 剧本过检 | 二 · 炼己 | 走 A5 清单，95 分制逐项签字 |
| `/情绪库` | 情绪关键帧 | 三 · 炼精化气 | 读 A4 模块，按情绪取帧 |
| `/道教` | 道教体系总纲 | 全阶 | 查三宝 / 三丹田 / 五行三关，定位坏在第几阶 |
| `/三关` | 五行门禁 | — | 查三关·形 / 四关·序 / 五关·验 的当前判据 |
| `/路由` | 本表 | — | 问「这条指令该读哪些文件」 |

> 这些是**触发词**，不是脚本命令。说中文原话也一样能触发，例如「按路由卡执行」「第 3 集开工」「这条指令该读哪些文件」。

---

## ⚙️ 快速开始

### 1. 安装

把 `xiaozhi-will` 整个文件夹复制到技能目录，按你的平台选：

| 平台 | 安装位置 |
|:---|:---|
| **WorkBuddy** | `C:\Users\<用户名>\.workbuddy\skills\xiaozhi-will\`（macOS / Linux：`~/.workbuddy/skills/xiaozhi-will/`） |
| **OpenClaw** | `openclaw skills install ./xiaozhi-will --as xiaozhi-will` |
| **Coze / Dify / 通用 LLM** | 把 `SKILL.md` 正文粘贴进系统提示词，`references/` 作为知识库上传 |

复制后不需要重启、不需要配置。在对话里说「**按路由卡执行**」「**这条指令该读哪些文件**」「**第 N 集开工**」「**新剧立项**」即可触发。

### 2. 建项目骨架

```bash
# 先看会建什么，不实际创建
python scripts/new_project_scaffold.py "<项目根目录>" --season 第一季 --episode 第1集 --dry-run

# 确认后真建（只新建缺失目录，绝不删除或覆盖任何已有文件）
python scripts/new_project_scaffold.py "<项目根目录>" --season 第一季 --episode 第1集

# 落盘 8 份模板并替换占位符（默认不覆盖已有文件）
python scripts/init_project_docs.py "<项目根目录>" --season 第一季 --episode 第1集
```

脚本实测：`new_project_scaffold.py` 建出 **21 个目录**，`init_project_docs.py` 落盘 **8 份模板**。

### 3. 替换占位符 + 锁 P0 参数

正文所有 `【方括号】` 都要换成本剧实际值，至少包括：

`【新剧名】【第N集】【题材】【主角】【常驻角色】【剧情源文件】【项目根目录】【画幅】【出图模型】【视频模型】【帧率】【风格】`

替换后写进**项目总索引参数卡**——它是全项目「本剧锁定值」的唯一权威，外部 skill 默认值不得覆盖（仲裁⑦）。

### 4. 给 AI 的最小执行序列

```
读 SKILL.md
  → 完成开工四项确认（剧名集号 / 剧情源 / 画幅模型 / 产物类型）
  → 查路由表：本次指令的第一依据是哪份文件
  → 方法论先行：按产物类型读 references/ 命中章节
  → 读项目总索引参数卡 ＋ 必读捆绑（精确到节）
  → 执行 ＋ SOP 核验 ＋ 方法论自检 ＋ 下游联动
  → 报你确认
```

---

## 🖥️ 适用平台与模型

| | 支持 |
|:---|:---|
| **Agent 平台** | WorkBuddy · OpenClaw · 豆包智能体 / 扣子 (Coze) · Dify 及通用 LLM |
| **视频 / 音频模型** | Seedance 2.5 · SeedAudio 1.0（官方投喂硬约束见 `09D`） |
| **输出** | 结构化投喂提示词组 · 关键帧公式稿 · 资产提示词 · 项目模板 md · 项目目录骨架 |

---

## 📦 目录结构

```
xiaozhi-will/
├── README.md                      本落地页（中文 + English）
├── LICENSE / .gitignore
├── assets/                        自绘 SVG 图（不依赖外链图床）
│   ├── banner.svg                 横幅
│   └── pipeline.svg               路由示意
└── xiaozhi-will/                  技能本体（154 文件）
    ├── SKILL.md                   主入口：六步流程 / 路由总表 / 仲裁 / 自检
    ├── DISTRIBUTE.md              安装与前置条件
    ├── references/                23 份方法论 ＋ 索引 ＋ 原版 HTML 备份
    │   ├── 08-nolan-cinematic.md              诺兰电影化手法全文（P0 基石，66KB）
    │   ├── 09A-domestic-gate-lib.md           A 库：Asset-First 六阶段 / 三铁律
    │   ├── 09B-overseas-three-libs.md         B 库：LIRA / CINEDANCE / ACTING
    │   ├── 09C-pipeline-detail-p0-p5.md       P0–P5 逐阶段详解
    │   ├── 09D-seedance-seedaudio-official.md Seedance 2.5 ＋ SeedAudio 1.0
    │   ├── 09E-yangzi-10skill-engineering.md  C 库：八阶段与门禁
    │   ├── 10-plot-source-iron-rules.md       剧情三不铁律 ＋ 改编白名单
    │   ├── 11-new-drama-bootstrap.md          立项清单 ＋ 占位符总表
    │   ├── 12-daoxue-cosmology.md             **道教体系全文**（道生万物 / 三丹田 / 五行 / 三宝）
    │   ├── 13-acting-master-profile.md        **表演说明书**：八块结构 + 两套范例 + 15 种坏表演反查
    │   ├── 14-anchor-coding.md                **资产锚点编码**：@CHR/@SCN/@PRP 格式与分配规则
    │   ├── 15-cinedance-six-locks.md          **六把锁英文短句**：填空模板 + FOV° 六档 + 20 问 QA
    │   ├── 16-lighting-palette.md             **调色与光影**：60/30/10 + 全剧五色系 + 三条禁则
    │   ├── 17-laoli-engines-map.md              **老李 12 引擎 · 道教六阶归位图**
    │   ├── 18-decision-engine.md               **炼气阶选型依据**：E01~E15 + 80/15/5 + 雷区双态
    │   ├── 19-dandao-mechanisms.md             **丹道五机**：锚形 / 调息 / 交济 / 还债 / 易地
    │   ├── 20-dandao-screenplay.md             **炼己筑基**：立骨 / 聚气 / 洗药（剧本结构与钩子）
    │   ├── 21-dandao-combat.md                 **炼形**：十一环动力链 / 打击三件套 / 三套物理
    │   ├── 22-dandao-feeding.md                **画符**：七段式 / 六道闸门 / 工程语言清洗
    │   ├── 23-dandao-qc.md                     **九转**：C1~C33 · H1~H12 / 三本账 / 转场门
    │   ├── 24-dandao-asset.md                  **三单**：角色 4 格 / 道具 4 格 / 场景 9 格 / 群像卡
    │   ├── 25-dandao-script.md                 **六候**：剧本六阶段 / 五席圆桌 / 台词七维 / 语速硬指标
    │   ├── 26-daoxue-full-system.md            **道教全体系八支**：哲学 / 易学 / 风水 / 符箓 / 戒律 / 择日 / 宫观
    │   └── route-card-full-source.html        原始 HTML 全量备份（172KB）
    ├── external-libs/             外部四库原库原文（342 文件）
    │   ├── A-short-drama-director/   28 份规则库 ＋ 打戏子库
    │   ├── B-overseas-three-libs/    LIRA / CINEDANCE / ACTING 中文全本
    │   ├── C-yangzi-10skill/         洋子 10-Skill 工程
    │   └── D-laoli-suite/            **漫剧老李全套**：V7.4.26 十二引擎 + V5.0.2 legacy 39 份（MIT）
    ├── templates/                 17 份空白项目模板 ＋ 索引
    │   ├── 01–10                  内容骨架（总索引 / 三资产包 / 分镜 / 机位图 / SOP / 剧本核对 / MasterProfile / 场景锁定）
    │   └── A0–A5                  工程纪律（铁律卡 / 项目状态 / 30秒分镜 / 情绪库 / 剧本过检）
    └── scripts/                   2 个本地脚本（均支持 --dry-run）
```

---

## 🛡️ 安全说明

**本技能自带 2 个脚本**，均支持 `--dry-run`：

| 脚本 | 行为 | 边界 |
|:---|:---|:---|
| `new_project_scaffold.py` | 只用 `os.makedirs` 新建目录 | 不删除 / 不移动 / 不覆盖 / 不联网 / 不读凭据 |
| `init_project_docs.py` | 复制模板并替换占位符 | **默认不覆盖已有文件**（需显式 `--force`） |

> 说明：`init_project_docs.py` 帮助文本标为「只新建，不覆盖」，但实际存在 `--force` 覆盖开关。**不加 `--force` 时行为与说明一致。**

**`external-libs/` 内的第三方脚本不会被本技能执行**，仅作资料保留：

- A 库 2 个 Python：`build_board_lite.py`、`check_fight_prompt.py`（本地文本检查）
- C 库 8 个安装脚本：`安装课程包.ps1` / `新建AI影视项目.ps1` / `配置本地知识库.ps1` / `更新本地知识库.ps1` / `升级旧电影工程规则.ps1` ＋ 3 个 `.command` ＋ `install_course.py`

> ⚠️ 这些是洋子课程包的安装器，会把 Skill 装进 Codex 的 `~/.codex/skills` 并写知识库路径。**运行前请先自己读一遍脚本内容。**

其余全是 Markdown 与一份原版 HTML 备份，无其它可执行代码。

---

## 🏆 赞助与合作

<div align="center">

**这个项目持续维护中。如果你的产品能帮到短剧 / 漫剧创作者，欢迎入驻。**

</div>

### 招商位

| 席位 | 适合谁 | 露出方式 | 状态 |
|:---:|:---|:---|:---:|
| 🥇 **主赞助** | AI 模型渠道 / 算力平台 / API 服务商 | README 顶部横幅位 ＋ 更新记录署名 ＋ 长期展示 | 虚位以待 |
| 🥈 **合作赞助** | 创作工具 / 发行平台 / 课程 / 团队 | 本表格席位 ＋ 功能介绍 ＋ 外链 | 虚位以待 |
| 🥉 **友情赞助** | 个人创作者 | 赞助者名录致谢 | 虚位以待 |

> 💡 **招商说明**：赞助位对 AI 模型渠道、算力平台、API 服务商、创作工具、发行平台及创作团队开放。
> 合作请联系：微信 **17344066178**

### 赞助者名录

感谢以下赞助者对项目的支持：

| 赞助者 | 支持方式 | 联系方式 |
|:---|:---|:---|
| *虚位以待* | — | — |

*你的名字会出现在这里。*

### 联系我

| 渠道 | 账号 |
|:---|:---|
| 📱 微信 | **17344066178** |
| 🐙 GitHub | [@ax2697](https://github.com/ax2697) |
| 💬 Issue | [提交问题或建议](https://github.com/ax2697/xiaozhi-will/issues) |

---

## 📜 更新记录

### v2.3.0 — 2026-10-26 · 判据二轮加固

**变更**

- `SKILL.md` / `references/12` §一二：三才逆行判据从「是否忠于原文，有无增删改」改为 **增/改/删各 = 0**、时间码**无断档**、三包**全 🔒**
- `templates/A5` §3.1–3.6：**28 项**「☐通过 ☐问题」全部补「怎么测」列
- `references/23`：M/S/H 三类各补「怎么验」，并给 H 类两问（接得上 / 好看）
- `references/25`：同口吻三测试补**算法**（标准差怎么算、专属词数几个）；密度铁律补**数法**
- `references/22`：虚假核验第 ⑨ 条补「怎么判」（看得出图才算看过）
- `references/24`：命名一致性补「怎么核」（三处并排抄下来比）

**为什么**

v2.2.0 改的是**主要判据**（六关/五维/三宝/A5 评分）。用同样的标准回头扫，又扫出 6 类漏网：

| 漏在哪 | 原文 | 问题 |
|:---|:---|:---|
| A5 §3.1–3.6 | 「☐通过 ☐问题」+ 空证据列 | **28 项没有任何查法**，全凭感觉勾 |
| 三才逆行 | 「是否忠于原文，有无增删改」 | 又是"是否"，且"有无"不给数 |
| 同口吻三测 | 「标准差 <2 字 → 不合格」 | 有阈值**没给算法**，怎么算标准差？ |
| 密度铁律 | 「≥2 条人声事件」 | 有阈值**没给数法**，什么算一条？ |
| M/S/H | 「真正好看、真正接得上」 | "真正"是加强语气，不是判据 |
| 虚假核验 ⑨ | 「本包看不到图」 | 什么叫"看不到"？ |

**改法举例**

| 原判据 | 现在怎么测 |
|:---|:---|
| 「主线纯度与因果链（抽掉主线是否仍成立）」 | **删掉主线相关场次，看剩下的是不是散了**；散 → 问题 |
| 「行为逻辑与反应合理性」 | 每个关键动作问「**以这个人设会不会这么做**」，能指出动机来源在第几场 |
| 「标准差 <2 字 → 不合格」 | 统计连续 5 句**字数**，用 `STDEV` 算；**<2 字 = 句子太均匀 = 机械** |
| 「真正好看、真正接得上」 | 接得上＝**脸/服装/光向/道具位置**四项逐项比；好看＝**随便暂停一帧，说不说得清在发生什么** |

**设计决策**

- **机检表不加「怎么测」**：M0–M12 由脚本判定，加人工判据反而误导。改为在表前写清**脚本命令 + 回执要求**。
- **给算法不给感觉**：凡涉及数字的判据（标准差、语速、人声密度）一律写出计算方式，否则同一个人两次算出的结果都可能不同。
- **「真正」这类词要拆**：语气词不是判据。「真正好看」必须落成可操作的两问。

**验收**

- 含「☐通过」的判据表 7 个，6 个已带「怎么测/怎么查/怎么验」
- 余 1 个是 M0–M12 机检表，表前已注明 `screenplay_review.py --strict --receipt` 命令与回执要求
- 13 项关键改造逐项确认到位

### v2.2.0 — 2026-10-26 · 全项目判据改为可验证式

**变更**

- `SKILL.md` §〇之零：六关判据从 1 列扩为 3 列（**怎么测 / 硬指标 / 不通过**）；五气朝元五维、三宝自查同步改为可执行
- `references/12-daoxue-cosmology.md` §四 / §六 / §七：同上三处
- `templates/A5-剧本过检清单模板.md` §3.7：九项 95 分制补「怎么测」列
- 全项目新增「**留证据**」硬要求：只写「已核对」「没问题」= 没验，按未通过处理

**为什么**

之前的判据写成「光影、色彩、构图**是否成立**」「结构、比例、材质**是否可信**」——这两句没法判。什么算成立？什么算可信？换个 AI 就是另一个答案。

判据如果不能被第二个人独立复核，它就不是判据，是许愿。

**改法：每条判据必须给三样**

| 列 | 作用 | 反例 → 正例 |
|:---|:---|:---|
| **怎么测** | 具体执行动作 | ❌「光影是否成立」→ ✅「缩到 1/4 图看主体能否与背景分开」 |
| **硬指标** | 可数或可指认 | ❌「材质可信」→ ✅「放大 200% 看手指数对/脚是否悬空/接缝是否错位」 |
| **不通过** | 命中即退回 | ❌「不合格」→ ✅「手指数错/脚悬空/穿模」命中任一 |

**四处改造实例**

| 位置 | 原来 | 现在 |
|:---|:---|:---|
| 六关 · 鼎关 | 「占位符全替换＋目录齐＋参数卡有值」 | 怎么测：检索 `【` / 数目录 / 逐字段看；硬指标：**0 处 / =12 个 / 无空值** |
| 五维 · 脾（笃实） | 「结构、比例、材质是否可信」 | 怎么测：**放大 200%** 看手/脚/五官/接缝；≤2 分：手指数错/脚悬空/穿模 |
| 三宝 · 精不亏 | 「拿默认值顶包、凭记忆动手」 | 怎么查：**说出读过的文件路径 + 参数来源哪一行**；判不过：说不出，或只说"我记得" |
| A5 · 第 7 项 | 「行为逻辑与反应合理性」（空判定列） | 怎么测：每个关键动作问「**以这个人设会不会这么做**」，能指出动机来源在第几场 |

**设计决策**

- **不追求"客观"只追求"可复核"**：审美类判据（明丽）无法完全客观，但可以做到「第二个人按同样动作看图，得出同样结论」。
- **每条判据都要能留证据**：证据形式允许是截图位置 / 对照哪一镜 / 命令输出。没有证据 = 没验。
- **宁可判据粗一点，也要可执行**：把"艺术感觉"写成判据是假精确，不如写"缩到 1/4 图能不能分开主体"。

**验收**

- 真模糊判据（是否成立/是否可信/是否合格/有没有问题）残留 **0** 处
- 剩余 8 处均属「⛔ 不写 XX」的禁止说明或任务描述，非判据
- 四处版本号一致

### v2.1.0 — 2026-10-26 · 明确「用户感知」的定义

**变更**

- `AGENTS.md` 新增「一之二 · 『用户感知』的可执行定义」（本机总纲，不上传）
- `开发状态.md` §〇 速查表同步三条判据 + 决策树 + 四个真实例子

**为什么**

v2.0.0 定规则时只写了「用户能感知的变化才升版本」，但「感知」这个词太模糊——可以解释成任何东西。结果就是规则写了，却判不了。这次把它拆成三条**可验证**的判据。

**三条判据**

| # | 判据 | 一句话检验 |
|:--:|:---|:---|
| 一 | **看得见** | 路径层面有增删改，或实质内容变了（>1KB） |
| 二 | **用得上** | 能写出「用户原本会 X，现在会 Y」且 X≠Y |
| 三 | **修得上** | P0 阻断/P1 误导 → 升；P2 瑕疵/P3 内部 → 不升，攒着 |

命中任一条 = 感知得到 → 升版本。三条都不命中 → 不升。

**判据二 是最硬的一条**：判据一可以靠"文件动了"蒙混，判据三只覆盖修复。判据二要求写出一句具体的「原本 X → 现在 Y」，写不出来就是没感知。

**反例复盘**

规则里附了这次 v2.0.0→5.0.0 七次升版的逐条复盘：3 次该升、3 次不该升（都属于"同一批任务的收尾"）、1 次该直接跳主号而非堆到 5。

**设计决策**

- **不写"重要程度"**：重要与否是主观的，写进规则就没法判。只写"能不能验证"。
- **判据三按 P0–P3 分级**：修复型变更最容易滥升（"我修了 bug 所以升版本"），必须区分"用户踩不踩得到"。
- **附反例而非只写正例**：规则要能防住具体犯过的错，抽象的正面教导没用。

**验收**

- 四处版本号一致（台账 frontmatter / 台账正文 / SKILL / README 标题 + badge）
- 判据在 AGENTS.md 与开发状态.md 两处表述一致

### v2.0.0 — 2026-10-26 · 立道教体系

**一次完整的体系重构。** 从"工程路由卡"升级为"道教体系驱动的影视生产系统"。

#### 一 · 六阶正名（依《性命圭旨》）

| 工序 | 阶名 | 田 | 守哪宝 | 卡哪关 |
|:--:|:---|:--:|:--:|:---|
| P0 立项 | **筑基** | 下丹田·精 | 精 | 鼎关 |
| P1 剧本 | **炼己** | 下丹田·精 | 精 | 药关 |
| P2 资产 | **炼精化气** | 下→中 | 精→气 | 形关 |
| P3 分镜 | **炼气化神** | 中丹田·气 | 气 | 序关 |
| P4 生成 | **炼神还虚** | 中→上 | 气→神 | 验关 |
| P5 交付 | **还虚合道** | 上丹田·神 | 神 | 收关 |

> 六阶是真实道典所载，不是网络修真小说的等级设定（炼气期/筑基期/金丹期属虚构玄幻，未采用）。

#### 二 · 道教全体系八支

内丹只解「怎么炼」，另七支解「炼什么、什么时候炼、跟谁炼、炼到哪停」。

| 支 | 解决什么 | 核心判据 |
|:--:|:---|:---|
| **① 哲学** | 一切判据的"为什么" | 道法自然 / 无为 / 反者道之动；齐物论多视角、庖丁解牛顺结构切 |
| **② 内丹** | 怎么炼 | 六阶六关，候候不到药不真 |
| **③ 易学** | 剧情抉择、分支 | 一场戏要有"反"；六爻即六段；一爻一个分支点 |
| **④ 风水** | 场景布局、机位 | 有遮挡、有纵深、有界限；左主右客；大景看形势小景看理气 |
| **⑤ 符箓** | 视觉符号、仪式 | 符三部位（头/胆/脚）立画面；科仪四段排一场戏 |
| **⑥ 戒律** | 合规红线 | 五戒是红线（杀盗淫妄酒），十善是底线 |
| **⑦ 择日** | 节奏与受众 | 十二建除定集节奏；二十八宿定受众；一剧只主打一象 |
| **⑧ 宫观** | 团队分工 | 谁知道资产在哪（知库）；一日不作一日不食 |

> **边界**：易学与择日只借结构框架，⛔ 不做算命、不做吉凶预测。

#### 三 · 14 份道教化文档（13–26）

| 组 | 文档 | 覆盖 |
|:---|:---|:---|
| **体系** | 12 道教体系 / 26 全体系八支 | 六阶 / 三丹田 / 三宝 / 六关 / 八支 |
| **内容库** | 13 形神谱 / 14 立名 / 15 定形 / 16 调色 | 表演 / 锚点编码 / 六把锁 / 60·30·10 |
| **老李改写** | 17 归位图 / 18 选型 / 19 五机 / 20 剧本 / 21 打戏 / 22 投喂 / 23 机检 / 24 资产 / 25 剧本六候 | 12 引擎全领域，**用道教因果重写而非贴标签** |

**关键改写示例**

| 原机制 | 道教改写 | 改写后多出来的判据 |
|:---|:---|:---|
| 七段式提示词 | **符的七位** | 格式错一个字，整段返工 |
| 机检 C1~C33 | **九转还丹** | M/S/H 三类不可冒充——脚本全绿只是 M 过 |
| 三单提取 | **分药** | 不是"先出图再补设定"，是"先分药再起火" |
| 剧本六阶段 | **采药六候** | 候是验不是手续 |
| 双线峰值不重叠 | **水火既济** | 不是都拉满，是轮流满 |
| 憋屈越久打脸越爽 | **承负** | 今日欠来日还，利息必须给足 |
| 地标挡脸漂移 | **以显代藏** | 不是修脸，是转移注意力 |
| 力从腰起 | **炁行周天** | 路径断了，周天不成 |

#### 四 · 新增模板（09–12）

| 模板 | 作用 |
|:---|:---|
| 09 角色形神卡 | 形五块 + 神三块 + 声谱，解决"念台词机器" |
| 10 场景定形表 | 16 项锁定 + 六锁英文短句 + 调色 + FOV |
| 11 视觉资产对账单 | 定穴 / 挂锚 / 覆率审计 / 放行签字 |
| 12 双轨交济表 | A/B 张力错峰 + 承负账本 |

#### 五 · D 库并入（漫剧老李）

- `external-libs/D-laoli-suite/`：V7.4.26 十二引擎（170 文件）+ V5.0.2 legacy（41 文件）
- **MIT 协议，原文零改动**，版权声明完整保留
- 道教化归类写在我们自己的 17–25 号文档，不侵入原包

#### 六 · 全量核查修复

- 修复 **33 处**路径断链（21 处失效引用 + 12 处路径错误）
- 9 类指令补齐阶 / 关标注
- A1 / A5 模板补道教开篇
- 六阶旧名残留清零

#### 验收

- references 11 → 23 份；templates 13 → 17 份；external-libs 三库 → 四库
- 断链 0；版本号四处一致；两个脚本可运行

### v1.1.0 — 2026-10-22 · 并入《晓之奥义》铁律体系

**新增**

- `templates/A0-铁律卡.md`（3,875 B）：三条顶层铁律 + AI 执行六条 + 各阶段最小必读集 + 交付前必跑三条命令。
- `templates/A1-项目状态模板.md`（10,952 B）：**唯一真相源**骨架，70+ 字段参数卡 + P0–P5 阶段状态 + 回执。
- `templates/A2-30秒分镜表模板.md`（1,550 B）：30 秒固定单元、10 字段、时间码 0.0–30.0 连续校验。
- `templates/A4-情绪关键帧库模板.md`（1,331 B）：4 情绪模块 + 8 种情绪速查（面部/肢体/光影）。
- `templates/A5-剧本过检清单模板.md`（12,623 B）：P1 强制门禁，7 大项逐项签字 + 9 项 95 分制。
- `SKILL.md` 新增「〇、三条铁律」章节，置于全部章节之首。
- `SKILL.md` 新增「〇、三条铁律」章节，置于全部章节之首。
- README 新增「三条铁律」中文段与英文段。
- **核心能力表** 新增 6 行：铁律 / 状态 / 门禁 / 情绪 / 单元 / 三库。
- **常用指令表** 新增 4 条：`/铁律` `/状态` `/过检` `/情绪库`。
- **英文 Core capabilities** 同步扩充 6 行。
- **目录结构** 区分 01–08 内容骨架与 A0–A5 工程纪律。
- **横幅 SVG** 版本号 v1.0.0 → v1.1.0。

**设计决策**

- **不设「免费版 / 会员版」档位**：全部能力并入单一技能 `xiaozhi-will`。
- **A 系列用前缀隔离**：原 01–05 编号与仓内已有 01–08 冲突，改用 `A0`–`A5` 前缀。
- **A1 与 01 分工**：`01-项目总索引` 管「剧是什么」；`A1-项目状态` 管「活干到哪」。

**验收**

- 模板 8 → 13 份，文件 159 → 165 个。

### v1.0.0 — 2026-10-22 · 首发

**新增**

- `SKILL.md`（19,049 字节）：六步响应流程、指令 → 文件路由总表（10 类指令）、机位图四类必读时机、关键帧跳三包取件清单、改动联动表、冲突仲裁 ⑧ 条、交付前自检清单、按需加载表、新剧第一次开工。
- `references/` 8 份方法论：诺兰电影化手法全文（66KB）、A 库流程门、B 库三库要点、P0–P5 逐阶段详解、Seedance 2.5 / SeedAudio 1.0 官方规则、C 库工程组织、剧情三不铁律、新剧立项清单；另附原版 HTML 全量备份（172KB）。
- `external-libs/` A/B/C 三库原库原文，共 130 个文件。
- `templates/` 8 份空白项目模板：总索引参数卡、三资产包、10 字段分镜表、机位图、SOP、剧本三不核对表。
- `scripts/` 2 个本地脚本：`new_project_scaffold.py`（建 21 个目录）、`init_project_docs.py`（落盘 8 份模板），均支持 `--dry-run`。
- `assets/` 2 张自绘 SVG 图（横幅 + 路由示意），不依赖外链图床，永不失效。
- README 中英双语落地页。

**设计决策**

- 采用**路由卡**而非「1 总控 + N 子技能」套装：执行事实源在**用户自己的项目磁盘**，拆成子技能会让每个子项无规则可依。
- 技能 `name` 与安装路径统一为 `xiaozhi-will`。
- 四层职责在单包内分层（路由 / 方法 / 原库 / 执行），靠 `SKILL.md` 串起，不拆目录。

**验收**

- 本地 159 文件 / 925,924 字节，远端 159 blob / 925,924 字节，逐文件比对零缺失。
- 脚本实跑：建目录 21 个、落盘模板 8 份，`py_compile` 通过。
- 全包检索旧名 `short-drama-route-card` 零残留。

<details>
<summary><b>版本路线图</b></summary>

- **v1.1** — 补充常见翻车案例库，把踩过的坑变成前置检查项
- **v1.2** — 新增项目模板快速预览图、路由走查动画
- **v1.3** — 补充英文版方法论摘要（`references/en/`）
- **v2.0** — 视情况评估是否拆分独立子技能

</details>

---

## 📄 来源与保真

来源：《_AI指令文件路由卡_万能模板_新短剧用(1).html》——工作流 ＋ 方法论骨架，**已剥离任何单剧剧本内容**。

原版 HTML 完整备份在 [`references/route-card-full-source.html`](xiaozhi-will/references/route-card-full-source.html)，需要按原始版式回看、整体回抄，或核对是否漏转时直接读它。

> 本仓库只分发**方法与模板**，不包含任何具体剧目的剧本、角色设定或分镜内容。

---

# English

<div align="right"><sub><a href="#-晓之意志--ai-短剧指令路由卡">↑ 回到中文 / Back to Chinese</a></sub></div>

## What is Xiaozhi Will?

**A routing card for AI assistants producing short-form drama.**

It creates nothing on its own. It answers one question:

> **"Given this instruction, which file — and which section of that file — should I read?"**

The answer is written down, so it never depends on the model's memory or on you re-explaining your project structure every session.

## Why it exists

Anyone who has built short drama with AI has hit these three walls:

**1. The AI doesn't know what to read.**
Every session starts with re-explaining: where the asset packs are, where the SOP lives, which version of the storyboard is current.

**2. When two files disagree, nobody knows which one wins.**
Your parameter card says 16:9; a third-party skill defaults to 9:16. Without arbitration rules, the model silently picks one — and doesn't tell you which.

**3. Change one thing, and everything downstream breaks.**
You edit a line of dialogue but forget to update the storyboard. You move a camera but forget the camera plan. You only find out when the renders don't match.

Xiaozhi Will answers these with **one routing table**, **one arbitration priority list**, and **one change-propagation table**.

## Three iron laws

**Rules do not constrain an AI. Iron laws do.** These three override everything else in this card. Break one and you stop and fix it first.

| # | Law | What it means | How you know it is done |
|:--:|:---|:---|:---|
| **1** | **Traceable & reversible** | Every change gets a Git commit (explicit `git add <file>`, never `git add .`); one step, one commit | There is a commit, and it can be reverted alone |
| **2** | **Ran means passed** | Verification scripts run green, with real command output and exit code pasted in; fix the root cause, never edit the test to make it green | Output, exit code, green |
| **3** | **A human confirms** | The AI cannot self-certify. Three levels, never skipped: AI self-check → independent AI verification → your final review | All three have receipts |

### Six execution rules derived from them

1. **Read before answering** — no answer without reading `项目状态.md` or the files named for the current stage
2. **One question, one stop** — advance one confirmation point per turn; never run P0→P5 in a single pass
3. **Never guess, never default** — stop when information is missing; mark assumptions `[assumption]` with consequences
4. **No repeat failures, gather before creating** — back off after three consecutive failures at the same spot
5. **Explicit state, governed context** — restate the goal at kickoff, read memory files across sessions, keep temp artifacts in an AI workspace, close in one of three states ✅/❌/🔄
6. **Find rules, do not read everything** — three kickoff questions: Did I read the rules? Did I build the checklist? Did I restate the state? Any no means do not start

> Plus two practices: **single source of truth** (only `项目状态.md`, no second record) and **no gate skipping**.

## Four checks before you start

Any item left unspecified means **stop and ask** — never silently substitute a default.

| # | Check | Notes |
|:--:|:---|:---|
| ① | Project name + episode | Written into the project's master index parameter card — the single source of truth for locked values |
| ② | Story source | Path to the original novel or user script. The only legitimate source of plot |
| ③ | Aspect ratio + image/video models | e.g. 16:9 + seedream for stills, seedance for video, plus frame rate |
| ④ | Deliverable type | Still image / retouch / video / script / storyboard / edit / QC |

## Four-layer module map

Unlike multi-skill suites, this is **one skill with four internal layers**, wired together by `SKILL.md`:

| Layer | Location | Responsibility |
|:---:|:---|:---|
| **L0 Routing** | `SKILL.md` | Six-step flow, routing table, 8 arbitration rules, change propagation, pre-delivery checklist |
| **L1 Method** | `references/` | 8 methodology briefs: Nolan techniques, A/B/C libraries, Seedance / SeedAudio rules, plot integrity rules, project bootstrap |
| **L2 Raw libraries** | `external-libs/` | 130 files of source material from the three libraries, for deeper reading |
| **L3 Execution** | `templates/` + `scripts/` | 13 blank project templates (8 content + 5 process A0–A5) and 2 local scripts |

## Six-step response flow

| Step | Action | Key point |
|:---:|:---|:---|
| **0** | Read the latest file from disk | Disk state always beats memory; summaries expire |
| **1** | Parse the instruction | Action + object + deliverable type |
| **2** | Method first | Load only the matching sections of `references/` |
| **3** | Read the master index | Parameter card, status, dual numbering, locked version |
| **4** | Collect the first authority + all bound sections | Copy fixed prefixes verbatim; pull upstream and locked assets |
| **5** | Execute · self-check · file it back | SOP check + methodology check + downstream sync + report back |

> **Drawings before construction.** Read the methodology before reading the project files — know *how* before knowing *what*.

## Core capabilities

| Area | What it does |
|:---|:---|
| 🧭 Bootstrap | 8 required project files + placeholder replacement table |
| 📇 Routing | First authority, bound sections (to the exact section), and output destination for 10 instruction types |
| 🎬 Cinematic language | Nolan techniques: non-linear time, flash-forwards, cross-cutting, double hooks — P0, read before any episode |
| ✍️ Script | Six-stage writing chain from source registration to round-table review |
| 📜 Plot integrity | Never add, never alter, never delete — with an explicit whitelist |
| 🖼️ Asset-first | Lock characters, sets and props before they enter the storyboard |
| 🎥 Spatial authority | Four cases where the camera plan is mandatory, two where it isn't |
| 🎬 Storyboard | 10-field shot table with a continuity anchor carried across every shot |
| 🖼️ Keyframes | One cross-pack checklist covering storyboard anchors and all three asset packs |
| 🚀 Prompt feeding | Seedance 2.5 seven hard rules, three-layer decoupling, six-step feeding check |
| 🎵 Audio | SeedAudio 1.0 T2A / A2A constraints |
| 🔗 Propagation | Six change types and exactly what must be updated downstream |
| ⚖️ Arbitration | Eight-level priority order when files disagree |
| ⚖️ Iron laws | Three top-level laws: traceable & reversible, ran means passed, a human confirms |
| 📋 Project state | Single-source-of-truth skeleton: 70+ parameter fields + P0–P5 stage status |
| 🔍 Script gate | 7-section sign-off with a nine-item 95-point scale — any score below 95 blocks submission |
| 🎭 Emotion keyframes | 4 modules (horror / action / emotion / catharsis) + 8 emotion quick-reference rows |
| ⏱️ 30s unit | Fixed 30-second segment with continuous 0.0–30.0 timecode validation |
| 📚 Three libraries | A for process gates, B for prompt writing, C for engineering structure |

## Install

Copy the whole `xiaozhi-will` folder into your skills directory:

| Platform | Location |
|:---|:---|
| **WorkBuddy** | `C:\Users\<you>\.workbuddy\skills\xiaozhi-will\` (macOS / Linux: `~/.workbuddy/skills/xiaozhi-will/`) |
| **OpenClaw** | `openclaw skills install ./xiaozhi-will --as xiaozhi-will` |
| **Coze / Dify / any LLM** | Paste `SKILL.md` into the system prompt, upload `references/` as the knowledge base |

Trigger it by saying things like *"follow the route card"*, *"which files should this instruction read?"*, *"start episode N"*, or *"new drama setup"*.

## Quick start

```bash
# Dry run first — shows what would be created, changes nothing
python scripts/new_project_scaffold.py "<project_root>" --season S1 --episode E1 --dry-run

# Create the folder skeleton (21 directories, never deletes or overwrites)
python scripts/new_project_scaffold.py "<project_root>" --season S1 --episode E1

# Drop in the 8 templates and substitute placeholders (never overwrites by default)
python scripts/init_project_docs.py "<project_root>" --season S1 --episode E1
```

## Three standing rules

| | Rule | Meaning |
|:---:|:---|:---|
| ⓪ | **Disk beats memory** | Read the file before acting; never work from recall |
| ⑦ | **This project's `.md` beats any external skill** | Third-party defaults (9:16, 21:9, "high-octane" presets) never override your locked values |
| ⑧ | **Story source > master outline > episode outline / script / storyboard** | The plot has exactly one legitimate source |

## Security

Two bundled scripts, both supporting `--dry-run`:

- `new_project_scaffold.py` — only calls `os.makedirs`. No deletion, no moves, no overwrites, no network, no credential access.
- `init_project_docs.py` — copies templates and substitutes placeholders. **Never overwrites existing files** unless you pass `--force`.

Third-party scripts inside `external-libs/` are **never executed by this skill**. They are kept for reference only. The eight installer scripts from the C library will write into `~/.codex/skills` — **read them before running**.

## Sponsor

This project is actively maintained. If your product helps short-drama creators, get in touch.

| Tier | Best for | Visibility |
|:---:|:---|:---|
| 🥇 Main sponsor | Model providers, GPU/API platforms | Top banner + release notes credit |
| 🥈 Partner | Creative tools, distribution, courses | Table slot + link |
| 🥉 Supporter | Individual creators | Name in the sponsor list |

Contact: WeChat **17344066178** · GitHub [@ax2697](https://github.com/ax2697)

## Changelog · License

See the Chinese 更新记录 section above for the full changelog.

**[MIT](LICENSE)** — free to use, modify and redistribute.

---

<div align="center">

**[MIT License](LICENSE)** · 用得好就点个 ⭐ · Star it if it helps

<sub>晓之意志 · 让 AI 先读对文件，再动手</sub>

</div>
