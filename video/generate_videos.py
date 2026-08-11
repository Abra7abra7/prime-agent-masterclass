#!/usr/bin/env python3
"""
Prime Agent Masterclass – Generátor video lekcií
================================================
Automaticky generuje inštrukcie pre HeyGen API (avatar),
Hyperframes screen demo, FFmpeg príkazy na spojenie,
a YouTube/TikTok popisy a tagy.

Použitie:
    python generate_videos.py --module 1 --lesson 1
    python generate_videos.py --module 1                  # všetky lekcie v module
    python generate_videos.py --all                        # všetky moduly a lekcie
    python generate_videos.py --module 1 --lesson 1 --dry-run  # len výpis, nespúšťa render

Závislosti:
    pip install pyyaml
    npm install -g hyperframes   (pre `npx hyperframes render`)
    ffmpeg                       (pre spojenie videa)
"""

import argparse
import json
import os
import re
import subprocess
import sys
from pathlib import Path
from textwrap import dedent, wrap
from datetime import datetime


# ── Konfigurácia ────────────────────────────────────────────────────────────

BASE_DIR = Path(__file__).resolve().parent.parent  # prime-agent-masterclass/
VIDEO_DIR = BASE_DIR / "video"
OUTPUT_DIR = VIDEO_DIR / "output"

# Mapovanie modulov na markdown súbory s detailnými scenármi
MODULE_FILES = {
    1: "module1-detail-sk.md",
    2: "module2-3-detail-sk.md",
    3: "module2-3-detail-sk.md",
    4: "module4-5-detail-sk.md",
    5: "module4-5-detail-sk.md",
    6: "module6-detail-sk.md",
    7: "module7-detail-sk.md",
    8: "module8-detail-sk.md",
}

# Názvy modulov a lekcií (zo súboru course-outline-sk.md)
COURSE = {
    1: {
        "title": "Úvod a inštalácia",
        "lessons": [
            "co-je-prime-agent",
            "architektura-a-komponenty",
            "instalacia",
            "konfiguracia-api-klucov",
            "prve-spustenie",
        ],
        "lesson_titles": [
            "Čo je Prime Agent a prečo ho potrebuješ",
            "Architektúra a kľúčové komponenty",
            "Inštalácia na macOS, Linux a Windows",
            "Konfigurácia API kľúčov a providerov",
            "Prvé spustenie a orientácia v rozhraní",
        ],
        "lesson_durations": [10, 15, 18, 12, 10],
    },
    2: {
        "title": "Prvé kroky s agentom",
        "lessons": [
            "prompt-engineering-pre-agentov",
            "ipython-kernel",
            "shell-prikazy",
            "praca-so-subormi",
            "debugging",
            "projekt-analyza-repozitara",
        ],
        "lesson_titles": [
            "Ako správne formulovať úlohy",
            "Práca s IPython kernelom",
            "Shell príkazy a %%bash bunky",
            "Čítanie, vyhľadávanie a editácia súborov",
            "Interpretácia výstupov a debugging",
            "Praktický projekt: Analýza repozitára",
        ],
        "lesson_durations": [12, 15, 12, 10, 10, 20],
    },
    3: {
        "title": "Skills a customizácia",
        "lessons": [
            "co-su-skilly",
            "objavovanie-skillov",
            "markdown-skilly",
            "python-skilly",
            "vytvaranie-skillu",
            "organizacia-skillov",
        ],
        "lesson_titles": [
            "Čo sú skills a ako ich agent používa",
            "Objavovanie a inštalácia skillov",
            "Markdown skilly – štruktúra SKILL.md",
            "Python skilly – importy, funkcie a CLI",
            "Vytváranie vlastného skillu",
            "Organizácia a správa knižnice skillov",
        ],
        "lesson_durations": [10, 12, 10, 12, 15, 8],
    },
    4: {
        "title": "Subagenti a delegovanie",
        "lessons": [
            "koncept-subagentov",
            "vytvaranie-subagenta",
            "komunikacia-medzi-agentmi",
            "monitoring-subagentov",
            "pokrocile-delegovanie",
            "projekt-tim-agentov",
        ],
        "lesson_titles": [
            "Koncept subagentov – prečo a kedy delegovať",
            "Vytváranie subagenta cez rlm()",
            "Komunikácia medzi agentmi",
            "Pozorovanie a monitoring subagentov",
            "Pokročilé delegovanie – reťazenie a špecializácia",
            "Praktický projekt: Tím agentov pre prieskum trhu",
        ],
        "lesson_durations": [10, 12, 10, 8, 12, 20],
    },
    5: {
        "title": "Automatizácia marketingu",
        "lessons": [
            "marketingove-skilly",
            "tvorba-obsahu",
            "seo-a-ai-viditelnost",
            "emailove-kampane",
            "prieskum-trhu",
            "socialne-siete",
        ],
        "lesson_titles": [
            "Prehľad marketingových skillov a orchestrácia",
            "Tvorba marketingového obsahu na mieru",
            "SEO a AI viditeľnosť",
            "Emailové kampane a marketingové slučky",
            "Prieskum trhu a zákaznícka analytika",
            "Sociálne siete a obsahový kalendár",
        ],
        "lesson_durations": [12, 15, 15, 15, 12, 15],
    },
    6: {
        "title": "Automatizácia predaja a supportu",
        "lessons": [
            "sales-enablement",
            "prospecting",
            "customer-support",
            "onboarding",
            "retencia-churn",
            "projekt-sales-pipeline",
        ],
        "lesson_titles": [
            "Sales enablement – battle cards, decky, one-pagery",
            "Prospecting a cold outreach",
            "Riadenie zákazníckej podpory",
            "Onboarding a aktivácia používateľov",
            "Retencia, churn prevencia a win-back",
            "Praktický projekt: End-to-end pipeline",
        ],
        "lesson_durations": [12, 15, 12, 12, 12, 25],
    },
    7: {
        "title": "Pokročilé techniky",
        "lessons": [
            "mcp-protocol",
            "google-workspace",
            "externe-api",
            "heartbeaty-cron",
            "pokrocila-orchestracia",
            "custom-nastroje",
        ],
        "lesson_titles": [
            "Model Context Protocol (MCP)",
            "Google Workspace integrácia",
            "Volanie externých API z Python skillov",
            "Plánovanie úloh – heartbeaty a cron joby",
            "Pokročilá orchestrácia – paralelné spracovanie",
            "Custom nástroje a rozšírenia – beyond skills",
        ],
        "lesson_durations": [15, 20, 15, 12, 15, 15],
    },
    8: {
        "title": "Produkčné nasadenie a best practices",
        "lessons": [
            "bezpecnost",
            "continual-harness",
            "monitoring-logovanie",
            "skalovanie",
            "verzionovanie-ci-cd",
            "best-practices",
        ],
        "lesson_titles": [
            "Bezpečnosť – API kľúče, permissions, sandboxing",
            "Continual harness – pamäť, skilly a prompt manažment",
            "Monitoring a logovanie agenta v produkcii",
            "Škálovanie – viacero agentov, load balancing",
            "Verzionovanie skillov a CI/CD pre agenta",
            "Best practices a lessons learned z praxe",
        ],
        "lesson_durations": [15, 15, 12, 12, 12, 15],
    },
}

