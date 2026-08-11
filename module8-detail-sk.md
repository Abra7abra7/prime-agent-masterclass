# Prime Agent Masterclass – Modul 8: Produkčné nasadenie

## Prehľad modulu

**Cieľ modulu:** Po absolvovaní tohto modulu budeš vedieť nasadiť Prime Agenta do produkčného prostredia s dôrazom na bezpečnosť, monitoring a škálovanie. Pochopíš, ako sa agenti vyvíjajú, aká je ich budúcnosť, a čo to znamená pre tvoj biznis. Absolvuješ záverečný projekt, v ktorom postavíš vlastný biznis bežiaci na autopilota.

**Celková dĺžka:** 45 minút videa + domáce úlohy + záverečný projekt

---

## Lekcia 1: Best practices a bezpečnosť
**Dĺžka videa:** 10 minút

### Detailný obsah / scenár

#### 0:00–1:00 | Úvod a hook
- **Povedať:** "Predstav si, že tvoj agent omylom pošle email všetkým tvojím zákazníkom. Alebo vymaže produkčnú databázu. Alebo vyzradí tvoje API kľúče. Znie to desivo? Dnes sa naučíš, ako tomu zabrániť. Bezpečnosť nie je 'nice to have' – je to základ."
- **Ukázať slide s nadpisom: "S veľkou silou prichádza veľká zodpovednosť."**

#### 1:00–3:00 | API kľúče a secrets management
- **Povedať:** "API kľúče sú kľúče od tvojho digitálneho domu. Ako ich chrániť?"
- **Pravidlo č. 1: Nikdy v kóde, nikdy v prompte**
  - ❌ `DEEPSEEK_API_KEY="sk-..."` v shell skripte commitnutom do Gitu
  - ❌ "Môj API kľúč je sk-..." v prompte pre agenta
  - ✅ Premenné prostredia: `export DEEPSEEK_API_KEY="sk-..."`
  - ✅ `.env` súbor (mimo Gitu): `DEEPSEEK_API_KEY=sk-...`
  - ✅ Secrets manager: 1Password CLI, AWS Secrets Manager, HashiCorp Vault

- **Ukázať správny setup:**
  ```bash
  # V ~/.zshrc alebo ~/.bashrc:
  export DEEPSEEK_API_KEY="sk-..."
  export ANTHROPIC_API_KEY="sk-ant-..."
  export MY_CRM_API_KEY="live_..."

  # Alebo .env + dotenv:
  # .env (pridaný do .gitignore!)
  ```
  ```python
  # V IPython kernel-i:
  from dotenv import load_dotenv
  load_dotenv()

  import os
  api_key = os.environ["MY_CRM_API_KEY"]  # ✅ Bezpečné
  ```

- **Povedať:** "Agent vidí premenné prostredia cez `os.environ`. Ale nikdy ich nevypisuj do logov!"

#### 3:00–5:00 | File system access – čo agent smie a nesmie
- **Povedať:** "Agent beží na tvojom stroji. To znamená, že má prístup k tvojim súborom. Obmedz mu ho."
- **Stratégie sandboxingu:**

**1. Pracovný adresár (Working Directory)**
  - Spúšťaj agenta vždy v špecifickom projektovom adresári:
    ```bash
    cd /Users/me/projects/marketing
    prime-agent  # agent vidí len tento adresár a podadresáre
    ```

**2. `.gitignore` pre citlivé súbory**
  - `.env`, `config.yaml`, `secrets/` – vždy v `.gitignore`

**3. Docker kontajnerizácia**
  ```bash
  docker run -v $(pwd):/workspace -w /workspace \
    -e DEEPSEEK_API_KEY=$DEEPSEEK_API_KEY \
    prime-agent-image prime-agent --prompt "..."
  ```
  - Agent vidí len `/workspace`, nie celý host systém

**4. Read-only prístup k citlivým adresárom**
  - Na Linuxe/macOS: `chmod` na read-only pre adresáre, ktoré agent nepotrebuje meniť

- **Povedať:** "Ideálny setup: agent beží v Docker-i s presne definovanými volumes."

#### 5:00–7:00 | Schvaľovanie (Human-in-the-loop)
- **Povedať:** "Pri kritických akciách by mal vždy rozhodnúť človek. Toto je princíp 'human-in-the-loop'."
- **Ktoré akcie vyžadujú schválenie:**

| Akcia | Riziko | Riešenie |
|-------|--------|----------|
| Odoslanie emailu | Stredné | Agent generuje draft → človek schvaľuje a odosiela |
| Úprava produkčného kódu | Vysoké | Agent vytvorí PR → človek review a merge |
| Zmena v databáze | Kritické | Agent navrhne SQL → človek spúšťa |
| Nákup / platba | Kritické | Agent nikdy neinicializuje platbu |
| Mazanie súborov | Vysoké | Agent presúva do `/.trash/`, človek maže |

