# Prime Agent Masterclass – Modul 7: Pokročilé techniky

## Prehľad modulu

**Cieľ modulu:** Po absolvovaní tohto modulu budeš ovládať pokročilé techniky Prime Agenta – integráciu externých služieb cez MCP, správu pamäte a skillov cez Continual Harness, plánovanie automatických úloh, prácu s API a webhookmi, a nonstop bežiacich agentov cez Heartbeats. Toto je modul, ktorý ťa posunie od "používateľa" k "architektovi" AI agentov.

**Celková dĺžka:** 60 minút videa + domáce úlohy

---

## Lekcia 1: MCP Connections – integrácia externých služieb
**Dĺžka videa:** 15 minút

### Detailný obsah / scenár

#### 0:00–1:30 | Úvod a hook
- **Povedať:** "Predstav si, že tvoj agent môže čítať tvoje emaily, spravovať kalendár, posielať správy do Slacku, sťahovať dáta z Google Analytics, vyhľadávať na webe a ešte k tomu komunikovať s tvojím CRM. A to všetko cez jeden štandard. To je MCP – Model Context Protocol."
- **Ukázať rýchle demo:** Agent cez MCP načíta neprečítané emaily, nájde v nich úlohy, vytvorí z nich Google Tasks a pošle sumár do Slacku.

#### 1:30–4:00 | Čo je MCP a prečo je to game-changer
- **Povedať:** "MCP je open-source štandard od Anthropic-u. Je to ako USB-C pre AI agentov – jeden konektor, cez ktorý agent komunikuje s akoukoľvek službou."
- **Vysvetliť architektúru MCP:**
  ```
  [Prime Agent] ←→ [MCP Client] ←→ [MCP Server] ←→ [Externá služba]
                                          ↑
                                   (Gmail, Slack, 
                                    Notion, GitHub,
                                    databáza, CRM...)
  ```
- **Tri kľúčové koncepty MCP:**
  1. **Resources** – dáta, ktoré agent číta (emaily, súbory, záznamy v databáze)
  2. **Tools** – akcie, ktoré agent vykonáva (pošli email, vytvor task, uprav súbor)
  3. **Prompts** – šablóny pre interakciu so službou
- **Povedať:** "Prime Agent má MCP zabudovaný priamo v jadre. Žiadne pluginy, žiadne zložité nastavovanie."

#### 4:00–7:00 | Konfigurácia MCP Connections cez /login
- **Povedať:** "MCP Connections sa nastavujú cez príkaz `/login`. Ukážme si to."
- **Krok za krokom na obrazovke:**
  ```bash
  # V Prime Agent napíš:
  /login
  ```
- **Ukázať, čo sa zobrazí:**
  - Výber LLM providera (DeepSeek, Anthropic, OpenAI, Google Gemini)
  - Zadanie API kľúča
  - **Sekcia MCP Connections** – zoznam dostupných integrácií
- **Prejsť dostupné MCP Connection typy:**
  - **Serper** (web search) – už predkonfigurovaný v Prime Agent
  - **Google Workspace** (Gmail, Drive, Calendar, Sheets, Docs, Chat)
  - **Slack**
  - **GitHub**
  - **Notion**
  - **Databázy** (PostgreSQL, MySQL cez MCP server)
  - **Vlastné MCP servery**
- **Ukázať konfiguráciu Google Workspace:**
  ```
  V /login → MCP Connections → Add Connection → Google Workspace
  → Autentifikácia cez OAuth 2.0
  → Výber scope-ov (Gmail read/send, Calendar, Drive...)
  → Hotovo! Agent teraz vidí tvoj Google účet.
  ```
- **Povedať:** "Po nastavení MCP Connection sa všetky GWS skilly (gws-gmail, gws-calendar, gws-sheets...) automaticky aktivujú."

#### 7:00–9:30 | Praktické príklady MCP integrácií

**Príklad 1: Gmail + Google Tasks**
  ```
  "Skontroluj moje neprečítané emaily. Pre každý email, 
  ktorý obsahuje úlohu, vytvor Google Task s deadlinom."
  ```
  - Agent cez MCP/GWS Gmail načíta emaily
  - Analyzuje, ktoré obsahujú akčné položky
  - Cez MCP/GWS Tasks vytvorí úlohy

**Príklad 2: Google Sheets reporting**
  ```
  "Vytiahni z Google Analytics návštevnosť za posledný týždeň, 
  spoj to s konverznými dátami zo Stripe a zapíš to do 
  Google Sheets – tabuľka 'Weekly Report'."
  ```

**Príklad 3: Slack notifikácie**
  ```
  "Keď agent dokončí prieskum konkurencie, pošli sumár 
  do Slack kanála #marketing."
  ```

- **Povedať:** "MCP Connections premosťujú priepasť medzi agentom a tvojím existujúcim stackom. Žiadne exporty, importy, copy-paste."