# HeyGen API konfigurácia (bez kľúča – používateľ doplní)
HEYGEN_API_URL = "https://api.heygen.com"
HEYGEN_AVATAR_ID = "YOUR_AVATAR_ID"  # Používateľ nahradí
HEYGEN_VOICE_ID = "YOUR_VOICE_ID"    # Používateľ nahradí

# YouTube / TikTok defaults
YOUTUBE_CHANNEL = "Prime Agent Masterclass"
TIKTOK_USERNAME = "@primeagentmasterclass"
HASHTAGS_BASE = [
    "PrimeAgent", "AIAgent", "CodingAgent", "AI", "ProgrammingTutorial",
    "AITools", "DeveloperTools", "Automation", "TerminalAI", "OpenSource",
]
HASHTAGS_MODULE = {
    1: ["Installation", "Setup", "GettingStarted", "DevEnvironment"],
    2: ["PromptEngineering", "IPython", "ShellScripting", "Debugging", "FileManagement"],
    3: ["Skills", "CustomSkills", "AIWorkflow", "Automation"],
    4: ["MultiAgent", "Delegation", "ParallelProcessing", "AIArchitecture"],
    5: ["Marketing", "SEO", "EmailMarketing", "ContentCreation", "SocialMedia"],
    6: ["Sales", "Prospecting", "CustomerSupport", "Onboarding", "Retention"],
    7: ["MCP", "GoogleWorkspace", "API", "Scheduling", "AdvancedAI"],
    8: ["Production", "DevOps", "Security", "CICD", "BestPractices"],
}


# ── Parsovanie avatar skriptov z markdown súborov ──────────────────────────