- **Ukázať implementáciu schvaľovania:**
  ```python
  # Agent vygeneruje akciu, ale nevykoná ju:
  # "Tu je draft emailu pre ACME Corp. 
  #  Uložený v /drafts/email-acme-2025-08-11.md.
  #  Pre odoslanie napíš 'odošli draft email-acme-2025-08-11'."
  ```

#### 7:00–9:00 | Bezpečnostné best practices – checklist
- **Povedať:** "Tu je kompletný bezpečnostný checklist pre produkčné nasadenie:"

**Pred spustením:**
- [ ] API kľúče sú len v env premenných / secrets manager-i
- [ ] `.env` a `config.yaml` sú v `.gitignore`
- [ ] Agent beží v limitovanom adresári (nie v `~`)
- [ ] Kritické akcie majú human-in-the-loop
- [ ] MCP Connections majú minimálne permissions (napr. Gmail: read+draft, nie send)

**Počas behu:**
- [ ] Logy neobsahujú API kľúče ani citlivé dáta
- [ ] Rate limiting na API volania (najmä platené)
- [ ] Session logy sa pravidelne rotujú (neukladať navždy)

**Pravidelne:**
- [ ] Rotácia API kľúčov (napr. raz za kvartál)
- [ ] Audit MCP Connections – sú všetky stále potrebné?
- [ ] Kontrola prístupových práv k súborovému systému

- **Povedať:** "Toto nie je rocket science. Sú to jednoduché pravidlá, ktoré ťa ochránia pred 95 % bezpečnostných incidentov."

#### 9:00–10:00 | Záver
- **Povedať:** "Bezpečnosť nie je konečný stav. Je to proces. Začni s týmto checklistom a pridávaj ďalšie opatrenia, ako rastie tvoje nasadenie."
- **Povedať:** "Pamätaj: agent je výkonný nástroj. Ako každý výkonný nástroj – keď s ním zaobchádzaš správne, vybuduješ impérium. Keď nie, môžeš si ublížiť."

### Kľúčové body
- API kľúče: nikdy v kóde, nikdy v prompte → env premenné / secrets manager
- File system: limitovať pracovný adresár, ideálne Docker kontajnerizácia
- Human-in-the-loop: kritické akcie (emaily, DB zmeny, platby) vyžadujú schválenie človekom
- MCP Connections: vždy minimálne permissions (princíp najmenších privilégií)
- Pravidelný audit: rotácia kľúčov, kontrola prístupov, čistenie logov

### Domáca úloha
1. Sprav si bezpečnostný audit svojho aktuálneho setup-u podľa checklist-u z lekcie – koľko bodov spĺňaš?
2. Nastav `.env` súbor a premiestni všetky API kľúče z kódu/skriptov doň (pridaj `.env` do `.gitignore`)
3. Implementuj aspoň jeden human-in-the-loop krok (napr. agent generuje emaily, ty ich schvaľuješ)
4. Ak používaš Docker, vytvor `docker-compose.yml` pre svojho agenta s limitovaným prístupom

---

## Lekcia 2: Monitoring a ladenie agentov
**Dĺžka videa:** 10 minút

### Detailný obsah / scenár

#### 0:00–1:00 | Úvod a hook
- **Povedať:** "Agent beží, úlohy sa plnia. Ale ako vieš, že naozaj všetko funguje? Že neminieš stovky eur na zbytočných API calls? Že agent nerobí chyby, ktoré si nikto nevšimne? Dnes sa naučíš monitoring – oči a uši tvojho produkčného nasadenia."
- **Ukázať rýchle demo:** Dashboard s prehľadom: koľko úloh agent spravil, koľko tokenov minul, aká je úspešnosť, koľko to stálo.

#### 1:00–3:00 | Čo všetko treba monitorovať
- **Povedať:** "Monitoring agenta má 4 dimenzie. Poďme si ich prejsť."

**1. Výkon (Performance)**
  - Koľko úloh agent spracoval za deň/týždeň?
  - Aká je úspešnosť (koľko úloh dokončil bez chyby)?
  - Priemerný čas na úlohu
  - Koľko úloh zlyhalo a prečo?

**2. Náklady (Cost)**
  - Tokeny spotrebované za deň
  - Cena v € (závisí od modelu: DeepSeek ~$1.5/M, Claude ~$15/M)
  - Rozdelenie podľa typu úloh (ktoré úlohy sú najdrahšie?)

**3. Kvalita (Quality)**
  - Koľko výstupov človek schválil vs. odmietol?
  - Koľkokrát agent spravil opravu po chybe?
  - Spätná väzba od používateľov (ak agent robí support)

**4. Zdravie (Health)**
  - Je agent online? (pre Heartbeats a nonstop session-y)
  - Nespadla session?
  - Nie sú MCP Connections nefunkčné?
  - Nie je prekročený rate limit?

- **Povedať:** "Nemusíš sledovať všetko od prvého dňa. Začni s nákladmi a úspešnosťou. To sú tvoje dve najdôležitejšie metriky."