#### 9:30–12:00 | Vytváranie vlastných MCP serverov
- **Povedať:** "A čo keď tvoja služba nemá hotový MCP server? Napíšeš si vlastný."
- **Ukázať minimálny MCP server v Pythone:**
  ```python
  # my_mcp_server.py
  from mcp.server import Server, Tool

  server = Server("my-crm")

  @server.tool("get_deals")
  async def get_deals(stage: str = "all"):
      """Vráti dealy z custom CRM."""
      # Tvoja logika pre API call do CRM
      return {"deals": [...]}

  @server.tool("update_deal")
  async def update_deal(deal_id: str, status: str):
      """Aktualizuje status deal-u."""
      # Tvoja logika
      return {"success": True}

  server.run()
  ```
- **Povedať:** "MCP server je ľahký – desiatky riadkov kódu. A Prime Agent ho okamžite vie používať."
- **Ako pripojiť vlastný MCP server:**
  ```bash
  # V /login → MCP Connections → Add Connection → Custom MCP Server
  # Zadaj cestu k serveru: /Users/me/my-mcp-servers/crm-server.py
  # Alebo URL: https://my-server.com/mcp
  ```
- **Povedať:** "Ekosystém MCP serverov rýchlo rastie – na GitHub-e sú stovky hotových serverov pre rôzne služby."

#### 12:00–14:00 | Best practices pre MCP
- **Povedať:** "MCP je výkonný nástroj, ale treba ho používať s rozumom."
- **Bezpečnosť:**
  - Dávaj agentovi len tie permissions, ktoré naozaj potrebuje (princíp najmenších privilégií)
  - Pre Gmail: radšej read + draft ako read + send (človek schváli pred odoslaním)
  - API kľúče ukladaj len cez `/login`, nikdy nie v plaintexte
- **Výkon:**
  - Každé MCP volanie = latency. Pre batch operácie zlúč volania.
  - Cache-uj často používané dáta (napr. zoznam kanálov v Slacku)
- **Spolehlivosť:**
  - MCP servery môžu spadnúť – agent by mal mať fallback (napr. uložiť draft lokálne)
  - Pri dlhých operáciách použi streaming

#### 14:00–15:00 | Záver
- **Povedať:** "MCP je budúcnosť AI integrácií. O rok bude mať MCP server každá SaaS služba. Ty už vieš, ako to celé funguje a ako si postaviť vlastný."

### Kľúčové body
- MCP (Model Context Protocol) = univerzálny štandard pre integráciu AI agentov s externými službami
- 3 koncepty: Resources (čítanie dát), Tools (vykonávanie akcií), Prompts (šablóny)
- Konfigurácia cez `/login` → MCP Connections
- Hotové integrácie: Google Workspace, Slack, GitHub, Notion, Serper
- Vlastné MCP servery: jednoduchý Python kód, okamžité použitie v agentovi
- Bezpečnosť: princíp najmenších privilégií, schvaľovanie človekom pri citlivých akciách

### Domáca úloha
1. Nastav MCP Connection pre Google Workspace (ak používaš) – vyskúšaj aspoň Gmail a Calendar
2. Vyber si jednu externú službu, ktorú používaš a nemá MCP server – napíš koncept, aké Resources a Tools by mal jej MCP server mať
3. Ak programuješ v Pythone, vytvor minimálny MCP server pre svoju službu (stačí 2-3 Tools)
4. Vyskúšaj reťazenie MCP volaní: napr. "prečítaj email → extrahuj dáta → zapíš do Google Sheets"

---

## Lekcia 2: Continual Harness – pamäť, skills, prompt notes
**Dĺžka videa:** 12 minút

### Detailný obsah / scenár

#### 0:00–1:30 | Úvod a hook
- **Povedať:** "Máš pocit, že agent pri každej novej session začína od nuly? Že mu musíš stále dookola vysvetľovať, čo robíš, aký je tvoj stack, kto sú tvoji zákazníci? Dnes to zmeníme. Continual Harness je dlhodobá pamäť a znalostná báza tvojho agenta."
- **Ukázať rýchle demo:** Otvoríš novú session, agent automaticky vie: "Pracuješ na projekte X, používaš DeepSeek, tvoji zákazníci sú B2B SaaS firmy, a preferuješ stručné odpovede."

#### 1:30–4:00 | Architektúra Continual Harness
- **Povedať:** "Continual Harness sú 4 typy znalostí, ktoré agentovi zostávajú naprieč session-mi."
- **Prejsť každý typ:**

**1. Memories (Spomienky)**
  - Fakty, ktoré si má agent pamätať
  - Príklad: "Môj produkt je CRM pre poisťovne. Náš hlavný konkurent je Salesforce."
  - `global_=True` → prežije aj medzi rôznymi projektmi
  - `global_=False` (default) → len pre aktuálny projekt/session