def parse_avatar_script(module_num: int) -> dict:
    """Načíta a parsuje markdown súbor s detailným scenárom modulu."""
    filename = MODULE_FILES.get(module_num)
    if not filename:
        return {}

    filepath = BASE_DIR / filename
    if not filepath.exists():
        print(f"  ⚠ Súbor {filename} neexistuje – avatar skript sa nepodarilo načítať.")
        return {}

    with open(filepath, encoding="utf-8") as f:
        content = f.read()

    # Najdi sekciu pre daný modul
    if module_num in (2, 3) and filename == "module2-3-detail-sk.md":
        module_pattern = rf"# Prime Agent Masterclass – Modul {module_num}:"
    elif module_num in (4, 5) and filename == "module4-5-detail-sk.md":
        module_pattern = rf"# Prime Agent Masterclass – Modul {module_num}:"
    else:
        module_pattern = r"# Prime Agent Masterclass – Modul \d+:"

    # Extrahuj všetky lekcie – hľadaj pattern "## Lekcia X: ..."
    lessons = {}
    lesson_pattern = re.compile(
        r"## Lekcia (\d+): (.+?)\n\*\*Dĺžka videa:\*\* (.+?)\n\n(.*?)(?=\n## Lekcia \d+:|$)",
        re.DOTALL,
    )
    for match in lesson_pattern.finditer(content):
        lesson_num = int(match.group(1))
        lesson_title = match.group(2).strip()
        duration_str = match.group(3).strip()
        body = match.group(4).strip()

        # Parsuj časové značky a hovorený text
        segments = parse_timestamps(body)

        lessons[lesson_num] = {
            "title": lesson_title,
            "duration": duration_str,
            "segments": segments,
            "full_script": body,
        }

    return lessons


def parse_timestamps(body: str) -> list[dict]:
    """Extrahuje časové segmenty a hovorený text z tela scenára."""
    segments = []
    # Hľadaj patterny ako "#### 0:00–1:00 | Názov sekcie" alebo podobné
    ts_pattern = re.compile(
        r"####\s*(\d+:\d+)[–\-](\d+:\d+)\s*\|\s*(.+?)\n(.*?)(?=\n####|\Z)",
        re.DOTALL,
    )
    for match in ts_pattern.finditer(body):
        start_time = match.group(1)
        end_time = match.group(2)
        section_title = match.group(3).strip()
        section_body = match.group(4).strip()

        # Extrahuj "Povedať:" a "Ukázať:" inštrukcie
        say_lines = []
        show_lines = []
        for line in section_body.split("\n"):
            stripped = line.strip()
            if stripped.startswith("- **Povedať:**") or stripped.startswith("- **Povedať: "):
                say_lines.append(stripped.replace("- **Povedať:**", "").replace("- **Povedať: ", "").strip().strip('"').strip('"').strip('„').strip('"'))
            elif stripped.startswith("- **Ukázať"):
                show_lines.append(stripped)

        segments.append({
            "start": start_time,
            "end": end_time,
            "section": section_title,
            "narration": " ".join(say_lines) if say_lines else section_body[:300],
            "screencast": show_lines,
        })

    return segments


# ── HeyGen API inštrukcie ───────────────────────────────────────────────────

def generate_heygen_instructions(
    module_num: int,
    lesson_num: int,
    lesson_title: str,
    narration_text: str,
    output_name: str,
) -> str:
    """Vygeneruje curl príkazy pre HeyGen API na vytvorenie avatar videa."""
    safe_narration = narration_text.replace('"', '\\"').replace('\n', ' ')[:2000]

    instructions = f"""
# ── HeyGen API: Avatar video ─────────────────────────────────────────────
# Lekcia: M{module_num}L{lesson_num} – {lesson_title}
# Výstup: {output_name}
#
# PRED SPUSTENIM:
#   1. Nastav HEYGEN_API_KEY v prostredí: export HEYGEN_API_KEY="sk-..."
#   2. Nahraď AVATAR_ID a VOICE_ID za tvoje hodnoty z HeyGen dashboardu
#   3. Avatar ID nájdeš v https://app.heygen.com/avatars
#   4. Voice ID nájdeš v https://app.heygen.com/voices
#
# POZNÁMKA: HeyGen API v2 podporuje streaming a async vytváranie videí.
#           Nižšie sú curl príkazy pre klasické dávkové generovanie.

# Krok 1: Vytvorenie avatar videa (classic batch)
curl -X POST "{HEYGEN_API_URL}/v2/video/generate" \\
  -H "X-Api-Key: $HEYGEN_API_KEY" \\
  -H "Content-Type: application/json" \\
  -d '{{
    "video_name": "{output_name}",
    "dimension": {{ "width": 1920, "height": 1080 }},
    "avatar_id": "{HEYGEN_AVATAR_ID}",
    "voice_id": "{HEYGEN_VOICE_ID}",
    "input_text": "{safe_narration}",
    "background": {{ "type": "color", "value": "#0a0a1a" }},
    "avatar_style": "normal"
  }}'

# Krok 2: Alternatívne – streaming avatar (rýchlejšie, v2 API)
curl -X POST "{HEYGEN_API_URL}/v2/video/template" \\
  -H "X-Api-Key: $HEYGEN_API_KEY" \\
  -H "Content-Type: application/json" \\
  -d '{{
    "template_name": "{output_name}_stream",
    "dimension": {{ "width": 1920, "height": 1080 }},
    "avatar_id": "{HEYGEN_AVATAR_ID}",
    "voice_id": "{HEYGEN_VOICE_ID}",
    "script": "{safe_narration}",
    "background": "#0a0a1a"
  }}'

# Krok 3: Stiahni video (doplň video_id z odpovede)
# curl -o {output_name} "{HEYGEN_API_URL}/v1/video/download?video_id=VIDEO_ID" \\
#   -H "X-Api-Key: $HEYGEN_API_KEY"
"""
    return dedent(instructions).strip()


