# Prime Agent Masterclass – Modul 1: Úvod a inštalácia

## Prehľad modulu

**Cieľ modulu:** Po absolvovaní tohto modulu budeš mať Prime Agent plne nainštalovaného, spusteného a pripraveného na prvý príkaz. Pochopíš, čo je AI agent, ako sa líši od chatbota, a prečo je Prime Agent momentálne najvýkonnejším open-source coding agentom na trhu.

**Celková dĺžka:** 65 minút videa + domáce úlohy

---

## Lekcia 1: Čo je Prime Agent a prečo teraz
**Dĺžka videa:** 10 minút

### Detailný obsah / scenár

#### 0:00–1:00 | Úvod a hook
- **Povedať:** „Predstav si, že máš vývojára, ktorý nikdy nespí, nikdy sa nesťažuje a rozumie celému tvojmu kódu. To je Prime Agent."
- Ukázať krátke demo: otvoriť terminál, napísať `prime-agent`, zadať jednoduchú úlohu (napr. „vytvor TODO app v Reacte") a nechať agenta vygenerovať kód – len 30-sekundový teaser bez vysvetľovania.

#### 1:00–3:30 | Čo je Prime Agent
- **Povedať:** Prime Agent je **RLM-native terminal coding agent** – AI, ktorá žije v tvojom termináli a programuje spolu s tebou.
- **Kľúčové charakteristiky:**
  - Beží v termináli (CLI + TUI rozhranie)
  - Má vlastný perzistentný **IPython kernel** – nie je to len „chat a copy-paste", agent reálne spúšťa kód
  - Je **open-source** (MIT licencia), vyvíjaný spoločnosťou **Prime Intellect** (open-superintelligence lab)
  - Aktuálna verzia: **0.7.x** (ukázať `prime-agent --version`)
  - Beží lokálne na tvojom stroji – tvoj kód, tvoja kontrola
- **Ukázať na obrazovke:**
  ```bash
  prime-agent --version
  # Prime Agent CLI v0.7.1
  ```

#### 3:30–6:00 | Prečo teraz?
- **Povedať:** Nachádzame sa v inflexnom bode. AI agenti prešli od „wow, to je cool demo" k „toto reálne používam každý deň."
- **Tri dôvody, prečo práve teraz:**
  1. **Modely dosiahli kritickú úroveň schopností** – Claude 4, DeepSeek, GPT-4o – modely už zvládajú komplexné úlohy s minimom chýb
  2. **Architektúra agentov dozrela** – Prime Agent používa RLM (Runtime-Language-Model) prístup, kde model nielen generuje kód, ale ho aj spúšťa, pozoruje výsledky a iteruje
  3. **Cena klesla 10-násobne** – pred rokom stál token $15/M, dnes $1.50/M (DeepSeek) – agenti sa stali dostupnými pre každého
- **Povedať:** „Ak nie si AI-native vývojár do konca roka 2025, budeš zaostávať. Toto je moment, keď sa to učíš."

#### 6:00–8:00 | Čo všetko Prime Agent dokáže
- **Prejsť rýchly prehľad schopností (ukázať, nie vysvetľovať):**
  - Číta a edituje súbory (skill: `edit`)
  - Vyhľadáva na webe (`websearch`)
  - Spúšťa shell príkazy a Python kód (IPython kernel)
  - Vytvára a spravuje vlastné skilly
  - Spúšťa pod-agentov pre paralelné úlohy
  - Kompaktuje kontext pre dlhé sessiony
  - Pracuje s obrázkami (`attach_image`)
  - Integruje sa s MCP (Model Context Protocol) servermi
  - Má zabudovaný TUI editor so syntax highlightingom
- **Vizuál:** Ukázať zoznam dostupných skillov cez `/skills`

#### 8:00–10:00 | Ekosystém Prime Intellect
- **Povedať:** Prime Agent je len špička ľadovca. Prime Intellect buduje celú open-source AGI infraštruktúru:
  - **Prime CLI** – GPU computing, inference, tréning modelov
  - **Environments Hub** – RL prostredia pre post-tréning
  - **Sandboxes** – bezpečné Docker prostredia pre AI-generovaný kód
  - **Inference API** – OpenAI-kompatibilné API pre frontier modely
- **Povedať:** „Prime Agent je tvoj vstup do tohto ekosystému. Dnes sa naučíš základy."

### Kľúčové body
- Prime Agent je open-source RLM-native CLI coding agent
- Beží lokálne, má perzistentný IPython kernel
- Modely, architektúra aj cena dozreli – toto je správny čas
- Je súčasťou širšieho ekosystému Prime Intellect

### Domáca úloha
1. Prečítaj si README Prime Agenta na GitHub-e ([github.com/PrimeIntellect-ai/prime-agent](https://github.com/PrimeIntellect-ai/prime-agent))
2. Pozri si aspoň 3 videá na YouTube s tagom „Prime Agent" alebo „AI coding agent" – napíš si 3 veci, ktoré ťa najviac prekvapili
3. Zamysli sa: Aký typ úloh by si chcel s Prime Agentom automatizovať? Napíš si zoznam aspoň 5 úloh

---

## Lekcia 2: Ako funguje AI agent vs chatbot
**Dĺžka videa:** 8 minút

### Detailný obsah / scenár

#### 0:00–1:30 | Chatbot – čo to je a limity
- **Povedať:** „Každý dnes pozná ChatGPT. Napíšeš otázku, dostaneš odpoveď. Ale to je len chatbot."
- **Ukázať na obrazovke:** Otvoriť ChatGPT/Claude web, zadať: „Napíš mi Python skript, ktorý vytiahne všetky nadpisy z webstránky."
  - Model vygeneruje kód
  - **Povedať:** „Super, mám kód. Ale teraz ho musím: skopírovať, vytvoriť súbor, spustiť, zistiť že nefunguje, vrátiť sa, opraviť, znova skopírovať..."
  - **Povedať:** „Toto je `generation gap` – priepasť medzi generovaním a exekúciou."

#### 1:30–3:30 | Ako chatbot reálne funguje
- **Ukázať jednoduchý diagram (nakresliť na obrazovku/slide):**
  ```
  [User Prompt] → [LLM] → [Text Response]
  ```
- **Povedať:** Chatbot je len LLM (Large Language Model). Vidí tvoju správu, vygeneruje odpoveď. Hotovo. Žiadna pamäť medzi requestami (okrem chatu), žiadne nástroje, žiadna akcia.
- **Ukázať limity na príklade:**
  - „Aké súbory mám v aktuálnom priečinku?" → Chatbot nevie, nevidí tvoj filesystém
  - „Refaktoruj tento súbor a otestuj ho" → Chatbot nevie spustiť kód

#### 3:30–6:00 | AI Agent – čo to je a ako funguje
- **Povedať:** „Agent = LLM + nástroje + slučka."
- **Ukázať rozšírený diagram:**
  ```
  [User Goal] → [LLM] → [Tool Call] → [Execute] → [Observe] → [LLM] → ... → [Done]
                    ↑                                                      |
                    └──────────────── spätná väzba ────────────────────────┘
  ```
- **Rozobrať každú časť:**
  - **LLM** – mozog, rozhoduje čo robiť
  - **Tools/Nástroje** – ruky agenta: `bash`, `ipython`, `edit`, `websearch`, `attach_image`...
  - **Execute** – agent reálne spustí príkaz a čaká na výsledok
  - **Observe** – agent prečíta výstup, chybovú hlášku, výsledok testu
  - **Iterate** – na základe pozorovania sa rozhodne pre ďalší krok (opraviť, vylepšiť, dokončiť)
- **Povedať:** „Toto je tá zásadná odlišnosť. Agent nevygeneruje odpoveď a nezmizne. Agent **koná**, **pozoruje** a **iteruje**, kým úlohu nedokončí."

#### 6:00–7:30 | Konkrétny príklad: agent vs chatbot
- **Ukázať na obrazovke rovnakú úlohu pre oba prístupy:**
  - Úloha: „Zisti, ktorý z mojich 50 JS súborov nemá TypeScript typy, a pridaj ich."
  - **Chatbot prístup:** Vygeneruje generický skript, ty ho musíš spustiť, ladiť, opravovať... 30+ minút manuálnej práce
  - **Agent prístup:** Prime Agent sám: `ls`, prečíta súbory, identifikuje chýbajúce typy, edituje ich, spustí kontrolu, opraví chyby... hotovo za 2 minúty

#### 7:30–8:00 | Prečo Prime Agent používa RLM architektúru
- **Povedať:** „Prime Agent je postavený na RLM architektúre – Runtime-Language-Model. Model komunikuje priamo s runtimeom (IPython kernel), nie cez textové rozhranie. To znamená:
  - Perzistentné premenné, importy, helper funkcie naprieč krokmi
  - Agent si pamätá kontext celej session
  - Môže spúšťať Python a shell v jednom prostredí"
- **Povedať:** „V ďalších moduloch pôjdeme hlbšie, ale kľúčové je toto: agent nie je glorifikovaný autocomplete. Je to kolega, ktorý reálne pracuje."

### Kľúčové body
- Chatbot generuje text, agent **koná** v reálnom prostredí
- Agent = LLM + nástroje + slučka (vykonaj-pozoruj-iteruj)
- RLM architektúra = model, ktorý má priamy prístup k runtime-u
- Prime Agent má perzistentný IPython kernel – premenné a stav prežívajú naprieč krokmi

### Domáca úloha
1. Nájdi si na internete článok „What are AI agents?" (napr. od Anthropic, OpenAI alebo LangChain) a prečítaj si ho
2. Otvor si akéhokoľvek chatbota (ChatGPT, Claude) a skús mu zadať úlohu: „Vytvor súbor hello.py a spusti ho." Všimni si, čo sa stane (resp. nestane). Napíš si postreh – prečo to nefunguje
3. Nakresli si vlastný diagram agenta podľa vzoru z lekcie a doplň doňho aspoň 5 konkrétnych nástrojov, ktoré si myslíš, že by si pri vývoji potreboval

---

## Lekcia 3: Inštalácia krok za krokom – Node.js, npm, prime-agent
**Dĺžka videa:** 15 minút

### Detailný obsah / scenár

#### 0:00–1:00 | Úvod k inštalácii
- **Povedať:** „V tejto lekcii prejdeme kompletnou inštaláciou Prime Agenta od nuly. Budeme potrebovať Node.js, npm a potom samotný Prime Agent. Ukážem inštaláciu na macOS, Linux aj Windows."
- **Ukázať slide s prehľadom:**
  1. Node.js ≥ 22.8.0
  2. Python 3.10+ (pre IPython kernel)
  3. Prime Agent (curl skript alebo npm)
  4. Overenie inštalácie

#### 1:00–4:30 | Node.js inštalácia (macOS / Linux / Windows)

**macOS:**
- **Povedať:** „Na macOS odporúčam použiť Homebrew alebo nvm (Node Version Manager)."
- **Ukázať v termináli:**
  ```bash
  # Skontrolovať, či už máme Node.js
  node --version

  # Ak nie, cez Homebrew:
  brew install node

  # Alebo cez nvm (odporúčané – lepšia správa verzií):
  curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.1/install.sh | bash
  nvm install 22
  nvm use 22
  node --version  # malo by ukázať v22.x.x
  ```
- **Poznámka:** Ukázať, ako overiť, že verzia je ≥ 22.8.0

**Linux (Ubuntu/Debian):**
- **Povedať:** „Na Linuxe použijeme NodeSource repozitár."
- **Ukázať v termináli:**
  ```bash
  curl -fsSL https://deb.nodesource.com/setup_22.x | sudo -E bash -
  sudo apt-get install -y nodejs
  node --version
  ```

**Windows:**
- **Povedať:** „Na Windowse stiahni inštalátor z nodejs.org – verziu 22 LTS."
- **Ukázať screenshoty z inštalácie** (alebo rýchly screen recording):
  - Ísť na https://nodejs.org
  - Stiahnuť Windows Installer (.msi) pre v22 LTS
  - Prejsť inštaláciou (Next → Next → Finish)
  - Otvoriť PowerShell/Terminál a overiť: `node --version`

#### 4:30–6:00 | Python kontrola
- **Povedať:** „Prime Agent používa IPython kernel, takže potrebuje Python 3.10+."
- **Ukázať:**
  ```bash
  python3 --version  # mal by byť ≥ 3.10
  ```
- **Ak chýba:**
  - macOS: `brew install python@3.12`
  - Linux: `sudo apt install python3 python3-pip`
  - Windows: stiahnuť z python.org
- **Povedať:** „Prime Agent si IPython kernel nastaví automaticky pri prvom spustení. Ak chceš použiť existujúce Python prostredie, nastav `PRIME_AGENT_KERNEL_PYTHON`."

#### 6:00–11:00 | Inštalácia Prime Agenta

**Metóda 1: curl skript (odporúčaná, najjednoduchšia)**
- **Povedať:** „Najjednoduchší spôsob je oficiálny inštalačný skript."
- **Ukázať v termináli:**
  ```bash
  # Stabilná verzia:
  curl -fsSL https://app.primeintellect.ai/prime-agent/install.sh | sh

  # Alebo beta verzia (najnovšie featur-y):
  curl -fsSL https://app.primeintellect.ai/prime-agent/install.sh | sh -s -- beta
  ```
- **Čo skript robí:**
  - Stiahne najnovší release
  - Nainštaluje ho globálne cez npm
  - Pridá `prime-agent` do PATH
- **Povedať:** „Po dokončení skontrolujeme:"
  ```bash
  prime-agent --version
  # Prime Agent CLI v0.7.1
  ```

**Metóda 2: npm (pre pokročilejších)**
- **Povedať:** „Ak preferuješ npm, môžeš nainštalovať priamo."
- **Ukázať:**
  ```bash
  npm install -g prime-agent
  prime-agent --version
  ```

**Metóda 3: Zo zdrojákov (pre contributorov)**
- **Povedať:** „Ak chceš prispievať do vývoja:"
  ```bash
  git clone https://github.com/PrimeIntellect-ai/prime-agent.git
  cd prime-agent
  npm install
  npm link
  ```

#### 11:00–13:30 | Post-install: prvé overenie
- **Ukázať v termináli:**
  ```bash
  # Verzia
  prime-agent --version

  # Help
  prime-agent --help

  # Zobrazenie dostupných providerov
  prime-agent --help  # ukázať --provider a --model flagy
  ```
- **Povedať:** „Ešte nespúšťaj – najprv musíme nastaviť API kľúč. To spravíme v Lekcii 5."
- **Ukázať štruktúru konfiguračného adresára:**
  ```bash
  ls ~/.prime/agent/
  # config.yaml (po prvom spustení)
  # skills/ (vlastné skilly)
  # sessions/ (história sessionov)
  ```

#### 13:30–15:00 | Riešenie bežných problémov
- **Povedať:** „Rýchly troubleshooting, ak niečo nefunguje:"
- **Problém 1:** `prime-agent: command not found`
  - Riešenie: Reštartovať terminál, skontrolovať PATH (`echo $PATH`), prípadne `npm config get prefix`
- **Problém 2:** `node: command not found` / nesprávna verzia
  - Riešenie: Preinštalovať Node.js ≥ 22.8.0 cez vyššie uvedené postupy
- **Problém 3:** Python kernel sa nenainštaluje
  - Riešenie: `pip3 install ipykernel` alebo nastaviť `PRIME_AGENT_KERNEL_PYTHON`
- **Problém 4:** Permission errors na Linux/Mac
  - Riešenie: Skontrolovať npm prefix alebo použiť nvm
- **Záver:** „Ak máš iný problém, napíš na [GitHub Issues](https://github.com/PrimeIntellect-ai/prime-agent/issues)."

### Kľúčové body
- Node.js ≥ 22.8.0, Python ≥ 3.10
- Inštalácia: `curl -fsSL https://app.primeintellect.ai/prime-agent/install.sh | sh`
- Overenie: `prime-agent --version`
- Konfiguračný adresár: `~/.prime/agent/`
- Bežné problémy a ich riešenia

### Domáca úloha
1. Nainštaluj Prime Agent podľa návodu (ak ešte nie je) – pošli screenshot úspešného `prime-agent --version` do diskusie
2. Preskúmaj výstup `prime-agent --help` a napíš si aspoň 5 zaujímavých prepínačov, ktoré si našiel
3. Pozri si štruktúru `~/.prime/agent/` a napíš, čo všetko sa tam nachádza (aj keď je zatiaľ prázdna)
4. Ak používaš Windows, prečítaj si [docs/windows.md](https://github.com/PrimeIntellect-ai/prime-agent/blob/main/docs/windows.md) v repozitári

---

## Lekcia 4: Prvé spustenie a orientácia v rozhraní
**Dĺžka videa:** 12 minút

### Detailný obsah / scenár

#### 0:00–0:45 | Úvod
- **Povedať:** „V tejto lekcii prvýkrát spustíme Prime Agenta a prejdeme si celé rozhranie. Toto je tvoja nová domovská obrazovka ako vývojára."
- **Predpoklad:** Mať nastavený API kľúč (napr. `export ANTHROPIC_API_KEY=...` alebo `export DEEPSEEK_API_KEY=...` – detaily v Lekcii 5)

#### 0:45–2:30 | Prvé spustenie
- **Ukázať v termináli:**
  ```bash
  # Spustenie s Anthropic Claude (ak máš kľúč)
  prime-agent

  # Alebo s DeepSeek
  prime-agent --provider deepseek --model deepseek-v4-flash

  # Alebo interaktívny výber
  prime-agent
  # Prime Agent sa spustí, ak nemá API kľúč, ponúkne /login
  ```
- **Povedať:** „Po spustení sa objaví TUI – Terminal User Interface. Toto nie je obyčajný terminál, je to plnohodnotné vývojové prostredie."

#### 2:30–6:00 | Prehliadka TUI rozhrania
- **Ukázať na obrazovke s popismi (screen share):**

**Horná lišta:**
  - Názov sessionu (automaticky generovaný)
  - Provider a model (napr. `deepseek/deepseek-v4-flash`)
  - Indikátor kontextu (token usage – napr. `12.3K / 200K`)

**Hlavná oblasť (chat/log):**
  - Konverzácia s agentom
  - Výstupy z nástrojov (bash, python)
  - Zobrazenie diffs pri editovaní súborov
  - Systémové správy

**Dolná lišta / stavový riadok:**
  - Working directory
  - Aktuálny stav (Thinking..., Running bash..., Idle)
  - Klávesové skratky

**Input area:**
  - Textový vstup pre správy/príkazy
  - Podpora multiline (Shift+Enter alebo editor)

#### 6:00–8:30 | Slash commands (/) – základné ovládanie
- **Povedať:** „Prime Agent sa ovláda nielen písaním správ, ale aj slash príkazmi."
- **Ukázať každý dôležitý príkaz:**

| Príkaz | Čo robí | Kedy použiť |
|--------|---------|-------------|
| `/help` | Zobrazí pomocníka | Keď si nevieš rady |
| `/clear` | Vyčistí konverzáciu | Nový začiatok v rámci sessionu |
| `/compact` | Skomprimuje kontext | Dlhá session, málo tokenov |
| `/undo` | Vráti poslednú akciu | Agent spravil chybu |
| `/login` | Nastavenie providera a API kľúča | Prvé spustenie, zmena modelu |
| `/skills` | Zobrazí dostupné skilly | Objavenie schopností |
| `/model` | Zmení model počas sessionu | Rýchle prepnutie modelu |
| `/editor` | Otvorí externý editor | Dlhšia správa/príkaz |

- **Povedať:** „Zapamätaj si hlavne `/login`, `/skills`, `/compact`, `/help` – toto sú tvoje každodenné príkazy."

#### 8:30–10:00 | Klávesové skratky
- **Ukázať na obrazovke a nechať účastníkov vyskúšať:**
  - `Ctrl+C` – preruší aktuálnu akciu agenta
  - `Ctrl+E` – otvorí editor pre písanie dlhšej správy
  - `Ctrl+L` – vyčistí obrazovku (ekvivalent `/clear`)
  - `Shift+Enter` – nový riadok v inpute
  - `Ctrl+V` – prilepenie z clipboardu

#### 10:00–11:30 | Session manažment
- **Povedať:** „Každé spustenie Prime Agenta je jedna **session**. Sessiony sa ukladajú a môžeš sa k nim vrátiť."
- **Ukázať:**
  ```bash
  # List sessions
  ls ~/.prime/agent/sessions/

  # Pokračovať v existujúcej session
  prime-agent --session <session-id>

  # Vytvoriť branch z existujúcej session
  prime-agent --branch <session-id>
  ```
- **Povedať:** „Branching je superužitočný – môžeš sa vrátiť k bodu, kde agent spravil zlé rozhodnutie, a ísť inou cestou."

#### 11:30–12:00 | Tipy na záver
- **Povedať:** „Tri tipy na efektívny štart:
  1. Vždy píš agentovi **konkrétne ciele**, nie vágne otázky
  2. Keď agent pracuje, **nechaj ho dokončiť myšlienku** – často sa opraví sám
  3. Používaj `Ctrl+C` len keď si istý, že agent zacyklil (stáva sa zriedka)"

### Kľúčové body
- Prime Agent je TUI (Terminal User Interface), nie obyčajný CLI
- Slash commands: `/help`, `/login`, `/skills`, `/compact`, `/clear`, `/undo`
- Klávesové skratky: `Ctrl+C` (prerušenie), `Ctrl+E` (editor)
- Sessiony sa ukladajú a dajú sa branchovať
- Píš konkrétne ciele, nechaj agenta iterovať

### Domáca úloha
1. Spusti Prime Agent a preskúmaj rozhranie – pošli screenshot do diskusie
2. Vyskúšaj všetky slash commands z tabuľky vyššie (`/help`, `/skills`, `/model`, `/editor`)
3. Spusti agenta, napíš „Ahoj, čo dokážeš?" a pozri si odpoveď – všimni si, ako agent odpovedá a aké nástroje spomína
4. Nájdi v `~/.prime/agent/sessions/` svoju session – pozri sa na súbor `state.json` (len si ho pozri, needituj!)

---

## Lekcia 5: Nastavenie modelu a API kľúča
**Dĺžka videa:** 10 minút

### Detailný obsah / scenár

#### 0:00–1:00 | Prečo záleží na výbere modelu
- **Povedať:** „Toto je jedna z najdôležitejších lekcií. Model, ktorý si vyberieš, zásadne ovplyvní kvalitu výstupov, rýchlosť a cenu."
- **Ukázať slide s porovnaním modelov:**

| Model | Provider | Kvalita kódu | Rýchlosť | Cena (1M input/output tokenov) |
|-------|----------|-------------|----------|-------------------------------|
| Claude Sonnet 4 | Anthropic | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ~$3/$15 |
| Claude Opus 4 | Anthropic | ⭐⭐⭐⭐⭐ | ⭐⭐ | ~$15/$75 |
| GPT-4o | OpenAI | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ~$2.50/$10 |
| DeepSeek V4 Flash | DeepSeek | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ~$0.50/$2 |
| DeepSeek V4 | DeepSeek | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ~$1.50/$6 |
| Gemini 2.5 Pro | Google | ⭐⭐⭐⭐ | ⭐⭐⭐ | ~$1.25/$5 |

- **Povedať:** „Moja osobná voľba: **DeepSeek V4 Flash** na každodennú prácu (najlepší pomer cena/výkon/rýchlosť), **Claude Sonnet 4** na kritické úlohy."

#### 1:00–3:30 | Získanie API kľúčov – krok za krokom

**Anthropic (Claude):**
- **Povedať:** „Anthropic ponúka Claude modely – momentálne najlepšie na komplexné programovanie."
- **Ukázať na obrazovke:**
  1. Ísť na https://console.anthropic.com
  2. Zaregistrovať sa / prihlásiť
  3. Ísť do „API Keys" v menu
  4. Kliknúť „Create Key" → pomenovať „prime-agent"
  5. **Skopírovať kľúč** (zobrazí sa len raz!)
  6. Nastaviť environment variable:
     ```bash
     export ANTHROPIC_API_KEY=sk-ant-...
     ```

**DeepSeek:**
- **Povedať:** „DeepSeek je momentálne najlepší pomer cena/výkon. Odporúčam si ho aktivovať."
- **Ukázať na obrazovke:**
  1. Ísť na https://platform.deepseek.com
  2. Zaregistrovať sa / prihlásiť
  3. Ísť do „API Keys"
  4. Vytvoriť nový kľúč, skopírovať
  5. ```bash
     export DEEPSEEK_API_KEY=sk-...
     ```

**OpenAI (GPT-4o):**
- **Povedať:** „Klasika. Ak už máš OpenAI účet, stačí API kľúč."
- **Ukázať na obrazovke:**
  1. Ísť na https://platform.openai.com/api-keys
  2. Vytvoriť nový kľúč
  3. ```bash
     export OPENAI_API_KEY=sk-...
     ```

- **Tip:** „API kľúče nikdy necommituj do gitu! Pridaj si ich do `~/.bashrc`, `~/.zshrc` alebo použi `.env` súbor."

#### 3:30–6:00 | `/login` – interaktívne nastavenie
- **Povedať:** „Najjednoduchší spôsob, ako nastaviť providera, je priamo v Prime Agentovi cez `/login`."
- **Ukázať krok za krokom:**
  1. Spustiť `prime-agent`
  2. Napísať `/login`
  3. Vybrať poskytovateľa (Anthropic, DeepSeek, OpenAI, Google, ...)
  4. Zadať API kľúč
  5. Hotovo – Prime Agent si kľúč bezpečne uloží
- **Povedať:** „Prime Agent ukladá kľúče šifrovane v `~/.prime/agent/`. Nemusíš ich mať v environment variables, ak použiješ `/login`."

#### 6:00–7:30 | CLI prepínače pre model
- **Povedať:** „Model vieš zmeniť aj pri spustení, bez `/login`:"
- **Ukázať:**
  ```bash
  # Štandardný model (podľa /login)
  prime-agent

  # Iný provider
  prime-agent --provider deepseek --model deepseek-v4-flash

  # S thinking mode (pre zložité úlohy)
  prime-agent --provider deepseek --model deepseek-v4 --thinking high

  # Lokálny model cez Ollama
  prime-agent --provider ollama --model llama3.3:70b
  ```
- **Povedať:** „Prepnúť model môžeš aj počas sessionu cez `/model`."

#### 7:30–8:30 | Thinking mode
- **Povedať:** „Dôležitý koncept: **thinking mode**. Niektoré modely (Claude, DeepSeek V4) podporujú rozšírené myslenie – model si vnútorne premyslí problém, kým odpovie."
- **Úrovne:**
  - `off` – bez thinkingu (najrýchlejšie)
  - `low` – minimálny thinking
  - `medium` – vyvážený (odporúčaný default)
  - `high` – maximálny thinking (najlepšie výsledky pri zložitých úlohách, pomalšie)
- **Povedať:** „Na jednoduché úlohy `off` alebo `low`. Na refaktoring, architektúru, zložité bugy – `medium` alebo `high`."

#### 8:30–9:30 | Uloženie default modelu
- **Povedať:** „Ak stále používaš ten istý model, ulož si ho ako default:"
- **Ukázať:**
  ```bash
  # Cez environment variable
  export PRIME_AGENT_PROVIDER=deepseek
  export PRIME_AGENT_MODEL=deepseek-v4-flash

  # Alebo cez /login raz nastav a Prime Agent si to zapamätá
  ```
- **Povedať:** „V kontinuálnom harness-i si môžeš uložiť aj preferovanú konfiguráciu – k tomu sa dostaneme v Module 3."

#### 9:30–10:00 | Bezpečnosť API kľúčov
- **Povedať:** „Rýchla bezpečnostná vsuvka:"
  - API kľúče = tvoje peniaze. Každé volanie modelu niečo stojí
  - Nikdy nezdieľaj kľúče, necommituj ich
  - Nastav si **usage limits** v konzole každého providera (Anthropic/OpenAI/DeepSeek)
  - Pre tímové použitie: každý člen má vlastný kľúč
  - Pri úniku kľúča: okamžite ho zruš (revoke) v konzole providera

### Kľúčové body
- DeepSeek V4 Flash = najlepší pomer cena/výkon na denné použitie
- Claude Sonnet 4 = najlepší na kritické komplexné úlohy
- `/login` = najjednoduchšie nastavenie API kľúča
- Thinking mode: `off/low/medium/high` – čím vyšší, tým lepšie výsledky ale pomalšie
- API kľúče chráň ako heslá – nastav limity, nenechávaj v gite

### Domáca úloha
1. Založ si účet aspoň u 2 providerov (odporúčam DeepSeek + Anthropic) a nastav API kľúče
2. Vyskúšaj `/login` v Prime Agentovi a prepni medzi modelmi
3. Spusti tú istú úlohu s `--thinking off` a potom s `--thinking medium` – porovnaj výsledky. Napíš, aký rozdiel si spozoroval
4. Nastav si usage limit v konzole providera (napr. $10/mesiac) – pošli screenshot

---

## Lekcia 6: Bonus – Tvoj prvý command: spusti agenta
**Dĺžka videa:** 10 minút

### Detailný obsah / scenár

#### 0:00–1:00 | Úvod – čas na akciu
- **Povedať:** „Dosť bolo teórie. V tejto bonusovej lekcii spustíš svojho prvého agenta a dáš mu reálnu úlohu. Toto je moment, kvôli ktorému si tu."
- **Povedať:** „Prejdeme si 3 praktické cvičenia od najjednoduchšieho po komplexnejšie."

#### 1:00–3:30 | Cvičenie 1: „Hello, Agent!" – prvý kontakt
- **Povedať:** „Začneme najjednoduchšou možnou úlohou – necháme agenta vytvoriť Python skript."
- **Ukázať na obrazovke (live demo):**
  ```bash
  prime-agent
  ```
- **Zadať agentovi:**
  ```
  Vytvor súbor hello.py, ktorý vypíše "Ahoj, Prime Agent!" a spusti ho.
  ```
- **Čo sa stane (komentovať počas behu):**
  1. Agent si premyslí úlohu (thinking)
  2. Spustí `ipython` tool
  3. V ňom vytvorí súbor (napr. cez `%%bash` cell: `echo 'print("Ahoj, Prime Agent!")' > hello.py`)
  4. Spustí ho: `python hello.py`
  5. Zobrazí výstup: `Ahoj, Prime Agent!`
  6. Oznámi splnenie úlohy
- **Povedať:** „Videl si celý cyklus: **myslenie → akcia → pozorovanie → odpoveď**. Presne takto agent pracuje pri každej úlohe."

#### 3:30–6:00 | Cvičenie 2: Práca so súbormi – reálna úloha
- **Povedať:** „Teraz niečo užitočnejšie. Dajme agentovi úlohu, ktorá sa podobá na reálnu prácu."
- **Pripraviť pôdu (ukázať):**
  ```bash
  mkdir ~/prime-agent-demo
  cd ~/prime-agent-demo
  # Vytvoríme pár súborov, s ktorými bude agent pracovať
  echo "name=John" > config.txt
  echo "debug=true" >> config.txt
  echo "port=3000" >> config.txt
  ```
- **Spustiť agenta:**
  ```bash
  prime-agent
  ```
- **Zadať agentovi:**
  ```
  V aktuálnom priečinku je config.txt. Načítaj ho, skonvertuj ho do JSON formátu 
  a ulož ako config.json. Potom ho pekne vypíš (pretty print).
  ```
- **Čo sa stane (komentovať počas behu):**
  1. Agent prečíta súbor cez `cat config.txt` alebo Python
  2. Napíše Python kód na parsovanie a konverziu
  3. Vytvorí `config.json` s obsahom:
     ```json
     {
       "name": "John",
       "debug": "true",
       "port": "3000"
     }
     ```
  4. Vypíše ho s pretty print
- **Povedať:** „Všimni si: agent sám zistil, že súbor používa formát `key=value`, napísal parser, vytvoril JSON. Nemusel si mu hovoriť ako – pochopil zadanie a vykonal ho."

#### 6:00–8:30 | Cvičenie 3: Web scraping + analýza
- **Povedať:** „Posledné cvičenie – ukážeme si, ako agent kombinuje viacero nástrojov naraz."
- **Zadať agentovi:**
  ```
  Vyhľadaj na webe "Prime Agent latest features 2025", nájdi 3 relevantné články, 
  a vytvor súbor research.md s ich názvami, URL a krátkym zhrnutím v slovenčine.
  ```
- **Čo sa stane (komentovať počas behu):**
  1. Agent použije `websearch` skill: `await websearch("Prime Agent latest features 2025")`
  2. Dostane výsledky (názvy, URL, snippety)
  3. Pre každý výsledok spraví krátke zhrnutie (použije LLM)
  4. Vytvorí `research.md` s pekným formátovaním v Markdown-e
  5. Uloží súbor
- **Povedať:** „Toto je ukážka **multi-tool workflow**: websearch → analýza → formátovanie → zápis. Agent sám rozhodol, ktoré nástroje použiť a v akom poradí."

#### 8:30–9:30 | Ako komunikovať s agentom efektívne
- **Povedať:** „Pár tipov, ktoré ti ušetria hodiny frustrácie:"
- **Zlaté pravidlá zadávania úloh:**
  1. **Buď konkrétny.** Nie „sprav niečo s dátami", ale „načítaj data.csv, vyčisti duplicitné riadky, zoraď podľa dátumu a ulož ako data_clean.csv"
  2. **Definuj výstup.** Povedz agentovi, čo má byť výsledkom – súbor, zmena v kóde, analýza
  3. **Nechaj ho premýšľať.** Neinštruuj ho krok po kroku – daj mu cieľ a nechaj ho nájsť cestu
  4. **Dávaj spätnú väzbu.** Ak výsledok nie je ideálny, povedz: „Super, ale ešte pridaj..." – agent bude iterovať
  5. **Používaj `/compact`.** Pri dlhších sessionoch kompaktuj kontext, aby agent nestratil prehľad
- **Povedať:** „Tieto pravidlá budeme rozvíjať v Module 2 – Prompt Engineering pre agentov."

#### 9:30–10:00 | Zhrnutie modulu a čo ďalej
- **Povedať:** „Gratulujem! Práve si dokončil Modul 1. Čo si sa naučil:"
  - ✅ Čo je Prime Agent a prečo je dôležitý práve teraz
  - ✅ Rozdiel medzi chatbotom a AI agentom
  - ✅ Kompletná inštalácia na akomkoľvek OS
  - ✅ Orientácia v TUI rozhraní a ovládanie
  - ✅ Nastavenie modelov a API kľúčov
  - ✅ Prvé reálne úlohy s agentom
- **Povedať:** „V Module 2 sa ponoríme do **Prompt Engineeringu** – naučíš sa, ako z agenta dostať maximum. Ale najprv: sprav domáce úlohy! Bez praxe to nejde."

### Kľúčové body
- Agent používa cyklus: myslenie → akcia → pozorovanie → odpoveď
- Zadávaj konkrétne ciele, nie kroky
- Agent kombinuje nástroje automaticky podľa potreby
- Používaj `/compact` na šetrenie kontextu
- Spätná väzba je kľúčová – agent sa zlepšuje iteráciou

### Domáca úloha
1. **Povinné:** Spusti agenta a nechaj ho vytvoriť jednoduchú webovú aplikáciu podľa tvojho výberu (napr. kalkulačka, TODO list, weather app). Pošli zdrojový kód a screenshot výsledku
2. Nechaj agenta vyhľadať na webe 5 tipov pre začínajúcich vývojárov AI a nechaj ho ich zhrnúť do slovenčiny do súboru `ai-tipy.md`
3. Experimentuj: Daj agentovi **zle** zadanú úlohu (napr. „oprav chybu" bez kontextu). Všimni si, čo sa stane. Potom mu daj **dobre** zadanú úlohu. Napíš krátku reflexiu (100 slov) o rozdiele
4. Splň všetky domáce úlohy z predchádzajúcich lekcií, ak si ešte neurobil

---

## Kontrolný zoznam Modulu 1

Odškrtni si po splnení:

- [ ] Lekcia 1: Chápem, čo je Prime Agent a prečo ho používať
- [ ] Lekcia 2: Viem vysvetliť rozdiel medzi chatbotom a AI agentom
- [ ] Lekcia 3: Mám Prime Agent nainštalovaný a spustený (`prime-agent --version` funguje)
- [ ] Lekcia 4: Ovládam TUI rozhranie, viem použiť `/help`, `/login`, `/skills`, `/compact`
- [ ] Lekcia 5: Mám nastavený aspoň 1 API kľúč a viem prepínať medzi modelmi
- [ ] Lekcia 6: Splnil som praktické cvičenia – agent mi reálne vykonal úlohy
- [ ] Všetky domáce úlohy odovzdané / splnené

---

*Prime Agent Masterclass © 2025 – Modul 1/6*
