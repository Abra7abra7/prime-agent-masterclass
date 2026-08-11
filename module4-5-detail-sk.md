# Prime Agent Masterclass – Modul 4: Subagenti a delegovanie

## Prehľad modulu

**Cieľ modulu:** Po absolvovaní tohto modulu budeš vedieť vytvárať hierarchické tímy agentov, delegovať komplexné úlohy na špecializované podjednotky, spúšťať ich paralelne a zbierať od nich výsledky. Toto je jadro škálovania – namiesto jedného agenta, ktorý robí všetko, budeš mať armádu špecialistov.

**Celková dĺžka:** 50 minút videa + domáce úlohy

---

## Lekcia 1: Čo sú subagenti a kedy ich použiť
**Dĺžka videa:** 8 minút

### Detailný obsah / scenár

#### 0:00–1:00 | Úvod a metafora
- **Povedať:** „Predstav si, že si CEO firmy. Nerobíš účtovníctvo, marketing, predaj aj vývoj sám – najímaš na to špecialistov. Prime Agent funguje rovnako. Ty si hlavný agent a na konkrétne úlohy si zavoláš subagenta."
- **Vizuál:** Ukázať jednoduchý diagram hierarchie:
  ```
  Hlavný agent (ty / orchestrátor)
    ├── Subagent 1: SEO audit
    ├── Subagent 2: Prieskum konkurencie
    └── Subagent 3: Copywriting
  ```
- **Povedať:** „Toto nie je teória – o 50 minút budeš mať spustenú content factory s 5 agentmi naraz."

#### 1:00–2:30 | Architektúra subagentov v Prime Agentovi
- **Povedať:** „Subagent je plnohodnotný Prime Agent spustený z tvojho hlavného agenta. Má vlastný IPython kernel, vlastný kontext, vlastné tools."
- **Kľúčové vlastnosti subagenta:**
  - **Izolovaný kontext** – subagent nevidí tvoju konverzáciu, dostane len task prompt
  - **Vlastné tools** – všetky skilly, ktoré má hlavný agent, má aj subagent
  - **Rodičovská komunikácia** – subagent vie posielať správy iba rodičovi, súrodencom a vlastným deťom
  - **Session per subagent** – každý subagent má vlastný session súbor v `/Users/<user>/.prime/agent/session-artifacts/`
- **Ukázať na obrazovke:** Otvoriť session artifacts priečinok a ukázať štruktúru:
  ```bash
  ls ~/.prime/agent/session-artifacts/
  # 019feced-c48b-7089-a9be-e5940b210111/
  #   sub-e0e633eb/
  #     ...
  ```

#### 2:30–4:30 | Subagent vs. Skill – kedy použiť čo
- **Povedať:** „Toto je najčastejšia otázka: Mám na to použiť skill alebo subagenta?"
- **Ukázať porovnávaciu tabuľku na slide:**

| Kritérium | Skill | Subagent |
|-----------|-------|----------|
| Trvanie úlohy | Sekundy–minúty | Minúty–hodiny |
| Komplexita | Jeden jasný krok | Viacero rozhodnutí a iterácií |
| Kontext | Zdieľa kontext rodiča | Vlastný izolovaný kontext |
| Paralelizmus | Nie | Áno – viacero naraz |
| Výsledok | Return value / súbor | Správa cez `agent_message` |
| Príklad | `websearch("query")` | „Urob kompletný SEO audit tejto domény" |

- **Povedať:** „Skill je funkcia. Subagent je kolega. Ak úloha vyžaduje samostatné rozmýšľanie, iterovanie a viacero krokov – potrebuješ subagenta."
- **Konkrétne príklady:**
  - ✅ Subagent: „Preskúmaj 5 konkurentov, sprav SWOT analýzu každého a vráť zhrnutie"
  - ✅ Subagent: „Napíš 10 LinkedIn príspevkov na základe tejto content stratégie"
  - ❌ Subagent (zbytočné): „Vyhľadaj 'Prime Agent tutorial' na webe" → toto je 1 volanie `websearch`

#### 4:30–6:30 | Hierarchia a rodokmeň agentov
- **Povedať:** „Prime Agent používa stromovú štruktúru. Hlavný agent je koreň. Každý subagent môže vytvárať vlastných subagentov."
- **Ukázať diagram hlbšej hierarchie:**
  ```
  Hlavný agent
    ├── Subagent A: Marketingová stratégia
    │     ├── Subagent A1: SEO audit
    │     └── Subagent A2: Content plán
    └── Subagent B: Technická analýza
          ├── Subagent B1: Code review
          └── Subagent B2: Performance audit
  ```
- **Povedať:** „Dôležité pravidlo: subagent vidí iba svojho rodiča, svojich súrodencov a svoje deti. Nie starých rodičov, nie bratrancov. Toto je zámer – udržuje to kontext čistý."
- **Ukázať v kóde koncept rodiny:**
  ```python
  # Z pohľadu Subagenta A1:
  # Rodič: Subagent A (môže mu posielať správy)
  # Súrodenci: Subagent A2 (môže mu posielať správy)
  # Deti: vlastné subagenty (môže im posielať správy)
  # Subagent B1: NEDOSTUPNÝ (bratranec – mimo dosahu)
  ```

#### 6:30–8:00 | Best practices a anti-patterny
- **Povedať:** „Pár rád, kým začneme kódovať:"
- **DOs:**
  - ✅ Daj subagentovi jasný, ohraničený cieľ („Urob X a vráť Y")
  - ✅ Jeden subagent = jedna zodpovednosť
  - ✅ Používaj paralelné spúšťanie keď úlohy nie sú závislé
  - ✅ Subagent nech posiela výsledky priebežne, nie až na konci
- **DON'Ts:**
  - ❌ Nevytváraj subagenta na 1 volanie skillu
  - ❌ Nečakaj, že subagent „uvidí" tvoje premenné z kernelu
  - ❌ Neposielaj subagentovi obrovský prompt (má vlastný context window)
  - ❌ Nezabúdaj, že subagent musí explicitne poslať výsledok – sám sa nevráti
- **Povedať:** „Najväčšia chyba začiatočníkov: vytvoriť subagenta a čakať, že sa výsledok objaví. Subagent ti musí správu POSLAŤ. Ak to neurobí, nikdy sa nič nedozvieš."

### Kľúčové body
- Subagent je plnohodnotný Prime Agent s vlastným kernelom a kontextom
- Skill = funkcia (sekundy), Subagent = kolega (minúty/hodiny)
- Hierarchia je stromová – agent vidí len rodiča + súrodencov + deti
- Každý subagent musí explicitne odoslať výsledok cez `agent_message.send()`
- Nepoužívaj subagenta na triviálne jednokrokové úlohy

### Domáca úloha
1. Nakresli si na papier hierarchický strom agentov pre svoj vysnívaný projekt. Koľko úrovní by si potreboval? Akých špecialistov?
2. Pre každú z týchto úloh rozhodni: skill alebo subagent? a) Zisti počasie v Bratislave, b) Napíš kompletný blog post s researchom, c) Prečítaj súbor config.yaml, d) Urob prieskum 3 konkurentov a vráť porovnávaciu tabuľku
3. Preštuduj si dokumentáciu `agent_message` skillu: otvor v termináli `cat ~/.npm-global/lib/node_modules/prime-agent/dist/skills/agent-message/SKILL.md` a prečítaj si ju celú

---

## Lekcia 2: Spúšťanie a riadenie subagentov
**Dĺžka videa:** 12 minút

### Detailný obsah / scenár

#### 0:00–1:30 | Spustenie prvého subagenta – Live Demo
- **Povedať:** „Dosť teórie. Poďme spustiť prvého subagenta."
- **Ukázať na obrazovke:** Otvoriť Prime Agent session, prejsť do IPython kernelu.
- **Napísať a spustiť:**
  ```python
  # Vytvorenie subagenta z IPython kernelu
  handle = await rlm('Urob SEO audit domény example.com a vráť top 5 odporúčaní')
  ```
- **Povedať:** „Pozri, čo sa vrátilo. Všimnite si – nevrátil sa výsledok SEO auditu. Vrátil sa HANDLE."
- **Ukázať návratovú hodnotu:**
  ```python
  print(handle)
  # {
  #   'rlm_child_id': '019fed18-...',
  #   'name': 'prime-agent-child-abc123',
  #   'session_dir': '/Users/.../sub-e0e633eb',
  #   'model': 'deepseek-v4-flash'
  # }
  ```
- **Povedať:** „`rlm()` vráti handle okamžite. Subagent beží na pozadí. Toto je kľúčový moment – ty a subagent teraz pracujete paralelne."

#### 1:30–3:00 | Anatómia task promptu pre subagenta
- **Povedať:** „Kvalita task promptu rozhoduje o kvalite výstupu. Subagent nemá kontext tvojej konverzácie – všetko, čo vie, je v tom jednom prompte."
- **Ukázať zlý prompt:**
  ```
  "Preskúmaj konkurenciu"
  ```
  - **Povedať:** „Čo presne? Ktorú konkurenciu? Aký formát výstupu? Ako to mám vrátiť? Toto je recept na zmätok."
- **Ukázať dobrý prompt:**
  ```
  "Si marketingový analytik. Preskúmaj týchto 3 konkurentov:
  - konkurent1.com
  - konkurent2.com
  - konkurent3.com

  Pre každého zistí: pricing, hlavné features, cieľovú skupinu, tone of voice.
  Výstup vráť ako markdown tabuľku.
  Keď skončíš, pošli výsledok rodičovi cez:
  await agent_message.send(vysledok, receiver_role='parent')"
  ```
- **Povedať:** „Všimni si 4 zložky dobrého promptu: 1) Rola, 2) Presný scope, 3) Formát výstupu, 4) Inštrukcia na odoslanie."

#### 3:00–5:00 | Sledovanie a čakanie na subagenta
- **Povedať:** „Ako zistíš, čo tvoj subagent robí?"
- **Ukázať 3 spôsoby monitoringu:**
- **Spôsob 1: `agent_observe`**
  ```python
  # Zoznam všetkých priamych detí
  children = await rlm.list_subagents()
  print(children)

  # Pozorovanie konkrétneho subagenta
  import agent_observe
  status = await agent_observe.observe_child(handle['name'])
  print(status)  # 'running', 'idle', 'completed', atď.
  ```
- **Spôsob 2: Čítanie logov**
  ```python
  import os
  session_dir = handle['session_dir']
  # Pozri konverzačný log subagenta
  log_files = os.listdir(session_dir)
  print(log_files)
  ```
- **Spôsob 3: `agent_message` – čakanie na správu**
  ```python
  # Subagent pošle výsledok a ty ho zachytíš
  # Toto sa deje automaticky – keď subagent zavolá send(),
  # správa sa objaví v tvojom kontexte
  ```

#### 5:00–7:30 | Lifecycle subagenta – od spustenia po výsledok
- **Povedať:** „Poďme si prejsť kompletný životný cyklus subagenta."
- **Ukázať timeline diagram:**
  ```
  [Rodič]           [Subagent]
    |                   |
    |-- rlm('úloha') -->|
    |   (handle späť)   |
    |                   |-- Číta task prompt
    |                   |-- Plánuje kroky
    |   (paralelne      |-- Spúšťa tools
    |    môže robiť     |-- Iteruje
    |    iné veci)      |-- Kompletizuje výsledok
    |                   |
    |<-- agent_message -|
    |   .send(výsledok) |
    |                   |
    |-- Spracuje        |-- Idle (čaká na ďalšiu úlohu
    |   výsledok        |    alebo sa ukončí)
  ```
- **Povedať:** „Kľúčový insight: rodič a subagent bežia PARALELNE. Kým subagent robí SEO audit, ty môžeš spúšťať ďalších subagentov alebo robiť niečo iné."
- **Ukázať praktický príklad:**
  ```python
  # Spustím subagenta
  seo_handle = await rlm('Urob SEO audit domény example.com')

  # Kým beží, robím niečo iné v mojom kerneli
  print("Subagent beží, ja medzitým...")
  # napr. sťahujem dáta, čítam súbory, atď.

  # Neskôr skontrolujem, či subagent poslal výsledok
  ```

#### 7:30–9:00 | Riadenie viacerých subagentov – fronta úloh
- **Povedať:** „Keď máš viac subagentov, potrebuješ ich organizovať."
- **Ukázať pattern s dictionary:**
  ```python
  # Udržiavaj si mapu subagentov
  subagents = {}

  # Spusti viacero subagentov
  subagents['seo'] = await rlm('Urob SEO audit mojastranka.sk')
  subagents['social'] = await rlm('Napíš 5 LinkedIn príspevkov o AI')
  subagents['email'] = await rlm('Vytvor welcome email sekvenciu')

  # Neskôr – skontroluj stav všetkých
  for name, handle in subagents.items():
      print(f"{name}: {handle['session_dir']}")
  ```