#### 3:00–5:30 | Nástroje na monitoring
- **Povedať:** "Ako tieto metriky zbierať? Tu sú konkrétne nástroje a postupy."

**1. Session logy (zabudované)**
  - Každá session agenta sa loguje do `~/.prime/agent/sessions/`
  - JSONL formát – každý riadok je jedna akcia
  - Obsahuje: prompt, tool calls, výsledky, tokeny, chyby
  - **Ukázať príklad logu a ako z neho čítať:**
    ```bash
    ls ~/.prime/agent/session-artifacts/
    # Každá session má vlastný podadresár s .jsonl súbormi
    ```
    ```python
    import json
    with open("session.jsonl") as f:
        for line in f:
            entry = json.loads(line)
            print(entry.get("type"), entry.get("tool", ""))
    ```

**2. Vlastný monitoring skript**
  ```python
  # monitoring.py – spúšťa sa denne cez cron
  import os, json, glob
  from datetime import date

  today = date.today().isoformat()
  sessions_dir = os.path.expanduser("~/.prime/agent/session-artifacts/")

  total_tokens = 0
  total_tasks = 0
  errors = 0

  for session_dir in glob.glob(f"{sessions_dir}/*"):
      for log_file in glob.glob(f"{session_dir}/*.jsonl"):
          # Parsuj logy a agreguj metriky
          ...

  print(f"Dátum: {today}")
  print(f"Dokončené úlohy: {total_tasks}")
  print(f"Spotrebované tokeny: {total_tokens:,}")
  print(f"Chyby: {errors}")
  ```

**3. Externé nástroje**
  - **Prometheus + Grafana** – pre pokročilý monitoring (metricky, dashboardy, alerty)
  - **Better Stack / Datadog** – managed monitoring pre agentov
  - **Vlastný dashboard v Google Sheets** – agent sám zapisuje metriky

#### 5:30–7:30 | Ladenie – keď agent nerobí to, čo chceš
- **Povedať:** "Aj najlepší agent občas zlyhá. Tu je systematický debugging postup."
- **Debugging flow:**

```
1. Prečítaj log session-y
   ├── Aká bola posledná akcia pred chybou?
   ├── Akú chybovú hlášku agent dostal?
   └── Ako na ňu agent reagoval?

2. Reprodukuj problém
   ├── Spusti agenta s rovnakým promptom
   ├── Zmenší scope (namiesto "sprav všetko" daj "sprav len krok 2")
   └── Sleduj, či sa chyba opakuje

3. Identifikuj koreňovú príčinu
   ├── Zlý prompt? → Preformuluj
   ├── Chýbajúci kontext? → Pridaj Memory / Prompt Note
   ├── Nedostatočné permissions? → Skontroluj MCP / file access
   ├── Model halucinuje? → Skús iný model / thinking level
   └── Bug v skille? → Oprav skill

4. Oprav a over
   ├── Sprav zmenu (prompt, skill, konfigurácia)
   ├── Spusti znova
   └── Dokumentuj – čo sa stalo a ako si to opravil
```

- **Povedať:** "90 % problémov s agentom sa vyrieši lepším promptom alebo pridaním kontextu do Continual Harness."

#### 7:30–9:00 | Notifikácie a alerting
- **Povedať:** "Nechceš každý deň kontrolovať logy. Chceš, aby ťa agent sám upozornil, keď niečo nie je v poriadku."
- **Čo notifikovať:**

| Situácia | Kanál | Príklad |
|----------|-------|--------|
| Úloha zlyhala | Email / Slack | "⚠️ SEO audit zlyhal: rate limit" |
| Kritický heartbeat problém | SMS / Push | "🔴 Produkčná app je DOWN" |
| Prekročenie budgetu | Email | "💰 Token usage tento mesiac: 120 € (limit 100 €)" |
| Session spadla | Slack / Email | "🔄 Agent session neočakávane skončila" |
| Týždenný sumár | Email | "✅ Týždeň: 47 úloh, 3 chyby, 2.3M tokenov, 18.50 €" |

- **Ukázať implementáciu:**
  ```python
  # V rámci heartbeat-u:
  if error_count > 5:
      await agent_message.send(
          f"⚠️ Kritické: {error_count} chýb za poslednú hodinu!",
          receiver_role="parent"  # notifikuje hlavného agenta
      )
  ```

#### 9:00–10:00 | Best practices a záver
- **Povedať:** "Zhrňme si to: dobrý monitoring je rozdiel medzi 'neviem čo sa deje' a 'presne viem, čo sa deje'. Začni dnes – aj keď len s manuálnou kontrolou logov raz za deň."
- **Minimálny monitoring (deň 1):** denne skontroluj počet úloh, chýb, a tokenov
- **Stredný monitoring (týždeň 2):** pridaj notifikácie pri chybách a týždenný sumár
- **Pokročilý monitoring (mesiac 1):** dashboard, alerty, cost tracking