**2. Skills (Zručnosti)**
  - Rozšírenia schopností agenta (markdown a Python)
  - Už poznáš z Modulu 3 – tu sa naučíš ich spravovať cez Harness API

**3. Prompt Notes (Inštrukčné poznámky)**
  - Pravidlá správania, preferencie, štylistické pokyny
  - Príklad: "Vždy odpovedaj v slovenčine." alebo "Preferujem bullet pointy namiesto dlhých odsekov."
  - Vkladajú sa do system promptu agenta

**4. Subagent Specs (Špecifikácie pod-agentov)**
  - Uložené definície špecializovaných subagentov
  - Príklad: "SEO Auditor" subagent so špecifickým promptom a skillmi

- **Ukázať diagram:**
  ```
  ┌─────────────────────────────────────────────┐
  │             CONTINUAL HARNESS               │
  ├─────────────────┬───────────────────────────┤
  │  LOCAL (session)│  GLOBAL (cross-session)   │
  ├─────────────────┼───────────────────────────┤
  │  • Memories     │  • Memories (global=True) │
  │  • Skills       │  • Skills (zdieľané)      │
  │  • Prompt Notes │  • Prompt Notes (global)  │
  │  • Subagent     │  • Subagent Specs         │
  └─────────────────┴───────────────────────────┘
  ```

#### 4:00–7:00 | Práca s Continual Harness cez IPython
- **Povedať:** "Harness sa ovláda cez Python API z IPython kernelu. Nie je to len pre vývojárov – je to jednoduché."
- **Prejsť základné CRUD operácie:**

**Memories:**
  ```python
  # Vytvorenie
  await rlm.harness.create_memory(
      content="Náš produkt je CRM pre malé poisťovne do 50 zamestnancov.",
      name="produkt-popis",
      tags=["produkt", "ICP"]
  )

  # Čítanie
  memories = await rlm.harness.overview()

  # Aktualizácia
  await rlm.harness.update_memory(
      name="produkt-popis", 
      content="Náš produkt je CRM pre poisťovne do 200 zamestnancov."
  )

  # Zmazanie
  await rlm.harness.delete_memory(name="produkt-popis")
  ```

**Prompt Notes:**
  ```python
  await rlm.harness.create_prompt_note(
      content="Vždy odpovedaj v slovenčine. Používaj tykanie.",
      name="jazykove-nastavenie"
  )
  ```

**Skills:**
  ```python
  await rlm.harness.create_skill(
      name="moj-custom-skill",
      description="..."
  )
  ```

- **Povedať:** "Najdôležitejšie je zapamätať si: `create`, `update`, `delete`, a `overview` pre každý typ."

#### 7:00–9:00 | Kedy použiť local vs global
- **Povedať:** "Toto je kľúčové rozhodnutie – čo patrí do projektu a čo je univerzálne."
- **Pravidlá:**

| Typ znalosti | Local (session/project) | Global (všetky projekty) |
|-------------|------------------------|--------------------------|
| **Memory** | "Používame React 19" | "Moja firma sídli v Bratislave" |
| **Skill** | Skill špecifický pre projekt | Univerzálny skill (napr. slovenský prekladač) |
| **Prompt Note** | "V tomto projekte generuj kód v TypeScripte" | "Vždy tykaj, používaj slovenčinu" |
| **Subagent** | Agent pre analýzu tohto projektu | Univerzálny "Code Reviewer" agent |

- **Povedať:** "Ak nevieš, začni s local. Global použi len vtedy, keď si istý, že to chceš vo všetkých projektoch."

#### 9:00–10:30 | Refinement workflow
- **Povedať:** "Harness nie je 'nastav a zabudni'. Je to živá znalostná báza, ktorú treba udržiavať."
- **Kedy spraviť refinement:**
  - Agent opakovane robí rovnakú chybu → pridaj Prompt Note
  - Zistil si nový fakt o trhu → aktualizuj Memory
  - Vytvoril si užitočný workflow → ulož ho ako Skill
  - Opakovaná delegácia na subagenta → vytvor Subagent Spec
- **Ukázať `rlm.harness.record_refinement()`:**
  ```python
  await rlm.harness.record_refinement(
      description="Pridaná memory o preferovanom modeli",
      entry_type="memory",
      entry_name="default-model",
      change="create"
  )
  ```
- **Povedať:** "Refinements ti dávajú históriu zmien – vidíš, ako sa tvoj agent vyvíja."

#### 10:30–12:00 | Best practices a záver
- **Povedať:** "Pár tipov na záver:"
  - **Menej je viac** – nezahlcuj Harness stovkami memories. Drž sa podstatného.
  - **Pomenúvaj systematicky** – `produkt-popis`, `ICP-finance`, `stack-frontend` – ľahko sa hľadá
  - **Pravidelne čisti** – raz za mesiac prejdi Harness a vymaž, čo už neplatí
  - **Prompt Notes sú silné** – dobre napísaná prompt note zmení správanie agenta viac, než 10 memories