- **Povedať:** „Toto je základný pattern – uchovávaš si handly a neskôr zbieraš výsledky."

#### 9:00–10:30 | Ako subagent vie, že má skončiť
- **Povedať:** „Dôležitý detail: subagent neskončí automaticky po vykonaní úlohy. Musí explicitne skončiť – buď odoslaním výsledku a ukončením, alebo čakaním na ďalšie inštrukcie."
- **Ukázať rozdiel:**
  ```python
  # Vo vnútri subagenta:
  # Verzia A: Pošlem výsledok a ďalej neriešim
  await agent_message.send("Hotovo, tu je výsledok...", receiver_role="parent")
  # Subagent ide do idle – čaká na ďalšiu správu od rodiča

  # Verzia B: Pošlem výsledok a explicitne skončím
  await agent_message.send("Hotovo, tu je výsledok...", receiver_role="parent")
  # Subagent sa ukončí (session sa uzavrie)
  ```
- **Povedať:** „V praxi Verzia A je častejšia – umožňuje ti poslať subagentovi follow-up: 'Super, ešte mi k tomu pridaj X'."

#### 10:30–12:00 | Debugging – keď subagent nevráti výsledok
- **Povedať:** „Čo keď subagent mlčí? Tu je checklist:"
- **Checklist 4 krokov:**
  1. **Skontroluj logy:** `ls <session_dir>` – existuje konverzačný log?
  2. **Skontroluj prompt:** Mal subagent v prompte inštrukciu `await agent_message.send(...)`?
  3. **Manuálne pošli správu:** `await agent_message.send("Ešte žiješ? Pošli priebežný status.", receiver_role="child", receiver_name=handle['name'])`
  4. **Timeout a retry:** Ak subagent nereaguje ani na follow-up, spusti nového s lepším promptom
- **Ukázať praktický debugging:**
  ```python
  # Pošli follow-up subagentovi
  await agent_message.send(
      "Ako pokračuješ? Pošli mi, čo si doteraz zistil.",
      receiver_role="child",
      receiver_name=handle['name']
  )
  ```

### Kľúčové body
- `rlm('úloha')` vráti handle okamžite, subagent beží paralelne
- Task prompt musí obsahovať: rolu, scope, formát výstupu, inštrukciu na odoslanie
- Subagenta monitoruješ cez `agent_observe`, `rlm.list_subagents()`, alebo čítanie logov
- Subagent musí explicitne poslať výsledok – sám sa k tebe nedostane
- Keď subagent mlčí: logy → follow-up správa → retry

### Domáca úloha
1. Spusti svojho prvého subagenta: `await rlm('Nájdi 5 najnovších správ o AI agentoch a vráť ich ako zoznam s URL')` a počkaj na výsledok
2. Experimentuj s rôznymi task promptmi: vyskúšaj príliš vágny, príliš široký a optimálny. Porovnaj výsledky.
3. Spusti 2 subagentov naraz a kým bežia, sprav niečo iné v kerneli. Nauč sa paralelne pracovať.

---

## Lekcia 3: Paralelné spracovanie – viac agentov naraz
**Dĺžka videa:** 10 minút

### Detailný obsah / scenár

#### 0:00–1:30 | Prečo paralelizmus mení hru
- **Povedať:** „Jeden agent = jeden výsledok za 5 minút. Päť agentov paralelne = päť výsledkov za 5 minút. Toto je násobič tvojej produktivity."
- **Ukázať porovnanie:**
  ```
  Sekvenčne:
  [SEO audit: 8 min] → [Content: 10 min] → [Social: 6 min] → [Email: 7 min]
  Celkom: 31 minút

  Paralelne:
  [SEO audit: 8 min]
  [Content: 10 min]
  [Social: 6 min]      = Celkom: 10 minút (najdlhšia úloha)
  [Email: 7 min]
  ```
- **Povedať:** „31 minút vs 10 minút. 3x rýchlejšie. A čím viac agentov, tým väčší rozdiel."
- **Vizuál:** Ukázať Ganttov diagram paralelného vs sekvenčného spracovania.

#### 1:30–3:30 | Spustenie viacerých subagentov naraz – Live Demo
- **Povedať:** „Poďme spustiť 4 subagentov naraz."
- **Ukázať na obrazovke – krok za krokom:**
  ```python
  import asyncio

  # Definuj tasky
  tasks = {
      'seo': 'Urob SEO audit domény mojastranka.sk. Vráť top 5 problémov.',
      'copy': 'Napíš landing page pre SaaS produkt "Prime Agent Masterclass".',
      'social': 'Vytvor 5 LinkedIn príspevkov o AI agentoch pre vývojárov.',
      'research': 'Preskúmaj 3 konkurenčné kurzy AI agentov a vráť porovnanie.'
  }

  # Spusti všetky naraz (každý v samostatnom rlm() volaní)
  handles = {}
  for name, task in tasks.items():
      handles[name] = await rlm(task)
      print(f"✅ Spustený: {name}")

  print(f"\n🚀 Všetci {len(handles)} subagenti bežia paralelne!")
  ```
- **Povedať:** „Pozri sa na to – všetky 4 handly sa vrátili okamžite. Teraz všetci 4 agenti pracujú SÚČASNE."

#### 3:30–5:30 | Zbieranie výsledkov z paralelných subagentov
- **Povedať:** „Ako pozbieraš výsledky, keď každý subagent skončí v inom čase?"
- **Ukázať pattern s pollingom:**
  ```python
  import time

  # Jednoduchý polling – kontroluj, či prišli správy
  results = {}
  timeout = 600  # 10 minút max

  start = time.time()
  while len(results) < len(handles) and (time.time() - start) < timeout:
      # Skontroluj každého subagenta
      for name, handle in handles.items():
          if name not in results:
              # Skús prečítať log subagenta (zjednodušené)
              session_dir = handle['session_dir']
              # ... kontrola výstupu ...
              pass
      time.sleep(10)  # Počkaj 10s pred ďalšou kontrolou

  print(f"Zozbieraných {len(results)}/{len(handles)} výsledkov")
  ```
- **Povedať:** „V praxi nemusíš pollingovať – Prime Agent daemon ti doručí správy od subagentov automaticky. Ale je dobré rozumieť mechanizmu."

#### 5:30–7:00 | Fan-out / Fan-in pattern
- **Povedať:** „Toto je najdôležitejší pattern pre paralelných agentov. Volá sa Fan-out / Fan-in."
- **Ukázať diagram:**
  ```
  FAN-OUT (distribúcia):
        Hlavný agent
       /    |    \    \
    SEO   Copy  Social  Research

  FAN-IN (zber výsledkov):
    SEO   Copy  Social  Research
       \    |    |    /
        Hlavný agent
             |
        Finálny výstup
  ```
- **Ukázať implementáciu:**
  ```python
  # FAN-OUT
  subtasks = ['audit', 'content', 'social', 'research']
  handles = {}
  for task in subtasks:
      handles[task] = await rlm(f'Urob {task} pre projekt X')

  # ... agenti pracujú paralelne ...

  # FAN-IN (keď všetci skončia)
  final_output = {}
  for name, handle in handles.items():
      # Spracuj výsledok od každého subagenta
      final_output[name] = f"Výsledok od {name}"

  # Teraz môžeš výsledky skombinovať
  combined = "\n\n".join(final_output.values())
  ```

#### 7:00–9:00 | Závislosti a orchestration patterns
- **Povedať:** „Nie všetky úlohy sú nezávislé. Niekedy subagent B potrebuje výstup subagenta A."
- **Ukázať 3 orchestračné patterny:**

**Pattern 1: Sekvenčný reťazec**
```python
# A → B → C
a_result = await rlm('Urob research')  # Počkaj na A
# Extrahuj výsledok z A
b_result = await rlm(f'Na základe tohto researchu: {a_result}, napíš content stratégiu')
c_result = await rlm(f'Na základe stratégie: {b_result}, vytvor obsahový kalendár')
```

**Pattern 2: Paralelný s jednou závislosťou**
```python
# A → (B, C, D paralelne)
base = await rlm('Analyzuj trh')  # Najprv A
# Potom všetci paralelne s výsledkom A
b_handle = await rlm(f'Na základe: {base}, napíš blog')
c_handle = await rlm(f'Na základe: {base}, priprav sociálne siete')
d_handle = await rlm(f'Na základe: {base}, navrhni email kampaň')
```

**Pattern 3: Pipeline**
```python
# Paralelná fáza 1 → Paralelná fáza 2
# Fáza 1: Všetci paralelne
phase1 = {name: await rlm(task) for name, task in phase1_tasks.items()}
# Počkaj na všetkých z fázy 1
# Fáza 2: Všetci paralelne (s výsledkami fázy 1)
phase2 = {name: await rlm(task) for name, task in phase2_tasks.items()}
```

#### 9:00–10:00 | Limity a best practices paralelizmu
- **Povedať:** „Pár praktických rád:"
- **Koľko subagentov naraz?**
  - 2–5: optimálne, bezproblémové
  - 5–10: stále OK, sleduj CPU a RAM
  - 10+: potrebuješ premyslieť resource management (každý subagent = samostatný proces s kernelom)
- **Rate limiting:**
  - Ak používaš externé API (napr. websearch), priveľa paralelných volaní môže trafiť rate limit
  - Riešenie: spusti agentov s miernym oneskorením (`asyncio.sleep(1)` medzi `rlm()` volaniami)
- **Kontextové okno:**
  - Každý subagent má vlastný context window – výsledky, ktoré posielaš späť rodičovi, môžu byť veľké
  - Ak subagent vráti 50KB text, rodič to musí spracovať
- **Povedať:** „Pravidlo palca: ak ti 5 subagentov funguje, 10 bude tiež. Ak máš problémy s 3, optimalizuj prompt, nie počet."

### Kľúčové body
- Paralelné spustenie násobí rýchlosť – 4 agenti = až 4x rýchlejšie
- Fan-out / Fan-in je základný pattern: rozdelenie úloh → paralelné spracovanie → zber výsledkov
- Tri orchestračné patterny: sekvenčný reťazec, paralelný s jednou závislosťou, pipeline
- 2–5 paralelných subagentov je sweet spot pre väčšinu úloh
- Pri závislých úlohách použi sekvenčné `await rlm()` namiesto paralelného spúšťania

### Domáca úloha
1. Spusti 3 subagentov naraz, každý nech vyhľadá inú tému cez `websearch`. Porovnaj časy – koľko rýchlejšie to bolo oproti sekvenčnému?
2. Implementuj Fan-out / Fan-in pattern: 4 subagenti (SEO, copy, social, research), každý nech vráti výsledok. Pozbieraj ich a skombinuj do jedného markdown súboru.
3. Vyskúšaj Pattern 2 (paralelný s jednou závislosťou): najprv nech subagent A spraví analýzu, potom subagenti B a C nech paralelne spracujú rôzne časti výsledku.

---

## Lekcia 4: Komunikácia medzi agentmi
**Dĺžka videa:** 10 minút

### Detailný obsah / scenár

#### 0:00–1:30 | Komunikačný model Prime Agenta
- **Povedať:** „Agenti musia medzi sebou komunikovať. Prime Agent používa model `agent_message` – jednoduché, bezpečné posielanie správ medzi agentmi v rodine."
- **Ukázať diagram komunikačných ciest:**
  ```
  Hlavný agent (root)
    ├──↕️ Subagent A
    │     ├──↕️ Subagent A1
    │     └──↕️ Subagent A2
    └──↕️ Subagent B
          └──↕️ Subagent B1

  ↕️ = obojsmerná komunikácia cez agent_message
  Subagent A1 ←→ Subagent A2 (súrodenci – môžu)
  Subagent A1 ←→ Subagent B1 (NIE – mimo dosahu)
  Subagent A1 → Hlavný agent (NIE priamo – iba cez rodiča A)
  ```
- **Povedať:** „Kľúčové pravidlá: 1) Hovoríš len s rodičom, deťmi a súrodencami. 2) Vždy používaš `agent_message.send()`. 3) Príjemca ťa vidí pod tvojím menom – žiadne spoofing."

#### 1:30–3:00 | `agent_message.send()` – kompletná syntax
- **Povedať:** „Poďme rozobrať API `agent_message.send()`."
- **Ukázať kompletnú syntax:**
  ```python
  import agent_message

  # Základné volanie
  await agent_message.send(
      message="Tu je výsledok SEO auditu...",
      receiver_role="parent"  # 'parent', 'child', alebo 'sibling'
  )

  # S menom príjemcu (keď je viac detí/súrodencov)
  await agent_message.send(
      message="Hotovo, pozri prílohu.",
      receiver_role="child",
      receiver_name="prime-agent-child-abc123"
  )

  # Súrodenecká komunikácia
  await agent_message.send(
      message="Hej, aké si našiel keywords?",
      receiver_role="sibling",
      receiver_name="prime-agent-child-def456"
  )
  ```