### Kľúčové body
- 4 dimenzie monitoringu: výkon, náklady, kvalita, zdravie
- Session logy v `~/.prime/agent/session-artifacts/` – JSONL formát
- Debugging flow: prečítaj log → reprodukuj → identifikuj príčinu → oprav → over
- 90 % problémov = lepší prompt alebo chýbajúci kontext v Continual Harness
- Notifikácie: pri chybách okamžite, sumárne týždenne
- Začni s manuálnou kontrolou logov, postupne automatizuj

### Domáca úloha
1. Nájdi a prečítaj si logy z posledných 3 session svojho agenta – čo sa z nich vieš naučiť?
2. Vytvor jednoduchý monitoring skript (Python/bash), ktorý z logov vyčíta: počet úloh, počet chýb, spotrebované tokeny
3. Nastav si aspoň jednu notifikáciu (napr. pri chybe v heartbeate)
4. Veď si denník debuggingu na týždeň: zapisuj si každý problém s agentom, jeho príčinu a riešenie

---

## Lekcia 3: Škálovanie – od 1 agenta k agent tímu
**Dĺžka videa:** 12 minút

### Detailný obsah / scenár

#### 0:00–1:30 | Úvod a hook
- **Povedať:** "Jeden agent je super. Ale čo keď potrebuješ 5 agentov? Alebo 20? Čo keď máš 50 klientov a každý chce svojho dedikovaného agenta? Dnes sa naučíš, ako škálovať od jedného agenta k celému tímu – a orchestrovať ich ako dirigent."
- **Ukázať rýchle demo:** Jeden hlavný agent rozdeľuje úlohy medzi 4 špecializovaných agentov, zbiera výsledky a vytvára report.

#### 1:30–4:00 | Architektúra agent tímu
- **Povedať:** "Poznáš subagentov z Modulu 4. Teraz to posunieme na produkčnú úroveň."
- **Tri úrovne škálovania:**

**Úroveň 1: Sólový agent (súčasný stav)**
  ```
  [Používateľ] → [Prime Agent] → [Výsledok]
  ```
  - Jeden agent, jedna session
  - Vhodné pre: osobné projekty, prototypovanie

**Úroveň 2: Hierarchický tím (Modul 4 + 7)**
  ```
  [Používateľ] → [Hlavný agent (Orchestrátor)]
                      ├── [Subagent: SEO]
                      ├── [Subagent: Content]
                      ├── [Subagent: Sales]
                      └── [Subagent: Support]
  ```
  - Jeden hlavný agent deleguje na špecialistov
  - Vhodné pre: malé firmy, jeden biznis

**Úroveň 3: Multi-agentová platforma (tento modul)**
  ```
  [Používatelia / Systémy]
        │
  [Load Balancer / Fronta úloh]
        │
  ├── [Agent 1: Klient A]
  ├── [Agent 2: Klient B]
  ├── [Agent 3: Monitoring]
  ├── [Agent 4: Reporting]
  └── [Agent 5: Maintenance]
  ```
  - Viacero nezávislých agentov, každý s vlastnou session
  - Centrálne riadenie úloh a monitoring
  - Vhodné pre: agentúry, SaaS platformy, viacero klientov

- **Povedať:** "Dnes sa zameriame na Úroveň 3 – ako prevádzkovať viacero agentov paralelne."

#### 4:00–6:30 | Spúšťanie viacerých agentov súčasne
- **Povedať:** "Prime Agent môžeš spustiť viackrát – každé spustenie je samostatný proces s vlastnou session."
- **Ukázať konkrétne spôsoby:**

**1. Manuálne – viacero terminálových okien**
  ```bash
  # Terminál 1 – SEO agent
  prime-agent --provider deepseek --model deepseek-v4-flash \
    --prompt "Si SEO špecialista. Monitoruj ranking mojastranka.sk..."

  # Terminál 2 – Sales agent
  prime-agent --provider anthropic --model claude-sonnet-4-20250514 \
    --prompt "Si sales agent. Sleduj pipeline v CRM..."
  ```

**2. Automaticky – supervisord / systemd**
  ```ini
  # /etc/supervisor/conf.d/prime-agents.conf
  [program:seo-agent]
  command=prime-agent --provider deepseek --model deepseek-v4-flash --prompt "..."
  directory=/home/user/projects/seo
  autostart=true
  autorestart=true

  [program:sales-agent]
  command=prime-agent --provider anthropic --model claude-sonnet-4-20250514 --prompt "..."
  directory=/home/user/projects/sales
  autostart=true
  autorestart=true
  ```

**3. Docker Compose – izolované prostredia**
  ```yaml
  # docker-compose.yml
  services:
    seo-agent:
      image: prime-agent
      volumes:
        - ./seo:/workspace
      environment:
        - DEEPSEEK_API_KEY=${DEEPSEEK_API_KEY}
      command: prime-agent --provider deepseek --prompt "..."

    sales-agent:
      image: prime-agent
      volumes:
        - ./sales:/workspace
      environment:
        - DEEPSEEK_API_KEY=${DEEPSEEK_API_KEY}
      command: prime-agent --provider deepseek --prompt "..."
  ```

