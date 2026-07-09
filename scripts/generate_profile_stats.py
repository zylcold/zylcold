#!/usr/bin/env python3
import json
import os
import urllib.request
from collections import Counter
from datetime import datetime, timezone
from html import escape
from pathlib import Path


USERNAME = os.getenv("PROFILE_USERNAME", "zylcold")
TOKEN = os.getenv("GITHUB_TOKEN")
API = "https://api.github.com"
OUT_DIR = Path("assets")
HIDE_LANGUAGES = {
    language.strip()
    for language in os.getenv("HIDE_LANGUAGES", "HTML,CSS,Perl").split(",")
    if language.strip()
}


def request_json(path):
    request = urllib.request.Request(f"{API}{path}")
    request.add_header("Accept", "application/vnd.github+json")
    request.add_header("X-GitHub-Api-Version", "2022-11-28")
    if TOKEN:
        request.add_header("Authorization", f"Bearer {TOKEN}")

    with urllib.request.urlopen(request, timeout=30) as response:
        return json.loads(response.read().decode("utf-8"))


def fetch_repos():
    repos = []
    page = 1
    while True:
        batch = request_json(f"/users/{USERNAME}/repos?per_page=100&page={page}&sort=updated")
        if not batch:
            break
        repos.extend(batch)
        page += 1
    return repos


def svg_card(width, height, title, subtitle, body):
    return f"""<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="title desc">
  <title id="title">{escape(title)}</title>
  <desc id="desc">{escape(subtitle)}</desc>
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="{width}" y2="{height}" gradientUnits="userSpaceOnUse">
      <stop stop-color="#111827"/>
      <stop offset="1" stop-color="#0F172A"/>
    </linearGradient>
  </defs>
  <rect width="{width}" height="{height}" rx="14" fill="url(#bg)"/>
  <rect x="0.5" y="0.5" width="{width - 1}" height="{height - 1}" rx="13.5" stroke="#334155"/>
  <text x="24" y="34" fill="#E5E7EB" font-family="Inter, Segoe UI, Arial, sans-serif" font-size="18" font-weight="700">{escape(title)}</text>
  <text x="24" y="58" fill="#94A3B8" font-family="Inter, Segoe UI, Arial, sans-serif" font-size="12">{escape(subtitle)}</text>
{body}
</svg>
"""


def metric_row(label, value, x, y):
    return f"""  <text x="{x}" y="{y}" fill="#94A3B8" font-family="Inter, Segoe UI, Arial, sans-serif" font-size="12">{escape(label)}</text>
  <text x="{x}" y="{y + 28}" fill="#F8FAFC" font-family="Inter, Segoe UI, Arial, sans-serif" font-size="26" font-weight="700">{escape(str(value))}</text>"""


def stats_svg(user, repos, originals):
    created = datetime.fromisoformat(user["created_at"].replace("Z", "+00:00"))
    now = datetime.now(timezone.utc)
    years = max(1, now.year - created.year)
    updated = now.strftime("%Y-%m-%d")

    body = "\n".join(
        [
            metric_row("Public repos", user["public_repos"], 24, 100),
            metric_row("Original repos", len(originals), 200, 100),
            metric_row("Followers", user["followers"], 376, 100),
            metric_row("GitHub years", f"{years}+", 24, 170),
            metric_row("Active originals", sum(1 for repo in originals if not repo.get("archived")), 200, 170),
            metric_row("Following", user["following"], 376, 170),
            f'  <text x="24" y="268" fill="#64748B" font-family="Inter, Segoe UI, Arial, sans-serif" font-size="11">Updated by GitHub Actions on {updated}</text>',
        ]
    )
    return svg_card(560, 292, "GitHub Activity", f"@{USERNAME} public profile snapshot", body)


def languages_svg(originals):
    languages = Counter(
        repo["language"]
        for repo in originals
        if repo.get("language") and repo["language"] not in HIDE_LANGUAGES
    )
    top = languages.most_common(6)
    max_count = max((count for _, count in top), default=1)
    colors = ["#F97316", "#3B82F6", "#FACC15", "#CC342D", "#22C55E", "#A855F7"]

    rows = []
    y = 96
    for index, (language, count) in enumerate(top):
        width = int(360 * count / max_count)
        color = colors[index % len(colors)]
        rows.append(
            f"""  <text x="24" y="{y}" fill="#CBD5E1" font-family="Inter, Segoe UI, Arial, sans-serif" font-size="13">{escape(language)}</text>
  <text x="500" y="{y}" fill="#CBD5E1" font-family="Inter, Segoe UI, Arial, sans-serif" font-size="13" text-anchor="end">{count}</text>
  <rect x="24" y="{y + 10}" width="360" height="8" rx="4" fill="#1E293B"/>
  <rect x="24" y="{y + 10}" width="{width}" height="8" rx="4" fill="{color}"/>"""
        )
        y += 34

    return svg_card(560, 292, "Primary Languages", "Original public repositories by main language", "\n".join(rows))