- **Povedať:** „Všimni si: `receiver_role` je povinný. `receiver_name` je povinný iba ak je v danej role viacero agentov."

#### 3:00–5:00 | Komunikácia s rodičom – praktický walkthrough
- **Povedať:** „Toto je najčastejší scenár: subagent posiela výsledok rodičovi."
- **Ukázať kompletný flow z pohľadu subagenta:**
  ```python
  # Vo vnútri subagenta:

  # 1. Vykonaj úlohu
  result = vykonaj_seo_audit("example.com")

  # 2. Sformátuj výsledok
  formatted = f"""## SEO Audit: example.com

  ### Nájdené problémy
  {result.problems}

  ### Odporúčania
  {result.recommendations}

  ### Skóre: {result.score}/100
  """

  # 3. Pošli rodičovi
  await agent_message.send(formatted, receiver_role="parent")

  # 4. Subagent môže pokračovať (čakať na follow-up) alebo skončiť
  ```
- **Povedať:** „Z pohľadu rodiča – správu od subagenta prijímaš automaticky. Zobrazí sa v tvojom kontexte. Nemusíš explicitne `receive()` – daemon to spraví za teba."

#### 5:00–6:30 | Follow-up komunikácia – konverzácia so subagentom
- **Povedať:** „Subagent nemusí byť 'fire and forget'. Môžeš s ním viesť konverzáciu."
- **Ukázať pattern dialógu:**
  ```python
  # Rodič → Subagent (prvá úloha)
  handle = await rlm('Urob SEO audit domény example.com')

  # Subagent dokončí a pošle výsledok...
  # Rodič vidí výsledok, chce upresnenie:

  # Rodič → Subagent (follow-up)
  await agent_message.send(
      "Super, videl som audit. Môžeš sa hlbšie pozrieť na problém č. 3 "
      "(chybajúce meta descriptions) a navrhnúť konkrétne texty?",
      receiver_role="child",
      receiver_name=handle['name']
  )

  # Subagent spracuje follow-up a opäť pošle výsledok...
  # Toto môže ísť dookola – plnohodnotný dialóg
  ```
- **Povedať:** „Toto je silný pattern: subagent = špecialista, s ktorým iteruješ. Nie 'jeden prompt, jeden výsledok', ale konverzácia."

#### 6:30–8:00 | Súrodenecká komunikácia a koordinácia
- **Povedať:** „Subagenti môžu komunikovať medzi sebou – to umožňuje koordináciu bez zásahu rodiča."
- **Ukázať príklad:**
  ```python
  # Subagent A (SEO auditor) zistí niečo relevantné pre Subagenta B (copywritera)
  # Vo vnútri Subagenta A:

  # Po dokončení SEO auditu zistím dôležité keywords
  keywords = ["AI agent tutorial", "Prime Agent návod", "AI coding agent 2025"]

  # Pošlem ich priamo Subagentovi B (súrodencovi)
  await agent_message.send(
      f"Hej, tu sú kľúčové keywords, ktoré som našiel: {keywords}. "
      "Použi ich prosím v tých blog postoch.",
      receiver_role="sibling",
      receiver_name="prime-agent-child-copywriter"
  )
  ```
- **Povedať:** „Výhoda: rodič nemusí byť sprostredkovateľ. Agenti si vymieňajú info priamo. Nevýhoda: rodič stráca prehľad – nevidí, čo si súrodenci povedali, pokiaľ mu to nepovedia."

#### 8:00–9:00 | Best practices pre agent komunikáciu
- **Povedať:** „Zlaté pravidlá komunikácie:"
- **1. Buď explicitný v každej správe**
  - ✅ „Tu je SEO audit pre example.com: [dáta]. Navrhujem prioritu 1: meta descriptions."
  - ❌ „Hotovo."
- **2. Jedna správa = jedna myšlienka**
  - Ak máš viac výstupov, pošli viac správ alebo ich jasne oddeľ
- **3. Vždy potvrď príjem kritických správ**
  - Rodič môže poslať: „Potvrdené, SEO audit prijatý. Pokračuj."
- **4. Timeout a retry**
  - Ak nepríde odpoveď do X minút, pošli follow-up
- **5. Nezahlcuj rodiča**
  - Neposielaj 50 malých správ. Dávkuj ich alebo zlúč do väčšieho reportu.

#### 9:00–10:00 | Debugging komunikačných problémov
- **Povedať:** „Najčastejšie problémy a ich riešenia:"
- **Problém 1: „Subagent poslal správu, ale nevidím ju"**
  - Skontroluj, či `receiver_role="parent"` (nie "child")
  - Skontroluj, či subagent používa správne `agent_message.send()`, nie `print()` ani `return`
- **Problém 2: „Subagent sa snaží poslať správu, ale padá na chybe"**
  - Importuje subagent `agent_message`? (`import agent_message`)
  - Je `agent_message` skill dostupný pre subagenta? (mal by byť automaticky)
- **Problém 3: „Posielam follow-up, ale subagent nereaguje"**
  - Skontroluj, či subagent ešte beží (cez `agent_observe`)
  - Možno už skončil – spusti nového
- **Ukázať praktický debugging session:**
  ```python
  # Diagnostický skript pre komunikačné problémy
  import agent_observe

  # 1. Zisti, či subagent existuje
  children = await rlm.list_subagents()
  print(f"Aktívne deti: {children}")

  # 2. Skontroluj, či subagent žije
  for child in children:
      status = await agent_observe.observe_child(child['name'])
      print(f"{child['name']}: {status}")
  ```

### Kľúčové body
- `agent_message.send(message, receiver_role)` je jediný spôsob komunikácie medzi agentmi
- Komunikovať môžeš len s rodičom, deťmi a súrodencami
- Rodič dostáva správy automaticky, nemusí explicitne `receive()`
- Follow-up pattern: subagent = špecialista, s ktorým vedieš dialóg
- Súrodenecká komunikácia je možná, ale rodič stráca prehľad – používaj uvážlivo

### Domáca úloha
1. Vytvor subagenta, ktorý spraví research a pošle ti výsledok. Potom mu pošli follow-up otázku a nechaj ho odpovedať. Celé to zdokumentuj.
2. Spusti 2 subagentov (súrodencov). Nech Subagent A nájde keywords a pošle ich Subagentovi B. Subagent B nech ich použije na napísanie blog postu. Over, či komunikácia prebehla.
3. Zámerne sprav chybu: pošli subagentovi správu s `receiver_role="parent"` namiesto `"child"`. Čo sa stane? Ako to opravíš?

---

## Lekcia 5: Praktický projekt – Content factory s 5 agentmi
**Dĺžka videa:** 10 minút

### Detailný obsah / scenár

#### 0:00–1:30 | Architektúra Content Factory
- **Povedať:** „Toto je vyvrcholenie modulu. Postavíme content factory – systém 5 špecializovaných subagentov, ktorí spolupracujú na tvorbe marketingového obsahu."
- **Ukázať architektúru:**
  ```
  ORCHESTRÁTOR (ty)
    │
    ├── Agent 1: STRATÉG (content strategy)
    │     └── Vytvorí plán: témy, keywords, formáty
    │
    ├── Agent 2: COPYWRITER (tvorba obsahu)
    │     └── Napíše blog posty, landing pages
    │
    ├── Agent 3: SOCIAL (sociálne siete)
    │     └── Vytvorí LinkedIn a Twitter/X príspevky
    │
    ├── Agent 4: EMAIL (emailové kampane)
    │     └── Vytvorí welcome a nurture sekvencie
    │
    └── Agent 5: SEO (SEO optimalizácia)
          └── Skontroluje a optimalizuje všetok obsah
  ```
- **Povedať:** „Päť agentov. Každý špecialista. Jeden cieľ: kompletný marketingový balíček za menej ako 15 minút."

#### 1:30–3:30 | Krok 1: Spustenie Stratéga a Copywritera (sekvenčne)
- **Povedať:** „Najprv potrebujeme stratégiu. Bez nej copywriter nevie, o čom písať."
- **Ukázať na obrazovke – Krok 1:**
  ```python
  # KROK 1: Spusti Stratéga
  strategy_handle = await rlm("""
  Si content stratég. Vytvor obsahovú stratégiu pre online kurz "Prime Agent Masterclass".

  Produkt: Kurz, ktorý učí vývojárov používať AI coding agentov.
  Cieľovka: Vývojári, ktorí chcú zvýšiť produktivitu.

  Vráť:
  1. 5 hlavných obsahových pilierov
  2. 10 konkrétnych tém blog postov
  3. Kľúčové SEO keywords
  4. Tone of voice a positioning

  Formát: Markdown.
  Pošli výsledok rodičovi cez agent_message.send().
  """)

  print(f"✅ Stratég spustený: {strategy_handle['name']}")
  ```

#### 3:30–5:30 | Krok 2: Paralelné spustenie Copywritera, Social a Email agenta
- **Povedať:** „Stratég beží. Kým skončí, pripravíme si tasky pre ostatných. Keď stratég vráti výsledok, spustíme zvyšných troch PARALELNE."
- **Ukázať na obrazovke – Krok 2:**
  ```python
  # Počkaj na výsledok od Stratéga...
  # (v reálnej session sa výsledok zobrazí automaticky)

  # Predpokladajme, že strategy_output obsahuje stratégiu
  strategy_output = """[výstup od stratéga]"""

  # KROK 2: Paralelne spusti Copywritera, Social a Email agenta
  copy_handle = await rlm(f"""
  Si copywriter. Na základe tejto content stratégie:
  {strategy_output}

  Napíš:
  1. Jeden kompletný blog post (1500 slov) na tému "Prečo každý vývojár potrebuje AI agenta v 2025"
  2. Landing page text pre Prime Agent Masterclass (hero, features, CTA, social proof)

  Použi tone of voice zo stratégie.
  Pošli výsledok rodičovi cez agent_message.send().
  """)

  social_handle = await rlm(f"""
  Si social media manažér. Na základe stratégie:
  {strategy_output[:500]}...

  Vytvor:
  1. 5 LinkedIn príspevkov (každý 150-250 slov)
  2. 3 Twitter/X thready (každý 5-7 tweetov)

  Použi kľúčové keywords. Každý príspevok nech má hook.
  Pošli výsledok rodičovi cez agent_message.send().
  """)

  email_handle = await rlm(f"""
  Si email marketing špecialista. Na základe stratégie:
  {strategy_output[:500]}...

  Vytvor:
  1. Welcome sekvenciu (3 emaily) pre nových študentov kurzu
  2. Nurture sekvenciu (5 emailov) pre nerozhodnutých

  Každý email: subject line, preheader, body, CTA.
  Pošli výsledok rodičovi cez agent_message.send().
  """)

  print("✅ Copywriter, Social a Email agent paralelne spustení!")
  ```

#### 5:30–7:00 | Krok 3: SEO optimalizácia všetkého obsahu
- **Povedať:** „Keď všetci traja skončia, SEO agent prejde všetok obsah a optimalizuje ho."
- **Ukázať na obrazovke – Krok 3:**
  ```python
  # Počkaj na výsledky od Copywritera, Social a Email agenta
  # ... (výsledky prídu automaticky)

  # KROK 3: SEO agent – sekvenčne (potrebuje všetky výstupy)
  seo_handle = await rlm(f"""
  Si SEO špecialista. Optimalizuj tento obsah:

  BLOG POST:
  {copy_output}

  SOCIAL:
  {social_output}

  EMAIL:
  {email_output}

  Pre každý kus obsahu:
  1. Skontroluj použitie keywords
  2. Navrhni optimalizované titulky/headlines
  3. Pridaj odporúčania pre meta descriptions
  4. Skontroluj readability a štruktúru

  Vráť optimalizované verzie + zoznam zmien.
  Pošli výsledok rodičovi cez agent_message.send().
  """)

  print("✅ SEO agent spustený!")
  ```

#### 7:00–9:00 | Krok 4: Finálna kompilácia a monitoring
- **Povedať:** „Teraz si orchestrátor. Tvoja úloha: pozbierať všetky výsledky a skompilovať finálny balíček."
- **Ukázať finálnu kompiláciu:**
  ```python
  # KROK 4: Zber a kompilácia

  # Predpokladajme, že všetci agenti poslali výsledky
  final_package = f"""
  # 📦 Content Factory Output – Prime Agent Masterclass

  ---

  ## 🎯 Content Strategy
  {strategy_output}

  ---

  ## ✍️ Blog Post + Landing Page
  {copy_output}

  ---

  ## 📱 Social Media Content
  {social_output}

  ---

  ## 📧 Email Campaigns
  {email_output}

  ---

  ## 🔍 SEO Optimizations
  {seo_output}

  ---

  *Vygenerované Content Factory – 5 agentov, {time_in_minutes} minút*
  """

  # Ulož finálny balíček
  with open('/Users/abra/Developer/content-factory-output.md', 'w') as f:
      f.write(final_package)

  print("✅ Content Factory hotová! Výstup uložený do content-factory-output.md")
  ```

