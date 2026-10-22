from __future__ import annotations

import argparse
import json
import os
import shutil
import sys
from datetime import datetime
from pathlib import Path


EXPECTED_SKILLS = [
    "ai-film-router",
    "film-synopsis",
    "film-characters",
    "film-worldbuilding",
    "film-treatment",
    "film-screenplay",
    "film-lira-assets",
    "film-acting",
    "film-cinedance",
    "film-knowledge-bridge",
]


def main() -> None:
    parser = argparse.ArgumentParser(description="安装 AI STUDIO 洋子 10 Skill 完整课程包")
    parser.add_argument("--codex-home", help="Codex 主目录，默认读取 CODEX_HOME 或 ~/.codex")
    args = parser.parse_args()

    codex_home = Path(
        args.codex_home or os.environ.get("CODEX_HOME") or Path.home() / ".codex"
    ).expanduser().resolve()
    source_root = Path(__file__).resolve().parent.parent / "skills"
    target_root = codex_home / "skills"

    for skill_name in EXPECTED_SKILLS:
        skill_file = source_root / skill_name / "SKILL.md"
        if not skill_file.is_file():
            raise FileNotFoundError(f"安装包不完整，缺少：{skill_file}")

    target_root.mkdir(parents=True, exist_ok=True)
    existing_config_candidates = [
        target_root / "film-knowledge-bridge" / "references" / "knowledge-base.json",
        target_root / "film-knowledge-bridge" / "knowledge-base.json",
    ]
    preserved_config = next(
        (path.read_bytes() for path in existing_config_candidates if path.is_file()),
        None,
    )
    conflicts = [name for name in EXPECTED_SKILLS if (target_root / name).exists()]
    backup_root: Path | None = None
    if conflicts:
        backup_root = codex_home / f"skills-backup-{datetime.now():%Y%m%d-%H%M%S-%f}"
        backup_root.mkdir(parents=True, exist_ok=False)
        for skill_name in conflicts:
            shutil.move(str(target_root / skill_name), str(backup_root / skill_name))

    for skill_name in EXPECTED_SKILLS:
        shutil.copytree(source_root / skill_name, target_root / skill_name)

    config_result = "无旧配置，首次调用知识库时选择一次文件夹"
    if preserved_config is not None:
        config_target = (
            target_root
            / "film-knowledge-bridge"
            / "references"
            / "knowledge-base.json"
        )
        template_target = config_target.with_name("knowledge-base-template.json")
        config_target.parent.mkdir(parents=True, exist_ok=True)
        try:
            installed_config = json.loads(
                (
                    config_target
                    if config_target.is_file()
                    else template_target
                ).read_text(encoding="utf-8")
            )
            previous_config = json.loads(preserved_config.decode("utf-8"))
            previous_config.pop("domain_paths", None)
            installed_config.update(previous_config)
            installed_config.pop("domain_paths", None)
            config_target.write_text(
                json.dumps(installed_config, ensure_ascii=False, indent=2),
                encoding="utf-8",
            )
        except (UnicodeDecodeError, json.JSONDecodeError, OSError):
            config_target.write_bytes(preserved_config)
        config_result = f"已保留原知识库路径：{config_target}"

    missing = [name for name in EXPECTED_SKILLS if not (target_root / name / "SKILL.md").is_file()]
    if missing:
        raise RuntimeError(f"安装校验失败，缺少：{'、'.join(missing)}")

    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    print("安装完成：10 个 Skill（原 9 个电影 Skill + 本地知识库外挂）")
    print(f"安装位置：{target_root}")
    print(f"旧版本备份：{backup_root if backup_root else '无（未发现同名 Skill）'}")
    print(f"知识库配置：{config_result}")


if __name__ == "__main__":
    main()