# ── Hyperframes inštrukcie ──────────────────────────────────────────────────

def find_hyperframes(module_num: int, lesson_num: int) -> list[Path]:
    """Nájde Hyperframes HTML súbory pre danú lekciu."""
    hf_dir = VIDEO_DIR / f"hyperframes-module{module_num}-sk"
    if not hf_dir.exists():
        return []

    # Hľadaj súbory s patternom lesson{N}*.html
    frames = []
    for pattern in [
        f"lesson{lesson_num}-*.html",
        f"m{module_num}l{lesson_num}-*.html",
        f"m{module_num}-l{lesson_num}-*.html",
    ]:
        frames.extend(sorted(hf_dir.glob(pattern)))

    return list(set(frames))  # odstráň duplicity


def generate_hyperframes_commands(
    module_num: int,
    lesson_num: int,
    output_name: str,
    frames: list[Path],
) -> str:
    """Vygeneruje príkazy na renderovanie Hyperframes."""

    if not frames:
        return f"""# ── Hyperframes Screen Demo ─────────────────────────────────────────────
# Lekcia: M{module_num}L{lesson_num}
# Status: ⚠ Nenašli sa žiadne HTML frames v video/hyperframes-module{module_num}-sk/
#
# Vytvor HTML frame súbory v adresári:
#   video/hyperframes-module{module_num}-sk/lesson{lesson_num}-{'{'}{'{'}scena{'}'}{'}'}.html
"""
    lines = [
        f"# ── Hyperframes Screen Demo ─────────────────────────────────────────────",
        f"# Lekcia: M{module_num}L{lesson_num}",
        f"# Počet frames: {len(frames)}",
        f"#",
    ]
    for i, frame in enumerate(frames, 1):
        out_mp4 = OUTPUT_DIR / f"{output_name}_screen_{i:02d}.mp4"
        lines.append(
            f"npx hyperframes render \\\n"
            f"  --input \"{frame}\" \\\n"
            f"  --output \"{out_mp4}\" \\\n"
            f"  --fps 30 \\\n"
            f"  --scale 1.0"
        )
        lines.append("")

    lines.append(
        f"# Spojenie všetkých screen častí do jedného videa:\n"
        f"# (vytvorí sa súbor so zoznamom častí a spojí sa)"
    )
    concat_list = OUTPUT_DIR / f"{output_name}_screen_files.txt"
    lines.append(f"# echo \"file '{output_name}_screen_01.mp4'\" > {concat_list}")
    for i in range(2, len(frames) + 1):
        lines.append(f"# echo \"file '{output_name}_screen_{i:02d}.mp4'\" >> {concat_list}")
    lines.append(f"# ffmpeg -f concat -safe 0 -i {concat_list} -c copy {OUTPUT_DIR / f'{output_name}_screen_full.mp4'}")

    return "\n".join(lines)


# ── FFmpeg príkazy na spojenie ──────────────────────────────────────────────