#### 9:00–10:00 | Výsledky, metriky a retrospektíva
- **Povedať:** „Poďme sa pozrieť, čo sme dosiahli:"
- **Ukázať sumár:**
  - ⏱️ Celkový čas: ~12–15 minút (namiesto 2–3 dní manuálnej práce)
  - 📄 Vygenerovaný obsah: 1 stratégia, 1 blog post, 1 landing page, 5 LinkedIn postov, 3 Twitter thready, 8 emailov, SEO audit
  - 🤖 Počet agentov: 5 (1 stratég + 1 copywriter + 1 social + 1 email + 1 SEO)
  - 🔄 Orchestračný pattern: Sekvenčný (stratég) → Paralelný (copy+social+email) → Sekvenčný (SEO)
- **Povedať:** „Čo sme sa naučili:"
  1. Rozdeľ komplexný cieľ na špecializované podúlohy
  2. Sekvenčné kroky tam, kde je závislosť (stratégia → obsah)
  3. Paralelné kroky tam, kde závislosť nie je (copy, social, email)
  4. SEO vždy ako posledný krok (potrebuje všetok obsah)
  5. Finálna kompilácia = tvoja pridaná hodnota ako orchestrátora
- **Povedať:** „Toto nie je demo. Toto je reálny systém, ktorý môžeš používať každý týždeň."

### Kľúčové body
- Content Factory = 5 špecializovaných agentov + orchestrátor
- Orchestračný pattern: Sekvenčný (závislosti) → Paralelný (nezávislé) → Sekvenčný (finalizácia)
- Každý agent dostane presný scope a formát výstupu
- Celkový čas: ~12–15 minút namiesto dní manuálnej práce
- Tento pattern môžeš aplikovať na akýkoľvek komplexný projekt – nie len marketing

### Domáca úloha
1. Postav si vlastnú Content Factory podľa tohto projektu. Prispôsob tasky svojmu biznisu/projektu.
2. Pridaj 6. agenta: "Dizajnér" – nech navrhne vizuálne koncepty (farby, rozloženie, typografia) pre landing page. Môžeš ho spustiť paralelne s ostatnými.
3. Spusti Content Factory 3x po sebe s mierne odlišnými parametrami (iná cieľovka, iný tone of voice). Porovnaj výstupy. Ktorý je najlepší a prečo?
4. Zdokumentuj celý proces (screenshoty, časy, výstupy) a zdieľaj v komunitnej skupine kurzu.

---

# Prime Agent Masterclass – Modul 5: Automatizácia marketingu

## Prehľad modulu

**Cieľ modulu:** Po absolvovaní tohto modulu budeš vedieť využívať Prime Agenta a jeho marketingové skilly na autonómnu tvorbu obsahu pre LinkedIn, Twitter/X, emailové kampane, SEO stratégiu a prieskum konkurencie. V závere postavíš plne autonómnu 30-dňovú marketingovú kampaň.

**Celková dĺžka:** 65 minút videa + domáce úlohy

---

## Lekcia 1: Agent pre LinkedIn obsah
**Dĺžka videa:** 12 minút

### Detailný obsah / scenár

#### 0:00–1:30 | Prečo LinkedIn a prečo agent
- **Povedať:** „LinkedIn je najvýkonnejšia B2B platforma na svete. 1 miliarda používateľov. Organický dosah, o ktorom sa Facebooku ani nesníva. A 99% ľudí tam publikuje nekonzistentne – lebo nevedia, čo písať."
- **Povedať:** „S Prime Agentom tento problém zmizne. Agent ti vygeneruje mesiac obsahu za 10 minút."
- **Ukázať štatistiky (na slide):**
  - LinkedIn organický dosah: až 10–30% followerov (Facebook: 1–3%)
  - 40% B2B marketerov považuje LinkedIn za #1 kanál pre lead generation
  - Konzistentní tvorcovia (3–5x týždenne) majú 5–10x väčší dosah
- **Povedať:** „Cieľ tejto lekcie: na konci budeš mať agenta, ktorý ti vygeneruje mesiac LinkedIn obsahu."

#### 1:30–3:30 | Príprava – definovanie tvojho LinkedIn profilu a cieľov
- **Povedať:** „Agent potrebuje poznať TVOJ kontext. Bez neho bude generovať generický obsah, ktorý nikoho nezaujíma."
- **Ukázať prípravný formulár – nechať študentov vyplniť:**
  ```markdown
  # Môj LinkedIn kontext:
  - Meno a rola: [napr. "Marek, Senior Developer & AI Consultant"]
  - Cieľovka: [napr. "CTOs, tech leads, developeri v korporátoch"]
  - Témy, o ktorých hovorím: [napr. "AI agenti, produktivita, automatizácia"]
  - Môj tone of voice: [napr. "Praktický, priamy, občas vtipný"]
  - Čo NIKDY nepíšem: [napr. "Motivačné citáty, osobné fotky"]
  - Cieľ: [napr. "Získať 500 followerov a 5 leadov mesačne"]
  ```
- **Povedať:** „Toto daj agentovi ako prvú časť promptu. Je to tvoj brand book."

#### 3:30–5:30 | Vytvorenie LinkedIn Content Agenta – Live Demo
- **Povedať:** „Poďme vytvoriť agenta pre LinkedIn."
- **Ukázať na obrazovke:**
  ```python
  # LinkedIn Content Agent
  linkedin_handle = await rlm("""
  Si špičkový LinkedIn ghostwriter pre B2B tech profesionálov.

  ## MÔJ PROFIL:
  - Meno a rola: Marek, Senior Developer & AI Consultant
  - Cieľovka: CTOs, tech leads, developeri v korporátoch
  - Témy: AI agenti, produktivita vývojárov, automatizácia, Prime Agent
  - Tone of voice: Praktický, priamy, data-driven, občas suchý humor
  - Vyhýbaj sa: motivačné frázy, osobné príbehy bez pointy, "korporátne" buzzwordy
  - Cieľ: Budovať autoritu v AI coding nástrojoch, získať leady na konzultácie

  ## ÚLOHA:
  Vytvor 20 LinkedIn príspevkov na mesiac.

  ### Formáty (mix):
  - 6x "Lekcia / How-to" (konkrétny tip, ktorý môže čitateľ hneď použiť)
  - 5x "Contrarian take" (názor, ktorý ide proti mainstreamu – s argumentmi)
  - 4x "Osobný príbeh s ponaučením" (nie motivačné, ale s konkrétnou lekciou)
  - 3x "Data / Štatistika s komentárom" (prekvapivé číslo + tvoj insight)
  - 2x "Behind the scenes" (ako reálne používaš AI agentov v práci)

  ### Pre každý príspevok:
  - **Hook** (prvý riadok – musí zastaviť scroll)
  - **Telo** (150–300 slov, krátke odseky, max 3 vety na odsek)
  - **CTA** (čo má čitateľ spraviť – komentovať, vyskúšať, prečítať článok)
  - **Hashtags** (3–5 relevantných)

  ### Pravidlá:
  - Žiadne "Agree?" na konci
  - Žiadne prázdne riadky medzi odsekmi (LinkedIn formát)
  - Hook musí byť v prvých 3 slovách chytľavý
  - Každý post nech má JEDNU hlavnú myšlienku

  Výstup vo formáte markdown. Zoraď podľa dní (Deň 1 – Deň 20).
  Pošli výsledok rodičovi cez agent_message.send().
  """)

  print(f"✅ LinkedIn agent spustený: {linkedin_handle['name']}")
  ```

#### 5:30–7:30 | Analýza výstupu – čo agent vygeneroval
- **Povedať:** „Pozrime sa, čo agent vygeneroval. Budeme hodnotiť podľa 5 kritérií:"
- **Ukázať checklist na hodnotenie:**
  1. **Hook quality** – Zastal by som pri scrollovaní?
  2. **Hodnota** – Dozvedel som sa niečo nové / použiteľné?
  3. **Tone of voice** – Znie to ako ja?
  4. **Formát** – Krátke odseky, dobrá štruktúra?
  5. **CTA** – Je jasné, čo mám spraviť?
- **Ukázať príklad dobrého a zlého výstupu:**
  ```markdown
  ❌ ZLÝ:
  "V dnešnej dobe je dôležité používať AI nástroje. Pomáhajú nám
  byť produktívnejšími. Čo si o tom myslíte?"

  ✅ DOBRÝ:
  "Minulý týždeň som napísal 2000 riadkov kódu.
  Presnejšie: môj agent ich napísal. Ja som len reviewoval.

  Tu je môj setup:
  1. Prime Agent v termináli
  2. Jasný task prompt
  3. Iteratívne review

  Výsledok: 4 hodiny práce namiesto 2 dní.

  Stále si píšeš všetko sám?"
  ```
- **Povedať:** „Vidíš ten rozdiel? Prvý je generický, druhý je konkrétny a autentický."

#### 7:30–9:30 | Iterácia a ladenie LinkedIn Agenta
- **Povedať:** „Prvý výstup málokedy sedí na 100%. Teraz ukážem, ako iterovať."
- **Ukázať follow-up pattern:**
  ```python
  # Follow-up: vylepši konkrétne veci
  await agent_message.send(
      """Super, prvých 20 postov je dobrý základ. Teraz ich vylepši:

      1. V "How-to" postoch pridaj konkrétne čísla/štatistiky
      2. V "Contrarian" postoch pridaj protiargument a vyvráť ho
      3. Skontroluj, či každý hook obsahuje "pattern interrupt" (niečo neočakávané)
      4. Pridaj ku každému postu "prečo to funguje" (1 veta pre mňa – nepublikuje sa)

      Vráť upravenú verziu.""",
      receiver_role="child",
      receiver_name=linkedin_handle['name']
  )
  ```
- **Povedať:** „Takto iteruješ, kým nie si spokojný. Typicky 2–3 kolá stačia."

#### 9:30–10:30 | Plánovanie a scheduling – obsahový kalendár
- **Povedať:** „Obsah máš. Teraz ho treba naplánovať."
- **Ukázať tvorbu kalendára:
  ```python
  # Nechaj agenta vytvoriť publish kalendár
  await agent_message.send(
      """Vytvor publikačný kalendár na 30 dní pre týchto 20 LinkedIn postov.

      Pravidlá:
      - Pondelok–Piatok: 1 post denne (najlepší čas 8:00–9:00)
      - Utorok a Štvrtok: najsilnejšie posty (najväčšia aktivita na LinkedIn)
      - Pondelok: "Lekcia / How-to" (ľudia hľadajú hodnotu na začiatok týždňa)
      - Streda: "Contrarian take" (mid-week engagement)
      - Piatok: ľahší, osobnejší tón

      Výstup: tabuľka s dňom, dátumom, typom postu a prvým riadkom hooku.
      Formát: Markdown tabuľka.""",
      receiver_role="child",
      receiver_name=linkedin_handle['name']
  )
  ```

#### 10:30–12:00 | Bonus – Cross-posting a repurposing
- **Povedať:** „Bonusový tip: nechaj agenta repurpose-ovať LinkedIn obsah na iné platformy."
- **Ukázať:**
  ```python
  # Repurpose agent
  repurpose_handle = await rlm(f"""
  Z týchto 20 LinkedIn príspevkov:
  {linkedin_output}

  Vytvor:
  1. 5 dlhších blog postov (spoj 3–4 súvisiace LinkedIn posty do jedného článku)
  2. 3 newsletter vydania (každé ako digest 5 najlepších postov + bonus insight)
  3. 10 tweetov (skráť najsilnejšie hooky do 280 znakov)

  Pošli výsledok rodičovi.
  """)
  ```
- **Povedať:** „Jeden mesiac LinkedIn obsahu → blog posty → newsletter → Twitter. Všetko z jedného zdroja."

### Kľúčové body
- Kvalitný LinkedIn obsah začína kvalitným kontextom (tvoj profil, tone of voice, cieľovka)
- Mix formátov (how-to, contrarian, príbeh, data, behind the scenes) udržiava engagement
- Hook je všetko – prvý riadok rozhoduje, či človek klikne "see more"
- Iteruj s agentom: 1. generácia → kontrola → follow-up → finálna verzia
- Repurpose: jeden obsah → viacero formátov a kanálov

### Domáca úloha
1. Vyplň si svoj LinkedIn kontextový profil (meno, rola, cieľovka, témy, tone of voice)
2. Spusti LinkedIn Content Agenta a nechaj ho vygenerovať 20 príspevkov pre tvoj profil
3. Vyber 3 najlepšie príspevky a skutočne ich publikuj na LinkedIn. Sleduj engagement (views, likes, komentáre) po 48 hodinách.
4. Porovnaj výkon tvojich manuálnych postov vs. agentom generovaných. Ktoré fungujú lepšie?

---

## Lekcia 2: Agent pre Twitter/X thready
**Dĺžka videa:** 10 minút

### Detailný obsah / scenár

