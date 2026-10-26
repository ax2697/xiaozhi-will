# 13 · Master Acting Profile 与 Voice Prompt

> **这一份补的是原始路由卡 9.10.6 缺口清单里的第一梯队第 ① 项**——「角色包加 Master Acting Profile + Voice prompt（【常驻角色】）」。
> 该项在原始卡里的状态是「唯一建议新增的前置资产（待用户拍板，AI 不自行开工）」。本文件即该资产的**可直接落盘的规格与范例**。

---

## 一、为什么需要它

角色包现有 x.1 设定图 / x.2 表情 / x.3 姿态 / x.4 服装 / x.5 锚点——**全是"长什么样"，没有一句"怎么演"**。

结果是：AI 出视频时只能靠台词推表演，角色变成**念台词机器**：情绪直给、动作无动机、每场演法一样。

Master Acting Profile 解决的就是这件事：**给每个常驻角色一份"行为说明书"**，写死他的身体习惯、心理引擎、语言节奏。写视频提示词时按场景改写，而不是每次重新想象。

> **公理**：表演是**压力下的行为**，不是情绪展示。
> 「他要什么 → 被什么挡住 → 于是他怎么做」——情绪是这三步的副产品，永远不直接写。

---

## 二、写在哪、怎么用

| 项 | 规定 |
|---|---|
| **放哪** | 角色包该角色 `x.6 专属基底` 附近，新增 **`x.7 Master Acting Profile`** 与 **`x.8 Voice Prompt`** |
| **谁要写** | 【常驻角色】一人一份。一次性配角只写一行 Voice，不写 Profile |
| **篇幅** | Profile **150–220 词英文流水段**（固定块顺序，不写小标题、不写要点符号，连成段） |
| **语言** | 英文（直接投喂给视频模型）；中文解释写在旁边的注释块，不进 Prompt |
| **写什么** | 只写**可观察行为**：身体传记 / 心理引擎 / 声音 / 带触发的 tic / 命名步态 / "However, when X" 裂缝 / 唯一柔软对象 / 眼活 |
| **不写什么** | ⛔ 不写服装、不写机位、不写色彩（那些归 x.4 / 机位图 / 调色板） |
| **冲突** | 不得与角色包既有视觉锚点（x.5）冲突。冲突时以 x.5 为准，改 Profile |
| **用法** | P4 写视频提示词时**按场景改写**为现场表演段，**禁止整段粘贴**。Voice 有台词逐字粘贴，无台词省略 |

---

## 三、固定块顺序（八块，缺一不可）

按这个顺序连成一段，不要打乱。每块一两句，总量控制在 150–220 词。

| # | 块 | 写什么 | 反例（别这么写） |
|:--:|:---|:---|:---|
| ① | **身体传记**（Body biography） | 这个人身体经历过什么，留下的痕迹：旧伤、职业习惯、常年姿势 | "他很帅" |
| ② | **心理引擎**（Psychological engine） | 驱动他的那一个核心匮乏或执念，一句话 | "他很复杂" |
| ③ | **声音**（Voice） | 音色、语速、口音、音量基线、紧张时怎么变 | "声音好听" |
| ④ | **带触发的 tic**（Triggered tic） | 什么情境下出现什么小动作。**必须写触发条件** | "他有时会摸鼻子"（没触发） |
| ⑤ | **命名步态**（Named gait） | 给他走法起个名字，便于跨场复用 | "走路自然" |
| ⑥ | **"However, when X…" 裂缝** | 唯一的失态条件。**必含此句式** | 只写"他很冷静"（没裂缝） |
| ⑦ | **唯一柔软对象**（One soft object） | 他唯一会卸下防备的人或物 | 无 |
| ⑧ | **眼活**（Eye life） | 视线习惯：看不看人眼睛、思考时看哪、说谎时眼神 | "眼神有戏" |

> **为什么 ⑥ 是硬要求**：没有裂缝的角色演不出层次。所有场次都稳如磐石，观众看不到人，只看到设定。

---

## 四、范例（照这个密度写）

### 范例 A · 冷面执法者（男，四十上下）

```
He spent nineteen years on night patrol before the desk job, and his right
shoulder still sits a centimeter lower than the left from a door that slammed
wrong. His engine is simple: he believes order is the only thing standing
between people and the dark, and he has never once been thanked for holding it.

Voice sits low and flat, sentences trimmed to their load-bearing words, and it
drops half a step quieter—not louder—when he is losing control. When someone
lies to him he stops blinking and lets the silence run two seconds longer than
comfortable; when he is tired he presses his thumb into the old scar under his
jaw. He walks like a man carrying something breakable, weight forward, no swing.
However, when a child is in the room, his shoulders come down and his voice
gains a warmth that surprises everyone who knows him. His one soft object is a
chipped enamel cup he refuses to replace. He looks at mouths when people speak,
not eyes—except when he is about to say something true.
```
（约 185 词，八块齐全）