def terminal_svg():
    font = "SFMono-Regular, Consolas, Menlo, monospace"
    left_items = [
        ("identity", "zylcold"),
        ("role", "iOS developer"),
        ("since", "2018"),
        ("mode", "build / automate / learn"),
    ]
    right_items = [
        ("01", "reverse engineering iOS apps"),
        ("02", "automation-first workflows"),
        ("03", "AR / VR exploration"),
        ("04", "Raspberry Pi tinkering"),
        ("05", "AI pair programming"),
    ]

    rows = [
        '  <rect x="18" y="18" width="864" height="34" rx="6" fill="#0F172A" stroke="#334155"/>',
        f'  <text x="34" y="40" fill="#22D3EE" font-family="{font}" font-size="13">zylcold-profile.tui</text>',
        f'  <text x="850" y="40" fill="#64748B" font-family="{font}" font-size="12" text-anchor="end">session: github</text>',
        '  <rect x="18" y="66" width="276" height="238" rx="6" fill="#020617" stroke="#334155"/>',
        '  <rect x="310" y="66" width="572" height="238" rx="6" fill="#020617" stroke="#334155"/>',
        '  <rect x="18" y="318" width="864" height="34" rx="6" fill="#0F172A" stroke="#334155"/>',
        f'  <text x="34" y="91" fill="#F8FAFC" font-family="{font}" font-size="13">┌─ profile</text>',
        f'  <text x="326" y="91" fill="#F8FAFC" font-family="{font}" font-size="13">┌─ interests / runtime</text>',
    ]

    y = 122
    for label, value in left_items:
        rows.append(
            f'  <text x="38" y="{y}" fill="#64748B" font-family="{font}" font-size="12">{escape(label)}</text>'
        )
        rows.append(
            f'  <text x="130" y="{y}" fill="#E2E8F0" font-family="{font}" font-size="12">{escape(value)}</text>'
        )
        y += 34

    y = 122
    for index, text in right_items:
        rows.append(
            f'  <text x="332" y="{y}" fill="#38BDF8" font-family="{font}" font-size="12">[{escape(index)}]</text>'
        )
        rows.append(
            f'  <text x="382" y="{y}" fill="#E2E8F0" font-family="{font}" font-size="12">{escape(text)}</text>'
        )
        y += 32

    rows.extend(
        [
            f'  <text x="332" y="292" fill="#A7F3D0" font-family="{font}" font-size="12">motto</text>',
            f'  <text x="382" y="292" fill="#F8FAFC" font-family="{font}" font-size="12">If it can be automated, it will be.</text>',
            f'  <text x="34" y="340" fill="#94A3B8" font-family="{font}" font-size="12">F1 help</text>',
            f'  <text x="120" y="340" fill="#94A3B8" font-family="{font}" font-size="12">F2 projects</text>',
            f'  <text x="226" y="340" fill="#94A3B8" font-family="{font}" font-size="12">F3 workflow</text>',
            f'  <text x="818" y="340" fill="#22C55E" font-family="{font}" font-size="12" text-anchor="end">READY</text>',
        ]
    )

    return f"""<svg width="900" height="370" viewBox="0 0 900 370" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="title desc">
  <title id="title">Fun Facts TUI</title>
  <desc id="desc">TUI-style snapshot of interests, workflow, and motto.</desc>
  <defs>
    <linearGradient id="terminalBg" x1="0" y1="0" x2="900" y2="370" gradientUnits="userSpaceOnUse">
      <stop stop-color="#020617"/>
      <stop offset="1" stop-color="#111827"/>
    </linearGradient>
  </defs>
  <rect width="900" height="370" rx="14" fill="url(#terminalBg)"/>
  <rect x="0.5" y="0.5" width="899" height="369" rx="13.5" stroke="#334155"/>
{chr(10).join(rows)}
</svg>
"""


def main():
    OUT_DIR.mkdir(exist_ok=True)
    user = request_json(f"/users/{USERNAME}")
    repos = fetch_repos()
    originals = [repo for repo in repos if not repo.get("fork")]

    (OUT_DIR / "github-activity.svg").write_text(stats_svg(user, repos, originals), encoding="utf-8")
    (OUT_DIR / "primary-languages.svg").write_text(languages_svg(originals), encoding="utf-8")
    (OUT_DIR / "terminal-snapshot.svg").write_text(terminal_svg(), encoding="utf-8")


if __name__ == "__main__":
    main()
