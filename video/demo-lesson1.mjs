import { render } from "hyperframes";

const frames = [
  // Frame 1: Intro - Dark screen with text
  {
    html: `<!DOCTYPE html>
<html><head><style>
* { margin: 0; padding: 0; box-sizing: border-box; }
body { 
  background: #0a0a0f; 
  display: flex; 
  align-items: center; 
  justify-content: center; 
  height: 100vh;
  font-family: system-ui, -apple-system, sans-serif;
  color: white;
}
.container { text-align: center; }
.title { 
  font-size: 72px; 
  font-weight: 800; 
  background: linear-gradient(135deg, #7c5cfc, #a78bfa);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  margin-bottom: 20px;
}
.subtitle { font-size: 32px; color: #a1a1aa; }
</style></head>
<body>
<div class="container">
  <div class="title">Prime Agent</div>
  <div class="subtitle">AI ktorá nerozpráva — ona ROBÍ</div>
</div>
</body></html>`,
    duration: 4
  },

  // Frame 2: Problem
  {
    html: `<!DOCTYPE html>
<html><head><style>
* { margin: 0; padding: 0; box-sizing: border-box; }
body { 
  background: #0a0a0f; 
  display: flex; 
  align-items: center; 
  justify-content: center; 
  height: 100vh;
  font-family: system-ui, sans-serif;
}
.card {
  background: #1a1a2e;
  border: 1px solid #2a2a3e;
  border-radius: 16px;
  padding: 48px;
  max-width: 700px;
}
h2 { color: #ef4444; font-size: 42px; margin-bottom: 24px; }
p { color: #d4d4d8; font-size: 28px; line-height: 1.6; }
.highlight { color: #fbbf24; font-weight: 600; }
</style></head>
<body>
<div class="card">
  <h2>⚠️ Problém</h2>
  <p>Stráviš <span class="highlight">15+ hodín týždenne</span> úlohami, ktoré nevyžadujú tvoj mozog.</p>
  <p style="margin-top:16px; font-size:22px; color:#71717a;">E-maily · Research · Reporty · Dáta · Operatíva</p>
</div>
</body></html>`,
    duration: 5
  },

  // Frame 3: Solution - What agent does
  {
    html: `<!DOCTYPE html>
<html><head><style>
* { margin: 0; padding: 0; box-sizing: border-box; }
body { 
  background: #0a0a0f; 
  display: flex; 
  align-items: center; 
  justify-content: center; 
  height: 100vh;
  font-family: system-ui, sans-serif;
}
.grid { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; max-width: 800px; }
.box {
  background: #1a1a2e;
  border: 1px solid #2a2a3e;
  border-radius: 12px;
  padding: 24px;
  text-align: center;
}
.icon { font-size: 40px; margin-bottom: 8px; }
.label { color: #d4d4d8; font-size: 22px; }
</style></head>
<body>
<div class="grid">
  <div class="box"><div class="icon">📧</div><div class="label">Odpovedá na maily</div></div>
  <div class="box"><div class="icon">🔍</div><div class="label">Robí prieskum trhu</div></div>
  <div class="box"><div class="icon">📊</div><div class="label">Generuje reporty</div></div>
  <div class="box"><div class="icon">📝</div><div class="label">Píše obsah</div></div>
</div>
</body></html>`,
    duration: 5
  },

  // Frame 4: Terminal demo
  {
    html: `<!DOCTYPE html>
<html><head><style>
* { margin: 0; padding: 0; box-sizing: border-box; }
body { 
  background: #0a0a0f; 
  display: flex; 
  align-items: center; 
  justify-content: center; 
  height: 100vh;
  font-family: 'Menlo', 'Monaco', monospace;
}
.terminal {
  background: #0d1117;
  border: 1px solid #30363d;
  border-radius: 12px;
  padding: 32px;
  max-width: 750px;
  width: 100%;
}
.prompt { color: #7c5cfc; font-size: 22px; }
.cmd { color: #e6edf3; font-size: 22px; }
.output { color: #7ee787; font-size: 20px; margin-top: 12px; line-height: 1.5; }
.cursor { animation: blink 1s infinite; color: #7c5cfc; }
@keyframes blink { 50% { opacity: 0; } }
</style></head>
<body>
<div class="terminal">
  <div><span class="prompt">$</span> <span class="cmd">prime-agent "Vytvor marketingový plán pre môj SaaS"</span><span class="cursor">█</span></div>
  <div class="output" style="margin-top:24px;">
    ✅ Analyzujem produkt...<br>
    ✅ Skúmam konkurenciu...<br>
    ✅ Generujem 90-dňový plán...<br>
    ✅ Hotovo! 13 kapitol vygenerovaných.
  </div>
</div>
</body></html>`,
    duration: 6
  },

  // Frame 5: CTA
  {
    html: `<!DOCTYPE html>
<html><head><style>
* { margin: 0; padding: 0; box-sizing: border-box; }
body { 
  background: linear-gradient(135deg, #0a0a0f, #1a1030);
  display: flex; 
  align-items: center; 
  justify-content: center; 
  height: 100vh;
  font-family: system-ui, sans-serif;
  color: white;
  text-align: center;
}
.container { max-width: 700px; }
h2 { font-size: 56px; font-weight: 800; margin-bottom: 16px; }
p { font-size: 28px; color: #a1a1aa; margin-bottom: 32px; }
.btn {
  display: inline-block;
  background: #7c5cfc;
  color: white;
  padding: 18px 48px;
  border-radius: 12px;
  font-size: 28px;
  font-weight: 600;
  text-decoration: none;
}
</style></head>
<body>
<div class="container">
  <h2>🚀 Pripravený?</h2>
  <p>Nauč sa spúšťať AI agentov, ktoré pracujú za teba.</p>
  <div class="btn">Pripoj sa na Skool →</div>
</div>
</body></html>`,
    duration: 5
  }
];

console.log(`Generujem video: ${frames.length} frames, ~${frames.reduce((s,f) => s + f.duration, 0)}s`);

await render({
  frames,
  output: "/Users/abra/Developer/prime-agent-masterclass/video/output/module1-lesson1-demo.mp4",
  width: 1080,
  height: 1350,
  fps: 30
});

console.log("✅ Hotovo!");