- **Povedať:** "Continual Harness premieňa agenta z 'nástroja na jedno použitie' na 'dlhodobého partnera', ktorý sa učí a rastie s tebou."

### Kľúčové body
- Continual Harness = 4 typy dlhodobej pamäte: Memories, Skills, Prompt Notes, Subagent Specs
- Local vs Global: local pre projektové, global pre univerzálne znalosti
- Ovládanie cez `rlm.harness.create/update/delete/overview` z IPython kernelu
- Refinement workflow = systematické vylepšovanie agenta na základe skúseností
- Pomenúvaj systematicky, pravidelne čisti, menej je viac

### Domáca úloha
1. Vytvor aspoň 3 Memories pre svoj aktuálny projekt (produkt, ICP, technický stack)
2. Pridaj aspoň 2 Prompt Notes (jazykové preferencie, formát odpovedí)
3. Sprav `rlm.harness.overview()` a skontroluj, čo všetko máš v Harness-e
4. Identifikuj jednu vec, ktorú agentovi stále opakuješ – a ulož ju ako Prompt Note

---

## Lekcia 3: Scheduling – automatizované úlohy
**Dĺžka videa:** 10 minút

### Detailný obsah / scenár

#### 0:00–1:00 | Úvod a hook
- **Povedať:** "Čo keby tvoj agent každé ráno o 7:00 skontroloval predajnú pipeline, o 8:00 poslal follow-upy, v pondelok spravil SEO audit, v piatok vygeneroval týždenný report – a to všetko bez toho, aby si pohol prstom? Toto je scheduling."
- **Ukázať rýchle demo:** Demo ukazuje naplánované úlohy v akcii – report, ktorý prišiel automaticky.

#### 1:00–3:30 | Ako scheduling funguje v Prime Agent
- **Povedať:** "Prime Agent nemá zabudovaný cron. Namiesto toho používa systém Heartbeatov a externých plánovačov. Poďme si to vysvetliť."
- **Tri spôsoby schedulovania:**

**1. Heartbeats (interné)**
  - Agent beží nonstop a v intervaloch vykonáva úlohy
  - Cez skill `rlm-heartbeat`
  - Vhodné pre: kontinuálne monitorovanie, real-time reakcie
  - Detailne v Lekcii 5

**2. Externý cron + Prime Agent CLI**
  - Klasický cron (Linux/macOS) alebo Task Scheduler (Windows)
  - Spustí `prime-agent` s konkrétnym promptom
  - Vhodné pre: denné/týždenné reporty, pravidelné audity

**3. GitHub Actions / CI/CD pipeline**
  - Prime Agent ako súčasť CI/CD
  - Spustenie pri push-i, PR, alebo podľa schedule
  - Vhodné pre: code review, automatické testy, dependency checky

- **Povedať:** "Dnes sa zameriame na možnosť 2 – externý cron – lebo je najjednoduchšia a najuniverzálnejšia."

#### 3:30–6:00 | Nastavenie cron úloh s Prime Agent
- **Povedať:** "Na macOS a Linux použijeme cron. Na Windowse Task Scheduler. Princíp je rovnaký."
- **Krok za krokom na macOS/Linux:**

**Krok 1: Vytvor shell skript**
  ```bash
  # /Users/me/scripts/weekly-seo-report.sh
  #!/bin/bash
  export DEEPSEEK_API_KEY="sk-..."
  cd /Users/me/projects/marketing

  prime-agent \
    --provider deepseek \
    --model deepseek-v4-flash \
    --prompt "Spusti SEO audit pre mojastranka.sk. 
              Výsledky ulož do /reports/seo-$(date +%Y-%m-%d).md. 
              Po dokončení pošli sumár na email."
  ```
  ```bash
  chmod +x /Users/me/scripts/weekly-seo-report.sh
  ```

**Krok 2: Pridaj do crontab-u**
  ```bash
  crontab -e
  # Pridaj riadok:
  # Každý pondelok o 8:00
  0 8 * * 1 /Users/me/scripts/weekly-seo-report.sh
  ```

**Krok 3: Overenie**
  ```bash
  crontab -l  # Zobraz naplánované úlohy
  ```

- **Ukázať aj na Windowse (screenshot):**
  - Otvor Task Scheduler
  - Create Basic Task
  - Trigger: Weekly, Monday 8:00
  - Action: Start a program → `prime-agent` s argumentmi

#### 6:00–8:00 | Užitočné schedulované úlohy – inšpirácia
- **Povedať:** "Tu je zoznam úloh, ktoré si môžeš naplánovať hneď dnes:"