- **Povedať:** "Docker Compose je ideálny pre produkčné nasadenie viacerých agentov. Každý agent má vlastný kontajner, vlastné volume-y, vlastné resources."

#### 6:30–8:30 | Orchestrácia – rozdeľovanie úloh medzi agentov
- **Povedať:** "Keď máš 5 agentov, potrebuješ mechanizmus, ktorý im prideľuje úlohy."
- **Architektúra s frontou úloh:**

  ```
  [Zadávateľ úloh] → [Fronta (Redis/SQLite)] → [Orchestrátor]
                                                     │
                          ┌───────────────────────────┤
                          ▼               ▼           ▼
                      [Agent 1]      [Agent 2]    [Agent 3]
  ```

- **Jednoduchá implementácia so SQLite frontou:**
  ```python
  # orchestrator.py
  import sqlite3, subprocess, time

  conn = sqlite3.connect("task_queue.db")
  conn.execute("""
      CREATE TABLE IF NOT EXISTS tasks (
          id INTEGER PRIMARY KEY,
          task_type TEXT,
          prompt TEXT,
          status TEXT DEFAULT 'pending',
          agent_id TEXT,
          created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
      )
  """)

  while True:
      task = conn.execute(
          "SELECT * FROM tasks WHERE status='pending' LIMIT 1"
      ).fetchone()

      if task:
          if task[1] == "seo":
              subprocess.Popen(["prime-agent", "--prompt", task[2]])
              conn.execute(
                  "UPDATE tasks SET status='running', agent_id='seo-1' WHERE id=?",
                  (task[0],)
              )

      time.sleep(5)
  ```

- **Povedať:** "Toto je základný dispatcher. V produkcii by si použil Redis/ RabbitMQ s acknowledgements, retry logikou a dead letter queue."

#### 8:30–10:30 | Multi-tenant – agenti pre viacerých klientov
- **Povedať:** "Ak prevádzkuješ agentúru alebo SaaS, potrebuješ izolovaných agentov pre každého klienta."
- **Kľúčové princípy multi-tenancy:**

**1. Izolácia:**
  - Každý klient = vlastné pracovné adresáre
  - Každý klient = vlastný Continual Harness (memories, skills, prompt notes)
  - Každý klient = vlastné API kľúče (nikdy nezdieľať!)
  ```
  /data/clients/
  ├── klient-a/
  │   ├── workspace/
  │   ├── .prime-agent/
  │   └── config.yaml
  ├── klient-b/
  │   ├── workspace/
  │   ├── .prime-agent/
  │   └── config.yaml
  ```

**2. Billing a monitoring per klient:**
  - Každý klient = vlastný tracking tokenov a nákladov
  - Mesačný report: "Váš agent spravil X úloh, minul Y tokenov, ušetril Z hodín"

**3. Templatizácia:**
  - Nepíš agenta pre každého klienta od nuly
  - Vytvor šablónu → klonuj pre nového klienta
  - Príklad: `prime-agent-setup --template ecommerce --client "Klient A"`

- **Povedať:** "Agent-as-a-Service je reálny biznis model. Ty poskytuješ agenta, klient platí mesačný poplatok."

#### 10:30–12:00 | Best practices a záver
- **Povedať:** "Škálovanie agentov – čo si zapamätať:"
  - **Začni s 1 agentom** – nepreškáluj predčasne
  - **Pridaj druhého, až keď prvý beží stabilne aspoň 2 týždne**
  - **Docker Compose je tvoj priateľ** – izolácia, reproducibilita, jednoduchá správa
  - **Fronta úloh** – nikdy nespúšťaj agentov "naslepo", vždy cez orchestrátor
  - **Monitoring per agent** – každý agent by mal reportovať svoje metriky

- **Povedať:** "V ďalšej lekcii sa pozrieme do budúcnosti – kam smerujú AI agenti a čo to znamená pre tvoj biznis."

### Kľúčové body
- 3 úrovne škálovania: sólový agent → hierarchický tím → multi-agentová platforma
- Viacero agentov: manuálne (terminály), supervisord/systemd, Docker Compose
- Orchestrácia: fronta úloh (Redis/SQLite) + dispatcher
- Multi-tenant: izolované adresáre, Continual Harness per klient, vlastné API kľúče
- Agent-as-a-Service = reálny biznis model
- Pravidlo: škáluj až keď to potrebuješ – začni s 1 agentom

### Domáca úloha
1. Spusti 2 agentov súčasne (napr. jeden SEO, jeden sales) a nechaj ich bežať aspoň 1 hodinu
2. Vytvor jednoduchú frontu úloh (SQLite) a dispatcher, ktorý rozdeľuje úlohy medzi agentov
3. Ak používaš Docker, vytvor `docker-compose.yml` pre 2 agentov
4. Napíš krátky plán: ako by si využil multi-agentovú platformu pre svoj biznis (alebo svojich klientov)?

