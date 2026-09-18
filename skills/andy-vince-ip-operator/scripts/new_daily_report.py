#!/usr/bin/env python3
from __future__ import annotations

import argparse
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

PLATFORMS = ("小红书", "抖音", "快手", "视频号", "X", "TikTok")

TEMPLATE = """# Andy小助手Vince 每日运营报告 - {day}

## 1. 结论


## 2. 前一天数据总览

| 平台 | 内容/账号 | 表层数据 | 深度数据 | 漏斗断点 | 下一步验证指标 |
| --- | --- | --- | --- | --- | --- |
{rows}

## 3. 第一性原理诊断

- 目标：
- 约束：
- 关键变量：
- 底层逻辑：
- 事实：
- 推断：
- Vince 判断：

## 4. 今天的动作

- 只选一个增长假设：
- 主攻选题/内容支柱：
- 平台适配：
- 成功标准：
- 需要复采的页面或权限：

## 5. 内容与分发

- 标题候选（先与历史标题查重）：
- 封面/首图方向：
- 主脚本或轮播大纲：
- 各平台文案：
- CTA：
- AIGC/商业合作/敏感表述检查：

## 6. 风险和明日实验

- 风险：
- 明日只验证一个变量：
"""

def main() -> None:
    parser = argparse.ArgumentParser(description="Create a non-overwriting daily report template.")
    parser.add_argument("--out-dir", default="reports")
    parser.add_argument("--date", help="YYYY-MM-DD; defaults to Australia/Sydney today")
    args = parser.parse_args()

    day = args.date or datetime.now(ZoneInfo("Australia/Sydney")).date().isoformat()
    try:
        datetime.strptime(day, "%Y-%m-%d")
    except ValueError as exc:
        raise SystemExit("--date must use YYYY-MM-DD") from exc

    rows = "\n".join(f"| {platform} |  |  |  |  |  |" for platform in PLATFORMS)
    path = Path(args.out_dir) / f"{day}-andy-vince-daily-report.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        path.write_text(TEMPLATE.format(day=day, rows=rows), encoding="utf-8")
    print(path)

if __name__ == "__main__":
    main()