| Frekvencia | Úloha | Prompt (stručne) |
|-----------|-------|------------------|
| **Denne** | Pipeline check | "Skontroluj pipeline CSV, nájdi dealy bez follow-upu >3 dni" |
| **Denne** | Support monitoring | "Skontroluj nové support tickety, odpovedz na how-to" |
| **Týždenne** | SEO monitoring | "Spusti SEO audit, porovnaj s minulým týždňom" |
| **Týždenne** | Sales report | "Vygeneruj týždenný sales report z CRM dát" |
| **Týždenne** | Marketing report | "Analyzuj traffic, konverzie, a výkon kampaní" |
| **Mesačne** | Content audit | "Skontroluj všetky blog posty, navrhni refresh" |
| **Mesačne** | Konkurenčná analýza | "Spusti competitor-profiling na top 5 konkurentov" |
| **Kvartálne** | Harness cleanup | "Prejdi Continual Harness, navrhni vyčistenie" |

- **Povedať:** "Začni s 2-3 úlohami. Pridávaj postupne."

#### 8:00–9:30 | Error handling a notifikácie
- **Povedať:** "Čo keď naplánovaná úloha zlyhá? Potrebuješ o tom vedieť."
- **Stratégie error handlingu:**
  1. **Logovanie** – presmeruj výstup do log súboru:
     ```bash
     prime-agent --prompt "..." >> /logs/agent-$(date +%Y-%m-%d).log 2>&1
     ```
  2. **Notifikácia pri zlyhaní** – script skontroluje exit code:
     ```bash
     #!/bin/bash
     prime-agent --prompt "..."
     if [ $? -ne 0 ]; then
       echo "Agent task FAILED: $(date)" | mail -s "⚠️ Agent Alert" ja@firma.sk
     fi
     ```
  3. **Retry logika** – skús znova s iným modelom alebo menším scope-om

- **Ukázať kompletný robustný skript:**

#### 9:30–10:00 | Best practices a záver
- **Povedať:** "Pár pravidiel pre produkčný scheduling:"
  - **Nespúšťaj príliš často** – API calls stoja peniaze. Reporting raz za deň stačí.
  - **Mimo špičky** – úlohy naplánuj na noc/ ráno, keď sú LLM API lacnejšie a rýchlejšie
  - **Postupné pridávanie** – začni s 1 úlohou, po týždni pridaj ďalšiu
  - **Monitoruj náklady** – sleduj, koľko tokenov mesačne minieš na schedulované úlohy
- **Povedať:** "Scheduling je most medzi 'agentom na požiadanie' a 'agentom, ktorý pracuje, kým ty spíš'."

### Kľúčové body
- 3 spôsoby schedulovania: Heartbeats, externý cron, GitHub Actions
- Cron: vytvor shell skript → `chmod +x` → `crontab -e`
- Na Windowse: Task Scheduler
- Užitočné úlohy: denný pipeline check, týždenný SEO audit, mesačný content audit
- Error handling: logovanie, notifikácie pri zlyhaní, retry logika
- Scheduluj s rozumom – API calls stoja peniaze

### Domáca úloha
1. Vytvor shell skript pre jednu automatizovanú úlohu (napr. denný pipeline check)
2. Nastav ju v cron-e (alebo Task Scheduler-i) a nechaj ju bežať aspoň 3 dni
3. Skontroluj log-y – prebehla úloha úspešne? Ak nie, oprav a spusti znova
4. Napíš si zoznam 3 ďalších úloh, ktoré by si chcel automatizovať – a naplánuj si ich nasadenie

---

## Lekcia 4: API a webhooky
**Dĺžka videa:** 12 minút

### Detailný obsah / scenár

#### 0:00–1:30 | Úvod a hook
- **Povedať:** "Tvoj agent je super – ale čo keď potrebuješ, aby komunikoval s tvojím produktom? Alebo aby reagoval na eventy z tvojho systému? Dnes sa naučíš, ako agenta napojiť na API a webhooky – a spraviť z neho plnohodnotnú súčasť tvojej infraštruktúry."
- **Ukázať rýchle demo:** Nový zákazník sa zaregistruje → webhook to pošle agentovi → agent pošle welcome email, vytvorí úlohu pre sales a zaloguje do CRM.

#### 1:30–4:00 | Volanie externých API z agenta
- **Povedať:** "Agent je Python runtime. To znamená, že môžeš používať `requests`, `httpx`, a akúkoľvek Python knižnicu na volanie API."
- **Ukázať v IPython kernel-i:**

**Jednoduché REST API volanie:**
  ```python
  import requests

  # Získanie dát z vlastného API
  resp = requests.get(
      "https://api.mojprodukt.sk/v1/deals",
      headers={"Authorization": f"Bearer {os.environ['MY_API_KEY']}"}
  )
  deals = resp.json()
  print(f"Našiel som {len(deals)} dealov")
  ```

**POST request – vytvorenie zdroja:**
  ```python
  resp = requests.post(
      "https://api.mojprodukt.sk/v1/tasks",
      json={"title": "Follow-up s ACME Corp", "priority": "high"},
      headers={"Authorization": f"Bearer {os.environ['MY_API_KEY']}"}
  )
  ```

