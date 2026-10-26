# 15 · CINEDANCE 六把锁 · 可直接复制的英文短句

> **补的是原始路由卡 9.10.6 缺口清单第一梯队第 ③ 项**——「机位图加 CINEDANCE 六把锁文字描述（英文短句，供 P4 复制）」。
> 原卡状态：「每场景 CINEDANCE 六把锁文字描述」缺失，导致 P4 每次都要重新想。本文件给出**填一次、全剧复用**的模板。

---

## 一、六把锁是什么

视频提示词最容易崩的五件事：**首帧空、空间乱、视线错、地标丢、跨镜断**。CINEDANCE 用六把锁分别钉死。

| # | 锁 | 钉死什么 | 不锁会怎样 |
|:--:|:---|:---|:---|
| **①** | **首帧占用**（First-frame occupancy） | 第 0 帧画面里谁在哪、占多大 | 首帧空镜，模型自由发挥，人物凭空出现 |
| **②** | **空间调度**（Spatial scheduling） | 人物在场景里的坐标关系 | 站位漂移，两人距离忽远忽近 |
| **③** | **视线-朝向分离**（Gaze-heading separation） | 脸朝哪 ≠ 眼看哪 | 视线与朝向绑死，转头就是瞪人 |
| **④** | **地标邻近**（Landmark proximity） | 用具体参照物锚定位置 | 只说"旁边"，模型不知道旁边是哪 |
| **⑤** | **多镜连续性**（Multi-shot continuity） | 镜与镜之间什么必须不变 | 切镜后衣服/光线/站位全变 |
| **⑥** | **上下文隔离**（Context isolation） | 当前镜只吃当前镜的信息 | 上一镜的残留污染这一镜 |

> **一句话记法**：**①谁在场 ②站哪里 ③看哪里 ④靠近什么 ⑤接得上 ⑥不串味。**

---

## 二、写法总则

| 规则 | 说明 |
|:---|:---|
| **英文写** | 直接投喂，不翻译。中文解释另起注释 |
| **短句** | 一句一锁，不超过 20 词。不写成段落 |
| **正向陈述** | 写"是什么"，不写"不要什么"（负向归 Layer 3） |
| **可量化** | 距离用 `within 1 meter`，不用 `near`（弱词禁用） |
| **每场景一套** | 同一场景跨集复用，改动需在总索引登记 |
| **不写风格** | 风格归 Layer 1，锁只管空间与连续性 |

### 弱词黑名单（必须替换）

| ❌ 弱词 | ✅ 替换 |
|---|---|
| near / around | `within 1 meter` / `within 2 meters` |
| beside | `at arm's length on his left` |
| in front of | `occupying the near third of frame, facing camera-left` |
| background | `in the far plane, out of focus, 4 meters behind` |
| someone / people | 具体码 + 位置 |

---

## 三、六把锁模板（填空即用）

### ① 首帧占用

```
Frame 0: @CHR-ZQ01 fills the centre third, head and shoulders in frame,
back to the door, feet planted shoulder-width.
```

**填空位**：谁 / 占画面多大 / 朝向 / 姿态。

> **硬要求**：第 0 帧必须有主体。**空镜首帧 = P4 阻断**（模型会自由生成，且首帧决定整段运动方向）。

### ② 空间调度

```
Spatial: @CHR-ZQ01 stands 1.2 meters from the altar, facing camera-left;
@CHR-ZQ02 holds the doorway at 3 meters behind him, facing camera-right.
```

**填空位**：每个人 / 距锚点物多远 / 朝哪个方向 / 相互关系。

> 两人同框时，必须写清**谁在前谁在后、相距多少、朝向是否对视**。缺任一项，站位必然漂。

### ③ 视线-朝向分离

```
Gaze: head angled 15 degrees camera-right; eyes locked on @CHR-ZQ02's hands,
not his face.
```

**填空位**：头偏多少度 / 眼看具体什么。

> 这一锁最容易被漏。**不写清楚，模型默认"脸朝哪眼看哪"**，所有"斜视""偷瞄""不敢直视"全演不出来。

### ④ 地标邻近

```
Landmark: his right shoulder sits within 20 cm of the doorframe's worn edge;
the enamel cup rests on the sill at hip height to his left.
```

**填空位**：身体某部位 / 距某个可见参照物多远 / 参照物在哪。

> **为什么不用"旁边"**：模型不知道旁边是哪。必须给**画面里看得见的东西**当参照，并给距离。

### ⑤ 多镜连续性

```
Continuity: keep @CHR-ZQ01's coat collar open, the cup in his right hand,
and the window light falling from camera-left across all shots in this group.
```

**填空位**：这组镜头里**哪些绝不能变**（服装状态 / 持物 / 光向 / 站位）。

> 只在**一组多镜**时写。单镜可省。

### ⑥ 上下文隔离

```
Sealed: this shot contains only @CHR-ZQ01 and @PRP-ZQ01; no other characters,
no furniture from the previous scene.
```

**填空位**：本镜只包含什么 / 明确排除什么。

> **这是防"串味"的**。上一镜有第三个人，这一镜模型会自作主张把他带进来。必须封死。

---

## 四、整套范例（一场戏六把锁齐）

### 场景：祠堂正厅（@SCN-ZQ01）· 林昭独处

