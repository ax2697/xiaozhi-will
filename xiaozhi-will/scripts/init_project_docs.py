# -*- coding: utf-8 -*-
"""
把 templates/ 的空白模板落盘到新项目，并批量替换【占位符】。

用法：
    python init_project_docs.py "<项目根目录>" --season 第一季 --episode 第1集 \
        --set "新剧名=某某某" --set "第N集=第1集" --set "画幅=16:9" \
        --set "出图模型=seedream_4.5" --set "视频模型=seedance_2.5" --set "帧率=24fps"

规则：
  * 只新建缺失文件；已存在的文件默认跳过，确认要覆盖再加 --force
  * 不删除、不移动、不联网、不改源文件
  * --dry-run 只打印将做什么
"""
import argparse
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
TEMPLATES = os.path.join(os.path.dirname(HERE), "templates")

# 模板文件 -> 目标子目录（相对项目根）
MAP = {
    "01-项目总索引（含P0参数卡）模板.md": "总控",
    "02-主要角色标准化视觉资产包 模板.md": "各个资产包汇总/角色",
    "03-核心场景标准化视觉资产包 模板.md": "各个资产包汇总/场景",
    "04-核心道具标准化视觉资产包 模板.md": "各个资产包汇总/道具",
    "05-10字段分镜表 模板.md": "各个资产包汇总/分镜",
    "06-空间顶视图与机位调度图 模板.md": "各个资产包汇总/分镜",
    "07-图片视频生成执行规范SOP 模板.md": "工作流程",
    "08-剧本包与三不核对表 模板.md": None,  # 落到 剧集/{季}/{集}
}

BASE_DIRS = [
    "各个资产包汇总/角色", "各个资产包汇总/场景", "各个资产包汇总/道具",
    "各个资产包汇总/分镜", "各个资产包汇总/脚本", "工作流程",
    "剧集/总纲", "剧集/预告片",
    "资产图片音频汇总/角色设定图", "资产图片音频汇总/场景设计图",
    "资产图片音频汇总/道具设计图", "资产图片音频汇总/关键帧",
    "资产图片音频汇总/视频片段", "资产图片音频汇总/音频资产",
    "参考", "总控",
]


def target_name(src_name):
    return src_name.replace(" 模板", "").replace("模板", "").replace(".md", ".md")


def apply_replacements(text, pairs):
    for k, v in pairs:
        text = text.replace("【%s】" % k, v)
    return text


def main():
    ap = argparse.ArgumentParser(description="落盘项目模板并替换占位符（只新建，不覆盖）")
    ap.add_argument("root", help="项目根目录绝对路径")
    ap.add_argument("--season", default="第一季")
    ap.add_argument("--episode", default="第1集")
    ap.add_argument("--set", action="append", default=[],
                    help="占位符赋值，格式 键=值，可多次；键不含【】，如 --set \"画幅=16:9\"")
    ap.add_argument("--force", action="store_true", help="覆盖已存在的目标文件")
    ap.add_argument("--dry-run", action="store_true", help="只打印将做什么")
    args = ap.parse_args()

    pairs = []
    for item in args.set:
        if "=" not in item:
            print("跳过无效赋值（缺 =）：%s" % item)
            continue
        k, v = item.split("=", 1)
        pairs.append((k.strip(), v.strip()))

    root = os.path.abspath(args.root)
    out = ["项目根目录：%s" % root, "占位符替换：%d 组 %s" % (len(pairs), pairs or "")]

    # 1. 目录骨架
    made_dirs = []
    for d in BASE_DIRS + ["剧集/%s/%s" % (args.season, args.episode)]:
        full = os.path.join(root, d)
        if not os.path.isdir(full):
            made_dirs.append(full)
            if not args.dry_run:
                os.makedirs(full, exist_ok=True)
    out.append("新建目录 %d 个" % len(made_dirs))

    # 2. 模板落盘
    written, skipped, missing = [], [], []
    for src_name, sub in MAP.items():
        src = os.path.join(TEMPLATES, src_name)
        if not os.path.isfile(src):
            missing.append(src_name)
            continue
        if sub is None:
            sub = "剧集/%s/%s" % (args.season, args.episode)
        sub = sub.replace("/", os.sep)
        dst_dir = os.path.join(root, sub)
        dst = os.path.join(dst_dir, target_name(src_name))
        if os.path.exists(dst) and not args.force:
            skipped.append(dst)
            continue
        text = open(src, encoding="utf-8").read()
        text = apply_replacements(text, pairs)
        written.append(dst)
        if not args.dry_run:
            os.makedirs(dst_dir, exist_ok=True)
            open(dst, "w", encoding="utf-8").write(text)

    out.append("%s模板 %d 份：" % ("将写入" if args.dry_run else "已写入", len(written)))
    out += ["  + %s" % p for p in written]
    if skipped:
        out.append("已存在跳过 %d 份（要覆盖加 --force）：" % len(skipped))
        out += ["  = %s" % p for p in skipped]
    if missing:
        out.append("未找到模板：%s" % missing)
    out.append("")
    out.append("下一步：先填《项目总索引》第一章 P0 参数卡，再依次填剧本包 → 三资产包 → 机位图 → 分镜表。")
    print("\n".join(out))
    return 0


if __name__ == "__main__":
    sys.exit(main())
