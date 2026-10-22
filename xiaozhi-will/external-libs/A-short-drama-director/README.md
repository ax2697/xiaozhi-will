# short-drama-director 专项模块（整合版）
> 规则单一真相源：见 references/00a-规则总库.md


> 本模块整合自「漫剧老李 short-drama-director V6.8」中与晓之奥义不重复的专项能力。
> 仅提供方法参考，不建立第二套流程、目录或项目状态。与晓之奥义 SKILL.md / 项目状态冲突时以晓之奥义为准。

## 引用映射（原 V6.8 权威文件 → 晓之奥义对应物）

以下文件在原 V6.8 中被本模块多个文件反复引用，因与晓之奥义现有能力重复而未复制，按此表对应：

| 原 V6.8 引用 | 晓之奥义对应文件 / 规则 |
|---|---|
| `model-adapters.md`（模型版本锁定/语法/禁写清单） | `references/29-seedance-2-5-prompt.md`、`references/17-wanxiang-3-prompt.md`、`references/runtime-config.json` |
| `aspect-ratio-adaptation.md`（画幅路由） | 画幅由用户确认并写入 `项目状态.md`，`references/runtime-config.json` 承载枚举 |
| `asset-first-pipeline.md`（Asset-First 六阶段） | 晓之奥义 P0～P5 路由（SKILL.md） |
| `quality-gate-review.md`（P0~P2 质检/声音三层） | `references/06-p5-quality.md`、`references/22-review-feedback.md` |
| `seedance-render-engine.md`（投喂主模板/时长预算） | `references/05-p4-generation.md`、`references/23-generation-execution.md` |
| `production-ledger-handbook.md`（CHR/SCN 台账） | `项目状态.md`（唯一台账，中文类别＋两位流水号） |
| `emotion-beat-curve.md`（12 节拍情绪曲线） | `references/02-p1-screenplay.md`（12 节拍诊断）+ `scripts/generate_emotion_curve.py` |
| `spatial-reference-system-V3.md`（V3 空间系统） | `references/21-spatial-transition-preflight.md`（空间预检） |
| `screenplay-gate-engine.md`（五阶门控剧本） | `references/02-p1-screenplay.md`、`references/19-screenwriting-performance.md` |
| `platform-safety-compliance-guide.md`（平台合规） | `references/31-all-ai-film-formats-and-compliance.md` |
| `cinematic-dramaturgy-rules.md`（视听文法） | `references/26-shot-group-directing.md`、`references/20-specialized-directing.md` |

## 本模块文件清单（27 refs + 1 script）

- 表情/表演：`★ facs-micro-expression.md`（FACS 总控）、`facs-au-dictionary.md`（AU 字典）、`facs-emotion-recipes.md`（情绪配方）、`wenxi-micro-expression.md`（文戏六阶段）
- 台词：`dialogue-doctor-7d.md`（七维诊断）、`dialogue-speed-check.md`（语速自检）
- 武打：`action-previs-15grid.md`（15格PREVIS）、`combat-direction-engine.md`（导演引擎）、`combat-rhythm-defense3state.md`（防守三态）、`action-cinematography-breakdown.md`（华语拉片）、`action-ultimate-finisher.md`（终结技）、`authentic-martial-taxonomy.md`（武学兵器库）、`martial-arts-arsenal.md`（招式库）、`martial-arts-combat-library.md`（实战库）、`xuanhuan-magic-combat.md`（玄幻法术）、`anime-ultimate-vfx-paradigm.md`（二次元大招）
- 镜头/空间：`camera-specs-15rules.md`（15秒规格）、`camera-transitions-6types.md`（转场六式）、`spatial-topview-camera.md`（顶视图CAM1~4）
- 资产/灯光/美学：`asset-spatial-ledger.md`（资产空间台账）、`character-lineage-and-sheets.md`（角色亲缘推导）、`lighting-and-antifake.md`（光线物理）、`audiovisual-aesthetic-presets.md`（美学预设）
- 流程增强：`★ prompt-feeding-checklist.md`（投喂清单）、`agent-platform-adapters.md`（多平台适配）、`comfyui-canvas-automation.md`（Canvas 自动化）、`storyboard-board-lite.md`（离线看板）
- 脚本：`scripts/build_board_lite.py`（md → 单文件 HTML 看板）