---

## Lekcia 4: Budúcnosť AI agentov a tvoj biznis
**Dĺžka videa:** 8 minút

### Detailný obsah / scenár

#### 0:00–1:30 | Úvod a hook
- **Povedať:** "Počas tohto kurzu si sa naučil ovládať Prime Agenta. Ale toto je len začiatok. AI agenti sú na prahu revolúcie – rovnako veľkej, ako bol internet v 90-tych rokoch alebo smartfóny v 2007. Dnes sa pozrieme, kam to celé smeruje."
- **Ukázať citát:** "AI agents will be bigger than SaaS." – Satya Nadella, Microsoft CEO

#### 1:30–3:30 | Trendy, ktoré definujú budúcnosť
- **Povedať:** "5 trendov, ktoré formujú budúcnosť AI agentov:"

**1. Modely sú stále lacnejšie a schopnejšie**
  - 2023: GPT-4 = $30/M tokenov
  - 2024: Claude 3.5 = $15/M, DeepSeek = $1.5/M
  - 2025: DeepSeek-v4, open-source modely na úrovni GPT-4
  - 2026?: Modely za <$0.50/M – agenti budú lacnejší ako ľudská práca

**2. Agenti preberajú celé pracovné roly**
  - Dnes: "agent, napíš mi tento kód"
  - Zajtra: "agent, spravuj celý môj marketing"
  - Pozajtra: "agent, veď moju firmu"
  - Už dnes: Devin (Cognition AI) – prvý AI software engineer za $500/mesiac

**3. Multi-agentové systémy**
  - Jeden agent je dobrý. Tím agentov je revolučný.
  - Špecializácia + spolupráca = schopnosti prevyšujúce akéhokoľvek jednotlivca
  - Príklad: ChatDevin – tím AI agentov, ktorí spolu vyvíjajú softvér

**4. Agent-native aplikácie**
  - Dnes: App-ky s API → agenti sa na ne napájajú
  - Zajtra: App-ky navrhnuté pre agentov ako primárnych používateľov
  - MCP štandard toto umožňuje

**5. Regulácia a etika**
  - EU AI Act, US Executive Orders
  - Transparentnosť, accountability, bezpečnosť
  - "Kto je zodpovedný, keď agent spraví chybu?" – otázka, ktorú bude riešiť celý svet

#### 3:30–5:00 | Čo to znamená pre tvoje podnikanie
- **Povedať:** "Nie si vývojár? Nevadí. AI agenti menia pravidlá hry pre každého podnikateľa."
- **Tri scenáre:**

**Scenár A: Si freelancer / konzultant**
  - Agent = tvoj junior partner, ktorý pracuje kým ty spíš
  - Zvýšiš kapacitu 5-10x bez náboru
  - Môžeš si dovoliť viac klientov pri rovnakej kvalite
  - **Akcia:** Vytvor balíček "Marketing na autopilota" pre klientov

**Scenár B: Si majiteľ SaaS / e-commerce**
  - Agent = tvoj prevádzkový riaditeľ
  - Automatizovaný support, marketing, sales, monitoring
  - Náklady na operácie klesajú, kvalita rastie
  - **Akcia:** Identifikuj 3 procesy, ktoré vieš odovzdať agentovi DO KONCA TOHTO TÝŽDŇA

**Scenár C: Si agentúra / studio**
  - Agenti = tvoja nová "pracovná sila"
  - Ponúkaj "Agent-as-a-Service" balíčky klientom
  - Spravuj desiatky agentov pre desiatky klientov
  - **Akcia:** Vytvor pilotný projekt pre 1 klienta – ukáž mu, čo agent dokáže

- **Povedať:** "Bez ohľadu na to, v akej si fáze – kľúčové je začať DNES. Konkurencia nespí."

#### 5:00–6:30 | Ako zostať relevantný v ére agentov
- **Povedať:** "Agenti nás nenahrádzajú. Nahrádzajú tých, ktorí agentov nepoužívajú."
- **5 krokov, ako si udržať náskok:**

1. **Buď AI-native** – agenta používaj denne. Nech je to tvoj druhý mozog.
2. **Uč sa prompt engineering** – schopnosť presne povedať agentovi čo chceš je nová "gramotnosť"
3. **Build automation** – každý opakovaný proces odovzdaj agentovi
4. **Špecializuj sa** – agenti zvládnu generické úlohy. Ty buď expert na svoju doménu.
5. **Mysli na systémovej úrovni** – nenahrádzaj človeka agentom. Navrhni systém, kde agenti a ľudia spolupracujú.

- **Povedať:** "O 5 rokov bude 'AI agent skills' rovnako bežná požiadavka v CV ako 'Excel' dnes. Buď vpredu."