#### 0:00–1:30 | Prečo Twitter/X thready
- **Povedať:** „Twitter/X thready sú momentálne najvirálnejší formát na sociálnych sieťach. Prečo?"
- **Ukázať dôvody:**
  - Thread = viac priestoru na rozvinutie myšlienky (oproti 280 znakom)
  - Každý tweet v thread-e je ďalšia šanca na engagement (like/retweet/reply)
  - Algoritmus X boostuje thready – vidí, že ľudia trávia čas čítaním
  - Jeden dobrý thread = 100K+ impresií, aj s malým follower countom
- **Povedať:** „Problém: napísať dobrý thread trvá 45–90 minút. S agentom: 2 minúty."

#### 1:30–3:30 | Anatómia vírusového threadu
- **Povedať:** „Predtým než spustíme agenta, musíme rozumieť, čo robí thread vírusovým."
- **Ukázať rozbor štruktúry:**
  ```markdown
  Tweet 1: HOOK – šokujúce tvrdenie, kontroverzia, alebo "tajomstvo"
  Tweet 2: Kontext – prečo je to dôležité
  Tweet 3–5: Hlavný obsah – 3 kľúčové body / kroky / lekcie
  Tweet 6: Zvrat alebo "aha moment"
  Tweet 7 (posledný): CTA + retweet request

  Príklad:
  Tweet 1: "90% vývojárov používa AI nástroje úplne zle."
  Tweet 2: "Používajú ich ako Google – pýtajú sa otázky a kopírujú odpovede."
  Tweet 3: "Tu je správny spôsob: 1. Daj agentovi KONTEXT, nie len otázku."
  Tweet 4: "2. Nauč sa iterovať. Prvý výstup je len draft."
  Tweet 5: "3. Dôveruj, ale verifikuj. Agent je junior developer."
  Tweet 6: "Keď toto zvládneš, tvoja produktivita sa zdvojnásobí."
  Tweet 7: "RT ak ti to pomohlo. A followni pre viac AI dev tipov."
  ```
- **Povedať:** „Túto štruktúru dáme agentovi ako template."

#### 3:30–5:30 | Vytvorenie Twitter Thread Agenta – Live Demo
- **Povedať:** „Poďme vytvoriť agenta pre Twitter thready."
- **Ukázať na obrazovke:**
  ```python
  thread_handle = await rlm("""
  Si Twitter/X ghostwriter pre tech profesionálov. Špecializuješ sa na virálne thready.

  ## MÔJ PROFIL:
  {linkedin_context}  # Použi rovnaký kontext ako pri LinkedIn

  ## ÚLOHA:
  Vytvor 10 Twitter/X threadov na mesiac.

  ### Štruktúra každého threadu (7 tweetov):
  - **Tweet 1: HOOK** – Šokujúce tvrdenie / kontroverzia / "tajomstvo" / "unpopular opinion"
    - Max 280 znakov
    - Musí obsahovať číslo alebo odvážne tvrdenie
    - Príklady: "90% ľudí robí X zle", "Prestaň robiť Y", "Nikto ti nepovie o Z"

  - **Tweet 2: KONTEXT** – Prečo je to dôležité, čo je v stávke
    - "Väčšina vývojárov..." / "Problém je, že..."

  - **Tweet 3–5: HLAVNÝ OBSAH** – 3 konkrétne body/kroky/lekcie
    - Každý tweet = 1 point
    - Číslované (1. 2. 3.)
    - Konkrétne, použiteľné, nie abstraktné

  - **Tweet 6: ZVRAT / AHA MOMENT** – Neočakávaný insight alebo zhrnutie
    - "Čo to znamená pre teba: ..."

  - **Tweet 7: CTA** – Jasná výzva + social proof
    - "RT ak ti to pomohlo 🔁"
    - "Followni pre viac AI tipov"
    - Môže obsahovať link (napr. na newsletter)

  ### Formátovanie:
  - Každý tweet na novom riadku, označený "Tweet 1:", "Tweet 2:", atď.
  - Prázdny riadok medzi threadmi
  - Žiadne hashtagy (na X sa už nenosia)
  - Používaj formátovanie: **bold**, odrážky, emoji (s mierou)

  ### Témy na tento mesiac (použi mix):
  1. AI agenti pre vývojárov
  2. Automatizácia workflowu
  3. Produktivita a deep work
  4. Chyby, ktoré vývojári robia
  5. Budúcnosť programovania

  Výstup: 10 threadov v markdowne.
  Pošli výsledok rodičovi cez agent_message.send().
  """)

  print(f"✅ Thread agent spustený: {thread_handle['name']}")
  ```

#### 5:30–7:00 | Hook writing – najdôležitejšia zručnosť
- **Povedať:** „Hook je 80% úspechu threadu. Poďme sa mu venovať špeciálne."
- **Ukázať hook formula:**
  - **Formula 1: Číslo + kontroverzia** – „90% developers use AI wrong"
  - **Formula 2: Zákaz** – „Stop using ChatGPT for coding"  
  - **Formula 3: Tajomstvo** – „The secret to 10x productivity nobody talks about"
  - **Formula 4: Porovnanie** – „Junior dev vs Senior dev: how they use AI"
  - **Formula 5: Časová tieseň** – „If you're not using AI agents by 2026, you're already behind"
- **Povedať:** „Nechaj agenta vygenerovať 20 hookov a vyber si top 10."

#### 7:00–8:30 | Thread scheduling a optimálne časy
- **Povedať:** „Kedy publikovať thready? Tu sú data:"
- **Ukázať optimálne časy:**
  - Najlepšie dni: Utorok, Streda, Štvrtok
  - Najlepší čas: 8:00–10:00 EST (13:00–15:00 nášho času), alebo 17:00–19:00 EST
  - Nikdy: Víkend pred 12:00 (mŕtva zóna)
- **Povedať:** „Nechaj agenta navrhnúť schedule:"
  ```python
  await agent_message.send(
      """Vytvor publikačný kalendár pre 10 threadov na 30 dní.
      Pravidlá:
      - Utorok a Štvrtok: najsilnejšie thready
      - Streda: kontroverzný/diskutabilný thread
      - Max 3 thready týždenne (nechceme spamovať)
      - Medzi threadmi aspoň 2 dni prestávka
      Výstup: tabuľka Deň, Dátum, Téma, Hook.""",
      receiver_role="child",
      receiver_name=thread_handle['name']
  )
  ```

#### 8:30–10:00 | Cross-promotion – Thread → LinkedIn → Newsletter
- **Povedať:** „Jeden thread = obsah na celý týždeň. Tu je workflow:"
- **Ukázať repurposing pipeline:**
  ```
  Twitter Thread
    ├── Rozšír na LinkedIn carousel (5-7 slidov)
    ├── Rozšír na blog post (800-1200 slov)
    ├── Skráť na 3 izolované tweet-y
    └── Použi ako newsletter tému
  ```
- **Ukázať implementáciu:**
  ```python
  # Agent pre repurposing threadov
  repurpose_handle = await rlm(f"""
  Z tohto threadu:
  {best_thread}

  Vytvor:
  1. LinkedIn post verziu (rozšír na 200-300 slov, LinkedIn formát)
  2. Blog post outline (5 sekcií, každá z jedného tweetu)
  3. 3 samostatné tweet-y z hlavných bodov
  4. Newsletter intro (2 vety, ktoré nalákajú na prečítanie celého threadu)

  Pošli výsledok rodičovi.
  """)
  ```
- **Povedať:** „1 hodina práce s agentom = obsah na celý týždeň na 3 platformy."

### Kľúčové body
- Thread = 7 tweetov: Hook → Kontext → 3 body → Zvrat → CTA
- Hook je 80% úspechu – nauč sa 5 formul pre hooks
- Optimálne publikovanie: Ut–Št, 13:00–15:00 alebo 17:00–19:00 nášho času
- Max 3 thready týždenne, aspoň 2 dni medzi nimi
- Jeden thread → multi-platform obsah (LinkedIn, blog, newsletter)

### Domáca úloha
1. Spusti Twitter Thread Agenta a nechaj ho vygenerovať 10 threadov na tvoje témy
2. Vyber najlepší thread, uprav ho (pridaj osobný touch) a publikuj na Twitter/X
3. Zmeraj výkon: koľko views, likes, retweetov, reply-ov si dostal za 48 hodín?
4. Repurpose svoj najlepší thread na LinkedIn príspevok. Porovnaj výkon na oboch platformách.

---

## Lekcia 3: Agent pre email kampane
**Dĺžka videa:** 12 minút

### Detailný obsah / scenár

#### 0:00–1:30 | Email marketing v ére AI
- **Povedať:** „Email stále generuje najvyššie ROI zo všetkých marketingových kanálov. $36 späť za každý $1 investovaný (Litmus, 2024)."
- **Povedať:** „Ale je tu problém: písanie dobrých emailov je zdĺhavé. Subject line, preheader, personalizácia, segmentation..."
- **Ukázať kontrast:**
  - Manuálne: 1 emailová sekvencia = 4–8 hodín
  - S Prime Agentom: 5 emailových sekvencií = 10 minút
- **Povedať:** „Dnes vytvoríme 3 kompletné emailové sekvencie agentom."

#### 1:30–3:30 | Typy emailových sekvencií a ich štruktúra
- **Povedať:** „Predtým než začneme, musíme rozumieť typom sekvencií."
- **Ukázať 3 hlavné typy:**

**1. Welcome sekvencia (3–5 emailov)**
- Cieľ: Aktivovať nového subscribera, doručiť "quick win"
- Email 1: Vitaj + lead magnet (ihneď po prihlásení)
- Email 2: Tvoj príbeh + prečo to robíš (Deň 2)
- Email 3: Najlepší obsah / top zdroje (Deň 4)
- Email 4: Social proof + výzva na engagement (Deň 7)

**2. Nurture sekvencia (5–7 emailov)**
- Cieľ: Budovať dôveru, vzdelávať, pripraviť na predaj
- Email 1: Problém, ktorý riešiš
- Email 2–4: 3 edukačné emaily (každý 1 kľúčový insight)
- Email 5: Prípadová štúdia / social proof
- Email 6: Soft pitch (tvoj produkt/služba ako riešenie)
- Email 7: Urgency / deadline / posledná šanca

**3. Re-engagement sekvencia (3 emaily)**
- Cieľ: Prebudiť neaktívnych subscriberov
- Email 1: "Chýbaš nám" + čo si zmeškal
- Email 2: Špeciálna ponuka / exkluzívny obsah
- Email 3: "Posledný email" – zostať alebo unsubscribe

#### 3:30–6:00 | Vytvorenie Email Campaign Agenta – Live Demo
- **Povedať:** „Poďme vytvoriť agenta, ktorý vygeneruje všetky 3 sekvencie naraz."
- **Ukázať na obrazovke:**
  ```python
  email_handle = await rlm("""
  Si špičkový email marketing copywriter pre online kurzy a SaaS produkty.

  ## KONTEXT:
  Produkt: "Prime Agent Masterclass" – online kurz pre vývojárov
  Cieľovka: Vývojári, ktorí chcú zvýšiť produktivitu pomocou AI agentov
  Brand voice: Praktický, priamy, priateľský, žiadny "hype"
  Odosielateľ: Marek (tvorca kurzu)
  Hlavné benefity: 10x rýchlejší vývoj, menej manuálnej práce, konkurenčná výhoda

  ## ÚLOHA:
  Vytvor 3 kompletné emailové sekvencie.

  ---

  ### SEKVEN CIA 1: WELCOME (4 emaily)
  Pre nových subscriberov, ktorí si stiahli lead magnet "10 AI Agent Tipov pre Vývojárov".

  **Email 1: Welcome + Lead Magnet (Deň 0)**
  - Subject line: prekvapivý, osobný
  - Preheader: doplňuje subject line
  - Body: krátke privítanie, link na stiahnutie, čo čakať od tohto newslettera
  - CTA: Stiahni si lead magnet

  **Email 2: Môj príbeh (Deň 2)**
  - Ako som objavil Prime Agenta, ako mi zmenil prácu
  - Prečo som vytvoril tento kurz
  - CTA: Odpíš mi – aký je tvoj najväčší pain point vo vývoji?

  **Email 3: Top zdroje (Deň 4)**
  - 5 najlepších zdrojov o AI agentoch (články, videá, nástroje)
  - Krátky komentár ku každému
  - CTA: Pozri si XY video

  **Email 4: Social Proof + Engagement (Deň 7)**
  - Čo hovoria študenti / čo sa naučili
  - Odkaz na komunitu / Discord
  - CTA: Pridaj sa do komunity

  ---

  ### SEKVEN CIA 2: NURTURE (5 emailov)
  Pre subscriberov, ktorí prešli welcome sekvenciou, ale ešte nekúpili.

  **Email 1: Problém (Deň 0)**
  - Prečo tradičný vývoj bez AI je pomalý a frustrujúci
  - Štatistiky / data
  - CTA: Zamysli sa – koľko času tráviš manuálnym codingom?

  **Email 2: Lekcia 1 – Automatizácia s AI (Deň 2)**
  - Konkrétny príklad: ako agent napísal 500 riadkov za 5 minút
  - Code snippet / screenshot
  - CTA: Skús toto (konkrétny tip)

  **Email 3: Lekcia 2 – Debugging s AI (Deň 4)**
  - Ako agent debuguje rýchlejšie ako človek
  - Reálny príbeh z praxe

  **Email 4: Prípadová štúdia (Deň 7)**
  - Ako študent X ušetril 15 hodín týždenne
  - Konkrétne čísla, citácie

  **Email 5: Soft pitch (Deň 10)**
  - Čo sa naučíš v Prime Agent Masterclass
  - Prečo teraz (cena, bonus, limitovaný prístup)
  - CTA: Pozri si sylabus kurzu

  ---

  ### SEKVEN CIA 3: RE-ENGAGEMENT (3 emaily)
  Pre subscriberov, ktorí neotvorili žiaden email za 30+ dní.

  **Email 1: Chýbaš nám (Deň 0)**
  - Subject line: "Stále ťa to baví?" / "Si OK?"
  - Čo si zmeškal (top 3 veci)
  - CTA: Klikni ak chceš zostať

  **Email 2: Exkluzívny obsah (Deň 4)**
  - Niečo špeciálne len pre teba (mini-lekcia, checklist)
  - "Toto ešte nebolo v newsletteri"

  **Email 3: Posledný email (Deň 8)**
  - "Toto je posledný email odo mňa..."
  - Možnosť zostať alebo unsubscribe
  - Čistý, úprimný, bez guilt-trippingu

  ---

  ### PRE KAŽDÝ EMAIL:
  - Subject line (max 50 znakov)
  - Preheader (max 100 znakov)
  - Telo emailu (150–300 slov, plain text štýl)
  - CTA (jeden, jasný)
  - Poznámka: prečo to funguje (1 veta – len pre mňa, nepublikuje sa)

  Celý výstup v markdowne. Pošli výsledok rodičovi cez agent_message.send().
  """)

  print(f"✅ Email agent spustený: {email_handle['name']}")
  ```

