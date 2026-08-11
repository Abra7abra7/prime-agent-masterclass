#!/usr/bin/env python3
"""Generate HTML video files for Module 4 and 5 of Prime Agent Masterclass."""
import os, json

COMMON_CSS = """* { margin: 0; padding: 0; box-sizing: border-box; }
body { background: #000; font-family: system-ui, -apple-system, sans-serif; display: flex; align-items: center; justify-content: center; height: 100vh; overflow: hidden; }
#screen { width: 1080px; height: 1350px; position: relative; overflow: hidden; background: #0a0a0f; transform: scale(0.55); transform-origin: center center; border-radius: 16px; box-shadow: 0 0 100px rgba(124,92,252,0.2); }
.scene { position: absolute; top: 0; left: 0; width: 100%; height: 100%; display: flex; align-items: center; justify-content: center; transition: opacity 0.5s ease; opacity: 0; pointer-events: none; }
.scene.active { opacity: 1; pointer-events: auto; }
.scene-number { position: absolute; bottom: 40px; right: 40px; color: #52525b; font-size: 20px; }
.title-text { font-size: 68px; font-weight: 800; background: linear-gradient(135deg, #7c5cfc, #c084fc); -webkit-background-clip: text; -webkit-text-fill-color: transparent; animation: fadeInUp 0.6s ease; }
.module-badge { font-size: 28px; color: #7c5cfc; margin-bottom: 12px; animation: fadeInUp 0.6s ease; font-weight: 600; letter-spacing: 2px; }
.subtitle-text { font-size: 32px; color: #a1a1aa; margin-top: 16px; animation: fadeInUp 0.6s ease 0.2s both; }
.card-dark { background: #1a1a2e; border: 1px solid #2a2a3e; border-radius: 20px; padding: 48px; max-width: 780px; }
.card-dark h2 { color: #7c5cfc; font-size: 44px; margin-bottom: 20px; }
.card-dark p { color: #d4d4d8; font-size: 28px; line-height: 1.5; margin-bottom: 12px; }
.card-dark ul { color: #d4d4d8; font-size: 26px; line-height: 1.6; list-style: none; padding: 0; }
.card-dark ul li { padding: 6px 0; }
.card-dark ul li::before { content: '▸ '; color: #7c5cfc; font-weight: bold; }
.highlight { color: #fbbf24; font-weight: 700; }
.highlight-green { color: #4ade80; font-weight: 700; }
.highlight-red { color: #ef4444; font-weight: 700; }
.highlight-purple { color: #c084fc; font-weight: 700; }
.grid-2 { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; max-width: 850px; }
.grid-3 { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 16px; max-width: 900px; }
.grid-box { background: #1a1a2e; border: 1px solid #2a2a3e; border-radius: 16px; padding: 28px; text-align: center; }
.grid-box .icon { font-size: 44px; margin-bottom: 10px; }
.grid-box .label { color: #d4d4d8; font-size: 22px; line-height: 1.4; }
.grid-box .label-small { color: #a1a1aa; font-size: 18px; margin-top: 6px; }
.terminal { background: #0d1117; border: 1px solid #30363d; border-radius: 16px; padding: 32px; max-width: 820px; width: 100%; }
.terminal .line { font-family: 'Menlo', 'Monaco', monospace; font-size: 22px; margin-bottom: 6px; }
.terminal .prompt { color: #7c5cfc; }
.terminal .cmd { color: #e6edf3; }
.terminal .output { color: #7ee787; font-size: 20px; }
.terminal .cursor { color: #7c5cfc; animation: blink 1s infinite; }
.terminal .comment { color: #8b949e; font-size: 20px; }
.cta-container h2 { font-size: 56px; font-weight: 800; color: white; margin-bottom: 16px; }
.cta-container p { font-size: 28px; color: #a1a1aa; margin-bottom: 36px; }
.cta-btn { background: #7c5cfc; color: white; padding: 18px 52px; border-radius: 14px; font-size: 30px; font-weight: 700; display: inline-block; animation: pulse 2s infinite; }
.diagram { font-family: 'Menlo', 'Monaco', monospace; font-size: 22px; color: #d4d4d8; line-height: 1.8; }
.diagram .purple { color: #c084fc; }
.diagram .green { color: #4ade80; }
.diagram .yellow { color: #fbbf24; }
.diagram .dim { color: #52525b; }
.code-block { background: #0d1117; border: 1px solid #30363d; border-radius: 12px; padding: 24px; font-family: 'Menlo', 'Monaco', monospace; font-size: 20px; color: #e6edf3; line-height: 1.6; max-width: 820px; text-align: left; }
.code-block .kw { color: #ff7b72; }
.code-block .fn { color: #d2a8ff; }
.code-block .str { color: #a5d6ff; }
.code-block .cm { color: #8b949e; }
.emoji-big { font-size: 72px; margin-bottom: 20px; }
.timeline-line { font-size: 24px; color: #a1a1aa; line-height: 2; font-family: 'Menlo', 'Monaco', monospace; }
.table-compare { width: 100%; border-collapse: collapse; font-size: 22px; }
.table-compare th { color: #c084fc; text-align: left; padding: 10px 16px; border-bottom: 1px solid #2a2a3e; }
.table-compare td { color: #d4d4d8; padding: 10px 16px; border-bottom: 1px solid #1a1a2e; }
.dos-donts { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; max-width: 850px; }
.do-box { background: #0d2818; border: 1px solid #166534; border-radius: 16px; padding: 28px; }
.do-box h3 { color: #4ade80; font-size: 28px; margin-bottom: 12px; }
.do-box li { color: #bbf7d0; font-size: 22px; line-height: 1.6; margin-left: 20px; }
.dont-box { background: #2e0f0f; border: 1px solid #7f1d1d; border-radius: 16px; padding: 28px; }
.dont-box h3 { color: #ef4444; font-size: 28px; margin-bottom: 12px; }
.dont-box li { color: #fecaca; font-size: 22px; line-height: 1.6; margin-left: 20px; }
.architecture-box { background: #1a1a2e; border: 1px solid #2a2a3e; border-radius: 16px; padding: 32px; max-width: 820px; }
.section-title { font-size: 36px; color: #c084fc; margin-bottom: 20px; font-weight: 700; }
.summary-item { background: #1a1a2e; border: 1px solid #2a2a3e; border-radius: 12px; padding: 18px 24px; margin-bottom: 10px; font-size: 22px; color: #d4d4d8; }
.summary-item .num { color: #7c5cfc; font-weight: 700; margin-right: 10px; }
.tag { display: inline-block; background: #1a1a2e; border: 1px solid #2a2a3e; border-radius: 8px; padding: 6px 14px; font-size: 18px; color: #a1a1aa; margin: 4px; }
@keyframes pulse { 0%, 100% { box-shadow: 0 0 0 0 rgba(124,92,252,0.4); } 50% { box-shadow: 0 0 0 20px rgba(124,92,252,0); } }
@keyframes fadeInUp { from { opacity: 0; transform: translateY(20px); } to { opacity: 1; transform: translateY(0); } }
@keyframes blink { 50% { opacity: 0; } }
#progress { position: fixed; top: 20px; left: 50%; transform: translateX(-50%); display: flex; gap: 8px; z-index: 100; }
#progress .dot { width: 12px; height: 12px; border-radius: 50%; background: #3f3f46; transition: all 0.3s; }
#progress .dot.active { background: #7c5cfc; width: 36px; border-radius: 6px; }
#controls { position: fixed; bottom: 30px; left: 50%; transform: translateX(-50%); display: flex; gap: 16px; z-index: 100; }
#controls button { background: #27272a; color: white; border: none; padding: 12px 28px; border-radius: 10px; font-size: 18px; cursor: pointer; transition: background 0.2s; }
#controls button:hover { background: #3f3f46; }
#controls button.play { background: #7c5cfc; }
#controls button.play:hover { background: #6d4ff0; }"""

COMMON_JS = """let currentScene = 0, isPlaying = false, timeout = null;
const scenes = document.querySelectorAll('.scene'), dots = document.querySelectorAll('.dot');
function showScene(i) { scenes.forEach((s, idx) => s.classList.toggle('active', idx === i)); dots.forEach((d, idx) => d.classList.toggle('active', idx === i)); currentScene = i; }
function nextScene() { let next = (currentScene + 1) % scenes.length; showScene(next); if (isPlaying) scheduleNext(); }
function prevScene() { let prev = (currentScene - 1 + scenes.length) % scenes.length; showScene(prev); if (isPlaying) scheduleNext(); }
function scheduleNext() { if (timeout) clearTimeout(timeout); let dur = parseInt(scenes[currentScene].dataset.duration) || 5000; timeout = setTimeout(nextScene, dur); }
function togglePlay() { isPlaying = !isPlaying; document.getElementById('playBtn').textContent = isPlaying ? '\u23f8 Pauza' : '\u25b6 Prehra\u0165'; if (isPlaying) scheduleNext(); else if (timeout) clearTimeout(timeout); }
document.addEventListener('keydown', e => { if (e.key === 'ArrowRight' || e.key === ' ') { e.preventDefault(); nextScene(); } if (e.key === 'ArrowLeft') { e.preventDefault(); prevScene(); } if (e.key === 'p') { e.preventDefault(); togglePlay(); } });"""

def make_html(module_num, module_title, lesson_num, lesson_title, duration_min, scenes_html):
    total_scenes = len(scenes_html)
    dots = '\n'.join([f'  <div class="dot{" active" if i == 0 else ""}" data-scene="{i}"></div>' for i in range(total_scenes)])

    scenes_str = '\n\n'.join(scenes_html)

    return f'''<!DOCTYPE html>
<html lang="sk">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Prime Agent Masterclass - M{module_num}L{lesson_num}: {lesson_title}</title>
<style>
{COMMON_CSS}
</style>
</head>
<body>

<div id="progress">
{dots}
</div>

<div id="screen">

{scenes_str}

</div>

<div id="controls">
  <button onclick="prevScene()">\u25c0 Sp\u00e4\u0165</button>
  <button class="play" id="playBtn" onclick="togglePlay()">\u25b6 Prehra\u0165</button>
  <button onclick="nextScene()">\u010ealej \u25b6</button>
</div>

<script>
{COMMON_JS}
console.log('\u{1f3ac} Prime Agent Masterclass - M{module_num}L{lesson_num}: {lesson_title}');
console.log('\u{1f3ae} Ovl\u00e1danie: \u0161\u00edpky \u2190 \u2192 alebo medzern\u00edk, P = play/pauza');
console.log('\u{1f4f1} Otvor v prehliada\u010di a prepni do fullscreenu (F11)');
</script>
</body>
</html>'''

def scene(duration_ms, html):
    return f'  <div class="scene" data-duration="{duration_ms}">\n{html}\n  </div>'

# --- BUILD ALL SCENES ---