#### 6:30–8:00 | Vízia a záver
- **Povedať:** "Kam to celé smeruje?"
- **Vízia na 3-5 rokov:**
  - Každý živnostník má svojho AI agenta (ako dnes každý používa smartfón)
  - Firmy prevádzkujú tímy agentov namiesto juniorných pozícií
  - "Agent director" je nová pracovná pozícia – človek, ktorý riadi tím agentov
  - Cena agenta = cena Netflix účtu (masová adopcia)
- **Povedať:** "Ty si v tomto bode – po 8 moduloch – v top 1 % ľudí, ktorí naozaj rozumejú AI agentom. Nie na teoretickej úrovni. Na praktickej. Vieš agenta nainštalovať, nakonfigurovať, naučiť nové skilly, delegovať na subagentov, napojiť na API, a prevádzkovať v produkcii."
- **Povedať:** "V záverečnej lekcii to celé spojíme do jedného projektu. Tvojho vlastného biznisu na autopilota."

### Kľúčové body
- 5 trendov: lacnejšie modely, agenti ako pracovné roly, multi-agent systémy, agent-native appky, regulácia
- 3 scenáre pre tvoj biznis: freelancer, SaaS majiteľ, agentúra
- Kľúčové je začať DNES – konkurencia nespí
- 5 krokov: AI-native, prompt engineering, automatizácia, špecializácia, systémové myslenie
- O 5 rokov: AI agent skills = nový Excel v CV

### Domáca úloha
1. Napíš si svoju 12-mesačnú víziu: ako budeš používať AI agentov vo svojom biznise? Aké procesy odovzdáš agentom?
2. Identifikuj 3 konkrétne procesy, ktoré vieš agentovi odovzdať DO KONCA TOHTO TÝŽDŇA – začni s jedným hneď dnes
3. Prečítaj si aspoň 2 články o budúcnosti AI agentov (napr. od Andreessen Horowitz, Sequoia Capital, alebo Anthropic)
4. Napíš si "AI Agent Manifesto" – 5 princípov, ktorými sa budeš pri používaní agentov riadiť

---

## Lekcia 5: Záverečný projekt – Vlastný biznis na autopilota
**Dĺžka videa:** 5 minút

### Detailný obsah / scenár

#### 0:00–1:00 | Úvod – čo ideme postaviť
- **Povedať:** "Toto je vyvrcholenie celého kurzu. Za posledných 8 modulov si sa naučil všetko potrebné. Teraz to spojíme do jedného projektu – tvojho vlastného biznisu, ktorý beží na autopilota."
- **Povedať:** "Nechceme prototyp. Chceme produkčný systém. Niečo, čo reálne generuje hodnotu – leadov, tržby, obsah, support – kým ty spíš, cvičíš, alebo buduješ ďalší projekt."
- **Ukázať schému systému, ktorý študent postaví:**

```
                    ┌──────────────────────────────┐
                    │     TVOJ BIZNIS NA AUTOPILOTA │
                    └──────────────────────────────┘
                                    │
        ┌───────────────┬───────────┼───────────┬───────────────┐
        ▼               ▼           ▼           ▼               ▼
   ┌─────────┐   ┌─────────┐  ┌─────────┐  ┌─────────┐   ┌─────────┐
   │ MARKETING│   │  SALES  │  │ SUPPORT │  │ANALYTICS│   │ MONITOR │
   │ Agent    │   │ Agent   │  │ Agent   │  │ Agent   │   │ Agent   │
   └─────────┘   └─────────┘  └─────────┘  └─────────┘   └─────────┘
        │               │           │           │               │
   ┌────┴────┐    ┌────┴────┐ ┌───┴────┐ ┌───┴────┐     ┌────┴────┐
   │SEO audit│    │Prospect │ │Ticket  │ │Týždenný│     │Health   │
   │Content  │    │Cold     │ │triage  │ │report   │     │checks   │
   │Social   │    │email    │ │FAQ       │ │Forecast│     │Alerts   │
   │Email    │    │Follow-up│ │Eskalácia│ │Grafy    │     │Logs     │
   └─────────┘    └─────────┘  └─────────┘ └─────────┘     └─────────┘
```

#### 1:00–2:30 | Čo presne postavíš
- **Povedať:** "Poďme si definovať, čo presne bude tvoj systém obsahovať."

**Minimálny životaschopný systém (MVP):**
- [ ] **1 hlavný agent** – orchestrátor, ktorý riadi všetky úlohy
- [ ] **Marketingová automatizácia** – aspoň 2 z týchto: SEO audit, blog post, social media post, email kampaň
- [ ] **Predajná automatizácia** – aspoň 1 z týchto: prospecting, cold outreach, follow-up sekvencia
- [ ] **Support automatizácia** – aspoň 1 z týchto: ticket triage, FAQ odpovede, analýza ticketov
- [ ] **1 naplánovaná úloha** (cron) – napr. týždenný report
- [ ] **1 heartbeat** – napr. pipeline monitoring
- [ ] **Continual Harness** – aspoň 3 memories a 2 prompt notes
- [ ] **Bezpečnostný checklist** – splnený aspoň na 80 %