#### 6:00–7:30 | Subject line veda a A/B testovanie
- **Povedať:** „Subject line rozhoduje o tom, či email vôbec niekto otvorí. Poďme sa mu venovať."
- **Ukázať 7 typov subject lines:**
  1. **Zvedavosť / Gap:** „Toto ti na Code Review nikto nepovie"
  2. **Číslo / List:** „5 chýb, ktoré robíš pri používaní AI"
  3. **Personalizované:** „Marek, tvoj kód môže byť 10x rýchlejší"
  4. **Urgency/Scarcity:** „Posledných 24 hodín na early bird cenu"
  5. **How-to:** „Ako som znížil čas developmentu o 70%"
  6. **Contrarian:** „Prestaň používať Copilota (a tu je prečo)"
  7. **Krátke/Intriguing:** „AI. Kód. Hotovo."
- **Povedať:** „Nechaj agenta vygenerovať A/B varianty:"
  ```python
  await agent_message.send(
      """Pre každý email v sekvenciách vygeneruj 3 alternatívne subject lines
      (rôzne typy: zvedavosť, číslo, contrarian).
      Ku každej napíš, ktorý typ to je a prečo by mal fungovať.""",
      receiver_role="child",
      receiver_name=email_handle['name']
  )
  ```

#### 7:30–9:30 | Personalizácia a dynamické polia
- **Povedať:** „Agenta môžeš naučiť používať merge tags pre personalizáciu."
- **Ukázať:**
  ```python
  # Segmentácia a personalizácia
  await agent_message.send(
      f"""Uprav všetky emaily tak, aby používali tieto personalizačné tokeny:
      - {{first_name}} – krstné meno
      - {{primary_language}} – hlavný jazyk (Python, JS, atď.)
      - {{pain_point}} – najväčší problém (zistený z lead magnet opt-inu)

      V každom emailovej sekcii, kde je to vhodné, vlož personalizovaný element.
      Napríklad: "Ahoj {{first_name}}, videl som že používaš {{primary_language}}..."

      Pridaj aj návrh, ako tieto dáta zbierať (opt-in formulár polia).""",
      receiver_role="child",
      receiver_name=email_handle['name']
  )
  ```

#### 9:30–11:00 | Automatizácia odosielania – integrácia s ESP
- **Povedať:** „Máš emaily. Čo teraz? Ako ich dostať do tvojho emailového nástroja?"
- **Ukázať workflow exportu:**
  ```python
  # Export do formátu pre rôzne ESP (Email Service Provider)
  await agent_message.send(
      """Exportuj všetky emailové sekvencie do týchto formátov:
      1. CSV pre import do ConvertKit/Mailchimp (stĺpce: sequence, email_num,
         subject, preheader, body, cta)
      2. JSON pre API import
      3. Plain text pre manuálne copy-paste (s jasnými oddeľovačmi)

      Pošli všetky 3 formáty.""",
      receiver_role="child",
      receiver_name=email_handle['name']
  )
  ```
- **Povedať:** „Plus – Prime Agent má priamu integráciu s Google Workspace. Ak používaš Gmail, môžeš emaily odosielať priamo cez `gws-gmail-send` skill."

#### 11:00–12:00 | Meranie a optimalizácia
- **Povedať:** „Emailová sekvencia nie je 'nastav a zabudni'. Musíš merať a optimalizovať."
- **Ukázať kľúčové metriky:**
  - Open rate (cieľ: >40% pre welcome, >25% pre nurture)
  - Click rate (cieľ: >5% pre welcome, >3% pre nurture)
  - Unsubscribe rate (cieľ: <0.5% na email)
  - Conversion rate (cieľ: závisí od ponuky)
- **Povedať:** „Ak niektorý email vypadáva, nechaj agenta navrhnúť vylepšenia:"
  ```python
  await agent_message.send(
      """Email č. 3 v nurture sekvencii má nízky open rate (18%).
      Navrhni 5 alternatívnych subject lines a 3 úpravy tela emailu,
      ktoré by mohli zvýšiť otvorenosť a engagement.""",
      receiver_role="child",
      receiver_name=email_handle['name']
  )
  ```

### Kľúčové body
- 3 typy sekvencií: Welcome (aktivácia), Nurture (vzdelávanie), Re-engagement (prebudenie)
- Každý email: subject line + preheader + body + jeden jasný CTA
- Subject line = 7 typov (zvedavosť, číslo, personalizované, urgency, how-to, contrarian, krátke)
- Personalizácia cez merge tags: `{first_name}`, `{primary_language}`, `{pain_point}`
- Export do CSV/JSON pre jednoduchý import do ConvertKit, Mailchimp, atď.

### Domáca úloha
1. Spusti Email Campaign Agenta a nechaj ho vygenerovať všetky 3 sekvencie pre tvoj produkt
2. Vyber jednu sekvenciu, nahraj ju do svojho ESP (alebo si ju priprav ako drafty v Gmaile)
3. Pre 3 emaily vymysli A/B test subject lines – nechaj agenta vygenerovať alternatívy a vyber lepšiu
4. Nastav si tracking (aspoň open rate) a odmeraj výkon po 7 dňoch

---

## Lekcia 4: Agent pre SEO a content stratégiu
**Dĺžka videa:** 15 minút

### Detailný obsah / scenár

#### 0:00–2:00 | SEO v ére AI – čo sa mení
- **Povedať:** „SEO prechádza najväčšou transformáciou od vzniku Googlu. AI Overviews, ChatGPT search, Perplexity – tradičné SEO už nestačí."
- **Ukázať novú realitu:**
  - Google AI Overviews: odpovedá priamo, používatelia menej klikajú na linky
  - ChatGPT/SearchGPT: nový typ vyhľadávania – konverzačné, kontextové
  - Perplexity: cituje zdroje – ak nie si citovaný, neexistuješ
  - Claude/Gemini: LLM si budujú vlastné znalostné bázy
- **Povedať:** „Preto potrebuješ SEO agenta, ktorý rozumie obom svetom: tradičnému SEO (Google) aj AI SEO (LLMs)."

#### 2:00–4:00 | Komponenty SEO a content stratégie
- **Povedať:** „SEO stratégia má 5 komponentov. Agent musí pokryť každý z nich."
- **Ukázať framework (na slide):**
  ```
  SEO & Content Strategy Framework

  1. AUDIT – technické SEO, on-page, off-page
  2. KEYWORDS – prieskum, klastre, intent
  3. CONTENT – obsahový plán, témy, formáty
  4. AI VISIBILITY – llms.txt, štruktúrované dáta, citovateľnosť
  5. MONITORING – rank tracking, traffic, konverzie
  ```
- **Povedať:** „Dnešný agent pokryje prvých 4. Monitoring je priebežný – na to použijeme marketingové slučky (Modul 5, Lekcia 6)."

#### 4:00–6:30 | Krok 1: SEO Audit s agentom
- **Povedať:** „Prvý krok každej SEO stratégie je audit. Zistíme, kde sme."
- **Ukázať SEO audit agenta:**
  ```python
  seo_audit_handle = await rlm(f"""
  Si senior SEO špecialista s 15-ročnou praxou.

  ## ÚLOHA:
  Urob kompletný SEO audit domény {moja_domena}.

  ### Čo skontrolovať:

  **Technické SEO:**
  - Rýchlosť načítania (Core Web Vitals odhad)
  - Mobilná responzívnosť
  - SSL certifikát
  - XML sitemap
  - Robots.txt
  - Kanonické URL
  - Broken links (404)

  **On-Page SEO:**
  - Title tagy (dĺžka, keywords, unikátnosť)
  - Meta descriptions
  - H1-H6 hierarchia
  - Keyword density a relevance
  - Obrázky (alt texty, veľkosť, formát)
  - Interné linkovanie

  **Obsahový audit:**
  - Top 10 stránok podľa návštevnosti (ak vieš zistiť)
  - Duplicitný obsah
  - Thin content (menej ako 300 slov)
  - Chýbajúce kľúčové stránky

  **Off-Page SEO:**
  - Spätné odkazy (odhad)
  - Doménová autorita (odhad)

  Pre každý problém: priorita (HIGH/MEDIUM/LOW), odhadovaný dopad, konkrétny fix.

  Výstup: Markdown report s executive summary (TOP 5 problémov) a detailným zoznamom.
  Pošli výsledok rodičovi cez agent_message.send().
  """)

  print(f"✅ SEO Audit agent spustený: {seo_audit_handle['name']}")
  ```

#### 6:30–9:00 | Krok 2: Keyword Research a obsahový plán
- **Povedať:** „Máme audit. Vieme, čo treba opraviť. Teraz potrebujeme vedieť, na čo cieliť."
- **Ukázať Keyword + Content agenta:**
  ```python
  content_strategy_handle = await rlm(f"""
  Si content stratég a SEO špecialista.

  ## KONTEXT:
  Doména: {moja_domena}
  Téma: AI agenti pre vývojárov, Prime Agent, automatizácia developmentu
  Cieľovka: Vývojári, tech leads, CTOs

  ## ÚLOHA:
  Vytvor kompletnú SEO content stratégiu.

  ### Časť 1: Keyword Research
  - Primárne keywords (high volume, high intent): 5–10
  - Sekundárne keywords (medium volume, long-tail): 15–20
  - Otázky, ktoré ľudia hľadajú (People Also Ask, "ako", "prečo", "čo je"): 10–15
  - Pre každé keyword: odhadovaný search volume (ak dostupný), intent (informačný/komerčný/navigačný), obtiažnosť

  ### Časť 2: Content Clusters
  - 4–5 obsahových klastrov (pillar pages + podporné články)
  - Pre každý klaster: pillar téma, 5–8 podporných tém
  - Interné linkovanie medzi klastrami

  ### Časť 3: Content Calendar (90 dní)
  - Týždenný plán: aký typ obsahu, aké keyword, aký formát
  - Mix: blog posty, how-to guides, porovnania, prípadové štúdie, listicles
  - Pre každý kus obsahu: pracovný názov, primárne keyword, sekundárne keywords, odhadovaná dĺžka

  ### Časť 4: Technické odporúčania
  - Návrh URL štruktúry
  - Návrh title tagov a meta descriptions pre top 10 stránok
  - Schema markup odporúčania (Article, FAQ, HowTo, BreadcrumbList)

  Výstup: Markdown dokument. Pošli výsledok rodičovi cez agent_message.send().
  """)

  print(f"✅ Content Strategy agent spustený: {content_strategy_handle['name']}")
  ```

#### 9:00–11:00 | Krok 3: AI SEO – llms.txt a OKF
- **Povedať:** „Tradičné SEO je len polovica. Druhá polovica je byť viditeľný pre AI."
- **Povedať:** „LLM (ChatGPT, Claude, Gemini, Perplexity) čítajú web inak ako Google. Potrebujú štruktúrovaný, ľahko stráviteľný obsah."
- **Ukázať AI SEO komponenty:**