- **Povedať:** "API kľúče nikdy nehardcoduj! Ukladaj ich cez premenné prostredia:"
  ```bash
  export MY_API_KEY="sk-live-..."
  # Alebo v ~/.prime/agent/config.yaml
  ```
- **Bezpečnostné upozornenie:** Nikdy nedávaj API kľúče priamo do promptu. Sú viditeľné v logoch.

#### 4:00–6:30 | Vytvorenie custom skillu s API integráciou
- **Povedať:** "Ak API voláš často, oplatí sa to zabaliť do skillu. Agent ho potom volá automaticky."
- **Ukázať štruktúru Python skillu s API:**

  ```python
  # skills/my-crm/SKILL.md
  # + skills/my-crm/crm_api.py

  import os
  import requests

  API_BASE = "https://api.mojcrm.sk/v1"
  API_KEY = os.environ.get("MY_CRM_API_KEY")

  def get_deals(status: str = "open"):
      """Získa dealy z CRM."""
      resp = requests.get(
          f"{API_BASE}/deals",
          params={"status": status},
          headers={"Authorization": f"Bearer {API_KEY}"}
      )
      resp.raise_for_status()
      return resp.json()

  def create_deal(company: str, value: float, stage: str):
      """Vytvorí nový deal v CRM."""
      resp = requests.post(
          f"{API_BASE}/deals",
          json={"company": company, "value": value, "stage": stage},
          headers={"Authorization": f"Bearer {API_KEY}"}
      )
      return resp.json()
  ```
- **Povedať:** "Agent potom prirodzene používa tieto funkcie: 'Získaj všetky otvorené dealy a sprav analýzu.'"

#### 6:30–9:00 | Webhooky – ako nechať agenta reagovať na eventy
- **Povedať:** "Webhook je opak API callu – nevoláš ty službu, služba volá teba. Ako prinútiť agenta, aby počúval?"
- **Architektúra webhook → agent:**

  ```
  [Tvoja app] → [Webhook] → [Lightweight server] → [Prime Agent CLI]
                   (HTTP POST)     (Flask/FastAPI)      (prime-agent --prompt "...")
  ```

- **Ukázať minimálny Flask server, ktorý spúšťa agenta:**
  ```python
  # webhook_listener.py
  from flask import Flask, request
  import subprocess, os

  app = Flask(__name__)

  @app.route("/webhook/new-customer", methods=["POST"])
  def new_customer():
      data = request.json
      customer_name = data["name"]
      customer_email = data["email"]

      # Spusti agenta s kontextom
      prompt = f"""
      Nový zákazník sa práve zaregistroval:
      Meno: {customer_name}
      Email: {customer_email}

      Vykonaj tieto akcie:
      1. Pošli welcome email cez GWS Gmail
      2. Vytvor Google Task pre sales: "Zavolať {customer_name} do 24h"
      3. Zaloguj do Google Sheets – tabuľka "New Customers 2025"
      """

      subprocess.run([
          "prime-agent",
          "--provider", "deepseek",
          "--model", "deepseek-v4-flash",
          "--prompt", prompt
      ])

      return {"status": "ok", "customer": customer_name}

  if __name__ == "__main__":
      app.run(port=5000)
  ```

- **Povedať:** "Tento server beží na pozadí. Keď tvoja app pošle webhook, agent sa spustí a vykoná úlohy."
- **Bezpečnosť:** Pridaj webhook signature verification (HMAC), aby si vedel, že request je naozaj z tvojej app-ky.

#### 9:00–11:00 | Pokročilé vzory – event-driven agent
- **Povedať:** "Poďme to celé posunúť na vyššiu úroveň. Event-driven architektúra s agentom."
- **Ukázať komplexnejší setup:**

  ```
  Eventy z tvojho systému:
  ├── customer.created → Agent: welcome + onboarding
  ├── payment.failed   → Agent: dunning email + support alert
  ├── trial.expiring   → Agent: upgrade offer + sales follow-up
  ├── nps.low          → Agent: "save" outreach od CS tímu
  └── feature.used_10x → Agent: case study request
  ```

- **Povedať:** "Každý event v tvojom systéme môže spúšťať agenta. Toto je skutočná automatizácia – agent reaguje na reálny svet v reálnom čase."
- **Ukázať, ako to spraviť škálovateľne:**
  - Použi Redis/ RabbitMQ ako frontu eventov
  - Jeden listener + Prime Agent procesy
  - Rate limiting – max 10 spustení agenta za minútu

#### 11:00–12:00 | Best practices a záver
- **Povedať:** "API a webhooky sú vstupnou bránou k plnej integrácii agenta do tvojej infraštruktúry."
- **Bezpečnosť na prvom mieste:**
  - API kľúče len v env premenných, nikdy v kóde
  - Webhook signature verification
  - Rate limiting na ochranu pred zahltením
  - Sandboxing – agent by nemal mať prístup k produkčnej databáze, len cez API