def build_all():
    # M4 L1: Co su subagenti (8 min)
    m4_l1 = []
    m4_l1.append(scene(4000, '''    <div style="text-align:center">
      <div class="module-badge">MODUL 4</div>
      <div class="title-text">\u010co s\u00fa subagenti</div>
      <div class="subtitle-text">Subagenti a delegovanie \u00b7 Lekcia 1 z 5 \u00b7 8 min</div>
    </div>'''))

    m4_l1.append(scene(6000, '''    <div class="card-dark">
      <div class="emoji-big">\U0001f3e2</div>
      <h2>Predstav si, \u017ee si CEO</h2>
      <p>Nerob\u00ed\u0161 \u00fa\u010dtovn\u00edctvo, marketing, predaj aj v\u00fdvoj s\u00e1m \u2014 <span class="highlight">naj\u00edma\u0161 \u0161pecialistov</span>.</p>
      <p style="margin-top:12px">Prime Agent funguje rovnako. Ty si hlavn\u00fd agent a na konkr\u00e9tne \u00falohy si zavol\u00e1\u0161 <span class="highlight-purple">subagenta</span>.</p>
    </div>
    <div class="scene-number">2 / 7</div>'''))

    m4_l1.append(scene(7000, '''    <div class="architecture-box">
      <div class="section-title">\U0001f3d7\ufe0f Hierarchia agentov</div>
      <div class="diagram" style="font-size:24px">
        <span class="purple">Hlavn\u00fd agent (ty / orchestr\u00e1tor)</span><br>
        <span class="dim">  \u251c\u2500\u2500</span> <span class="green">Subagent 1: SEO audit</span><br>
        <span class="dim">  \u251c\u2500\u2500</span> <span class="green">Subagent 2: Prieskum konkurencie</span><br>
        <span class="dim">  \u2514\u2500\u2500</span> <span class="green">Subagent 3: Copywriting</span>
      </div>
      <p style="color:#a1a1aa;font-size:22px;margin-top:20px">O 50 min\u00fat bude\u0161 ma\u0165 spusten\u00fa <span class="highlight">content factory s 5 agentmi</span> naraz.</p>
    </div>
    <div class="scene-number">3 / 7</div>'''))

    m4_l1.append(scene(7000, '''    <div class="architecture-box">
      <div class="section-title">\u2699\ufe0f Subagent = plnohodnotn\u00fd Prime Agent</div>
      <div class="grid-2" style="margin-top:16px">
        <div class="grid-box"><div class="icon">\U0001f9e0</div><div class="label">Vlastn\u00fd IPython kernel</div></div>
        <div class="grid-box"><div class="icon">\U0001f4cb</div><div class="label">Vlastn\u00fd kontext a tools</div></div>
        <div class="grid-box"><div class="icon">\U0001f4ac</div><div class="label">Komunikuje len s rodinou</div></div>
        <div class="grid-box"><div class="icon">\U0001f4c1</div><div class="label">Vlastn\u00fd session s\u00fabor</div></div>
      </div>
    </div>
    <div class="scene-number">4 / 7</div>'''))

    m4_l1.append(scene(8000, '''    <div class="card-dark">
      <h2>Skill vs. Subagent</h2>
      <table class="table-compare">
        <tr><th>Krit\u00e9rium</th><th style="color:#4ade80">Skill</th><th style="color:#c084fc">Subagent</th></tr>
        <tr><td>Trvanie</td><td>Sekundy\u2013min\u00faty</td><td>Min\u00faty\u2013hodiny</td></tr>
        <tr><td>Komplexita</td><td>Jeden krok</td><td>Viacero iter\u00e1ci\u00ed</td></tr>
        <tr><td>Kontext</td><td>Zdie\u013ea rodi\u010da</td><td>Vlastn\u00fd izolovan\u00fd</td></tr>
        <tr><td>Paralelizmus</td><td>Nie</td><td>\u00c1no \u2013 viac naraz</td></tr>
        <tr><td>Pr\u00edklad</td><td style="color:#a5d6ff">websearch()</td><td style="color:#a5d6ff">Kompletn\u00fd SEO audit</td></tr>
      </table>
      <p style="margin-top:20px;font-size:26px"><span class="highlight">Skill = funkcia.</span> <span class="highlight-purple">Subagent = kolega.</span></p>
    </div>
    <div class="scene-number">5 / 7</div>'''))

    m4_l1.append(scene(7000, '''    <div class="dos-donts">
      <div class="do-box">
        <h3>\u2705 DOs</h3>
        <ul>
          <li>Jasn\u00fd, ohrani\u010den\u00fd cie\u013e</li>
          <li>Jeden subagent = jedna zodpovednos\u0165</li>
          <li>Paraleln\u00e9 sp\u00fa\u0161\u0165anie nez\u00e1visl\u00fdch \u00faloh</li>
          <li>Priebe\u017en\u00e9 posielanie v\u00fdsledkov</li>
        </ul>
      </div>
      <div class="dont-box">
        <h3>\u274c DON\u2019Ts</h3>
        <ul>
          <li>Subagent na 1 skill call</li>
          <li>Spolieha\u0165 sa na premenn\u00e9 z kernelu</li>
          <li>Obrovsk\u00fd prompt</li>
          <li>Zabudn\u00fa\u0165 na agent_message.send()</li>
        </ul>
      </div>
    </div>
    <div class="scene-number">6 / 7</div>'''))

    m4_l1.append(scene(5000, '''    <div class="card-dark" style="text-align:center">
      <h2>\U0001f3af K\u013e\u00fa\u010dov\u00e9 body</h2>
      <p>Subagent = plnohodnotn\u00fd Prime Agent s <span class="highlight">vlastn\u00fdm kernelom</span></p>
      <p style="font-size:24px;margin-top:12px"><span class="highlight-green">Skill</span> = funkcia (sekundy) | <span class="highlight-purple">Subagent</span> = kolega (min\u00faty)</p>
      <p style="font-size:24px;margin-top:12px">Hierarchia je <span class="highlight">stromov\u00e1</span> \u2013 agent vid\u00ed len rodi\u010da + s\u00faro dencov + deti</p>
      <p style="font-size:24px;margin-top:12px">V\u00fdsledok mus\u00ed explicitne odosla\u0165 cez <span class="highlight-yellow" style="color:#fbbf24">agent_message.send()</span></p>
    </div>
    <div class="scene-number">7 / 7</div>'''))

    m4l1_html = make_html(4, "Subagenti a delegovanie", 1, "\u010co s\u00fa subagenti a kedy ich pou\u017ei\u0165", 8, m4_l1)

    # M4 L2
    m4_l2 = []
    m4_l2.append(scene(4000, '''    <div style="text-align:center">
      <div class="module-badge">MODUL 4</div>
      <div class="title-text">Sp\u00fa\u0161\u0165anie a riadenie</div>
      <div class="subtitle-text">Subagenti a delegovanie \u00b7 Lekcia 2 z 5 \u00b7 12 min</div>
    </div>'''))

    m4_l2.append(scene(6000, '''    <div class="terminal">
      <div class="section-title">\U0001f680 Prv\u00fd subagent \u2013 Live Demo</div>
      <div class="line"><span class="prompt">>>> </span><span class="cmd">handle = await rlm('Urob SEO audit dom\u00e9ny example.com')</span></div>
      <div style="margin-top:24px; color:#8b949e; font-size:20px;line-height:1.6">
        # Vr\u00e1ti HANDLE, nie v\u00fdsledok:<br>
        {<br>
        &nbsp;&nbsp;'rlm_child_id': '019fed18-...',<br>
        &nbsp;&nbsp;'name': 'prime-agent-child-abc123',<br>
        &nbsp;&nbsp;'session_dir': '/Users/.../sub-e0e633eb',<br>
        &nbsp;&nbsp;'model': 'deepseek-v4-flash'<br>
        }
      </div>
      <p style="color:#fbbf24;font-size:22px;margin-top:16px">\u26a0\ufe0f rlm() vr\u00e1ti handle okam\u017eite. Subagent be\u017e\u00ed na pozad\u00ed.</p>
    </div>
    <div class="scene-number">2 / 8</div>'''))

    m4_l2.append(scene(6000, '''    <div class="card-dark">
      <h2>\U0001f4dd Anat\u00f3mia dobr\u00e9ho task promptu</h2>
      <p><span class="highlight">1. Rola</span> \u2013 \u201eSi marketingov\u00fd analytik\u201c</p>
      <p><span class="highlight">2. Presn\u00fd scope</span> \u2013 \u201ePresk\u00famaj t\u00fdchto 3 konkurentov: ...\u201c</p>
      <p><span class="highlight">3. Form\u00e1t v\u00fdstupu</span> \u2013 \u201eV\u00fdstup vr\u00e1\u0165 ako markdown tabu\u013eku.\u201c</p>
      <p><span class="highlight">4. In\u0161trukcia na odoslanie</span> \u2013 \u201ePo\u0161li v\u00fdsledok cez agent_message.send()\u201c</p>
      <p style="margin-top:16px;color:#ef4444;font-size:24px">\u274c Zl\u00fd prompt: \u201ePresk\u00famaj konkurenciu\u201c</p>
    </div>
    <div class="scene-number">3 / 8</div>'''))

    m4_l2.append(scene(6000, '''    <div class="architecture-box">
      <div class="section-title">\U0001f4e1 3 sp\u00f4soby monitoringu</div>
      <div class="summary-item"><span class="num">1</span> <span class="highlight-purple">agent_observe</span> \u2013 observe_child(), list_subagents()</div>
      <div class="summary-item"><span class="num">2</span> <span class="highlight-green">\u010c\u00edtanie logov</span> \u2013 session_dir subagenta obsahuje konverza\u010dn\u00fd log</div>
      <div class="summary-item"><span class="num">3</span> <span class="highlight">agent_message</span> \u2013 spr\u00e1va od subagenta pr\u00edde automaticky</div>
    </div>
    <div class="scene-number">4 / 8</div>'''))

    m4_l2.append(scene(7000, '''    <div class="architecture-box">
      <div class="section-title">\u23f1\ufe0f Lifecycle subagenta</div>
      <div class="diagram" style="font-size:22px; line-height:2">
        <span class="purple">[Rodi\u010d]</span>                <span class="green">[Subagent]</span><br>
        &nbsp;&nbsp;|<span class="dim">\u2500\u2500 rlm('\u00faloha') \u2500\u2500</span>\u2192|<br>
        &nbsp;&nbsp;|   <span class="dim">(handle sp\u00e4\u0165)</span>   |<span class="dim">\u2500\u2500 \u010c\u00edta prompt, pl\u00e1nuje</span><br>
        &nbsp;&nbsp;|   <span class="dim">(paralelne</span>      |<span class="dim">\u2500\u2500 Sp\u00fa\u0161\u0165a tools, iteruje</span><br>
        &nbsp;&nbsp;|    <span class="dim">m\u00f4\u017ee robi\u0165</span>     |<span class="dim">\u2500\u2500 Kompletizuje v\u00fdsledok</span><br>
        &nbsp;&nbsp;|    <span class="dim">in\u00e9 veci)</span>    |<br>
        &nbsp;&nbsp;|\u2190<span class="dim">\u2500\u2500 agent_message \u2500\u2500</span>|<br>
        &nbsp;&nbsp;|<span class="dim">   .send(v\u00fdsledok)    </span>|<br>
        &nbsp;&nbsp;|<span class="dim">\u2500\u2500 Spracuje v\u00fdsledok</span> |<span class="dim">\u2500\u2500 Idle / koniec</span>
      </div>
    </div>
    <div class="scene-number">5 / 8</div>'''))

    m4_l2.append(scene(5000, '''    <div class="terminal">
      <div class="section-title">\U0001f5c2\ufe0f Riadenie viacer\u00fdch subagentov</div>
      <div class="line"><span class="prompt">>>> </span><span class="cmd">subagents = {}</span></div>
      <div class="line output">subagents['seo'] = await rlm('Urob SEO audit')</div>
      <div class="line output">subagents['social'] = await rlm('Nap\u00ed\u0161 5 LinkedIn postov')</div>
      <div class="line output">subagents['email'] = await rlm('Vytvor welcome sekvenciu')</div>
      <div style="margin-top:16px; color:#fbbf24; font-size:20px"># Udr\u017eiavaj si mapu subagentov, zbiera\u0161 v\u00fdsledky nesk\u00f4r</div>
    </div>
    <div class="scene-number">6 / 8</div>'''))

    m4_l2.append(scene(5000, '''    <div class="card-dark">
      <h2>\U0001f527 Debugging: Ke\u010f subagent ml\u010d\u00ed</h2>
      <div class="summary-item"><span class="num">1</span>Skontroluj logy: existuje konverza\u010dn\u00fd log?</div>
      <div class="summary-item"><span class="num">2</span>Mal prompt in\u0161trukciu na <span class="highlight-purple">agent_message.send()</span>?</div>
      <div class="summary-item"><span class="num">3</span>Po\u0161li follow-up: <span class="highlight-green">receiver_role="child"</span></div>
      <div class="summary-item"><span class="num">4</span>Timeout a retry s lep\u0161\u00edm promptom</div>
    </div>
    <div class="scene-number">7 / 8</div>'''))

    m4_l2.append(scene(5000, '''    <div class="card-dark" style="text-align:center">
      <h2>\U0001f3af K\u013e\u00fa\u010dov\u00e9 body</h2>
      <p><span class="highlight">rlm()</span> vr\u00e1ti handle okam\u017eite, subagent be\u017e\u00ed paralelne</p>
      <p style="font-size:24px;margin-top:10px">Task prompt: <span class="highlight-green">rola + scope + form\u00e1t + odoslanie</span></p>
      <p style="font-size:24px;margin-top:10px">Monitoring: agent_observe, list_subagents(), logy</p>
      <p style="font-size:24px;margin-top:10px">Ke\u010f ml\u010d\u00ed: <span class="highlight-red">logy \u2192 follow-up \u2192 retry</span></p>
    </div>
    <div class="scene-number">8 / 8</div>'''))

    m4l2_html = make_html(4, "Subagenti a delegovanie", 2, "Sp\u00fa\u0161\u0165anie a riadenie subagentov", 12, m4_l2)

    # M4 L3
    m4_l3 = []
    m4_l3.append(scene(4000, '''    <div style="text-align:center">
      <div class="module-badge">MODUL 4</div>
      <div class="title-text">Paraleln\u00e9 spracovanie</div>
      <div class="subtitle-text">Subagenti a delegovanie \u00b7 Lekcia 3 z 5 \u00b7 10 min</div>
    </div>'''))

    m4_l3.append(scene(6000, '''    <div class="card-dark">
      <h2>\u26a1 Pre\u010do paralelizmus men\u00ed hru</h2>
      <div style="margin-bottom:16px">
        <p style="color:#ef4444">Sekven\u010dne:</p>
        <p style="font-size:24px">[SEO: 8min] \u2192 [Content: 10min] \u2192 [Social: 6min] \u2192 [Email: 7min]</p>
        <p style="font-size:28px;color:#ef4444">Celkom: 31 min\u00fat</p>
      </div>
      <div style="margin-top:20px">
        <p style="color:#4ade80">Paralelne:</p>
        <p style="font-size:24px">[SEO: 8min] | [Content: 10min] | [Social: 6min] | [Email: 7min]</p>
        <p style="font-size:28px;color:#4ade80">Celkom: 10 min\u00fat (najdlh\u0161ia \u00faloha)</p>
      </div>
      <p style="font-size:32px;margin-top:16px;color:#fbbf24">\U0001f680 3x r\u00fdchlej\u0161ie!</p>
    </div>
    <div class="scene-number">2 / 7</div>'''))

    m4_l3.append(scene(6000, '''    <div class="terminal">
      <div class="section-title">Spustenie 4 subagentov naraz</div>
      <div class="line"><span class="prompt">>>> </span><span class="cmd">tasks = {'seo': 'Urob SEO audit...', 'copy': 'Nap\u00ed\u0161 landing page...',</span></div>
      <div class="line" style="margin-left:28px"><span class="cmd">'social': 'Vytvor 5 LinkedIn postov...', 'research': 'Presk\u00famaj konkurenciu...'}</span></div>
      <div style="margin-top:10px; color:#8b949e; font-size:18px"># Spusti v\u0161etky paralelne</div>
      <div class="line"><span class="prompt">>>> </span><span class="cmd">handles = {}</span></div>
      <div class="line"><span class="prompt">>>> </span><span class="cmd">for name, task in tasks.items():</span></div>
      <div class="line" style="margin-left:28px"><span class="cmd">handles[name] = await rlm(task)</span></div>
      <div class="line output" style="margin-top:10px">\U0001f680 V\u0161etci 4 subagenti be\u017eia paralelne!</div>
    </div>
    <div class="scene-number">3 / 7</div>'''))

    m4_l3.append(scene(6000, '''    <div class="architecture-box" style="text-align:center">
      <div class="section-title">\U0001f4e1 Fan-out / Fan-in Pattern</div>
      <div class="diagram" style="font-size:22px;line-height:1.8">
        <span style="color:#fbbf24">FAN-OUT (distrib\u00facia):</span><br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="purple">Hlavn\u00fd agent</span><br>
        &nbsp;&nbsp;<span class="dim">/ &nbsp;&nbsp;&nbsp;| &nbsp;&nbsp;&nbsp;\\ &nbsp;&nbsp;&nbsp;\\</span><br>
        <span class="green">SEO &nbsp;Copy &nbsp;Social &nbsp;Research</span><br><br>
        <span style="color:#fbbf24">FAN-IN (zber v\u00fdsledkov):</span><br>
        <span class="green">SEO &nbsp;Copy &nbsp;Social &nbsp;Research</span><br>
        &nbsp;&nbsp;<span class="dim">\\ &nbsp;&nbsp;&nbsp;| &nbsp;&nbsp;&nbsp;| &nbsp;&nbsp;&nbsp;/</span><br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="purple">Hlavn\u00fd agent</span><br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="highlight">Fin\u00e1lny v\u00fdstup</span>
      </div>
    </div>
    <div class="scene-number">4 / 7</div>'''))

    m4_l3.append(scene(7000, '''    <div class="card-dark">
      <h2>\U0001f504 3 Orchestra\u010dn\u00e9 patterny</h2>
      <p><span class="highlight">Pattern 1: Sekven\u010dn\u00fd re\u0165azec</span></p>
      <p style="font-size:22px;margin-left:20px;color:#a1a1aa">A \u2192 B \u2192 C (ka\u017ed\u00fd \u010dak\u00e1 na predch\u00e1dzaj\u00faceho)</p>
      <p style="margin-top:12px"><span class="highlight">Pattern 2: Paraleln\u00fd s 1 z\u00e1vislos\u0165ou</span></p>
      <p style="font-size:22px;margin-left:20px;color:#a1a1aa">A \u2192 (B, C, D paralelne s v\u00fdsledkom A)</p>
      <p style="margin-top:12px"><span class="highlight">Pattern 3: Pipeline</span></p>
      <p style="font-size:22px;margin-left:20px;color:#a1a1aa">Paraleln\u00e1 f\u00e1za 1 \u2192 Paraleln\u00e1 f\u00e1za 2</p>
      <p style="margin-top:16px;color:#fbbf24;font-size:24px">\U0001f4a1 2\u20135 paraleln\u00fdch agentov = sweet spot</p>
    </div>
    <div class="scene-number">5 / 7</div>'''))

    m4_l3.append(scene(5000, '''    <div class="grid-2">
      <div class="grid-box"><div class="icon">\u26a1</div><div class="label">2\u20135 agentov: optim\u00e1lne</div></div>
      <div class="grid-box"><div class="icon">\u26a0\ufe0f</div><div class="label">5\u201310: sleduj CPU a RAM</div></div>
      <div class="grid-box"><div class="icon">\U0001f6d1</div><div class="label">10+: resource management</div></div>
      <div class="grid-box"><div class="icon">\U0001f4a1</div><div class="label">Rate limiting: asyncio.sleep(1)</div></div>
    </div>
    <div class="scene-number">6 / 7</div>'''))

    m4_l3.append(scene(5000, '''    <div class="card-dark" style="text-align:center">
      <h2>\U0001f3af K\u013e\u00fa\u010dov\u00e9 body</h2>
      <p>Paralelizmus = <span class="highlight">a\u017e 4x r\u00fdchlej\u0161ie</span> v\u00fdsledky</p>
      <p style="font-size:24px;margin-top:10px"><span class="highlight-purple">Fan-out / Fan-in</span> = z\u00e1kladn\u00fd pattern</p>
      <p style="font-size:24px;margin-top:10px">3 orchestra\u010dn\u00e9 patterny: re\u0165azec, paraleln\u00fd s z\u00e1vislos\u0165ou, pipeline</p>
      <p style="font-size:24px;margin-top:10px"><span class="highlight-green">2\u20135 paraleln\u00fdch</span> = sweet spot</p>
    </div>
    <div class="scene-number">7 / 7</div>'''))

    m4l3_html = make_html(4, "Subagenti a delegovanie", 3, "Paraleln\u00e9 spracovanie \u2013 viac agentov naraz", 10, m4_l3)

    # M4 L4
    m4_l4 = []
    m4_l4.append(scene(4000, '''    <div style="text-align:center">
      <div class="module-badge">MODUL 4</div>
      <div class="title-text">Komunik\u00e1cia medzi agentmi</div>
      <div class="subtitle-text">Subagenti a delegovanie \u00b7 Lekcia 4 z 5 \u00b7 10 min</div>
    </div>'''))

    m4_l4.append(scene(6000, '''    <div class="architecture-box" style="text-align:center">
      <div class="section-title">\U0001f310 Komunika\u010dn\u00fd model</div>
      <div class="diagram" style="font-size:22px;line-height:1.8">
        <span class="purple">Hlavn\u00fd agent (root)</span><br>
        <span class="dim">  \u251c\u2500\u2500\u2194\ufe0f</span> <span class="green">Subagent A</span><br>
        <span class="dim">  \u2502     \u251c\u2500\u2500\u2194\ufe0f</span> <span class="green">Subagent A1</span><br>
        <span class="dim">  \u2502     \u2514\u2500\u2500\u2194\ufe0f</span> <span class="green">Subagent A2</span><br>
        <span class="dim">  \u2514\u2500\u2500\u2194\ufe0f</span> <span class="green">Subagent B</span><br>
        <span class="dim">        \u2514\u2500\u2500\u2194\ufe0f</span> <span class="green">Subagent B1</span>
      </div>
      <p style="color:#fbbf24;font-size:20px;margin-top:16px">\u2194\ufe0f = obojsmern\u00e1 cez agent_message<br>A1\u2194A2 (s\u00faro denci) \u2713 | A1\u2194B1 (mimo dosahu) \u2717</p>
    </div>
    <div class="scene-number">2 / 7</div>'''))

    m4_l4.append(scene(6000, '''    <div class="terminal">
      <div class="section-title">\U0001f4e8 agent_message.send()</div>
      <div class="line"><span class="comment"># Rodi\u010dovi</span></div>
      <div class="line"><span class="prompt">>>> </span><span class="cmd">await agent_message.send(</span></div>
      <div class="line" style="margin-left:28px"><span class="str">"Tu je SEO audit..."</span>, <span class="kw">receiver_role</span>=<span class="str">"parent"</span>)</div>
      <div class="line" style="margin-top:12px"><span class="comment"># Die\u0165a\u0165u</span></div>
      <div class="line"><span class="prompt">>>> </span><span class="cmd">await agent_message.send(</span></div>
      <div class="line" style="margin-left:28px"><span class="str">"Super, e\u0161te uprav..."</span>, <span class="kw">receiver_role</span>=<span class="str">"child"</span>,</div>
      <div class="line" style="margin-left:28px"><span class="kw">receiver_name</span>=<span class="str">"prime-agent-child-abc123"</span>)</div>
    </div>
    <div class="scene-number">3 / 7</div>'''))

    m4_l4.append(scene(6000, '''    <div class="card-dark">
      <h2>\U0001f504 Follow-up = dial\u00f3g so subagentom</h2>
      <p>Subagent <span class="highlight">nie je</span> \u201efire and forget\u201c</p>
      <p style="margin-top:8px;font-size:24px;color:#a1a1aa">1. Spust\u00ed\u0161 subagenta \u2192 dostane\u0161 v\u00fdsledok</p>
      <p style="font-size:24px;color:#a1a1aa">2. Po\u0161le\u0161 follow-up: <span class="highlight-green">receiver_role="child"</span></p>
      <p style="font-size:24px;color:#a1a1aa">3. Subagent spracuje \u2192 po\u0161le op\u00e4\u0165</p>
      <p style="margin-top:12px;font-size:26px"><span class="highlight-purple">Plnohodnotn\u00fd dial\u00f3g.</span> Subagent = \u0161pecialista, s ktor\u00fdm iteruje\u0161.</p>
    </div>
    <div class="scene-number">4 / 7</div>'''))

    m4_l4.append(scene(5000, '''    <div class="architecture-box">
      <div class="section-title">\U0001f46b S\u00farodeneck\u00e1 komunik\u00e1cia</div>
      <div class="diagram" style="font-size:20px;line-height:1.8">
        <span class="green">Subagent A (SEO)</span> \u2192 <span class="green">Subagent B (Copy)</span><br>
        <span style="color:#a1a1aa">"Hej, tu s\u00fa keywords: AI agent tutorial,</span><br>
        <span style="color:#a1a1aa">&nbsp;Prime Agent n\u00e1vod. Pou\u017ei ich v postoch."</span>
      </div>
      <p style="margin-top:16px;color:#4ade80;font-size:22px">\u2705 V\u00fdhoda: rodi\u010d nemus\u00ed sprostredkova\u0165</p>
      <p style="color:#ef4444;font-size:22px">\u26a0\ufe0f Nev\u00fdhoda: rodi\u010d str\u00e1ca preh\u013ead</p>
    </div>
    <div class="scene-number">5 / 7</div>'''))

    m4_l4.append(scene(5000, '''    <div class="card-dark">
      <h2>\U0001faaa Zlat\u00e9 pravidl\u00e1 komunik\u00e1cie</h2>
      <div class="summary-item"><span class="num">1</span>Bu\u010f <span class="highlight">explicitn\u00fd</span> v ka\u017edej spr\u00e1ve</div>
      <div class="summary-item"><span class="num">2</span>Jedna spr\u00e1va = <span class="highlight">jedna my\u0161lienka</span></div>
      <div class="summary-item"><span class="num">3</span>Potvr\u010f pr\u00edjem <span class="highlight">kritick\u00fdch spr\u00e1v</span></div>
      <div class="summary-item"><span class="num">4</span>Timeout a retry ak <span class="highlight-red">nepr\u00edde odpove\u010f</span></div>
      <div class="summary-item"><span class="num">5</span>Nezahlcuj rodi\u010da \u2013 <span class="highlight-purple">d\u00e1vkuj spr\u00e1vy</span></div>
    </div>
    <div class="scene-number">6 / 7</div>'''))

    m4_l4.append(scene(5000, '''    <div class="card-dark" style="text-align:center">
      <h2>\U0001f3af K\u013e\u00fa\u010dov\u00e9 body</h2>
      <p><span class="highlight-purple">agent_message.send()</span> = jedin\u00fd sp\u00f4sob komunik\u00e1cie</p>
      <p style="font-size:24px;margin-top:10px">Komunikuje\u0161 len s: <span class="highlight">rodi\u010dom, de\u0165mi, s\u00farodencami</span></p>
      <p style="font-size:24px;margin-top:10px">Rodi\u010d prij\u00edma spr\u00e1vy automaticky</p>
      <p style="font-size:24px;margin-top:10px">Follow-up = <span class="highlight-green">dial\u00f3g so \u0161pecialistom</span></p>
    </div>
    <div class="scene-number">7 / 7</div>'''))

    m4l4_html = make_html(4, "Subagenti a delegovanie", 4, "Komunik\u00e1cia medzi agentmi", 10, m4_l4)

    # M4 L5: Content factory s 5 agentmi
    m4_l5 = []
    m4_l5.append(scene(4000, '''    <div style="text-align:center">
      <div class="module-badge">MODUL 4</div>
      <div class="title-text">Content Factory</div>
      <div class="subtitle-text">Subagenti a delegovanie \u00b7 Lekcia 5 z 5 \u00b7 10 min</div>
    </div>'''))

    m4_l5.append(scene(7000, '''    <div class="architecture-box" style="text-align:center">
      <div class="section-title">\U0001f3ed Architekt\u00fara Content Factory</div>
      <div class="diagram" style="font-size:20px;line-height:1.6">
        <span class="purple">ORCHESTR\u00c1TOR (ty)</span><br>
        <span class="dim">  \u2502</span><br>
        <span class="dim">  \u251c\u2500\u2500</span> <span class="green">Agent 1: STRAT\u00c9G</span><br>
        <span class="dim">  \u2502     \u2514\u2500\u2500</span> <span style="color:#a1a1aa">T\u00e9my, keywords, form\u00e1ty</span><br>
        <span class="dim">  \u251c\u2500\u2500</span> <span class="green">Agent 2: COPYWRITER</span><br>
        <span class="dim">  \u2502     \u2514\u2500\u2500</span> <span style="color:#a1a1aa">Blog posty, landing pages</span><br>
        <span class="dim">  \u251c\u2500\u2500</span> <span class="green">Agent 3: SOCIAL</span><br>
        <span class="dim">  \u2502     \u2514\u2500\u2500</span> <span style="color:#a1a1aa">LinkedIn a Twitter/X</span><br>
        <span class="dim">  \u251c\u2500\u2500</span> <span class="green">Agent 4: EMAIL</span><br>
        <span class="dim">  \u2502     \u2514\u2500\u2500</span> <span style="color:#a1a1aa">Welcome a nurture sekvencie</span><br>
        <span class="dim">  \u2514\u2500\u2500</span> <span class="green">Agent 5: SEO</span><br>
        <span class="dim">        \u2514\u2500\u2500</span> <span style="color:#a1a1aa">Optimaliz\u00e1cia v\u0161etk\u00e9ho</span>
      </div>
      <p style="color:#fbbf24;font-size:22px;margin-top:16px">5 agentov. Jeden cie\u013e. &lt;15 min\u00fat.</p>
    </div>
    <div class="scene-number">2 / 7</div>'''))

    m4_l5.append(scene(6000, '''    <div class="card-dark">
      <h2>\U0001f4cb Krok 1: Strat\u00e9g \u2192 potom zvy\u0161ok</h2>
      <p style="color:#4ade80;font-size:26px">1. Spusti Strat\u00e9ga <span style="color:#a1a1aa">(sekven\u010dne \u2013 mus\u00ed by\u0165 prv\u00fd)</span></p>
      <p style="font-size:22px;color:#a1a1aa;margin-left:20px">Vytvor\u00ed obsahov\u00fa strat\u00e9giu: piliere, t\u00e9my, keywords</p>
      <p style="color:#fbbf24;font-size:26px;margin-top:12px">2. Copywriter + Social + Email <span style="color:#a1a1aa">(PARALELNE)</span></p>
      <p style="font-size:22px;color:#a1a1aa;margin-left:20px">Ka\u017ed\u00fd dostane strat\u00e9giu ako kontext</p>
      <p style="color:#c084fc;font-size:26px;margin-top:12px">3. SEO agent <span style="color:#a1a1aa">(sekven\u010dne \u2013 potrebuje v\u0161etok obsah)</span></p>
      <p style="font-size:22px;color:#a1a1aa;margin-left:20px">Optimalizuje keywords, headlines, meta descriptions</p>
    </div>
    <div class="scene-number">3 / 7</div>'''))

    m4_l5.append(scene(5000, '''    <div class="terminal">
      <div class="section-title">Krok 2: Paraleln\u00e9 spustenie</div>
      <div class="line"><span class="comment"># Po z\u00edskan\u00ed strat\u00e9gie od Strat\u00e9ga...</span></div>
      <div class="line"><span class="prompt">>>> </span><span class="cmd">copy_handle = await rlm("Si copywriter. Na z\u00e1klade strat\u00e9gie...")</span></div>
      <div class="line output">\u2705 Copywriter spusten\u00fd</div>
      <div class="line"><span class="prompt">>>> </span><span class="cmd">social_handle = await rlm("Si social media mana\u017e\u00e9r...")</span></div>
      <div class="line output">\u2705 Social agent spusten\u00fd</div>
      <div class="line"><span class="prompt">>>> </span><span class="cmd">email_handle = await rlm("Si email marketing \u0161pecialista...")</span></div>
      <div class="line output">\u2705 Email agent spusten\u00fd</div>
      <div style="color:#4ade80;font-size:22px;margin-top:12px">\U0001f680 Copywriter, Social a Email be\u017eia paralelne!</div>
    </div>
    <div class="scene-number">4 / 7</div>'''))

    m4_l5.append(scene(5000, '''    <div class="architecture-box">
      <div class="section-title">\U0001f4ca Krok 4: Fin\u00e1lna kompil\u00e1cia</div>
      <div style="color:#d4d4d8;font-size:22px;line-height:1.8">
        <span style="color:#fbbf24">\U0001f4e6 Content Factory Output:</span><br>
        <span style="color:#a1a1aa">\u251c\u2500\u2500 \U0001f3af Content Strategy</span><br>
        <span style="color:#a1a1aa">\u251c\u2500\u2500 \u270d\ufe0f Blog Post + Landing Page</span><br>
        <span style="color:#a1a1aa">\u251c\u2500\u2500 \U0001f4f1 Social Media (LinkedIn + Twitter)</span><br>
        <span style="color:#a1a1aa">\u251c\u2500\u2500 \U0001f4e7 Email Campaigns (Welcome + Nurture)</span><br>
        <span style="color:#a1a1aa">\u2514\u2500\u2500 \U0001f50d SEO Optimizations</span>
      </div>
      <p style="color:#4ade80;font-size:22px;margin-top:20px">\U0001f4be Ulo\u017een\u00e9 do content-factory-output.md</p>
    </div>
    <div class="scene-number">5 / 7</div>'''))

    m4_l5.append(scene(7000, '''    <div class="card-dark">
      <h2>\U0001f4c8 V\u00fdsledky a metriky</h2>
      <div class="grid-2">
        <div class="grid-box"><div class="icon">\u23f1\ufe0f</div><div class="label">~12\u201315 min\u00fat</div><div class="label-small">namiesto 2\u20133 dn\u00ed</div></div>
        <div class="grid-box"><div class="icon">\U0001f916</div><div class="label">5 agentov</div><div class="label-small">strat\u00e9g + copy + social + email + SEO</div></div>
        <div class="grid-box"><div class="icon">\U0001f4c4</div><div class="label">1 strat\u00e9gia + blog + landing page</div><div class="label-small">+ 5 LinkedIn + 3 thready + 8 emailov</div></div>
        <div class="grid-box"><div class="icon">\U0001f504</div><div class="label">Sekven\u010dn\u00fd \u2192 Paraleln\u00fd \u2192 Sekven\u010dn\u00fd</div><div class="label-small">orchestra\u010dn\u00fd pattern</div></div>
      </div>
    </div>
    <div class="scene-number">6 / 7</div>'''))

    m4_l5.append(scene(5000, '''    <div class="card-dark" style="text-align:center">
      <h2>\U0001f3af K\u013e\u00fa\u010dov\u00e9 body</h2>
      <p>Content Factory = <span class="highlight">5 \u0161pecialistov + orchestr\u00e1tor</span></p>
      <p style="font-size:24px;margin-top:10px">Pattern: <span class="highlight-purple">Sekven\u010dn\u00fd \u2192 Paraleln\u00fd \u2192 Sekven\u010dn\u00fd</span></p>
      <p style="font-size:24px;margin-top:10px">~12\u201315 min\u00fat = <span class="highlight-green">namiesto 2\u20133 dn\u00ed</span> manu\u00e1lnej pr\u00e1ce</p>
      <p style="font-size:24px;margin-top:10px">Pou\u017eite\u013en\u00e9 na <span class="highlight">ak\u00fdko\u013evek komplexn\u00fd projekt</span></p>
    </div>
    <div class="scene-number">7 / 7</div>'''))

    m4l5_html = make_html(4, "Subagenti a delegovanie", 5, "Content factory s 5 agentmi", 10, m4_l5)

    # --- MODULE 5 ---
    # M5 L1
    m5_l1 = []
    m5_l1.append(scene(4000, '''    <div style="text-align:center">
      <div class="module-badge">MODUL 5</div>
      <div class="title-text">Agent pre LinkedIn obsah</div>
      <div class="subtitle-text">Automatiz\u00e1cia marketingu \u00b7 Lekcia 1 z 6 \u00b7 12 min</div>
    </div>'''))

    m5_l1.append(scene(6000, '''    <div class="card-dark">
      <h2>\U0001f537 Pre\u010do LinkedIn</h2>
      <div class="grid-2">
        <div class="grid-box"><div class="icon">\U0001f465</div><div class="label">1 miliarda pou\u017e\u00edvate\u013eov</div></div>
        <div class="grid-box"><div class="icon">\U0001f4c8</div><div class="label">10\u201330% organick\u00fd dosah</div></div>
        <div class="grid-box"><div class="icon">\U0001f3af</div><div class="label">#1 B2B lead generation</div></div>
        <div class="grid-box"><div class="icon">\u26a1</div><div class="label">5\u201310x v\u00e4\u010d\u0161\u00ed dosah pri konzistencii</div></div>
      </div>
      <p style="margin-top:16px;font-size:26px;color:#fbbf24">Agent ti vygeneruje <span class="highlight">mesiac obsahu za 10 min\u00fat</span>.</p>
    </div>
    <div class="scene-number">2 / 8</div>'''))

    m5_l1.append(scene(5000, '''    <div class="card-dark">
      <h2>\U0001f4cb Definuj svoj LinkedIn kontext</h2>
      <div style="color:#a1a1aa;font-size:22px;line-height:1.8">
        <span style="color:#c084fc">M\u00f4j LinkedIn kontext:</span><br>
        \u2022 Meno a rola<br>
        \u2022 Cie\u013eovka<br>
        \u2022 T\u00e9my, o ktor\u00fdch hovor\u00edm<br>
        \u2022 Tone of voice<br>
        \u2022 \u010co NIKDY nep\u00ed\u0161em<br>
        \u2022 Cie\u013e (followers, leady)
      </div>
      <p style="margin-top:12px;font-size:22px;color:#fbbf24">\u26a0\ufe0f Bez kontextu = generick\u00fd obsah. Toto je tvoj brand book.</p>
    </div>
    <div class="scene-number">3 / 8</div>'''))

    m5_l1.append(scene(7000, '''    <div class="card-dark">
      <h2>\U0001f4dd Mix form\u00e1tov (20 postov/mesiac)</h2>
      <div class="summary-item"><span class="num">6\u00d7</span> <span class="highlight-green">Lekcia / How-to</span> \u2013 konkr\u00e9tny tip</div>
      <div class="summary-item"><span class="num">5\u00d7</span> <span class="highlight">Contrarian take</span> \u2013 proti mainstreamu</div>
      <div class="summary-item"><span class="num">4\u00d7</span> <span class="highlight-purple">Osobn\u00fd pr\u00edbeh</span> \u2013 s konkr\u00e9tnou lekciou</div>
      <div class="summary-item"><span class="num">3\u00d7</span> <span class="highlight-yellow" style="color:#fbbf24">Data / \u0160tatistika</span> \u2013 prekvapiv\u00e9 \u010d\u00edslo + insight</div>
      <div class="summary-item"><span class="num">2\u00d7</span> <span class="highlight-red">Behind the scenes</span> \u2013 ako re\u00e1lne pou\u017e\u00edva\u0161 AI</div>
      <p style="margin-top:10px;font-size:22px">Pre ka\u017ed\u00fd: <span style="color:#4ade80">Hook \u2192 Telo \u2192 CTA \u2192 Hashtags</span></p>
    </div>
    <div class="scene-number">4 / 8</div>'''))

    m5_l1.append(scene(7000, '''    <div class="card-dark">
      <h2>\u270d\ufe0f Dobr\u00fd vs. Zl\u00fd LinkedIn post</h2>
      <div class="dont-box" style="margin-bottom:16px">
        <h3>\u274c ZL\u00dd</h3>
        <p style="color:#fecaca;font-size:22px">"V dne\u0161nej dobe je d\u00f4le\u017eit\u00e9 pou\u017e\u00edva\u0165 AI n\u00e1stroje. Pom\u00e1haj\u00fa n\u00e1m by\u0165 produkt\u00edvnej\u0161\u00edmi. \u010co si o tom mysl\u00edte?"</p>
      </div>
      <div class="do-box">
        <h3>\u2705 DOBR\u00dd</h3>
        <p style="color:#bbf7d0;font-size:22px">"Minul\u00fd t\u00fd\u017ede\u0148 som nap\u00edsal 2000 riadkov k\u00f3du. Presnej\u0161ie: m\u00f4j agent ich nap\u00edsal. Ja som len reviewoval. V\u00fdsledok: 4 hodiny namiesto 2 dn\u00ed."</p>
      </div>
      <p style="margin-top:10px;font-size:24px;color:#fbbf24">Rozdiel: <span class="highlight">konkr\u00e9tny, autentick\u00fd, data-driven</span></p>
    </div>
    <div class="scene-number">5 / 8</div>'''))

    m5_l1.append(scene(5000, '''    <div class="terminal">
      <div class="section-title">\U0001f504 Iter\u00e1cia s agentom</div>
      <div class="line"><span class="comment"># 1. gener\u00e1cia \u2192 kontrola \u2192 follow-up \u2192 fin\u00e1lna verzia</span></div>
      <div class="line" style="margin-top:12px"><span class="prompt">>>> </span><span class="cmd">await agent_message.send("Super z\u00e1klad. Teraz:</span></div>
      <div class="line output">1. V How-to postoch pridaj konkr\u00e9tne \u010d\u00edsla</div>
      <div class="line output">2. V Contrarian postoch pridaj protiargument</div>
      <div class="line output">3. Skontroluj pattern interrupt v hookoch</div>
      <div class="line"><span class="str">", receiver_role="child", receiver_name=handle['name'])</span></div>
      <div style="margin-top:12px;color:#4ade80;font-size:20px"># Typicky 2\u20133 kol\u00e1 sta\u010dia</div>
    </div>
    <div class="scene-number">6 / 8</div>'''))

    m5_l1.append(scene(6000, '''    <div class="card-dark">
      <h2>\U0001f4c5 Publika\u010dn\u00fd kalend\u00e1r</h2>
      <div style="color:#d4d4d8;font-size:22px;line-height:1.8">
        <span style="color:#7c5cfc">Pondelok:</span> Lekcia / How-to<br>
        <span style="color:#7c5cfc">Utorok:</span> Najsilnej\u0161\u00ed post (najv\u00e4\u010d\u0161ia aktivita)<br>
        <span style="color:#7c5cfc">Streda:</span> Contrarian take<br>
        <span style="color:#7c5cfc">\u0160tvrtok:</span> Najsilnej\u0161\u00ed post<br>
        <span style="color:#7c5cfc">Piatok:</span> \u013dah\u0161\u00ed, osobn\u00fd t\u00f3n
      </div>
      <p style="margin-top:12px;font-size:22px;color:#fbbf24">\U0001f4a1 Repurpose: 1 mesiac LinkedIn \u2192 blog \u2192 newsletter \u2192 Twitter</p>
    </div>
    <div class="scene-number">7 / 8</div>'''))

    m5_l1.append(scene(5000, '''    <div class="card-dark" style="text-align:center">
      <h2>\U0001f3af K\u013e\u00fa\u010dov\u00e9 body</h2>
      <p>Kvalitn\u00fd obsah za\u010d\u00edna <span class="highlight">kvalitn\u00fdm kontextom</span></p>
      <p style="font-size:24px;margin-top:10px">Mix form\u00e1tov = <span class="highlight-green">konzistentn\u00fd engagement</span></p>
      <p style="font-size:24px;margin-top:10px"><span class="highlight-purple">Hook</span> je v\u0161etko \u2013 prv\u00fd riadok = scroll stop</p>
      <p style="font-size:24px;margin-top:10px">Iteruj: <span class="highlight">gener\u00e1cia \u2192 kontrola \u2192 follow-up</span></p>
    </div>
    <div class="scene-number">8 / 8</div>'''))

    m5l1_html = make_html(5, "Automatiz\u00e1cia marketingu", 1, "Agent pre LinkedIn obsah", 12, m5_l1)

    # M5 L2
    m5_l2 = []
    m5_l2.append(scene(4000, '''    <div style="text-align:center">
      <div class="module-badge">MODUL 5</div>
      <div class="title-text">Agent pre Twitter/X thready</div>
      <div class="subtitle-text">Automatiz\u00e1cia marketingu \u00b7 Lekcia 2 z 6 \u00b7 10 min</div>
    </div>'''))

    m5_l2.append(scene(6000, '''    <div class="card-dark">
      <h2>\U0001f426 Pre\u010do Twitter/X thready</h2>
      <div class="grid-2">
        <div class="grid-box"><div class="icon">\U0001f4cf</div><div class="label">Viac priestoru ako 280 znakov</div></div>
        <div class="grid-box"><div class="icon">\U0001f4ac</div><div class="label">Ka\u017ed\u00fd tweet = \u010fal\u0161\u00ed engagement</div></div>
        <div class="grid-box"><div class="icon">\U0001f680</div><div class="label">Algoritmus boostuje thready</div></div>
        <div class="grid-box"><div class="icon">\U0001f4ca</div><div class="label">1 thread = 100K+ impresi\u00ed</div></div>
      </div>
      <p style="margin-top:16px;font-size:24px;color:#fbbf24">Manu\u00e1lne: 45\u201390 min. <span class="highlight">S agentom: 2 min\u00faty.</span></p>
    </div>
    <div class="scene-number">2 / 7</div>'''))

    m5_l2.append(scene(7000, '''    <div class="card-dark">
      <h2>\U0001f9ec Anat\u00f3mia v\u00edrusov\u00e9ho threadu</h2>
      <div style="color:#d4d4d8;font-size:22px;line-height:1.7">
        <span style="color:#fbbf24">Tweet 1:</span> <span class="highlight">HOOK</span> \u2013 \u0161okuj\u00face tvrdenie<br>
        <span style="color:#fbbf24">Tweet 2:</span> KONTEXT \u2013 pre\u010do je to d\u00f4le\u017eit\u00e9<br>
        <span style="color:#fbbf24">Tweet 3\u20135:</span> HLAVN\u00dd OBSAH \u2013 3 body/kroky<br>
        <span style="color:#fbbf24">Tweet 6:</span> ZVRAT / AHA MOMENT<br>
        <span style="color:#fbbf24">Tweet 7:</span> <span class="highlight-purple">CTA + RT request</span>
      </div>
      <p style="margin-top:16px;font-size:26px;color:#7c5cfc">Hook je 80% \u00faspechu threadu!</p>
    </div>
    <div class="scene-number">3 / 7</div>'''))

    m5_l2.append(scene(7000, '''    <div class="card-dark">
      <h2>\U0001faa9 5 formul pre hooks</h2>
      <div class="summary-item"><span class="num">1</span><span class="highlight">\u010c\u00edslo + kontroverzia:</span> \u201e90% developers use AI wrong\u201c</div>
      <div class="summary-item"><span class="num">2</span><span class="highlight">Z\u00e1kaz:</span> \u201eStop using ChatGPT for coding\u201c</div>
      <div class="summary-item"><span class="num">3</span><span class="highlight-purple">Tajomstvo:</span> \u201eThe secret to 10x productivity nobody talks about\u201c</div>
      <div class="summary-item"><span class="num">4</span><span class="highlight-green">Porovnanie:</span> \u201eJunior dev vs Senior dev: how they use AI\u201c</div>
      <div class="summary-item"><span class="num">5</span><span class="highlight-red" style="color:#ef4444">\u010casov\u00e1 tiese\u0148:</span> \u201eIf you're not using AI agents by 2026...\u201c</div>
      <p style="margin-top:10px;font-size:22px;color:#fbbf24">\U0001f4a1 Nechaj agenta vygenerova\u0165 20 hookov a vyber top 10.</p>
    </div>
    <div class="scene-number">4 / 7</div>'''))

    m5_l2.append(scene(5000, '''    <div class="card-dark">
      <h2>\u23f0 Optim\u00e1lne \u010dasy publikovania</h2>
      <div style="color:#d4d4d8;font-size:24px;line-height:1.8">
        <span class="highlight-green">Najlep\u0161ie dni:</span> Utorok, Streda, \u0160tvrtok<br>
        <span class="highlight-green">Najlep\u0161\u00ed \u010das:</span> 13:00\u201315:00 alebo 17:00\u201319:00<br>
        <span class="highlight-red">Nikdy:</span> V\u00edkend pred 12:00<br>
        <span class="highlight-purple">Max:</span> 3 thready t\u00fd\u017edenne, min. 2 dni medzi
      </div>
    </div>
    <div class="scene-number">5 / 7</div>'''))

    m5_l2.append(scene(6000, '''    <div class="architecture-box">
      <div class="section-title">\U0001f504 Repurposing Pipeline</div>
      <div class="diagram" style="font-size:22px;line-height:1.8">
        <span class="purple">Twitter Thread</span><br>
        <span class="dim">  \u251c\u2500\u2500</span> <span class="green">Roz\u0161\u00edr na LinkedIn carousel</span><br>
        <span class="dim">  \u251c\u2500\u2500</span> <span class="green">Roz\u0161\u00edr na blog post (800\u20131200 slov)</span><br>
        <span class="dim">  \u251c\u2500\u2500</span> <span class="green">Skr\u00e1\u0165 na 3 izolovan\u00e9 tweety</span><br>
        <span class="dim">  \u2514\u2500\u2500</span> <span class="green">Pou\u017ei ako newsletter t\u00e9mu</span>
      </div>
      <p style="margin-top:16px;font-size:24px;color:#fbbf24">1 hodina s agentom = obsah na cel\u00fd t\u00fd\u017ede\u0148 na 3 platformy</p>
    </div>
    <div class="scene-number">6 / 7</div>'''))

    m5_l2.append(scene(5000, '''    <div class="card-dark" style="text-align:center">
      <h2>\U0001f3af K\u013e\u00fa\u010dov\u00e9 body</h2>
      <p>Thread = <span class="highlight">Hook \u2192 Kontext \u2192 3 body \u2192 Zvrat \u2192 CTA</span></p>
      <p style="font-size:24px;margin-top:10px">Hook = <span class="highlight-purple">80% \u00faspechu</span>, nau\u010d sa 5 formul</p>
      <p style="font-size:24px;margin-top:10px">Publikuj <span class="highlight-green">Ut\u2013\u0160t, 13:00\u201319:00</span>, max 3 t\u00fd\u017edenne</p>
      <p style="font-size:24px;margin-top:10px">1 thread \u2192 <span class="highlight">multi-platform obsah</span></p>
    </div>
    <div class="scene-number">7 / 7</div>'''))

    m5l2_html = make_html(5, "Automatiz\u00e1cia marketingu", 2, "Agent pre Twitter/X thready", 10, m5_l2)

    # M5 L3
    m5_l3 = []
    m5_l3.append(scene(4000, '''    <div style="text-align:center">
      <div class="module-badge">MODUL 5</div>
      <div class="title-text">Agent pre email kampane</div>
      <div class="subtitle-text">Automatiz\u00e1cia marketingu \u00b7 Lekcia 3 z 6 \u00b7 12 min</div>
    </div>'''))

    m5_l3.append(scene(6000, '''    <div class="card-dark">
      <h2>\U0001f4e7 Email = ROI kr\u00e1\u013e</h2>
      <div class="emoji-big" style="font-size:56px">\U0001f4b5</div>
      <p><span class="highlight">$36 sp\u00e4\u0165</span> za ka\u017ed\u00fd $1 investovan\u00fd</p>
      <div style="margin-top:24px">
        <p style="color:#ef4444;font-size:24px">Manu\u00e1lne: 1 sekvencia = 4\u20138 hod\u00edn</p>
        <p style="color:#4ade80;font-size:24px">S Prime Agentom: 5 sekvenci\u00ed = 10 min\u00fat</p>
      </div>
    </div>
    <div class="scene-number">2 / 7</div>'''))

    m5_l3.append(scene(7000, '''    <div class="card-dark">
      <h2>\U0001f4ec 3 typy emailov\u00fdch sekvenci\u00ed</h2>
      <div class="summary-item"><span class="num">1</span><span class="highlight-green">WELCOME</span> (3\u20135 emailov) \u2013 aktivova\u0165, quick win</div>
      <div style="color:#a1a1aa;font-size:20px;margin:4px 0 12px 28px">Vitaj \u2192 Pr\u00edbeh \u2192 Top zdroje \u2192 Social proof</div>
      <div class="summary-item"><span class="num">2</span><span class="highlight-purple">NURTURE</span> (5\u20137 emailov) \u2013 d\u00f4vera, vzdel\u00e1vanie</div>
      <div style="color:#a1a1aa;font-size:20px;margin:4px 0 12px 28px">Probl\u00e9m \u2192 Lekcie \u2192 Case study \u2192 Soft pitch</div>
      <div class="summary-item"><span class="num">3</span><span class="highlight">RE-ENGAGEMENT</span> (3 emaily) \u2013 prebudenie</div>
      <div style="color:#a1a1aa;font-size:20px;margin:4px 0 0 28px">Ch\u00fdba\u0161 n\u00e1m \u2192 Exkluz\u00edvny obsah \u2192 Posledn\u00fd email</div>
    </div>
    <div class="scene-number">3 / 7</div>'''))

    m5_l3.append(scene(6000, '''    <div class="card-dark">
      <h2>\U0001f4e8 Anat\u00f3mia ka\u017ed\u00e9ho emailu</h2>
      <div style="color:#d4d4d8;font-size:24px;line-height:1.8">
        <span class="highlight">Subject line</span> (max 50 znakov)<br>
        <span class="highlight-purple">Preheader</span> (max 100 znakov)<br>
        <span style="color:#a1a1aa">Telo emailu</span> (150\u2013300 slov, plain text)<br>
        <span class="highlight-green">CTA</span> (jeden, jasn\u00fd)<br>
        <span style="color:#52525b">Pozn\u00e1mka pre teba: pre\u010do to funguje</span>
      </div>
    </div>
    <div class="scene-number">4 / 7</div>'''))

    m5_l3.append(scene(7000, '''    <div class="card-dark">
      <h2>\U0001f52c 7 typov subject lines</h2>
      <div class="summary-item"><span class="num">1</span>Zvedavos\u0165: <span style="color:#a1a1aa">\u201eToto ti na Code Review nikto nepovie\u201c</span></div>
      <div class="summary-item"><span class="num">2</span>\u010c\u00edslo: <span style="color:#a1a1aa">\u201e5 ch\u00fdb pri pou\u017e\u00edvan\u00ed AI\u201c</span></div>
      <div class="summary-item"><span class="num">3</span>Personalizovan\u00e9: <span style="color:#a1a1aa">\u201eMarek, tvoj k\u00f3d m\u00f4\u017ee by\u0165 10x r\u00fdchlej\u0161\u00ed\u201c</span></div>
      <div class="summary-item"><span class="num">4</span>Urgency: <span style="color:#a1a1aa">\u201ePosledn\u00fdch 24 hod\u00edn na early bird\u201c</span></div>
      <div class="summary-item"><span class="num">5</span>How-to: <span style="color:#a1a1aa">\u201eAko som zn\u00ed\u017eil \u010das v\u00fdvoja o 70%\u201c</span></div>
      <div class="summary-item"><span class="num">6</span>Contrarian: <span style="color:#a1a1aa">\u201ePresta\u0148 pou\u017e\u00edva\u0165 Copilota\u201c</span></div>
      <div class="summary-item"><span class="num">7</span>Kr\u00e1tke: <span style="color:#a1a1aa">\u201eAI. K\u00f3d. Hotovo.\u201c</span></div>
    </div>
    <div class="scene-number">5 / 7</div>'''))

    m5_l3.append(scene(5000, '''    <div class="card-dark">
      <h2>\U0001f4ca K\u013e\u00fa\u010dov\u00e9 metriky</h2>
      <div class="grid-2">
        <div class="grid-box"><div class="icon">\U0001f4ec</div><div class="label">Open rate</div><div class="label-small">&gt;40% welcome<br>&gt;25% nurture</div></div>
        <div class="grid-box"><div class="icon">\U0001f446</div><div class="label">Click rate</div><div class="label-small">&gt;5% welcome<br>&gt;3% nurture</div></div>
        <div class="grid-box"><div class="icon">\U0001f4c9</div><div class="label">Unsubscribe</div><div class="label-small">&lt;0.5% na email</div></div>
        <div class="grid-box"><div class="icon">\U0001f3af</div><div class="label">Conversion</div><div class="label-small">Z\u00e1vis\u00ed od ponuky</div></div>
      </div>
    </div>
    <div class="scene-number">6 / 7</div>'''))

    m5_l3.append(scene(5000, '''    <div class="card-dark" style="text-align:center">
      <h2>\U0001f3af K\u013e\u00fa\u010dov\u00e9 body</h2>
      <p>3 typy: <span class="highlight-green">Welcome</span> \u00b7 <span class="highlight-purple">Nurture</span> \u00b7 <span class="highlight">Re-engagement</span></p>
      <p style="font-size:24px;margin-top:10px">Ka\u017ed\u00fd email: subject + preheader + body + <span class="highlight">1 CTA</span></p>
      <p style="font-size:24px;margin-top:10px">7 typov subject lines \u2013 <span class="highlight-purple">A/B testuj!</span></p>
      <p style="font-size:24px;margin-top:10px">Export do CSV/JSON pre <span class="highlight-green">ConvertKit, Mailchimp</span></p>
    </div>
    <div class="scene-number">7 / 7</div>'''))

    m5l3_html = make_html(5, "Automatiz\u00e1cia marketingu", 3, "Agent pre email kampane", 12, m5_l3)

    # M5 L4
    m5_l4 = []
    m5_l4.append(scene(4000, '''    <div style="text-align:center">
      <div class="module-badge">MODUL 5</div>
      <div class="title-text">Agent pre SEO a content strat\u00e9giu</div>
      <div class="subtitle-text">Automatiz\u00e1cia marketingu \u00b7 Lekcia 4 z 6 \u00b7 15 min</div>
    </div>'''))

    m5_l4.append(scene(6000, '''    <div class="card-dark">
      <h2>\U0001f310 SEO v \u00e9re AI</h2>
      <div class="grid-2">
        <div class="grid-box"><div class="icon">\U0001f916</div><div class="label">Google AI Overviews</div><div class="label-small">Odpoved\u00e1 priamo</div></div>
        <div class="grid-box"><div class="icon">\U0001f4ac</div><div class="label">ChatGPT/SearchGPT</div><div class="label-small">Konverza\u010dn\u00e9 vyh\u013ead\u00e1vanie</div></div>
        <div class="grid-box"><div class="icon">\U0001f50d</div><div class="label">Perplexity</div><div class="label-small">Cituje zdroje</div></div>
        <div class="grid-box"><div class="icon">\U0001f9e0</div><div class="label">Claude/Gemini</div><div class="label-small">Vlastn\u00e9 znalostn\u00e9 b\u00e1zy</div></div>
      </div>
      <p style="margin-top:12px;font-size:24px;color:#fbbf24">Potrebuje\u0161 SEO agenta pre <span class="highlight">oba svety</span>: tradi\u010dn\u00fd Google + AI LLM.</p>
    </div>
    <div class="scene-number">2 / 8</div>'''))

    m5_l4.append(scene(6000, '''    <div class="architecture-box">
      <div class="section-title">\U0001f4d0 SEO & Content Strategy Framework</div>
      <div style="color:#d4d4d8;font-size:24px;line-height:2">
        <span class="highlight-red">1. AUDIT</span> \u2013 technick\u00e9, on-page, off-page<br>
        <span class="highlight">2. KEYWORDS</span> \u2013 prieskum, klastre, intent<br>
        <span class="highlight-green">3. CONTENT</span> \u2013 pl\u00e1n, t\u00e9my, form\u00e1ty<br>
        <span class="highlight-purple">4. AI VISIBILITY</span> \u2013 llms.txt, \u0161trukt\u00farovan\u00e9 d\u00e1ta<br>
        <span style="color:#52525b">5. MONITORING</span> \u2013 rank tracking, traffic
      </div>
    </div>
    <div class="scene-number">3 / 8</div>'''))

    m5_l4.append(scene(6000, '''    <div class="card-dark">
      <h2>\U0001f50d Krok 1: SEO Audit</h2>
      <p style="font-size:24px;color:#c084fc">\u010co agent skontroluje:</p>
      <div class="grid-2" style="margin-top:12px">
        <div style="color:#a1a1aa;font-size:20px;line-height:1.6">\u2699\ufe0f <span style="color:#d4d4d8">Technick\u00e9</span><br>R\u00fdchlos\u0165, mobil, SSL, sitemap, broken links</div>
        <div style="color:#a1a1aa;font-size:20px;line-height:1.6">\U0001f4dd <span style="color:#d4d4d8">On-Page</span><br>Title tagy, meta, H1-H6, alt texty</div>
        <div style="color:#a1a1aa;font-size:20px;line-height:1.6">\U0001f4c4 <span style="color:#d4d4d8">Obsah</span><br>Top str\u00e1nky, duplicity, thin content</div>
        <div style="color:#a1a1aa;font-size:20px;line-height:1.6">\U0001f517 <span style="color:#d4d4d8">Off-Page</span><br>Sp\u00e4tn\u00e9 odkazy, dom\u00e9nov\u00e1 autorita</div>
      </div>
      <p style="margin-top:12px;font-size:22px;color:#fbbf24">Pre ka\u017ed\u00fd probl\u00e9m: priorita + dopad + fix.</p>
    </div>
    <div class="scene-number">4 / 8</div>'''))

    m5_l4.append(scene(6000, '''    <div class="card-dark">
      <h2>\U0001f3af Krok 2: Keyword Research</h2>
      <div class="summary-item"><span class="num">5\u201310</span><span class="highlight">Prim\u00e1rne keywords</span> (high volume, high intent)</div>
      <div class="summary-item"><span class="num">15\u201320</span><span class="highlight-purple">Sekund\u00e1rne keywords</span> (long-tail)</div>
      <div class="summary-item"><span class="num">10\u201315</span><span class="highlight-green">Ot\u00e1zky</span> (People Also Ask, \u201eako\u201c, \u201epre\u010do\u201c)</div>
      <p style="margin-top:16px;font-size:22px">Pre ka\u017ed\u00e9: <span class="highlight">search volume</span> \u00b7 intent \u00b7 obtia\u017enos\u0165</p>
      <p style="font-size:22px;margin-top:8px">4\u20135 <span class="highlight-purple">obsahov\u00fdch klastrov</span> (pillar + podporn\u00e9 \u010dl\u00e1nky)</p>
      <p style="font-size:22px;margin-top:8px"><span class="highlight-green">90-d\u0148ov\u00fd obsahov\u00fd kalend\u00e1r</span></p>
    </div>
    <div class="scene-number">5 / 8</div>'''))

    m5_l4.append(scene(7000, '''    <div class="card-dark">
      <h2>\U0001f916 Krok 3: AI SEO \u2013 llms.txt</h2>
      <div class="terminal" style="font-size:18px">
        <div style="color:#8b949e"># llms.txt pre mojadomena.sk</div>
        <div style="color:#a1a1aa">&gt; Kurzy a n\u00e1vody o AI agentoch pre v\u00fdvoj\u00e1rov.</div>
        <div style="color:#8b949e;margin-top:8px">## Dokument\u00e1cia</div>
        <div style="color:#a5d6ff">- Prime Agent n\u00e1vod: In\u0161tal\u00e1cia, skills, subagenti</div>
        <div style="color:#a5d6ff">- Skills Referencia: V\u0161etky skilly a ich pou\u017eitie</div>
        <div style="color:#8b949e;margin-top:8px">## Blog</div>
        <div style="color:#a5d6ff">- AI agent pre v\u00fdvoj\u00e1rov: Anal\u00fdza, porovnanie</div>
        <div style="color:#a5d6ff">- 10 ch\u00fdb pri pou\u017e\u00edvan\u00ed AI: Praktick\u00e9 tipy</div>
      </div>
      <p style="margin-top:12px;font-size:22px;color:#fbbf24">llms.txt = robots.txt pre AI. Do kore\u0148a dom\u00e9ny.</p>
    </div>
    <div class="scene-number">6 / 8</div>'''))

    m5_l4.append(scene(5000, '''    <div class="card-dark">
      <h2>\U0001f4d0 Krok 4: Programatick\u00e9 SEO</h2>
      <p><span class="highlight">Template + Data = 100+ str\u00e1nok</span></p>
      <p style="font-size:22px;color:#a1a1aa;margin-top:8px">Typy programatick\u00fdch str\u00e1nok:</p>
      <div class="summary-item"><span class="num">1</span>\u201e[N\u00e1stroj] alternativa\u201c str\u00e1nky</div>
      <div class="summary-item"><span class="num">2</span>\u201e[T\u00e9ma] pre [rola]\u201c str\u00e1nky</div>
      <div class="summary-item"><span class="num">3</span>\u201e[Keyword] n\u00e1vod\u201c str\u00e1nky</div>
    </div>
    <div class="scene-number">7 / 8</div>'''))

    m5_l4.append(scene(5000, '''    <div class="card-dark" style="text-align:center">
      <h2>\U0001f3af K\u013e\u00fa\u010dov\u00e9 body</h2>
      <p>Modern\u00e9 SEO = <span class="highlight">tradi\u010dn\u00e9 + AI SEO</span> (LLMs, AI Overviews)</p>
      <p style="font-size:24px;margin-top:10px">Framework: <span class="highlight-purple">Audit \u2192 Keywords \u2192 Content \u2192 AI Vis \u2192 Monitoring</span></p>
      <p style="font-size:24px;margin-top:10px"><span class="highlight-green">llms.txt</span> = nov\u00fd \u0161tandard pre AI \u010ditate\u013enos\u0165</p>
      <p style="font-size:24px;margin-top:10px">90-d\u0148ov\u00fd pl\u00e1n: <span class="highlight">Mesiac 1 opravy, 2 obsah, 3 \u0161k\u00e1lovanie</span></p>
    </div>
    <div class="scene-number">8 / 8</div>'''))

    m5l4_html = make_html(5, "Automatiz\u00e1cia marketingu", 4, "Agent pre SEO a content strat\u00e9giu", 15, m5_l4)

    # M5 L5
    m5_l5 = []
    m5_l5.append(scene(4000, '''    <div style="text-align:center">
      <div class="module-badge">MODUL 5</div>
      <div class="title-text">Agent pre prieskum konkurencie</div>
      <div class="subtitle-text">Automatiz\u00e1cia marketingu \u00b7 Lekcia 5 z 6 \u00b7 10 min</div>
    </div>'''))

    m5_l5.append(scene(6000, '''    <div class="card-dark">
      <h2>\U0001f50e Pre\u010do prieskum konkurencie</h2>
      <p>V\u00e4\u010d\u0161ina \u013eud\u00ed si pozrie len <span class="highlight-red">homepage a pricing</span>. To nesta\u010d\u00ed.</p>
      <div style="margin-top:16px;font-size:22px;color:#a1a1aa">
        Dobr\u00fd prieskum ti d\u00e1:<br>
        <span class="highlight-green">\u2713</span> Positioning gaps<br>
        <span class="highlight-green">\u2713</span> Obsahov\u00e9 diery<br>
        <span class="highlight-green">\u2713</span> Cenov\u00e9 pr\u00edle\u017eitosti<br>
        <span class="highlight-green">\u2713</span> N\u00e1pady, \u010do spravi\u0165 <span class="highlight">INAK</span>
      </div>
      <p style="margin-top:12px;font-size:24px;color:#fbbf24">Agent to sprav\u00ed za 5 min\u00fat. Na jedn\u00e9ho konkurenta.</p>
    </div>
    <div class="scene-number">2 / 7</div>'''))

    m5_l5.append(scene(7000, '''    <div class="card-dark">
      <h2>\U0001f4cb 7 \u010dast\u00ed profilu konkurenta</h2>
      <div class="summary-item"><span class="num">1</span><span class="highlight">Z\u00e1kladn\u00fd profil</span> \u2013 n\u00e1zov, t\u00edm, misia</div>
      <div class="summary-item"><span class="num">2</span><span class="highlight-purple">Produktov\u00e1 anal\u00fdza</span> \u2013 features, USP, pricing</div>
      <div class="summary-item"><span class="num">3</span><span class="highlight-green">Positioning</span> \u2013 messaging, tone of voice, pain pointy</div>
      <div class="summary-item"><span class="num">4</span><span class="highlight">Obsahov\u00e1 anal\u00fdza</span> \u2013 blog, soci\u00e1lne siete, lead magnety</div>
      <div class="summary-item"><span class="num">5</span><span class="highlight-yellow" style="color:#fbbf24">SEO anal\u00fdza</span> \u2013 keywords, traffic, sp\u00e4tn\u00e9 odkazy</div>
      <div class="summary-item"><span class="num">6</span><span class="highlight-red">SWOT</span> \u2013 siln\u00e9, slab\u00e9 str\u00e1nky, pr\u00edle\u017eitosti, hrozby</div>
      <div class="summary-item"><span class="num">7</span><span class="highlight-purple">Ak\u010dn\u00e9 odpor\u00fa\u010dania</span> \u2013 5 vec\u00ed spravi\u0165 lep\u0161ie</div>
    </div>
    <div class="scene-number">3 / 7</div>'''))

    m5_l5.append(scene(6000, '''    <div class="terminal">
      <div class="section-title">\u26a1 Paraleln\u00fd prieskum 5 konkurentov</div>
      <div class="line"><span class="comment"># Spusti v\u0161etk\u00fdch PARALELNE</span></div>
      <div class="line"><span class="prompt">>>> </span><span class="cmd">competitors = [</span></div>
      <div class="line"><span class="str">    {"name": "Cursor AI", "url": "https://cursor.com"},</span></div>
      <div class="line"><span class="str">    {"name": "GitHub Copilot", "url": "https://github.com/..."},</span></div>
      <div class="line"><span class="str">    {"name": "Codeium", "url": "https://codeium.com"},</span></div>
      <div class="line"><span class="str">    {"name": "Tabnine", "url": "https://tabnine.com"},</span></div>
      <div class="line"><span class="str">    {"name": "Amazon CodeWhisperer", "url": "..."}</span></div>
      <div class="line"><span class="cmd">]</span></div>
      <div class="line output" style="margin-top:8px">\U0001f680 5 konkurentov sa analyzuje paralelne!</div>
    </div>
    <div class="scene-number">4 / 7</div>'''))

    m5_l5.append(scene(6000, '''    <div class="card-dark">
      <h2>\U0001f4ca Competitive Landscape Report</h2>
      <p>Ke\u010f m\u00e1\u0161 profily v\u0161etk\u00fdch konkurentov, <span class="highlight">syntetizuj</span>:</p>
      <div style="margin-top:12px;font-size:22px;color:#a1a1aa;line-height:1.8">
        <span class="highlight">1.</span> Executive summary<br>
        <span class="highlight-purple">2.</span> Porovn\u00e1vacia tabu\u013eka<br>
        <span class="highlight-green">3.</span> Positioning mapa (2 osi)<br>
        <span class="highlight">4.</span> GAP anal\u00fdza \u2013 \u010do nikto nerob\u00ed<br>
        <span class="highlight-red">5.</span> Odpor\u00fa\u010dania pre strat\u00e9giu<br>
        <span class="highlight-purple">6.</span> Battle card \u2013 3 vety pre sales
      </div>
    </div>
    <div class="scene-number">5 / 7</div>'''))

    m5_l5.append(scene(5000, '''    <div class="card-dark">
      <h2>\U0001f504 Automatizovan\u00fd monitoring</h2>
      <div class="summary-item"><span class="num">\U0001f4c5</span>T\u00fd\u017edenn\u00fd subagent skontroluje v\u0161etk\u00fdch konkurentov</div>
      <div class="summary-item"><span class="num">\U0001f4cb</span>Weekly Competitive Brief \u2013 1 strana, k\u013e\u00fa\u010dov\u00e9 zmeny</div>
      <div class="summary-item"><span class="num">\U0001f514</span>Notifik\u00e1cie: \u010do eskalova\u0165 okam\u017eite</div>
      <p style="margin-top:16px;font-size:22px;color:#fbbf24">Konkurencia sa men\u00ed. Monitoring = n\u00e1skok.</p>
    </div>
    <div class="scene-number">6 / 7</div>'''))

    m5_l5.append(scene(5000, '''    <div class="card-dark" style="text-align:center">
      <h2>\U0001f3af K\u013e\u00fa\u010dov\u00e9 body</h2>
      <p>Prieskum = <span class="highlight">Profil + Positioning + Obsah + SEO + SWOT + Akcia</span></p>
      <p style="font-size:24px;margin-top:10px">5 konkurentov paralelne = <span class="highlight-green">5x r\u00fdchlej\u0161ie</span></p>
      <p style="font-size:24px;margin-top:10px">Synt\u00e9za je k\u013e\u00fa\u010dov\u00e1 \u2013 profily s\u00fa d\u00e1ta, <span class="highlight-purple">synt\u00e9za je strat\u00e9gia</span></p>
      <p style="font-size:24px;margin-top:10px">Monitoring = <span class="highlight">t\u00fd\u017edenn\u00fd subagent</span></p>
    </div>
    <div class="scene-number">7 / 7</div>'''))

    m5l5_html = make_html(5, "Automatiz\u00e1cia marketingu", 5, "Agent pre prieskum konkurencie", 10, m5_l5)

    # M5 L6
    m5_l6 = []
    m5_l6.append(scene(4000, '''    <div style="text-align:center">
      <div class="module-badge">MODUL 5</div>
      <div class="title-text">30-d\u0148ov\u00e1 kampa\u0148 na autopilota</div>
      <div class="subtitle-text">Automatiz\u00e1cia marketingu \u00b7 Lekcia 6 z 6 \u00b7 6 min</div>
    </div>'''))

    m5_l6.append(scene(8000, '''    <div class="architecture-box">
      <div class="section-title">\U0001f680 30-Day Marketing Autopilot</div>
      <div style="color:#d4d4d8;font-size:19px;line-height:1.6">
        <span class="highlight">T\u00dd\u017dDE\u0147 1: FOUNDATION</span><br>
        <span style="color:#a1a1aa">\u251c\u2500\u2500 De\u0148 1: SEO Audit + Technick\u00e9 opravy</span><br>
        <span style="color:#a1a1aa">\u251c\u2500\u2500 De\u0148 2: Competitive Research (5 konkurentov)</span><br>
        <span style="color:#a1a1aa">\u251c\u2500\u2500 De\u0148 3: Content Strategy + Keyword Plan</span><br>
        <span style="color:#a1a1aa">\u251c\u2500\u2500 De\u0148 4: LinkedIn Content (20 postov)</span><br>
        <span style="color:#a1a1aa">\u2514\u2500\u2500 De\u0148 5: Email Welcome Sekvencia</span><br><br>
        <span class="highlight-purple">T\u00dd\u017dDE\u0147 2: CONTENT ENGINE</span><br>
        <span style="color:#a1a1aa">\u251c\u2500\u2500 De\u0148 6\u20137: Blog Post 1 + 2</span><br>
        <span style="color:#a1a1aa">\u251c\u2500\u2500 De\u0148 8: Twitter Thread 1</span><br>
        <span style="color:#a1a1aa">\u251c\u2500\u2500 De\u0148 9: LinkedIn Post (z threadu)</span><br>
        <span style="color:#a1a1aa">\u2514\u2500\u2500 De\u0148 10: Email Nurture 1\u20132</span><br><br>
        <span class="highlight-green">T\u00dd\u017dDE\u0147 3: DISTRIBUTION</span><br>
        <span style="color:#a1a1aa">\u251c\u2500\u2500 De\u0148 11\u201312: Blog Post 3 + 4</span><br>
        <span style="color:#a1a1aa">\u251c\u2500\u2500 De\u0148 13: Twitter Thread 2</span><br>
        <span style="color:#a1a1aa">\u251c\u2500\u2500 De\u0148 14: LinkedIn Post</span><br>
        <span style="color:#a1a1aa">\u2514\u2500\u2500 De\u0148 15: Email Nurture 3\u20134</span><br><br>
        <span class="highlight">T\u00dd\u017dDE\u0147 4: AMPLIFICATION</span><br>
        <span style="color:#a1a1aa">\u251c\u2500\u2500 De\u0148 16\u201317: Programmatic SEO Pages</span><br>
        <span style="color:#a1a1aa">\u251c\u2500\u2500 De\u0148 18: Cross-platform Repurposing</span><br>
        <span style="color:#a1a1aa">\u251c\u2500\u2500 De\u0148 19: Community Engagement</span><br>
        <span style="color:#a1a1aa">\u2514\u2500\u2500 De\u0148 20: Email Nurture 5 + Pitch</span><br><br>
        <span class="highlight-red">T\u00dd\u017dDE\u0147 5: ANALYSIS</span><br>
        <span style="color:#a1a1aa">\u251c\u2500\u2500 De\u0148 21\u201325: Monitoring + Analytics</span><br>
        <span style="color:#a1a1aa">\u251c\u2500\u2500 De\u0148 26\u201328: A/B Test Variations</span><br>
        <span style="color:#a1a1aa">\u251c\u2500\u2500 De\u0148 29: Competitive Update</span><br>
        <span style="color:#a1a1aa">\u2514\u2500\u2500 De\u0148 30: Retro + Next Month Plan</span>
      </div>
    </div>
    <div class="scene-number">2 / 5</div>'''))

    m5_l6.append(scene(6000, '''    <div class="card-dark">
      <h2>\U0001f3bc Master Orchestrator Agent</h2>
      <p>Vytvor\u00ed\u0161 <span class="highlight-purple">jedn\u00e9ho agenta</span>, ktor\u00fd riadi cel\u00fa kampa\u0148.</p>
      <div style="margin-top:16px;font-size:22px;color:#a1a1aa;line-height:1.8">
        <span class="highlight-green">\u2713</span> Sp\u00fa\u0161\u0165a subagentov pod\u013ea harmonogramu<br>
        <span class="highlight-green">\u2713</span> Nez\u00e1visl\u00e9 \u00falohy = paralelne<br>
        <span class="highlight-green">\u2713</span> Z\u00e1visl\u00e9 \u00falohy = sekven\u010dne<br>
        <span class="highlight-green">\u2713</span> Zaznamen\u00e1va progress do <span class="highlight">campaign-log.md</span><br>
        <span class="highlight-green">\u2713</span> Posiela priebe\u017en\u00e9 statusy
      </div>
    </div>
    <div class="scene-number">3 / 5</div>'''))

    m5_l6.append(scene(5000, '''    <div class="card-dark">
      <h2>\U0001f4ca Campaign Tracker</h2>
      <div style="font-size:20px;color:#a1a1aa;line-height:1.8">
        <span class="highlight">Progress:</span> 12/25 \u00faloh (48%)<br><br>
        <span class="highlight-green">\u2705 Dokon\u010den\u00e9:</span> SEO Audit, Competitive Research, Content Strategy<br><br>
        <span class="highlight">\U0001f504 Prebiehaj\u00face:</span> Blog Post 1, LinkedIn Content<br><br>
        <span class="highlight-purple">\U0001f4c5 Nasleduj\u00face:</span> Blog Post 2, Twitter Thread 1
      </div>
      <p style="margin-top:12px;font-size:22px;color:#fbbf24">5 min\u00fat denne namiesto 8 hod\u00edn.</p>
    </div>
    <div class="scene-number">4 / 5</div>'''))

    m5_l6.append(scene(5000, '''    <div class="card-dark" style="text-align:center">
      <h2>\U0001f3af \u010co \u010falej po 30 d\u0148och?</h2>
      <p style="font-size:28px;margin:12px 0"><span class="highlight">1.</span> Analyzuj v\u00fdsledky \u2013 \u010do fungovalo?</p>
      <p style="font-size:28px;margin:12px 0"><span class="highlight-purple">2.</span> Iteruj \u2013 uprav strat\u00e9giu, vylep\u0161i SEO</p>
      <p style="font-size:28px;margin:12px 0"><span class="highlight-green">3.</span> \u0160k\u00e1luj \u2013 pridaj YouTube, podcast, webin\u00e1re</p>
      <p style="font-size:28px;margin:12px 0"><span class="highlight">4.</span> Automatizuj e\u0161te viac \u2013 marketing-loop!</p>
      <p style="margin-top:20px;font-size:32px;color:#fbbf24">U\u017e nie si len pou\u017e\u00edvate\u013e. Si <span class="highlight">riadite\u013e arm\u00e1dy agentov</span>.</p>
    </div>
    <div class="scene-number">5 / 5</div>'''))

    m5l6_html = make_html(5, "Automatiz\u00e1cia marketingu", 6, "30-d\u0148ov\u00e1 kampa\u0148 na autopilota", 6, m5_l6)

    # Write all files
    base = '/Users/abra/Developer/prime-agent-masterclass/video/output'
    files = {
        'module4/m4_l01_co-su-subagenti.html': m4l1_html,
        'module4/m4_l02_spustanie-riadenie-subagentov.html': m4l2_html,
        'module4/m4_l03_paralelne-spracovanie.html': m4l3_html,
        'module4/m4_l04_komunikacia-medzi-agentmi.html': m4l4_html,
        'module4/m4_l05_content-factory.html': m4l5_html,
        'module5/m5_l01_agent-linkedin-obsah.html': m5l1_html,
        'module5/m5_l02_agent-twitter-thready.html': m5l2_html,
        'module5/m5_l03_agent-email-kampane.html': m5l3_html,
        'module5/m5_l04_agent-seo-content-strategia.html': m5l4_html,
        'module5/m5_l05_agent-prieskum-konkurencie.html': m5l5_html,
        'module5/m5_l06_30-dnova-kampan-autopilot.html': m5l6_html,
    }

    for path, html in files.items():
        full = os.path.join(base, path)
        with open(full, 'w', encoding='utf-8') as f:
            f.write(html)
        size_kb = len(html) / 1024
        print(f"\u2705 {path} ({size_kb:.1f} KB)")

    print(f"\n\U0001f389 Hotovo! {len(files)} HTML s\u00faborov vytvoren\u00fdch.")

if __name__ == '__main__':
    build_all()
