#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
seedance-fight-sequence 交付前自检器

用法:
    python check_fight_prompt.py <提示词文件>

退出码:
    0 = 无硬缺项（可能带建议 W 系列）
    1 = 有硬缺项（H 系列），逐条列出
    2 = 用法错误（未传参 / 文件不存在）

判据编号与 references/04-交付与自检.md 的 21 项清单一一对应。
纯标准库，无第三方依赖。

⚠️ 实现注意：本文件内的提示消息**一律用字符串拼接**，不要用 % 格式化——
消息里会带字面 % 号（如百分比），与 %s 冲突会抛 TypeError。
"""

import os
import re
import sys

HARD = []
WARN = []


def fail(code, msg):
    HARD.append((code, msg))


def warn(code, msg):
    WARN.append((code, msg))


# ── 敏感词（必换档）────────────────────────────────────────────
MUST_REPLACE = [
    "血", "死", "战争", "战斗", "打斗", "打架", "斗殴",
    "子弹", "机炮", "火炮", "大炮", "导弹", "火箭弹", "枪",
    "开火", "扫射", "射击", "爆炸", "炸毁", "摧毁",
    "尸", "自杀", "自毁", "追猎", "猎杀", "击中", "打中",
    "垂死", "临死",
]

# 替换词里不得回用的敏感词根（H17）
BAD_ROOTS = ["炸损", "炸裂", "炸开", "摔伤", "灼伤", "割伤"]

# 首帧暗色痕迹的合法写法
DARK_WORDS = ["深色污渍", "暗色湿痕", "暗色痕迹", "暗色湿渍", "深色湿痕"]

# 群体场景触发词
GROUP_WORDS = ["围攻", "千军", "群战", "混战", "敌群", "以一敌多", "以一敌千"]

# 场景类型 → 节点数区间
NODE_RANGE = {
    "宏大": (4, 6),
    "中等": (3, 4),
    "狭小": (1, 2),
}

CATEGORIES = [
    "动作姿态", "武器", "特效画质", "镜头节奏",
    "场景逻辑", "位移穿梭", "人物比例", "结局",
]


def read_text(path):
    for enc in ("utf-8", "utf-8-sig", "gbk"):
        try:
            with open(path, "r", encoding=enc) as f:
                return f.read()
        except (UnicodeDecodeError, LookupError):
            continue
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        return f.read()


def find_section(text, start_kw, end_kws):
    """取 start_kw 到最近的 end_kw 之间的文本；找不到返回空串。"""
    i = text.find(start_kw)
    if i < 0:
        return ""
    j = len(text)
    for kw in end_kws:
        k = text.find(kw, i + len(start_kw))
        if k > 0:
            j = min(j, k)
    return text[i:j]


def to_seconds(mm, ss, cs):
    return int(mm) * 60 + int(ss) + int(cs) / 100.0


def main():
    if len(sys.argv) < 2:
        print("用法: python check_fight_prompt.py <提示词文件>")
        return 2
    path = sys.argv[1]
    if not os.path.exists(path):
        print("文件不存在: " + path)
        return 2

    text = read_text(path)
    flat = text.replace("　", " ")

    # ── 分区 ────────────────────────────────────────────────
    sec_total = find_section(flat, "正向总述", ["逐段分镜"])
    sec_shots = find_section(flat, "逐段分镜", ["收尾总结"])
    sec_sum = find_section(flat, "收尾总结", ["负面提示词"])
    sec_neg = find_section(flat, "负面提示词", ["\n\n\n"])

    # ── H1 四部分齐 ─────────────────────────────────────────
    missing = []
    if "正向总述" not in flat:
        missing.append("正向总述")
    if "逐段分镜" not in flat:
        missing.append("逐段分镜")
    if "收尾总结" not in flat:
        missing.append("收尾总结")
    if "负面提示词" not in flat:
        missing.append("负面提示词")
    if missing:
        fail("H1", "四部分不全，缺：" + "、".join(missing))

    # ── H2-H5 槽位 ─────────────────────────────────────────
    if "【场景描述】" not in flat:
        fail("H2", "缺【场景描述】槽位")
    else:
        if not re.search(r"场景类型[：:]\s*(宏大|中等|狭小)", flat):
            warn("H2", "【场景描述】未标注场景类型（宏大/中等/狭小）——节点数分档缺判据来源")
    if "【角色A】" not in flat:
        fail("H3", "缺【角色A】槽位")
    if "【角色B】" not in flat:
        fail("H4", "缺【角色B】槽位")
    if "【核心规则】" not in flat:
        fail("H5", "缺【核心规则】槽位")

    core = ""
    m = re.search(r"【核心规则】([^\n]*)", flat)
    if m:
        core = m.group(1)

    # ── H6-H10 核心规则必含项 ───────────────────────────────
    for code, kw, label in [
        ("H6", "时长", "时长"),
        ("H7", "镜头数量", "镜头数量"),
        ("H8", "平均单镜", "平均单镜"),
        ("H9", "场景节点数", "场景节点数"),
        ("H10", "结尾方式", "结尾方式"),
    ]:
        if core and kw not in core:
            fail(code, "【核心规则】未写「" + label + "」")

    # ── H11 群体场景 ────────────────────────────────────────
    if any(w in flat for w in GROUP_WORDS):
        if "【群体/敌方】" not in flat:
            fail("H11", "出现群体/围攻/混战场景，但缺【群体/敌方】槽位")
        if "敌我数量比" not in flat:
            fail("H11", "出现群体场景，但【核心规则】未写「敌我数量比」")

    # ── 解析镜次 ────────────────────────────────────────────
    shot_lines = re.findall(r"^镜头\s*(\d+)\s*[｜|].*$", flat, re.M)
    shot_headers = re.findall(r"^镜头\s*\d+\s*[｜|].*$", flat, re.M)
    time_re = re.compile(
        r"(\d{1,2}):(\d{2})\.(\d{1,2})\s*[-—~－]\s*(\d{1,2}):(\d{2})\.(\d{1,2})"
    )

    if len(shot_headers) < 4:
        fail("H12", "分镜镜次不足 4 个（实际 " + str(len(shot_headers))
             + " 个）——镜次格式应为：镜头N｜起止时间｜场景位置｜景别·运镜方式")

    no_time = []
    durs = []
    for line in shot_headers:
        tm = time_re.search(line)
        if not tm:
            no_time.append(line.strip()[:40])
            continue
        a = to_seconds(tm.group(1), tm.group(2), tm.group(3))
        b = to_seconds(tm.group(4), tm.group(5), tm.group(6))
        durs.append(b - a)
    if no_time:
        fail("H13", "以下镜次缺起止时间：" + " / ".join(no_time[:5]))

    # ── H14 每镜时长 ────────────────────────────────────────
    bad_dur = []
    for idx, d in enumerate(durs):
        if d < 0.5 - 1e-6 or d > 1.5 + 1e-6:
            bad_dur.append("第 " + str(idx + 1) + " 个镜次 = " + ("%.2f" % d) + " 秒")
    if bad_dur:
        fail("H14", "镜长超出 0.5-1.5 秒：" + "；".join(bad_dur[:5]))

    # ── H15 镜数与平均单镜 ──────────────────────────────────
    dec_cnt = None
    m = re.search(r"镜头数量[：:]\s*(\d+)", flat)
    if m:
        dec_cnt = int(m.group(1))
    elif re.search(r"共\s*(\d+)\s*镜", flat):
        dec_cnt = int(re.search(r"共\s*(\d+)\s*镜", flat).group(1))

    real_cnt = len(shot_headers)
    if dec_cnt is None:
        warn("H15", "未找到「镜头数量：N」的声明，无法核对镜数")
    elif dec_cnt != real_cnt:
        fail("H15", "声明镜数 " + str(dec_cnt) + " 个，实际 " + str(real_cnt)
             + " 个——增删镜头后须回头同步【核心规则】")

    dec_dur = None
    m = re.search(r"时长[：:]\s*(\d+(?:\.\d+)?)\s*秒", flat)
    if m:
        dec_dur = float(m.group(1))
    if dec_dur and real_cnt:
        avg = dec_dur / real_cnt
        if avg < 0.75 - 1e-6 or avg > 0.95 + 1e-6:
            fail("H15", "平均单镜 = " + ("%.2f" % dec_dur) + " ÷ " + str(real_cnt)
                 + " = " + ("%.3f" % avg) + " 秒，落在 0.75-0.95 区间之外——"
                 + "先定镜数再算平均，落在区间外说明排镜有误")

    # ── H16 必换敏感词 ──────────────────────────────────────
    hits = []
    for w in MUST_REPLACE:
        if w in flat:
            hits.append(w)
    if hits:
        fail("H16", "命中必换敏感词：" + "、".join(hits)
             + "（须按 references/03 替换表逐处替换）")

    # ── H17 敏感词根 ────────────────────────────────────────
    roots = [w for w in BAD_ROOTS if w in flat]
    if roots:
        fail("H17", "命中敏感词根组合：" + "、".join(roots)
             + "（替换词不得回用敏感词根：炸损→破损，摔伤→坠落受创）")

    # ── H18 无判据词 ────────────────────────────────────────
    if "大半" in flat:
        fail("H18", "出现无判据词「大半」——纵深对峙镜须写「占画面宽度 1/3-1/2」")

    # ── H19 首帧承接 ────────────────────────────────────────
    if "首帧" in flat:
        if not any(w in flat for w in DARK_WORDS):
            warn("H19", "有首帧承接但未出现暗色痕迹写法（深色污渍/暗色湿痕/"
                        "暗色痕迹）——若首帧无痕迹可忽略；有痕迹须换词不换画面")
        else:
            if "不新增" not in flat and "冻结" not in flat:
                warn("H19", "首帧暗色痕迹未写明「只延续不新增 / 位置面积冻结」四条硬约束")

    # ── H20 场景节点数与场景类型匹配 ────────────────────────
    m = re.search(r"场景类型[：:]\s*(宏大|中等|狭小)", flat)
    if m:
        stype = m.group(1)
        lo, hi = NODE_RANGE[stype]
        m2 = re.search(r"场景节点数[：:]\s*(\d+)", flat)
        if not m2:
            m2 = re.search(r"共\s*(\d+)\s*个场景节点", flat)
        if m2:
            n = int(m2.group(1))
            if n < lo or n > hi:
                fail("H20", "场景类型「" + stype + "」要求节点 " + str(lo) + "-"
                     + str(hi) + " 个，实际写 " + str(n) + " 个")

    # ── H21 收尾总结必含 ────────────────────────────────────
    if sec_sum:
        lack = [k for k in ("镜头数量", "平均单镜", "场景节点") if k not in sec_sum]
        if lack:
            fail("H21", "收尾总结缺：" + "、".join(lack))
        if "总时长" not in sec_sum and "时长" not in sec_sum:
            fail("H21", "收尾总结缺「总时长」")
    else:
        fail("H21", "未找到收尾总结段")

    # ── H22 负面提示词分类齐 ────────────────────────────────
    if sec_neg:
        found = []
        for c in CATEGORIES:
            if c in sec_neg:
                found.append(c)
        if len(found) < 8:
            fail("H22", "负面提示词分类不足（找到 " + str(len(found))
                 + " 类）：" + "、".join(found))
        if "1/3" not in sec_neg and "画面宽" not in sec_neg:
            warn("H22", "负面「人物比例类」建议补：前景人物不足画面宽度 1/3")
    else:
        fail("H22", "未找到负面提示词段")

    # ── W 系列（建议）──────────────────────────────────────
    if sec_shots:
        stable = 0
        for line in re.findall(r"^镜头\s*\d+\s*[｜|].*$", sec_shots, re.M):
            if "稳定" in line or "固定镜头" in line or "三脚架" in line:
                stable += 1
        if stable > 3:
            warn("W1", "稳定镜头 " + str(stable) + " 个，超出配额 3——按砍除顺序："
                       "唯美段 → 结尾大全景 → 开场远景 → 慢动作时刻最后砍")

        slow = 0
        for line in re.findall(r"^镜头\s*\d+\s*[｜|].*$", sec_shots, re.M):
            if "慢动作时刻" in line or "极慢速" in line:
                slow += 1
        if slow > 1:
            warn("W3", "慢动作镜 " + str(slow) + " 个，每段最多 1 段（1-1.2 秒）")

    if not any(w in flat for w in ["手持", "晃动", "颠簸", "荷兰角", "FPV", "快摇"]):
        warn("W2", "未见晃动/手持相关描述——运镜是本技能的核心差异化价值，必须写足")

    if "快摇" in flat and not re.search(r"快摇[^。\n]{0,40}?\d+\.\d+\s*秒", flat):
        warn("W4", "快摇转场未标持续时长——须 ≤0.3 秒，模糊只允许横向拖影")

    if "攻击回合" not in flat:
        warn("W5", "未见攻击回合映射说明——建议写明「1 中镜 + 1 短镜」并校验 2N ≤ 镜数")

    if sec_total and any(w in sec_total for w in ["画幅", "16:9", "9:16", "分辨率"]):
        warn("W6", "【正向总述】出现画幅/分辨率——画幅由生成端手动设定（默认 16:9），"
                   "不写进提示词")

    # ── 输出 ────────────────────────────────────────────────
    print("=" * 58)
    print("seedance-fight-sequence 交付前自检")
    print("文件：" + path)
    print("镜次：" + str(real_cnt) + " 个" +
          ("，时长合计 " + ("%.2f" % sum(durs)) + " 秒" if durs else ""))
    print("=" * 58)

    if HARD:
        print("\n【硬缺项 " + str(len(HARD)) + " 条】")
        for code, msg in HARD:
            print("  ✗ " + code + "  " + msg)
    else:
        print("\n【硬缺项】无 ✓")

    if WARN:
        print("\n【建议 " + str(len(WARN)) + " 条】")
        for code, msg in WARN:
            print("  · " + code + "  " + msg)
    else:
        print("\n【建议】无")

    print("")
    return 1 if HARD else 0


if __name__ == "__main__":
    sys.exit(main())