- **Povedať:** "V ďalšej lekcii dokončíme obraz – Heartbeats, ktoré umožnia agentovi bežať nonstop."

### Kľúčové body
- Agent volá externé API cez Python `requests`/`httpx` priamo z IPython kernelu
- API kľúče ukladaj v premenných prostredia, nikdy nie v kóde alebo prompte
- Opakované API volania zabaľ do Python skillu – agent ich volá prirodzene
- Webhooky: Flask/FastAPI server, ktorý pri evente spúšťa `prime-agent --prompt "..."`
- Event-driven architektúra: každý event v tvojom systéme môže spúšťať špecifickú akciu agenta
- Bezpečnosť: API kľúče v env, webhook signature, rate limiting, sandboxing

### Domáca úloha
1. Vyber si jedno API, ktoré používaš (CRM, Stripe, vlastný produkt) a napíš Python skill, ktorý ho obaľuje (2-3 funkcie)
2. Vyskúšaj volať API z agenta – získaj dáta, spracuj ich, vypíš výsledky
3. Postav minimálny webhook listener (Flask/FastAPI), ktorý spúšťa agenta pri HTTP POST
4. Premysli si: aké eventy z tvojho systému by mali spúšťať agenta? Napíš si 5 eventov + čo by mal agent pre každý spraviť

---

## Lekcia 5: Heartbeats – agent ktorý beží nonstop
**Dĺžka videa:** 11 minút

### Detailný obsah / scenár

#### 0:00–1:30 | Úvod a hook
- **Povedať:** "Čo keby tvoj agent nikdy nespal? Čo keby 24/7 monitoroval tvoj biznis, kontroloval pipeline, odpovedal na urgentné tickety, a upozorňoval ťa len vtedy, keď sa naozaj niečo deje? Vitaj vo svete Heartbeatov."
- **Ukázať rýchle demo:** Terminál s bežiacim agentom, ktorý každých 15 minút vypisuje "❤️ Heartbeat: Pipeline OK, 3 follow-upy odoslané, 0 urgentných ticketov."

#### 1:30–3:30 | Čo je Heartbeat a ako funguje
- **Povedať:** "Heartbeat je pravidelný 'tep' agenta. V stanovenom intervale agent vykoná definovanú sadu akcií a reportuje výsledok."
- **Architektúra Heartbeat-u:**
  ```
  [Prime Agent beží nonstop]
       │
       ├── Každých N minút:
       │   1. Preberie sa
       │   2. Vykoná heartbeat úlohy
       │   3. Zaloguje/notifikuje výsledok
       │   4. Ide spať
       │
       └── Ak sa stane niečo kritické → okamžitá notifikácia
  ```
- **Kľúčové vlastnosti:**
  - Beží v rámci session-y agenta (session musí byť aktívna)
  - Využíva IPython kernel – stav sa zachováva medzi heartbeat-mi
  - Môže mať viacero heartbeatov s rôznymi intervalmi
  - Agent medzi heartbeat-mi "spí" – nespotrebúva tokeny

#### 3:30–6:00 | Vytvorenie prvého Heartbeat-u
- **Povedať:** "Heartbeat sa vytvára cez skill `rlm-heartbeat`. Poďme si vytvoriť prvý."
- **Krok za krokom:**

**Krok 1: Spusti agenta v dlhodobej session:**
  ```bash
  prime-agent --provider deepseek --model deepseek-v4-flash
  ```

**Krok 2: Vytvor heartbeat:**
  ```python
  await rlm_heartbeat.create(
      name="pipeline-monitor",
      interval_minutes=15,
      task="""
      Skontroluj pipeline CSV v /data/pipeline.csv.
      Nájdi všetky dealy, kde:
      - Posledný kontakt bol pred >3 dňami
      - Deal je v štádiu "Demo" alebo "Proposal"

      Pre každý takýto deal:
      1. Vygeneruj follow-up email
      2. Ulož ho do /follow-ups/pending/

      Ak nájdeš kritické problémy (deal stagnuje >14 dní),
      pošli mi notifikáciu cez GWS Gmail.
      """
  )
  ```

**Krok 3: Over, že heartbeat beží:**
  ```python
  heartbeats = await rlm_heartbeat.list()
  print(heartbeats)
  # [{"name": "pipeline-monitor", "interval": 15, "status": "active", ...}]
  ```

- **Povedať:** "Od tohto momentu agent každých 15 minút skontroluje pipeline."
- **Ukázať výstup v konzole:**
  ```
  [14:00] ❤️ Heartbeat 'pipeline-monitor': 2 follow-upy vygenerované. Všetko OK.
  [14:15] ❤️ Heartbeat 'pipeline-monitor': 1 follow-up vygenerovaný. Všetko OK.
  [14:30] ❤️ Heartbeat 'pipeline-monitor': ⚠️ Deal #47 stagnuje 16 dní! 
          Notifikácia odoslaná.
  ```