### 范例 B · 少年学徒（女，十六七）

```
She grew up carrying water up four flights, so her forearms are stronger than
anyone expects and she still grips things with her whole hand. Her engine is the
fear of being sent back—back to the village, back to being nobody—so she says yes
too fast and then regrets it visibly.

Her voice runs quick and bright, tripping over the ends of sentences, and climbs
even faster when she is nervous. When she is trying to impress someone she
over-explains and then catches herself and stops mid-word. Her gait has a name
among the others: the half-run—three fast steps, one hesitation, three fast
steps, as if she is always slightly late. However, when she is handed real
responsibility, her whole body slows down and her voice drops into something
steady that sounds ten years older. Her one soft object is a folded paper crane
in her sleeve. She watches hands, not faces, when she is learning something.
```
（约 175 词）

---

## 五、Voice Prompt（x.8）

Profile 管"整个人怎么演"，Voice 管"这一句话怎么说"。**单独一条，短**。

### 格式

```
[角色名] · Voice: <音色一句话> | pace <语速> | pitch <音高> | rasp <沙哑度> | accent <口音> | baseline <情绪基线> | stress-shift <紧张时怎么变>
```

### 范例

```
林昭 · Voice: low male baritone, slight gravel on long vowels | pace slow, 0.9x | pitch low-mid | rasp light | accent neutral-northern | baseline flat, withheld | stress-shift: quieter and slower, never louder
```

### 三条硬规则

1. **有台词 → 逐字粘贴进音频层**；无台词 → 整条省略，不要写「沉默」占位。
2. **不写情绪形容词**（"愤怒地说" ❌）——写**声学参数**，情绪由表演段承载。
3. **同一角色跨集不变**。要改必须先改角色包 x.8，并在总索引登记变更。

---

## 六、自查（写完逐项打勾）

- [ ] 150–220 词，英文流水段，无小标题无要点符号
- [ ] 八块齐全，顺序未乱
- [ ] ④ tic **带触发条件**（"when…" 开头）
- [ ] ⑥ 含 `However, when X…` 句式
- [ ] ⑦ 唯一柔软对象具体（不是"家人"这种泛称）
- [ ] ⑧ 眼活写了"看哪 / 不看哪"
- [ ] ⛔ 没写服装、机位、色彩
- [ ] 与 x.5 视觉锚点无冲突
- [ ] Voice 一行，含六参数 + stress-shift
- [ ] 中文解释只在注释块，不进 Prompt

---

## 七、与 15 种坏表演的对照

写完 Profile，拿这 15 条反查一遍。命中任一条，回去改。

| # | 坏表演 | Profile 里对应的修法 |
|:--:|:---|:---|
| 1 | 情绪直给（直接演"愤怒"） | 写 ② 心理引擎 + ③ 声音变化，让愤怒从行为里长出来 |
| 2 | 无动机动作 | ② 引擎必须能被翻译成"他要什么" |
| 3 | 每场演法一样 | ⑥ 裂缝 + ④ 触发 tic 制造场次差异 |
| 4 | 念台词机器 | ⑤ 命名步态 + ⑧ 眼活，让人在说话之外也在演 |
| 5 | 视线乱飘或死盯 | ⑧ 明确"看哪 / 不看哪" |
| 6 | 手无处放 | ④ tic 给手一个默认位置 |
| 7 | 走位随机 | ⑤ 命名步态定死走法 |
| 8 | 情绪无过渡 | ⑥ 给出失态边界，过渡才有落点 |
| 9 | 全员同一语速 | ③ + ⑧ Voice 逐人区分 |
| 10 | 紧张就提高音量 | ③ 明确 stress-shift 方向（多为降低） |
| 11 | 用形容词写表演 | 全篇只写可观察行为 |
| 12 | 角色无过去 | ① 身体传记 |
| 13 | 对谁都用一副面孔 | ⑦ 唯一柔软对象 |
| 14 | 无破防时刻 | ⑥ 裂缝 |
| 15 | 眼无神 | ⑧ 眼活 |

---

## 八、一句话

> **Profile 不是人物小传，是行为说明书。**
> 小传写"他是谁"，Profile 写"他在压力下会怎么做"。
> 只有后者，模型才演得出来。