def generate_ffmpeg_commands(
    output_name: str,
    has_avatar: bool = True,
    has_screen: bool = True,
) -> str:
    """Vygeneruje FFmpeg príkazy na spojenie avatar a screen demo videí."""

    avatar_file = OUTPUT_DIR / f"{output_name}_avatar.mp4"
    screen_file = OUTPUT_DIR / f"{output_name}_screen_full.mp4"
    output_file = OUTPUT_DIR / f"{output_name}_final.mp4"

    commands = [
        "# ── FFmpeg: Finálne spojenie ────────────────────────────────────────────",
    ]

    if has_avatar and has_screen:
        # Side-by-side: avatar vľavo (malý), screen demo vpravo (väčší)
        commands.append(f"# Variant A: Avatar vľavo (malý), screen demo vpravo")
        commands.append(
            f"ffmpeg -i \"{avatar_file}\" -i \"{screen_file}\" \\\n"
            f"  -filter_complex \"\n"
            f"    [0:v]scale=480:270,format=yuv420p[avatar];\n"
            f"    [1:v]scale=1440:810,format=yuv420p[screen];\n"
            f"    [avatar]pad=1920:1080:20:810:black[left];\n"
            f"    [left][screen]overlay=480:0[out]\n"
            f"  \" \\\n"
            f"  -map \"[out]\" -map 1:a \\\n"
            f"  -c:v libx264 -preset medium -crf 23 \\\n"
            f"  -c:a aac -b:a 128k \\\n"
            f"  -shortest \\\n"
            f"  \"{output_file}\""
        )

        commands.append("")
        commands.append(f"# Variant B: Avatar + screen vedľa seba (50/50 split)")

    if has_avatar and not has_screen:
        commands.append(
            f"# Len avatar (fullscreen):\n"
            f"ffmpeg -i \"{avatar_file}\" \\\n"
            f"  -c:v libx264 -preset medium -crf 23 \\\n"
            f"  -c:a aac -b:a 128k \\\n"
            f"  \"{output_file}\""
        )

    if has_screen and not has_avatar:
        commands.append(
            f"# Len screen demo (fullscreen):\n"
            f"ffmpeg -i \"{screen_file}\" \\\n"
            f"  -c:v libx264 -preset medium -crf 23 \\\n"
            f"  -c:a aac -b:a 128k \\\n"
            f"  \"{output_file}\""
        )

    if has_avatar and has_screen:
        commands.append(f"# Po dokončení skontroluj výsledok:")
        commands.append(f"# ffprobe \"{output_file}\"")

    # Shorts verzia (vertikálne 9:16 pre TikTok/Shorts/Reels)
    shorts_file = OUTPUT_DIR / f"{output_name}_shorts.mp4"
    commands.append("")
    commands.append(f"# Shorts verzia (9:16 vertikálne pre TikTok/Shorts/Reels):")
    if has_avatar:
        commands.append(
            f"ffmpeg -i \"{output_file}\" \\\n"
            f"  -vf \"crop=1080:1920:420:0,scale=1080:1920\" \\\n"
            f"  -c:v libx264 -preset fast -crf 23 \\\n"
            f"  -c:a aac -b:a 128k \\\n"
            f"  \"{shorts_file}\""
        )
    else:
        commands.append(
            f"ffmpeg -i \"{screen_file}\" \\\n"
            f"  -vf \"crop=1080:1920:420:0,scale=1080:1920\" \\\n"
            f"  -c:v libx264 -preset fast -crf 23 \\\n"
            f"  -c:a aac -b:a 128k \\\n"
            f"  \"{shorts_file}\""
        )

    return "\n".join(commands)


# ── YouTube / TikTok popis a tagy ───────────────────────────────────────────

def generate_social_metadata(
    module_num: int,
    lesson_num: int,
    module_title: str,
    lesson_title: str,
    duration_min: int,
    total_modules: int = 8,
) -> dict:
    """Vygeneruje YouTube/TikTok popis, titulok a tagy pre lekciu."""

    # YouTube titulok
    youtube_title = (
        f"Prime Agent Masterclass – M{module_num}: {module_title} "
        f"| Lekcia {lesson_num} – {lesson_title}"
    )

    # TikTok titulok (kratší)
    tiktok_title = (
        f"Nauč sa {lesson_title.split('–')[0].strip().lower()} s Prime Agentom 🚀"
    )

    # YouTube popis
    youtube_description = f"""{youtube_title}

📚 **Prime Agent Masterclass** – Kompletný kurz pre vývojárov a marketérov.
Modul {module_num}: {module_title} – Lekcia {lesson_num} z {len(COURSE[module_num]['lesson_titles'])}.

⏱️ Dĺžka: {duration_min} minút
📅 Publikované: {datetime.now().strftime('%Y-%m-%d')}

🔗 **Užitočné odkazy:**
• Prime Agent GitHub: https://github.com/PrimeIntellect-ai/prime-agent
• Prime Intellect: https://primeintellect.ai
• Dokumentácia: https://docs.primeintellect.ai

📋 **V tejto lekcii:**
• Kľúčový bod 1
• Kľúčový bod 2
• Kľúčový bod 3

🎯 **Domáca úloha:** Pozri popis v kurze.

💬 **Diskusia:** Máte otázky? Napíšte komentár!

#PrimeAgent #AIAgent #CodingTutorial #Masterclass

---
🔔 **Nezabudni odoberať** pre ďalšie lekcie Prime Agent Masterclass!
"""

    # TikTok popis (kratší, virálnejší)
    tiktok_description = f"""{lesson_title} za {duration_min} minút! ⚡

🎓 Prime Agent Masterclass – Modul {module_num}
Nauč sa používať AI agenta v termináli.

{' '.join('#' + t for t in HASHTAGS_BASE[:5])}
#PrimeAgentMasterclass #LearnToCode"""

    # YouTube tagy
    youtube_tags = [
        f"M{module_num}",
        f"Modul {module_num}",
        module_title,
        lesson_title,
        "Prime Agent",
        "Prime Agent Masterclass",
        "AI Agent tutorial",
        "coding agent",
        "AI coding",
        "terminal AI",
        "autonomous agent",
        "Prime Intellect",
        "open source AI agent",
        "AI developer tools",
        "programovanie s AI",
        "AI tutoriál",
        *HASHTAGS_BASE,
        *HASHTAGS_MODULE.get(module_num, []),
    ]

    # TikTok tagy
    tiktok_tags = [
        "primeagent",
        "aiagent",
        "codingagent",
        "aitutorial",
        "programming",
        "developer",
        "terminal",
        "automation",
        "learnai",
        "techtok",
        "codetok",
        "aitools",
        *[t.lower() for t in HASHTAGS_MODULE.get(module_num, [])[:5]],
    ]

    return {
        "youtube_title": youtube_title,
        "youtube_description": youtube_description.strip(),
        "youtube_tags": youtube_tags[:50],  # YouTube limit
        "tiktok_title": tiktok_title,
        "tiktok_description": tiktok_description.strip(),
        "tiktok_tags": tiktok_tags[:20],
    }