#### 6:00–8:00 | Užitočné heartbeat vzory
- **Povedať:** "Tu sú overené heartbeat vzory z praxe:"

| Heartbeat | Interval | Čo robí |
|-----------|----------|---------|
| **Pipeline Watch** | 15-30 min | Sleduje predajnú pipeline, upozorňuje na stagnujúce dealy |
| **Support Triage** | 5-10 min | Kontroluje nové tickety, odpovedá na jednoduché, eskaluje urgentné |
| **Uptime Monitor** | 1-5 min | Ping-uje tvoju aplikáciu, notifikuje pri výpadku |
| **Content Guardian** | 60 min | Sleduje zmeny na konkurenčných weboch, notifikuje |
| **Budget Watch** | 60 min | Kontroluje API spending, upozorní pri prekročení limitu |
| **Security Patrol** | 15 min | Skenuje logy na podozrivé aktivity |
| **Stock/Inventory** | 30 min | Sleduje stav zásob, notifikuje pri nízkom stave |

- **Povedať:** "Kombinuj viacero heartbeatov – každý nech robí jednu vec dobre."

#### 8:00–9:30 | Správa a monitoring heartbeatov
- **Povedať:** "Heartbeaty treba spravovať – pozastaviť, upraviť, zastaviť."
- **Základné operácie:**
  ```python
  # Výpis všetkých heartbeatov
  await rlm_heartbeat.list()

  # Pozastavenie
  await rlm_heartbeat.pause(name="pipeline-monitor")

  # Obnovenie
  await rlm_heartbeat.resume(name="pipeline-monitor")

  # Zmena intervalu
  await rlm_heartbeat.update(name="pipeline-monitor", interval_minutes=30)

  # Zastavenie
  await rlm_heartbeat.stop(name="pipeline-monitor")
  ```
- **Monitoring – čo sledovať:**
  - Koľkokrát heartbeat zlyhal za posledných 24h?
  - Aká je priemerná doba vykonania?
  - Koľko tokenov heartbeat spotreboval?
- **Povedať:** "Raz za týždeň skontroluj logy heartbeatov. Ak niektorý stále reportuje 'všetko OK', možno je zbytočný. Ak často zlyháva, uprav task."

#### 9:30–11:00 | Heartbeat vs Cron – kedy použiť čo
- **Povedať:** "Máš dve možnosti automatizácie – Heartbeats a Cron. Kedy použiť ktorú?"

| Kritérium | Heartbeat | Cron |
|-----------|-----------|------|
| **Session** | Vyžaduje bežiacu session | Spúšťa novú session |
| **Perzistentný stav** | Áno (IPython kernel) | Nie (každé spustenie = čistý štít) |
| **Vhodné pre** | Kontinuálne monitorovanie, real-time reakcie | Dávkové úlohy, reporty |
| **Frekvencia** | Sekundy až hodiny | Minúty až dni |
| **Náklady** | Session beží nonstop (ale tokeny len pri heartbeat-e) | Tokeny len pri spustení |
| **Zložitosť** | Jednoduché (všetko v agentovi) | Vyžaduje shell skripty, cron syntax |

- **Pravidlo:**
  - **Heartbeat** = potrebuješ rýchlu reakciu (minúty) a kontinuálny stav
  - **Cron** = periodická úloha (hodiny/dni), každé spustenie je nezávislé

- **Záver modulu:**
  - "V tomto module si sa posunul od používateľa k architektovi. Ovládaš MCP integrácie, Continual Harness, scheduling, API a Heartbeats. Tvoj agent už nie je len nástroj – je to infraštruktúra."
  - "V Module 8 to celé zabalíme do produkčného balíka: bezpečnosť, monitoring, škálovanie a záverečný projekt."

### Kľúčové body
- Heartbeat = pravidelný "tep" agenta, ktorý vykonáva definované úlohy v intervaloch
- Vytvára sa cez `rlm_heartbeat.create(name, interval_minutes, task)`
- Operácie: list, pause, resume, update, stop
- Užitočné vzory: Pipeline Watch, Support Triage, Uptime Monitor, Budget Watch
- Heartbeat vs Cron: Heartbeat = kontinuálny stav + rýchla reakcia, Cron = nezávislé dávkové úlohy
- Agent medzi heartbeat-mi nespotrebúva tokeny

### Domáca úloha
1. Vytvor aspoň jeden Heartbeat pre svoj biznis (napr. pipeline monitor alebo support triage)
2. Nechaj ho bežať aspoň 2 hodiny a sleduj logy
3. Vyskúšaj operácie pause, update a resume na svojom heartbeate
4. Navrhni kombináciu Heartbeat + Cron, ktorá pokrýva tvoje potreby – napíš krátky plán: čo beží cez Heartbeat a čo cez Cron

---