**1. llms.txt súbor**
```markdown
# llms.txt pre mojadomena.sk
> Kurzy a návody o AI agentoch pre vývojárov. Nauč sa Prime Agent, automatizáciu a 10x produktivitu.

## Dokumentácia
- [Prime Agent - Kompletný návod](https://mojadomena.sk/prime-agent-navod): Inštalácia, konfigurácia, prvé kroky, skills, subagenti
- [Skills Referencia](https://mojadomena.sk/skills): Všetky dostupné skilly a ich použitie

## Blog
- [Prečo každý vývojár potrebuje AI agenta](https://mojadomena.sk/blog/ai-agent-pre-vyvojarov): Analýza prínosov, porovnanie nástrojov, prípadové štúdie
- [10 chýb pri používaní AI v kóde](https://mojadomena.sk/blog/chyby-ai-kod): Praktické tipy na opravu
```

**2. Štruktúrované dáta (Schema.org)**
```json
{
  "@type": "Article",
  "headline": "Prečo každý vývojár potrebuje AI agenta",
  "author": {"@type": "Person", "name": "Marek"},
  "datePublished": "2025-06-15",
  "description": "Analýza prínosov AI agentov pre vývojárov"
}
```

- **Ukázať AI SEO agenta:**
  ```python
  ai_seo_handle = await rlm(f"""
  Si špecialista na AI SEO – optimalizáciu pre LLM a AI vyhľadávače.

  ## ÚLOHA:
  Na základe tejto content stratégie:
  {content_strategy_output}

  Vytvor:
  1. **llms.txt súbor** – prehľadný, štruktúrovaný, s popismi čo je na každej stránke
  2. **OKF (Open Knowledge Format) balík** – štruktúrovaný export kľúčového obsahu pre LLM
  3. **Schema markup** pre top 5 stránok (JSON-LD formát):
     - Article schema
     - FAQ schema (kde relevantné)
     - HowTo schema (kde relevantné)
     - BreadcrumbList schema
  4. **AI citovateľnosť checklist:**
     - Ktoré stránky sú "citeable" (faktické, autoritatívne) a ktoré treba vylepšiť
     - Odporúčania pre zvýšenie šance na citovanie LLM

  Výstup: Markdown s kódovými blokmi pre JSON-LD a llms.txt.
  Pošli výsledok rodičovi cez agent_message.send().
  """)

  print(f"✅ AI SEO agent spustený: {ai_seo_handle['name']}")
  ```
- **Povedať:** „llms.txt sa umiestňuje do koreňa domény (`/llms.txt`). Je to ako robots.txt, ale pre AI. Štandard navrhnutý Jeremym Howardom a rýchlo sa rozširuje."

#### 11:00–13:00 | Krok 4: Programatické SEO stránky
- **Povedať:** „Ak chceš škálovať, potrebuješ programatické SEO. To znamená generovať stovky cielených stránok z template + data."
- **Ukázať príklad:**
  ```python
  programmatic_seo_handle = await rlm(f"""
  Si špecialista na programatické SEO.

  Na základe keyword researchu:
  {keyword_research_output}

  Navrhni a vytvor:
  1. **3 typy programatických stránok:**
     - "[Nástroj] alternativa" (napr. "Copilot alternativa", "Cursor alternativa")
     - "[Téma] pre [rola]" (napr. "AI agenti pre CTO", "AI agenti pre freelancerov")
     - "[Keyword] návod" (napr. "Prime Agent inštalácia návod", "Prime Agent skills návod")

  2. Pre každý typ:
     - Template (HTML/Markdown štruktúra)
     - Dátový model (aké premenné sa menia)
     - 5 konkrétnych príkladov stránok (plne vyplnených)

  3. URL štruktúra a interné linkovanie medzi programatickými stránkami

  Výstup: Markdown s ukážkami. Pošli výsledok rodičovi.
  """)

  print(f"✅ Programmatic SEO agent spustený: {programmatic_seo_handle['name']}")
  ```

#### 13:00–15:00 | Integrácia výsledkov a finálny SEO plán
- **Povedať:** „Teraz všetko spojíme do jedného SEO master plánu."
- **Ukázať finálnu integráciu:**
  ```python
  # Kompilácia SEO Master Plánu
  seo_master_plan = f"""
  # 🎯 SEO Master Plan – {moja_domena}

  ## 1. Audit (Čo treba opraviť)
  {seo_audit_output}

  ## 2. Keyword & Content Strategy (Na čo cieliť)
  {content_strategy_output}

  ## 3. AI Visibility (Byť viditeľný pre LLM)
  {ai_seo_output}

  ## 4. Programatické SEO (Škálovanie)
  {programmatic_seo_output}

  ---

  ## 📅 90-dňový Akčný Plán

  ### Mesiac 1: Opraviť základy
  - Týždeň 1–2: Technické SEO opravy (podľa auditu)
  - Týždeň 3: Nasadiť llms.txt a schema markup
  - Týždeň 4: Optimalizovať top 10 stránok

  ### Mesiac 2: Tvoriť obsah
  - Publikovať 8 blog postov podľa content calendar
  - Spustiť prvé programatické stránky
  - Začať budovať spätné odkazy

  ### Mesiac 3: Škálovať a optimalizovať
  - Publikovať ďalších 8 blog postov
  - Rozšíriť programatické SEO o ďalšie typy stránek
  - Vyhodnotiť traffic, ranky a konverzie
  """

  with open('/Users/abra/Developer/seo-master-plan.md', 'w') as f:
      f.write(seo_master_plan)

  print("✅ SEO Master Plan hotový!")
  ```

### Kľúčové body
- Moderné SEO = tradičné SEO (Google) + AI SEO (LLMs, AI Overviews)
- SEO stratégia má 5 komponentov: Audit → Keywords → Content → AI Visibility → Monitoring
- llms.txt je nový štandard pre AI čitateľnosť (umiestniť do koreňa domény)
- Programatické SEO = template + data = stovky cielených stránok
- 90-dňový plán: Mesiac 1 opravy, Mesiac 2 obsah, Mesiac 3 škálovanie

### Domáca úloha
1. Spusti SEO Audit agenta na svoju doménu (alebo ak nemáš doménu, na akúkoľvek známu)
2. Vytvor llms.txt súbor podľa vzoru a nahraj ho do koreňa svojej domény (`/llms.txt`)
3. Spusti Content Strategy agenta a vytvor 90-dňový obsahový kalendár
4. Vyber si 1 keyword z researchu a napíš naň blog post. Optimalizuj ho podľa SEO agentových odporúčaní.

---

## Lekcia 5: Agent pre prieskum konkurencie
**Dĺžka videa:** 10 minút

### Detailný obsah / scenár

#### 0:00–1:30 | Prečo potrebuješ prieskum konkurencie
- **Povedať:** „Väčšina ľudí robí prieskum konkurencie zle. Pozrú si homepage, možno pricing, a hotovo. To nestačí."
- **Povedať:** „Dobrý prieskum konkurencie ti dá: positioning gaps, obsahové diery, cenové príležitosti, a čo najviac – nápady, čo spraviť INAK."
- **Ukázať framework:**
  ```
  Prieskum konkurencie = 
    Profilovanie (čo robia)
    + Positioning (ako sa prezentujú)
    + Obsahová analýza (čo publikujú)
    + SEO analýza (na aké keywords cielia)
    + SWOT (silné a slabé stránky)
  ```
- **Povedať:** „Agent toto všetko spraví za 5 minút. Na jedného konkurenta."

#### 1:30–4:00 | Vytvorenie Competitor Research Agenta – Live Demo
- **Povedať:** „Poďme vytvoriť agenta, ktorý spraví kompletný profil konkurenta."
- **Ukázať na obrazovke:**
  ```python
  competitor_handle = await rlm(f"""
  Si konkurenčný analytik a marketér. Tvojou úlohou je vytvoriť detailný profil konkurenta.

  ## KONKURENT NA ANALÝZU:
  - Názov: {competitor_name}
  - URL: {competitor_url}
  - Čo ponúka: {competitor_offering}

  ## TVOJ PRODUKT (pre porovnanie):
  - Názov: Prime Agent Masterclass
  - URL: mojakurzova-stranka.sk
  - Ponuka: Online kurz pre vývojárov o AI coding agentoch

  ## ÚLOHA:
  Vytvor kompletný profil konkurenta.

  ### 1. ZÁKLADNÝ PROFIL
  - Názov, URL, rok založenia (odhad)
  - Tím / zakladatelia
  - Funding / revenue (ak verejné)
  - Misia a vízia (z about page)

  ### 2. PRODUKTOVÁ ANALÝZA
  - Hlavné features a funkcionalita
  - Unikátne selling pointy (USP)
  - Technologický stack (odhad podľa indícií)
  - UX/UI dojem (ak máš prístup)
  - Pricing model a ceny (ak verejné)
  - Cieľová skupina (podľa jazyka, imagov, messaggingu)

  ### 3. POSITIONING A MESSAGING
  - Hlavný headline / value proposition
  - Tone of voice (formálny, priateľský, technický, ...)
  - Aké emócie sa snaží vyvolať (dôvera, FOMO, autorita, ...)
  - Na aké pain pointy cieli
  - Ako sa odlišuje od alternatív (podľa ich vlastných slov)

  ### 4. OBSAHOVÁ ANALÝZA
  - Blog: frekvencia publikovania, témy, kvalita, dĺžka
  - Social media: ktoré platformy, frekvencia, engagement
  - Email marketing: opt-in incentíva, typy sekvencií (ak viditeľné)
  - Lead magnety: čo ponúkajú za email
  - Webináre / eventy / podcast

  ### 5. SEO ANALÝZA
  - Na aké keywords cielia (odhad podľa title tagov, H1, obsahu)
  - Odhadovaná mesačná návštevnosť
  - Top stránky (odhad)
  - Spätné odkazy (odhad)

  ### 6. SWOT ANALÝZA (z nášho pohľadu)
  - Strengths: Čo robia fakt dobre, v čom sú lepší ako my
  - Weaknesses: Kde zaostávajú, čo im chýba
  - Opportunities: Čo môžeme využiť, kde je medzera na trhu
  - Threats: Čím nás ohrozujú, na čo si dať pozor

  ### 7. AKČNÉ ODPORÚČANIA
  - 5 konkrétnych vecí, ktoré môžeme spraviť lepšie/inak na základe tejto analýzy
  - 3 veci, ktoré robia dobre a oplatí sa inšpirovať (nie kopírovať)
  - 2 veci, ktoré robia zle – a my to využijeme

  Celý výstup v prehľadnom markdowne. Buď konkrétny, nie vágny.
  Pošli výsledok rodičovi cez agent_message.send().
  """)

  print(f"✅ Competitor Research agent spustený: {competitor_handle['name']}")
  ```

#### 4:00–6:00 | Paralelný prieskum viacerých konkurentov
- **Povedať:** „Jeden konkurent je fajn. Ale skutočný prehľad získaš, až keď analyzuješ 3–5 konkurentov paralelne."
- **Ukázať paralelný setup:**
  ```python
  # Zoznam konkurentov na analýzu
  competitors = [
      {"name": "Cursor AI", "url": "https://cursor.com", "offering": "AI code editor"},
      {"name": "GitHub Copilot", "url": "https://github.com/features/copilot", "offering": "AI coding assistant"},
      {"name": "Codeium", "url": "https://codeium.com", "offering": "AI code completion"},
      {"name": "Tabnine", "url": "https://tabnine.com", "offering": "AI code assistant"},
      {"name": "Amazon CodeWhisperer", "url": "https://aws.amazon.com/codewhisperer", "offering": "AI coding companion"},
  ]

  # Spusti analyzu všetkých PARALELNE
  competitor_handles = {}
  for comp in competitors:
      competitor_handles[comp['name']] = await rlm(f"""
      Si konkurenčný analytik. Vytvor detailný profil konkurenta.

      Konkurent: {comp['name']}
      URL: {comp['url']}
      Ponuka: {comp['offering']}

      Tvoj produkt (pre porovnanie): Prime Agent Masterclass

      Vytvor profil podľa štandardnej štruktúry:
      1. Základný profil, 2. Produktová analýza, 3. Positioning,
      4. Obsahová analýza, 5. SEO, 6. SWOT, 7. Akčné odporúčania.

      Výstup v markdowne. Pošli rodičovi cez agent_message.send().
      """)
      print(f"✅ Spustená analýza: {comp['name']}")

  print(f"\n🚀 {len(competitor_handles)} konkurentov sa analyzuje paralelne!")
  ```