```
① Frame 0: @CHR-ZQ01 fills the centre third, head and shoulders in frame,
   back to the altar, feet planted shoulder-width, coat collar open.

② Spatial: @CHR-ZQ01 stands 1.5 meters from the altar table, facing
   camera-left at 30 degrees off-axis; no other character in the room.

③ Gaze: head angled 10 degrees camera-left; eyes lowered to the enamel cup
   in his right hand, not toward the door.

④ Landmark: his left shoulder sits within 30 cm of the altar table's corner;
   the cup is at chest height, 40 cm in front of his sternum.

⑤ Continuity: keep the coat collar open, the cup in his right hand, and
   window light falling from camera-left across all shots in this group.

⑥ Sealed: this shot contains only @CHR-ZQ01 and @PRP-ZQ01; no other
   characters, no furniture from the previous scene.
```

---

## 五、FOV° 六档对照（不用 mm）

CINEDANCE 规定**用视角度数，不用毫米焦距**——因为模型对角度响应更准。

| FOV° | 大致对应 | 视觉结果 | 什么时候用 |
|:--:|:---|:---|:---|
| **8°** | 超长焦 | 极度压缩，背景糊成一片，人脸占满 | 情绪特写、窥视感 |
| **18°** | 长焦 | 压缩明显，人物与背景贴近 | 对话正反打、私密感 |
| **29°** | 中长焦 | 接近人眼，最自然 | 常规叙事（**默认**） |
| **47°** | 标准 | 略有透视，空间开始展开 | 中景、人物带环境 |
| **84°** | 广角 | 透视夸张，边缘拉伸 | 空间交代、压迫感 |
| **107°** | 超广角 | 强烈畸变，包裹感 | 极端环境、眩晕 |

### 防漂移短语（必须跟一个）

只给度数，模型仍会漂。**每个 FOV° 后必须跟一句"可见结果"**：

| FOV° | 跟这句 |
|:--:|:---|
| 8° | `background compresses into a flat wash; face fills 70% of frame` |
| 18° | `shoulders and background sit within 30 cm of apparent depth` |
| 29° | `natural human-eye perspective, no edge distortion` |
| 47° | `walls converge slightly; room depth reads clearly` |
| 84° | `doorframe edges stretch; foreground hand appears oversized` |
| 107° | `corners bow outward; ceiling curves into frame` |

> **长焦 ≥4、广角 ≥3 可见结果短语**：意思是长焦类（8/18/29°）至少写 4 个视觉结果，广角类（84/107°）至少 3 个。否则必漂。

---

## 六、硬切六式（多镜只许这六种）

CINEDANCE 规定：**默认单镜头；多镜只许硬切，禁淡叠化。**

| 式 | 名称 | 用法 | 英文标记 |
|:--:|:---|:---|:---|
| 1 | **HARD** | 直接切，无过渡 | `HARD CUT` |
| 2 | **SMASH** | 冲击切，配合动作峰值 | `SMASH CUT on impact` |
| 3 | **MATCH** | 匹配切，形状/动作对齐 | `MATCH CUT on the cup` |
| 4 | **INSERT** | 插入切，切细节 | `INSERT CUT to the hand` |
| 5 | **REVERSE** | 反打切，正反打 | `REVERSE CUT to the doorway` |
| 6 | **WHIP** | 甩镜切，快速摇过去 | `WHIP CUT camera-left` |

> ⛔ **禁**：`dissolve` `fade` `cross-dissolve` `morph`。模型对叠化处理极差，一定糊。

---

## 七、二十问静默 QA（出稿前自查，不写进 Prompt）

写完提示词，心里过这 20 条。有一条不过，回去改。

| # | 问 | 归属锁 |
|:--:|:---|:--:|
| 1 | 第 0 帧有主体吗？ | ① |
| 2 | 主体占画面比例写了吗？ | ① |
| 3 | 每个人物都有位置吗？ | ② |
| 4 | 距离是具体数值还是弱词？ | ② |
| 5 | 朝向用画左画右表述了吗？ | ② |
| 6 | 头偏角度写了吗？ | ③ |
| 7 | 眼睛看的是具体什么？ | ③ |
| 8 | 视线与朝向是分离的吗？ | ③ |
| 9 | 有具体参照物吗？ | ④ |
| 10 | 参照物在画面里看得见吗？ | ④ |
| 11 | 距离是 within X 吗？ | ④ |
| 12 | 多镜时写了"什么不能变"吗？ | ⑤ |
| 13 | 组内光线方向一致吗？ | ⑤ |
| 14 | 本镜排除了不该有的东西吗？ | ⑥ |
| 15 | 上一镜的残留清掉了吗？ | ⑥ |
| 16 | FOV 是度数不是 mm 吗？ | 光学 |
| 17 | FOV 后跟了可见结果短语吗？ | 光学 |
| 18 | 多镜用了硬切六式之一吗？ | 切镜 |
| 19 | 没有叠化/淡入淡出吗？ | 切镜 |
| 20 | 守 180° 轴线了吗？ | 空间 |

**20 问全过，才交稿。**

---

## 八、自查

- [ ] 六把锁都写了，无一遗漏
- [ ] 全英文、短句、一句一锁
- [ ] 第 0 帧有明确主体 + 占比
- [ ] 距离全用 `within X meter`，无弱词
- [ ] 视线与朝向分离，且写了具体看什么
- [ ] 地标是画面内可见物 + 数值距离
- [ ] 多镜组写了连续性清单
- [ ] 每镜有 sealed 行
- [ ] FOV 用度数，后跟可见结果短语（长焦≥4 / 广角≥3）
- [ ] 多镜只用硬切六式，无叠化
- [ ] 20 问自检全过

---

## 九、一句话

> **六把锁不写，模型就自由发挥；自由发挥的片子，十次里九次接不上。**
> 锁是给模型的约束，也是给返工的止损。