# ── Hlavný generátor ────────────────────────────────────────────────────────

def generate_lesson(
    module_num: int,
    lesson_num: int,
    dry_run: bool = False,
) -> None:
    """Vygeneruje všetky výstupy pre jednu lekciu."""

    module = COURSE.get(module_num)
    if not module:
        print(f"❌ Modul {module_num} neexistuje.")
        return

    lesson_idx = lesson_num - 1
    if lesson_idx < 0 or lesson_idx >= len(module["lesson_titles"]):
        print(f"❌ Lekcia {lesson_num} v module {module_num} neexistuje.")
        return

    lesson_title = module["lesson_titles"][lesson_idx]
    lesson_slug = module["lessons"][lesson_idx]
    duration = module["lesson_durations"][lesson_idx]

    output_name = f"m{module_num:02d}_l{lesson_num:02d}_{lesson_slug}"

    print()
    print("=" * 72)
    print(f"  🎬 Generujem: M{module_num}L{lesson_num} – {lesson_title}")
    print(f"  ⏱️  Dĺžka: {duration} minút")
    print(f"  📁 Výstupný prefix: {output_name}")
    print("=" * 72)

    # 1. Načítaj avatar skript
    print("\n📖 [1/4] Načítavam avatar skript...")
    avatar_data = parse_avatar_script(module_num)
    lesson_avatar = avatar_data.get(lesson_num, {})

    if lesson_avatar:
        print(f"  ✓ Nájdený scenár: {len(lesson_avatar.get('segments', []))} segmentov")
        narration = "\n".join(
            seg["narration"] for seg in lesson_avatar.get("segments", [])
        )
    else:
        print("  ⚠ Avatar scenár nenájdený – použijem placeholder.")
        narration = f"Vitajte v lekcii {lesson_num} modulu {module_num}: {lesson_title}. V tejto lekcii sa naučíte kľúčové koncepty a praktické postupy."

    # 2. Nájdi Hyperframes
    print("\n🖥️  [2/4] Hľadám Hyperframes...")
    frames = find_hyperframes(module_num, lesson_num)
    if frames:
        print(f"  ✓ Nájdených {len(frames)} HTML frames:")
        for f in frames:
            print(f"    - {f.name}")
    else:
        print(f"  ⚠ Nenašli sa Hyperframes v video/hyperframes-module{module_num}-sk/")
        print(f"    Očakávaný pattern: lesson{lesson_num}-*.html")

    # 3. Generuj výstupy
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    output_file = OUTPUT_DIR / f"{output_name}_instructions.txt"

    with open(output_file, "w", encoding="utf-8") as f:
        # HeyGen inštrukcie
        f.write("=" * 72 + "\n")
        f.write("  PRIME AGENT MASTERCLASS – GENEROVANÉ INŠTRUKCIE\n")
        f.write(f"  Lekcia: M{module_num}L{lesson_num} – {lesson_title}\n")
        f.write(f"  Vygenerované: {datetime.now().isoformat()}\n")
        f.write("=" * 72 + "\n\n")

        # ── Časť A: HeyGen ──
        f.write("## ČASŤ A: HEYGEN AVATAR VIDEO\n\n")
        heygen = generate_heygen_instructions(
            module_num, lesson_num, lesson_title, narration, output_name
        )
        f.write(heygen)
        f.write("\n\n")

        # ── Časť B: Hyperframes ──
        f.write("## ČASŤ B: HYPERFRAMES SCREEN DEMO\n\n")
        hf_commands = generate_hyperframes_commands(
            module_num, lesson_num, output_name, frames
        )
        f.write(hf_commands)
        f.write("\n\n")

        # ── Časť C: FFmpeg ──
        f.write("## ČASŤ C: FFMPEG SPOJENIE\n\n")
        ffmpeg = generate_ffmpeg_commands(
            output_name,
            has_avatar=bool(lesson_avatar or True),  # avatar vždy predpokladáme
            has_screen=bool(frames),
        )
        f.write(ffmpeg)
        f.write("\n\n")

        # ── Časť D: YouTube/TikTok ──
        f.write("## ČASŤ D: YOUTUBE / TIKTOK METADÁTA\n\n")
        social = generate_social_metadata(
            module_num, lesson_num, module["title"], lesson_title, duration
        )

        f.write("### YouTube\n\n")
        f.write(f"**Titulok:**\n{social['youtube_title']}\n\n")
        f.write(f"**Popis:**\n{social['youtube_description']}\n\n")
        f.write(f"**Tagy:**\n{', '.join(social['youtube_tags'])}\n\n")

        f.write("### TikTok\n\n")
        f.write(f"**Titulok:**\n{social['tiktok_title']}\n\n")
        f.write(f"**Popis:**\n{social['tiktok_description']}\n\n")
        f.write(f"**Tagy:**\n{', '.join(social['tiktok_tags'])}\n\n")

        # ── Časť E: Zhrnutie ──
        f.write("## ČASŤ E: ZHRNUTIE – POSTUP KROK ZA KROKOM\n\n")
        f.write(f"1. Vygeneruj avatar video cez HeyGen (Časť A)\n")
        if frames:
            f.write(f"2. Vyrenderuj screen demo cez Hyperframes (Časť B)\n")
            f.write(f"3. Spoj avatar + screen demo cez FFmpeg (Časť C)\n")
            f.write(f"4. Vytvor Shorts verziu (Časť C)\n")
            f.write(f"5. Nahraj na YouTube s pripravenými titulkami (Časť D)\n")
            f.write(f"6. Postni TikTok/Shorts/Reels s pripraveným popisom (Časť D)\n")
        else:
            f.write(f"2. Spoj avatar video cez FFmpeg (Časť C)\n")
            f.write(f"3. Vytvor Shorts verziu (Časť C)\n")
            f.write(f"4. Nahraj na YouTube s pripravenými titulkami (Časť D)\n")
            f.write(f"5. Postni TikTok/Shorts/Reels s pripraveným popisom (Časť D)\n")

    print(f"\n✅ Inštrukcie uložené do: {output_file}")

    # Vypíš na stdout
    print(f"\n{'─' * 72}")
    print(f"📋 RÝCHLY PREHĽAD – M{module_num}L{lesson_num}")
    print(f"{'─' * 72}")

    # HeyGen curl
    print("\n🔹 HEYGEN CURL (skopíruj a spusti s API kľúčom):")
    print(f"    curl -X POST \"{HEYGEN_API_URL}/v2/video/generate\" \\")
    print(f"      -H \"X-Api-Key: $HEYGEN_API_KEY\" \\")
    print(f"      -d '{{\"video_name\": \"{output_name}\", ...}}'  # plné v {output_file}")

    # Hyperframes
    if frames:
        print(f"\n🔹 HYPERFRAMES RENDER ({len(frames)} frames):")
        for frame in frames:
            print(f"    npx hyperframes render --input \"{frame}\" --output \"{OUTPUT_DIR}/{output_name}_screen_XX.mp4\"")
    else:
        print(f"\n🔹 HYPERFRAMES: ⚠ žiadne HTML frames – vytvor ich v video/hyperframes-module{module_num}-sk/")

    # FFmpeg
    print(f"\n🔹 FFMPEG SPOJENIE:")
    print(f"    ffmpeg -i \"{OUTPUT_DIR}/{output_name}_avatar.mp4\" -i \"{OUTPUT_DIR}/{output_name}_screen_full.mp4\" \\")
    print(f"      -filter_complex \"...\" \"{OUTPUT_DIR}/{output_name}_final.mp4\"")

    # Social
    print(f"\n🔹 YOUTUBE TITULOK:")
    print(f"    {social['youtube_title']}")
    print(f"\n🔹 TIKTOK TITULOK:")
    print(f"    {social['tiktok_title']}")

    # Render spustiť (ak nie dry-run a existujú framy)
    if not dry_run and frames:
        print(f"\n🖥️  Spúšťam Hyperframes render...")
        for i, frame in enumerate(frames, 1):
            out_mp4 = OUTPUT_DIR / f"{output_name}_screen_{i:02d}.mp4"
            print(f"  [{i}/{len(frames)}] Renderujem: {frame.name} → {out_mp4.name}")
            try:
                subprocess.run(
                    ["npx", "hyperframes", "render",
                     "--input", str(frame),
                     "--output", str(out_mp4),
                     "--fps", "30",
                     "--scale", "1.0"],
                    check=True,
                    timeout=600,  # 10 minút max na frame
                )
                print(f"    ✓ Hotovo")
            except subprocess.CalledProcessError as e:
                print(f"    ✗ Chyba: {e}")
            except FileNotFoundError:
                print(f"    ✗ 'npx hyperframes' nie je nainštalovaný. Nainštaluj: npm i -g hyperframes")
                break
    elif not dry_run and not frames:
        print(f"\n⏭️  Hyperframes render preskočený (žiadne frames).")