**Pokročilý systém (ak máš hotový MVP):**
- [ ] MCP integrácia (Google Workspace, Slack, vlastné API)
- [ ] Multi-agent setup (2+ agenti v Docker Compose)
- [ ] Monitoring dashboard
- [ ] Human-in-the-loop schvaľovanie

#### 2:30–4:00 | Postup – krok za krokom
- **Povedať:** "Ako postaviť tento systém za 5 dní:"

**Deň 1: Základy**
  - Vytvor Continual Harness pre svoj biznis (memories, prompt notes)
  - Definuj ICP a produktový kontext
  - Spusti prvú manuálnu úlohu (napr. SEO audit)

**Deň 2: Marketingová a predajná automatizácia**
  - Spusti SEO audit + vygeneruj 1 blog post
  - Spusti prospecting pre svoje ICP
  - Vygeneruj cold emaily pre nájdených leadov
  - Nastav prvý cron job (napr. týždenný SEO report)

**Deň 3: Support a monitoring**
  - Vytvor knowledge base pre support agenta
  - Otestuj ticket triage na vzorových ticketoch
  - Nastav heartbeat pre pipeline monitoring
  - Implementuj human-in-the-loop pre odosielanie emailov

**Deň 4: Bezpečnosť a integrácie**
  - Sprav bezpečnostný audit podľa checklist-u
  - Nastav `.env` a Docker (ak používaš)
  - Pridaj MCP Connection (napr. Google Workspace)
  - Otestuj celý flow end-to-end

**Deň 5: Finalizácia a dokumentácia**
  - Spusti kompletný systém a nechaj ho bežať 2-4 hodiny
  - Skontroluj logy a oprav chyby
  - Zdokumentuj svoj setup (čo beží, kedy, prečo)
  - **Povedať:** "Tento dokument je tvoj 'operator's manual' – keď o 3 mesiace zabudneš, čo si postavil, presne vieš, kde nájsť odpovede."

#### 4:00–5:00 | Záver kurzu
- **Povedať:** "Gratulujem! Práve si dokončil Prime Agent Masterclass."
- **Rekapitulácia toho, čo si sa naučil:**
  - **Modul 1:** Čo je AI agent, inštalácia, prvé spustenie
  - **Modul 2:** IPython kernel, shell príkazy, práca so súbormi, prompt engineering
  - **Modul 3:** Skills ekosystém, markdown a Python skilly, custom skill development
  - **Modul 4:** Subagenti, delegovanie, komunikácia, hierarchické tímy
  - **Modul 5:** Marketingová automatizácia – SEO, copywriting, social, emails, prieskum
  - **Modul 6:** Predaj a support – prospecting, cold outreach, support agent, analýza, follow-up
  - **Modul 7:** Pokročilé techniky – MCP, Continual Harness, scheduling, API, Heartbeats
  - **Modul 8:** Produkčné nasadenie, bezpečnosť, monitoring, škálovanie, budúcnosť
- **Povedať:** "Si pripravený. Zvyšok je na tebe."
- **Povedať:** "Tri veci, ktoré si odnes:"
  1. **Konaj** – každý deň, keď nepoužívaš agenta, je deň, keď tvoja konkurencia áno
  2. **Iteruj** – tvoj prvý setup nebude dokonalý. To je v poriadku. Spusti, uč sa, vylepši.
  3. **Zdieľaj** – pomôž ostatným. Napíš o svojich skúsenostiach. Vybuduj si reputáciu AI-native profesionála.
- **Povedať:** "Vitaj v budúcnosti. Budúcnosť, ktorú si práve postavil."

### Kľúčové body
- Záverečný projekt = kompletný biznis na autopilota s 5 agentmi (marketing, sales, support, analytics, monitoring)
- MVP checklist: 8 položiek, ktoré musí systém spĺňať
- 5-dňový plán výstavby: základy → marketing a sales → support → bezpečnosť → finalizácia
- Víťazný mindset: konaj, iteruj, zdieľaj
- Absolvoval si 8 modulov a ovládaš Prime Agenta na expertnej úrovni

### Domáca úloha – Záverečný projekt
1. Postav svoj vlastný biznis na autopilota podľa MVP checklist-u (8 položiek)
2. Nechaj systém bežať aspoň 24 hodín a zdokumentuj výsledky (koľko úloh spravil, koľko tokenov minul, aké boli výstupy)
3. Napíš krátku "case study" (1-2 strany): čo si postavil, čo fungovalo, čo si sa naučil, čo plánuješ ďalej
4. Zdieľaj svoj projekt s komunitou (Discord, LinkedIn, Twitter) – taguj @PrimeIntellect

---

*Koniec Modulu 8 – a koniec Prime Agent Masterclass. 🎉*

---

*Vitaj v budúcnosti. Tvoj agent čaká.*
