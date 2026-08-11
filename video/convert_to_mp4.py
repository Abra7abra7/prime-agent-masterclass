#!/usr/bin/env python3
"""HTML → MP4 - univerzálny konvertor"""
import subprocess, re, shutil, argparse
from pathlib import Path
from playwright.sync_api import sync_playwright

OUTPUT_DIR = Path(__file__).parent / "output"
TEMP_DIR = Path("/tmp/prime-agent-video-frames")
FPS = 24

def parse_scenes(html_path):
    html = Path(html_path).read_text()
    scenes = re.findall(r'data-duration="(\d+)"', html)
    return [int(d) / 1000 for d in scenes]

def html_to_mp4(html_path, output_path=None, width=1080, height=1350, skip_existing=True):
    html_path = Path(html_path)
    output_path = Path(output_path or html_path.with_suffix('.mp4'))

    if skip_existing and output_path.exists():
        size_mb = output_path.stat().st_size / (1024*1024)
        if size_mb > 0.1:
            print(f"⏭️  {html_path.name}: už existuje ({size_mb:.1f} MB)")
            return True

    durations = parse_scenes(html_path)
    if not durations:
        print(f"❌ {html_path.name}: žiadne scény")
        return False

    total_dur = sum(durations)
    print(f"🎬 {html_path.name}: {len(durations)} scén, {total_dur:.0f}s → ", end="", flush=True)

    TEMP_DIR.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": width, "height": height})
        page.goto(f"file://{html_path.resolve()}")
        page.wait_for_timeout(1500)

        scene_count = len(durations)
        for i in range(scene_count):
            # Aktivujem scénu: call showScene ak existuje, inak cez DOM
            try:
                page.evaluate(f'''
                    if (typeof showScene === "function") {{
                        showScene({i});
                    }} else {{
                        var scenes = document.querySelectorAll(".scene");
                        scenes.forEach(function(s, idx) {{
                            s.classList.toggle("active", idx === {i});
                        }});
                        var dots = document.querySelectorAll(".dot");
                        dots.forEach(function(d, idx) {{
                            d.classList.toggle("active", idx === {i});
                        }});
                    }}
                ''')
            except:
                pass
            page.wait_for_timeout(500)
            page.screenshot(path=str(TEMP_DIR / f"scene_{i:03d}.png"), full_page=False)

        browser.close()

    # ffmpeg concat
    concat = TEMP_DIR / "concat.txt"
    with open(concat, 'w') as f:
        for i, dur in enumerate(durations):
            f.write(f"file 'scene_{i:03d}.png'\n")
            f.write(f"duration {dur}\n")
        f.write(f"file 'scene_{len(durations)-1:03d}.png'\n")

    result = subprocess.run([
        "ffmpeg", "-y", "-loglevel", "error",
        "-f", "concat", "-safe", "0", "-i", str(concat),
        "-vf", f"fps={FPS},format=yuv420p",
        "-c:v", "libx264", "-preset", "ultrafast",
        str(output_path)
    ], capture_output=True, text=True)

    if result.returncode == 0:
        size_mb = output_path.stat().st_size / (1024*1024)
        print(f"✅ {size_mb:.1f} MB")
        return True
    else:
        print(f"❌ {result.stderr.strip()[:150]}")
        return False

def main():
    p = argparse.ArgumentParser()
    p.add_argument("html", nargs="?")
    p.add_argument("--all", action="store_true")
    p.add_argument("--module", type=int)
    p.add_argument("--width", type=int, default=1080)
    p.add_argument("--height", type=int, default=1350)
    p.add_argument("--force", action="store_true", help="Prepíš existujúce MP4")
    args = p.parse_args()

    if args.all:
        files = list(OUTPUT_DIR.glob("**/lesson*.html")) + list(OUTPUT_DIR.glob("trailer.html"))
        print(f"🎬 {len(files)} súborov\n")
        ok = sum(1 for f in sorted(files) if html_to_mp4(f, width=args.width, height=args.height, skip_existing=not args.force))
        print(f"\n✅ {ok}/{len(files)} hotovo!")
        shutil.rmtree(TEMP_DIR, ignore_errors=True)
    elif args.module:
        for f in sorted((OUTPUT_DIR / f"module{args.module}").glob("lesson*.html")):
            html_to_mp4(f, width=args.width, height=args.height)
    elif args.html:
        html_to_mp4(args.html, width=args.width, height=args.height)
    else:
        p.print_help()

if __name__ == "__main__":
    main()