# ── CLI rozhranie ───────────────────────────────────────────────────────────

def main():
    global OUTPUT_DIR

    parser = argparse.ArgumentParser(
        description="Prime Agent Masterclass – Generátor video lekcií",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=dedent("""\
        Príklady:
          python generate_videos.py --module 1 --lesson 1
          python generate_videos.py --module 1
          python generate_videos.py --all
          python generate_videos.py --module 1 --lesson 1 --dry-run
          python generate_videos.py --module 1 --list-lessons
        """),
    )

    parser.add_argument(
        "--module", "-m",
        type=int,
        choices=range(1, 9),
        help="Číslo modulu (1-8)",
    )
    parser.add_argument(
        "--lesson", "-l",
        type=int,
        choices=range(1, 7),
        help="Číslo lekcie (1-6)",
    )
    parser.add_argument(
        "--all", "-a",
        action="store_true",
        help="Vygeneruj všetky moduly a lekcie",
    )
    parser.add_argument(
        "--dry-run", "-n",
        action="store_true",
        help="Len vypíš inštrukcie, nespúšťaj render",
    )
    parser.add_argument(
        "--list-lessons",
        action="store_true",
        help="Vypíš zoznam všetkých lekcií",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=OUTPUT_DIR,
        help=f"Výstupný adresár (default: {OUTPUT_DIR})",
    )

    args = parser.parse_args()

    OUTPUT_DIR = Path(args.output_dir)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # --list-lessons
    if args.list_lessons:
        print("\n📚 Prime Agent Masterclass – Zoznam lekcií\n")
        total = 0
        for m_num in sorted(COURSE):
            m = COURSE[m_num]
            print(f"Modul {m_num}: {m['title']} ({len(m['lesson_titles'])} lekcií)")
            for i, title in enumerate(m["lesson_titles"], 1):
                print(f"  {i}. [{m['lesson_durations'][i-1]}min] {title}")
                total += 1
            print()
        total_duration = sum(
            d for m in COURSE.values() for d in m["lesson_durations"]
        )
        print(f"Celkom: {total} lekcií, {total_duration} minút "
              f"({total_duration // 60}h {total_duration % 60}m)")
        return

    # Validácia
    if args.all:
        modules_to_process = list(COURSE.keys())
    elif args.module:
        modules_to_process = [args.module]
    else:
        parser.print_help()
        print("\n❌ Musíš zadať --module, alebo --all")
        sys.exit(1)

    # Spracovanie
    for m_num in modules_to_process:
        module = COURSE[m_num]
        if args.lesson:
            # Len jedna lekcia
            if args.lesson > len(module["lesson_titles"]):
                print(f"❌ Lekcia {args.lesson} v module {m_num} neexistuje "
                      f"(max {len(module['lesson_titles'])})")
                continue
            generate_lesson(m_num, args.lesson, dry_run=args.dry_run)
        else:
            # Všetky lekcie v module
            print(f"\n{'█' * 72}")
            print(f"  MODUL {m_num}: {module['title']}")
            print(f"{'█' * 72}")
            for l_num in range(1, len(module["lesson_titles"]) + 1):
                generate_lesson(m_num, l_num, dry_run=args.dry_run)

    print(f"\n{'═' * 72}")
    print(f"  ✅ Všetky inštrukcie sú v: {OUTPUT_DIR}")
    print(f"{'═' * 72}")


if __name__ == "__main__":
    main()
