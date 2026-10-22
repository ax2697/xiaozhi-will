# -*- coding: utf-8 -*-
"""
新短剧项目目录骨架脚手架（对应《AI 指令→文件路由卡》2026-09-06 新布局 / 第十一章立项清单）。

只负责"新建缺失目录"，绝不删除、不移动、不覆盖任何已有文件。
用法：
    python new_project_scaffold.py "<项目根目录>"
    python new_project_scaffold.py "<项目根目录>" --season 第一季 --episode 第1集
"""
import argparse
import os
import sys

BASE_DIRS = [
    "各个资产包汇总/角色",
    "各个资产包汇总/场景",
    "各个资产包汇总/道具",
    "各个资产包汇总/分镜",
    "各个资产包汇总/脚本",
    "工作流程",
    "剧集/总纲",
    "剧集/预告片",
    "资产图片音频汇总/角色设定图",
    "资产图片音频汇总/场景设计图",
    "资产图片音频汇总/道具设计图",
    "资产图片音频汇总/关键帧",
    "资产图片音频汇总/视频片段",
    "资产图片音频汇总/音频资产",
    "参考",
    "总控",
]


def main():
    ap = argparse.ArgumentParser(description="建立短剧项目目录骨架（只新建，不删改）")
    ap.add_argument("root", help="项目根目录绝对路径")
    ap.add_argument("--season", default=None, help="季名，如 第一季")
    ap.add_argument("--episode", default=None, help="集名，如 第1集")
    ap.add_argument("--dry-run", action="store_true", help="只打印将做什么，不实际创建")
    args = ap.parse_args()

    root = os.path.abspath(args.root)
    targets = list(BASE_DIRS)
    if args.season and args.episode:
        targets.append("剧集/%s/%s" % (args.season, args.episode))
    elif args.season:
        targets.append("剧集/%s" % args.season)

    created, existed = [], []
    for d in targets:
        full = os.path.join(root, d)
        if os.path.isdir(full):
            existed.append(full)
            continue
        created.append(full)
        if not args.dry_run:
            os.makedirs(full, exist_ok=True)

    print("项目根目录：%s" % root)
    print("已存在（未改动）：%d" % len(existed))
    for p in existed:
        print("  = %s" % p)
    print("%s目录：%d" % ("将新建" if args.dry_run else "已新建", len(created)))
    for p in created:
        print("  + %s" % p)
    if not os.path.isdir(root):
        print("\n注意：根目录本身不存在，%s" % ("请加 --dry-run 先确认路径拼写。" if args.dry_run else "已连同子目录一起创建。"))
    print("\n下一步：按 references/11-new-drama-bootstrap.md 建立 8 类文件，并替换全部【占位符】。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