#### 6:00–8:00 | Syntéza – Competitive Landscape Report
- **Povedať:** „Jednotlivé profily sú super. Ale skutočnú hodnotu má syntéza – keď všetky dáta spojíš do jedného prehľadu."
- **Ukázať syntézneho agenta:**
  ```python
  # Po získaní všetkých profilov...
  synthesis_handle = await rlm(f"""
  Si hlavný strategický analytik.

  Máš k dispozícii profily {len(competitor_handles)} konkurentov:
  {all_competitor_profiles}

  ## ÚLOHA:
  Vytvor "Competitive Landscape Report" – syntézu všetkých profilov.

  ### 1. EXECUTIVE SUMMARY
  - 1 odstavec: aký je trh, kto dominuje, kde sú príležitosti

  ### 2. POROVNÁVACIA TABUĽKA
  | Feature | My | Konkurent 1 | Konkurent 2 | ... |
  |---------|-----|-------------|-------------|-----|
  | Cena | | | | |
  | Hlavný USP | | | | |
  | ... | | | | |

  ### 3. POZICIONING MAPA
  - 2 osi (napr. "Cena" vs "Features", alebo "Pre začiatočníkov" vs "Pre expertov")
  - Kde je každý hráč

  ### 4. GAP ANALYSIS
  - Čo robia všetci, čo nikto nerobí, čo robíme len my

  ### 5. ODPORÚČANIA PRE NAŠU STRATÉGIU
  - Positioning odporúčanie
  - Produktové odporúčanie
  - Marketingové odporúčanie
  - Cenové odporúčanie

  ### 6. BATTLE CARD
  - Pre každého kľúčového konkurenta: 3 vety pre sales tím

  Výstup: Markdown. Pošli rodičovi cez agent_message.send().
  """)

  print(f"✅ Synthesis agent spustený: {synthesis_handle['name']}")
  ```

#### 8:00–10:00 | Automatizovaný monitoring konkurencie
- **Povedať:** „Konkurencia sa mení. Preto potrebuješ monitoring."
- **Ukázať monitoring setup:**
  ```python
  monitoring_handle = await rlm("""
  Si špecialista na monitoring konkurencie.

  ## ÚLOHA:
  Vytvor plán automatizovaného monitoringu konkurencie.

  ### 1. ČO MONITOROVAŤ
  - Zmeny na webe (nový obsah, zmena cien, nové features)
  - Nové blog posty a obsah
  - Sociálne siete (nové kampane, zmena messaggingu)
  - Zmeny v teame (kľúčové hiringy, odchody)
  - Recenzie a hodnotenia (G2, Capterra, Reddit)

  ### 2. AKO MONITOROVAŤ S PRIME AGENTOM
  - Týždenný monitoring skript (subagent, ktorý skontroluje všetkých konkurentov)
  - Template pre weekly competitive brief (1 strana, najdôležitejšie zmeny)
  - Notifikačné pravidlá (čo eskalovať okamžite, čo v týždennom reporte)

  ### 3. SAMPLE WEEKLY BRIEF
  - Vytvor príklad weekly competitive briefu pre tento týždeň:
    - Hlavné zmeny u konkurentov
    - Čo to znamená pre nás
    - Odporúčané akcie

  Výstup: Markdown. Pošli rodičovi cez agent_message.send().
  """)

  print(f"✅ Monitoring agent spustený: {monitoring_handle['name']}")
  ```

### Kľúčové body
- Prieskum konkurencie = Profil + Positioning + Obsah + SEO + SWOT + Akčné odporúčania
- 5 konkurentov paralelne = 5x rýchlejšie (namiesto 1 dňa, 15 minút)
- Syntéza je kľúčová – jednotlivé profily sú dáta, syntéza je stratégia
- Battle card: 3 vety pre sales tím, aby vedeli reagovať na každého konkurenta
- Automatizovaný monitoring = týždenný subagent, ktorý kontroluje zmeny

### Domáca úloha
1. Spusti Competitor Research Agenta na 3 tvojich konkurentov
2. Spusti Synthesis Agenta a vytvor Competitive Landscape Report
3. Z reportu si vyber 3 akčné odporúčania a implementuj aspoň 1
4. Nastav si pripomienku: o 2 týždne znova spustiť monitoring a porovnať, čo sa zmenilo

---

## Lekcia 6: Praktický projekt – 30-dňová marketingová kampaň na autopilota
**Dĺžka videa:** 6 minút

### Detailný obsah / scenár

#### 0:00–1:30 | Architektúra 30-dňovej kampane
- **Povedať:** „Toto je finále Modulu 5. Spojíme všetko, čo sme sa naučili, do jednej autonómnej 30-dňovej marketingovej kampane."
- **Ukázať architektúru:**
  ```
  🎯 30-DAY MARKETING AUTOPILOT

  TÝŽDEŇ 1: FOUNDATION
  ├── Deň 1: SEO Audit + Technické opravy
  ├── Deň 2: Competitive Research (5 konkurentov)
  ├── Deň 3: Content Strategy + Keyword Plan
  ├── Deň 4: LinkedIn Content (20 postov)
  └── Deň 5: Email Welcome Sekvencia

  TÝŽDEŇ 2: CONTENT ENGINE
  ├── Deň 6–7: Blog Post 1 + 2
  ├── Deň 8: Twitter Thread 1
  ├── Deň 9: LinkedIn Post (z threadu)
  ├── Deň 10: Email Nurture 1–2

  TÝŽDEŇ 3: DISTRIBUTION
  ├── Deň 11–12: Blog Post 3 + 4
  ├── Deň 13: Twitter Thread 2
  ├── Deň 14: LinkedIn Post (z threadu)
  ├── Deň 15: Email Nurture 3–4

  TÝŽDEŇ 4: AMPLIFICATION
  ├── Deň 16–17: Programmatic SEO Pages
  ├── Deň 18: Cross-platform Repurposing
  ├── Deň 19: Community Engagement
  ├── Deň 20: Email Nurture 5 + Pitch

  TÝŽDEŇ 5 (BONUS): ANALYSIS
  ├── Deň 21–25: Monitoring + Analytics
  ├── Deň 26–28: A/B Test Variations
  ├── Deň 29: Competitive Update
  └── Deň 30: Retro + Next Month Plan
  ```
- **Povedať:** „Toto nie je teória. Každý deň má konkrétne úlohy. A každú úlohu spraví agent."

#### 1:30–3:00 | Implementácia – Master Orchestrator Agent
- **Povedať:** „Vytvoríme 'Master Orchestrator' – agenta, ktorý riadi celú kampaň."
- **Ukázať na obrazovke:**
  ```python
  orchestrator_handle = await rlm("""
  Si Marketing Operations Manager. Riadíš 30-dňovú marketingovú kampaň
  pre produkt "Prime Agent Masterclass".

  ## TVOJA ÚLOHA:
  Spusti a skoordinuj všetkých subagentov potrebných pre 30-dňovú kampaň.

  ## PRODUKT INFO:
  - Názov: Prime Agent Masterclass
  - Typ: Online kurz pre vývojárov
  - Cieľovka: Vývojári, tech leads, CTOs
  - Hlavný benefit: 10x rýchlejší vývoj s AI agentmi
  - Cena: €499 (early bird: €349)
  - Doména: mojakurzova-stranka.sk

  ## FÁZA 1: FOUNDATION (spusti teraz)
  1. Spusti SEO audit agenta
  2. Paralelne spusti Competitive Research pre 5 konkurentov
  3. Po dokončení oboch: spusti Content Strategy agenta
  4. Po stratégii: paralelne spusti LinkedIn Content agenta a Email agenta

  ## FÁZA 2–4: (spúšťaj postupne podľa harmonogramu)
  - Blog posty: 2x týždenne
  - Twitter thready: 1x týždenne
  - LinkedIn posty: 3x týždenne
  - Emaily: podľa nurture sekvencie
  - Repurposing: z každého blog postu sprav social + email

  ## FÁZA 5: ANALÝZA (Deň 21–30)
  - Zber metriík
  - A/B test variácií
  - Competitive update
  - Retrospektíva a plán na ďalší mesiac

  ## PRAVIDLÁ:
  - Každá úloha = samostatný subagent
  - Nezávislé úlohy spúšťaj paralelne
  - Závislé úlohy reťaz postupne
  - Každý subagent nech pošle výsledok a ty ho zaznamenaj
  - Vytvor "campaign-log.md" a priebežne ho aktualizuj

  Začni Fázou 1 teraz. Spusti SEO audit a Competitive Research paralelne.
  Pošli mi priebežný status po každej dokončenej fáze.
  """)
  ```

#### 3:00–4:30 | Campaign Tracker a Dashboard
- **Povedať:** „Dobrý orchestrátor potrebuje dashboard. Vytvorme jednoduchý campaign tracker."
- **Ukázať tracker štruktúru:**
  ```markdown
  # 📊 30-Day Campaign Tracker – Prime Agent Masterclass

  **Spustené:** {start_date}
  **Dnes je:** {current_date}
  **Progress:** {completed_tasks}/{total_tasks} ({progress_percent}%)

  ---

  ## ✅ Dokončené úlohy
  | # | Deň | Úloha | Agent | Výstup | Status |
  |---|-----|-------|-------|--------|--------|
  | 1 | 1 | SEO Audit | seo-agent-1 | seo-audit.md | ✅ |
  | 2 | 1 | Competitor Research | comp-agent-1..5 | competitor-profiles/ | ✅ |
  | 3 | 3 | Content Strategy | strategy-agent-1 | content-strategy.md | ✅ |
  | 4 | 4 | LinkedIn Content | linkedin-agent-1 | linkedin-posts.md | ✅ |
  | 5 | 5 | Welcome Emails | email-agent-1 | welcome-sequence.md | ✅ |

  ## 🔄 Prebiehajúce úlohy
  | # | Deň | Úloha | Agent | Spustené |
  |---|-----|-------|-------|----------|
  | 6 | 6 | Blog Post 1 | copy-agent-1 | 14:30 |

  ## 📅 Nasledujúce úlohy
  | # | Deň | Úloha | Závisí na |
  |---|-----|-------|-----------|
  | 7 | 7 | Blog Post 2 | #6 |
  | 8 | 8 | Twitter Thread 1 | #3 |

  ---

  ## 📈 Metriky
  - SEO skóre: {seo_score}/100 (pred: {previous_seo_score})
  - Vygenerovaný obsah: {content_pieces} kusov
  - Emaily v sekvencii: {email_count}
  - LinkedIn posty: {linkedin_count}
  - Twitter thready: {thread_count}
  ```

#### 4:30–6:00 | Spustenie, monitoring a next steps
- **Povedať:** „Kampaň spustená. Čo teraz?"
- **Ukázať monitoring rutinu:**
  ```python
  # Denná monitoring rutina (5 minút ráno)
  async def daily_checkin():
      # 1. Skontroluj progress tracker
      with open('campaign-tracker.md', 'r') as f:
          tracker = f.read()
      print(tracker[:500])  # Sumár

      # 2. Skontroluj, či všetci agenti dobehli
      children = await rlm.list_subagents()
      for child in children:
          if child['status'] == 'running':
              print(f"⏳ {child['name']} stále beží...")

      # 3. Ak sú dokončené úlohy na dnes, spusti zajtrajšie
      # ...

      # 4. Pošli follow-up ak niekto mešká
      # ...

  await daily_checkin()
  ```
- **Povedať:** „Toto je krása – 5 minút denne namiesto 8 hodín. Zvyšok spravia agenti."
- **Povedať:** „Čo ďalej po 30 dňoch?"
  - Analyzuj výsledky: čo fungovalo, čo nie
  - Iteruj: uprav obsahovú stratégiu, vylepši SEO
  - Škáluj: pridaj ďalšie kanály (YouTube, podcast, webináre)
  - Automatizuj ešte viac: premeň kampaň na marketing-loop (beží donekonečna)
- **Povedať:** „Dokončil si Modul 5. Už nie si len používateľ Prime Agenta. Si marketingový riaditeľ armády agentov."

### Kľúčové body
- 30-dňová kampaň = 5 fáz (Foundation → Content → Distribution → Amplification → Analysis)
- Master Orchestrator = agent, ktorý riadi všetkých ostatných agentov
- Campaign Tracker = živý dashboard, ktorý ukazuje progress
- Denná rutina: 5 minút kontroly, zvyšok robia agenti
- Po 30 dňoch: analyzuj, iteruj, škáluj, automatizuj ďalej

### Domáca úloha
1. Spusti Master Orchestrator agenta a nechaj ho vykonať Fázu 1 (Foundation) – SEO audit + Competitive Research + Content Strategy + LinkedIn + Emaily
2. Vytvor si vlastný Campaign Tracker (markdown súbor) a manuálne doň zapisuj progress počas 7 dní
3. Na konci týždňa sprav mini-retrospektívu: čo fungovalo, čo nie, čo zlepšiť
4. Priprav si plán na reálnu 30-dňovú kampaň pre svoj projekt – s konkrétnymi úlohami, termínmi a metrikami

---

*Koniec Modulu 4 a Modulu 5. V Module 6 sa naučíš automatizovať predaj a zákaznícku podporu.*
