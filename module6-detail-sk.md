# Prime Agent Masterclass – Modul 6: Automatizácia predaja a supportu

## Prehľad modulu

**Cieľ modulu:** Po absolvovaní tohto modulu budeš vedieť kompletne automatizovať predajný proces – od vyhľadávania leadov cez cold outreach až po zákaznícku podporu a follow-up sekvencie. Pomocou Prime Agenta a jeho špecializovaných skillov vybuduješ end-to-end pipeline, ktorá šetrí desiatky hodín manuálnej práce.

**Celková dĺžka:** 55 minút videa + domáce úlohy

---

## Lekcia 1: Agent pre vyhľadávanie leadov
**Dĺžka videa:** 12 minút

### Detailný obsah / scenár

#### 0:00–1:00 | Úvod a hook
- **Povedať:** "Viete, čo zaberie obchodníkovi najviac času? Hľadanie tých správnych ľudí, ktorým má zavolať. Dnes si postavíme agenta, ktorý to spraví za neho – za 2 minúty namiesto 2 hodín."
- **Ukázať rýchle demo:** Agent dostane zadanie "nájdi 50 SaaS firiem v Berlíne do 50 zamestnancov, ktoré práve expandujú", spustí vyhľadávanie a vráti štruktúrovaný zoznam.

#### 1:00–3:30 | Čo znamená prospecting a prečo ho automatizovať
- **Povedať:** Prospecting je proces vyhľadávania a kvalifikácie potenciálnych zákazníkov. V B2B svete je to základ celého predaja.
- **Kľúčové body:**
  - Manuálny prospecting = 60-70% času obchodníka ide do researchu
  - Automatizácia = obchodník sa venuje len uzatváraniu obchodov
  - Agent dokáže paralelne spracovať desiatky zdrojov (LinkedIn, web, databázy)
- **Ukázať skill `prospecting`:**
  ```bash
  # Otvoríme skill v agentovi
  # Prime Agent: "Použi skill prospecting a nájdi mi..."
  ```

#### 3:30–7:00 | Definovanie ICP a vyhľadávacích kritérií
- **Povedať:** "Predtým než agenta pustíme do sveta, musíme mu povedať, koho hľadá. Toto je **ICP – Ideal Customer Profile**."
- **Prejsť štruktúru ICP zadania:**
  - **Odvetvie:** SaaS, e-commerce, fintech, health-tech...
  - **Veľkosť firmy:** počet zamestnancov, revenue range
  - **Lokalita:** krajina, mesto, remote-first
  - **Technológie:** aký stack používajú (napr. "firmy používajúce AWS a React")
  - **Signály:** nedávno získali funding, expandujú, menili CTO...
- **Ukázať na obrazovke – príklad promptu:**
  ```
  Nájdi mi 50 B2B SaaS firiem v DACH regióne, ktoré:
  - majú 10–100 zamestnancov
  - používajú Kubernetes
  - za posledných 6 mesiacov získali Series A alebo B
  - majú technického CTO (nie outsourcovaný vývoj)

  Pre každú firmu vráť: názov, web, LinkedIn URL, odhadovaný revenue,
  technologický stack, meno CTO/VP Engineering (ak je dostupné),
  a signál, prečo by ich náš produkt mohol zaujímať.
  ```
- **Povedať:** "Čím detailnejšie ICP, tým kvalitnejší výstup. Agent použije `websearch` na viacero zdrojov a dáta spojí."

#### 7:00–9:30 | Spustenie agenta a čítanie výstupu
- **Spustiť agenta s reálnym príkladom:**
  ```bash
  # V termináli:
  prime-agent
  # Zadanie: "Použi skill prospecting. Nájdi 20 e-commerce firiem..."
  ```
- **Komentovať, čo agent robí:**
  - "Agent spúšťa websearch na LinkedIn, Crunchbase, a Google"
  - "Zbierajú sa dáta z viacerých zdrojov"
  - "Agent deduplikuje a čistí výsledky"
- **Ukázať výstup – tabuľka v Markdowne alebo CSV:**
  ```
  | Názov | Web | LinkedIn | Veľkosť | Technológie | Signál |
  |-------|-----|----------|---------|-------------|--------|
  | ShopFlow | shopflow.io | /company/shopflow | 45 zam. | AWS, React | Series A v marci 2025 |
  ...
  ```
- **Povedať:** "Tento výstup môžeme rovno poslať do CRM alebo použiť ako vstup pre cold outreach v Lekcii 2."

#### 9:30–11:00 | Uloženie a export leadov
- **Ukázať, ako nechať agenta exportovať dáta:**
  - CSV export: `"Ulož výsledky do /leads/berlin-saas-2025-08.csv"`
  - Google Sheets (cez GWS skills): `"Pošli výsledky do Google Sheets – názov 'Prospecting Q3 2025'"`
  - JSON pre API integráciu: `"Ulož ako JSON pre import do HubSpot"`
- **Povedať:** "Agent nie je len vyhľadávač – je to plnohodnotný data pipeline engine."

#### 11:00–12:00 | Best practices a záver
- **Zhrnutie tipov:**
  - Vždy definuj jasné ICP – "firmy ako náš top zákazník"
  - Použi viacero zdrojov pre krížovú validáciu
  - Dáta vždy nechaj agenta vyčistiť a deduplikovať
  - Exportuj do formátu, ktorý používa tvoj CRM
- **Povedať:** "Toto je prvý krok automatizovaného predaja. V ďalšej lekcii tieto leady oslovíme."

### Kľúčové body
- Prospecting = vyhľadávanie a kvalifikácia leadov podľa ICP
- Skill `prospecting` kombinuje websearch, LinkedIn a verejné databázy
- Detailné ICP zadanie = kvalitný výstup (odvetvie, veľkosť, lokalita, signály)
- Agent deduplikuje, čistí a exportuje dáta do CSV, Google Sheets alebo JSON

### Domáca úloha
1. Definuj ICP pre svoj produkt/službu – napíš aspoň 5 špecifických kritérií (odvetvie, veľkosť, lokalita, technológie, signály)
2. Spusti agenta s `prospecting` skillom a nájdi aspoň 30 leadov podľa svojho ICP
3. Exportuj výsledky do CSV a manuálne skontroluj kvalitu aspoň 10 leadov – koľko z nich je skutočne relevantných?
4. Napíš si zoznam 5 ďalších zdrojov dát, ktoré by si chcel, aby agent prehľadával (okrem LinkedIn a Crunchbase)

---

## Lekcia 2: Agent pre cold outreach
**Dĺžka videa:** 10 minút

### Detailný obsah / scenár

#### 0:00–1:00 | Úvod a hook
- **Povedať:** "V minulej lekcii sme našli leadov. Teraz ich oslovíme – a nie generickým spamom. Agent napíše personalizovaný email pre každého leada. A nie jeden – celú follow-up sekvenciu."
- **Ukázať rýchle demo:** Agent dostane CSV s leadmi a vygeneruje 20 personalizovaných cold emailov s menom, referenciou na ich produkt a konkrétnym dôvodom, prečo im píše.

#### 1:00–3:00 | Psychológia cold emailu – čo funguje v roku 2025
- **Povedať:** "Cold email v roku 2025 nie je o šablónach. Je o relevancii a personalizácii."
- **5 princípov efektívneho cold emailu:**
  1. **Personalizovaný predmet** – nie "Spolupráca", ale "Nápad pre [NázovFirmy] po tom Series A"
  2. **Rešpekt k času** – maximálne 5-6 viet
  3. **Konkrétny dôvod** – prečo práve im a práve teraz
  4. **Jasná CTA** – nie "dajme si kávu", ale "15-minútový call o X"
  5. **Žiadne prílohy v prvom emaile** – zvyšuje spam skóre
- **Ukázať skill `cold-email`:** Agent používa tieto princípy automaticky, keď mu dáme kontext o leadovi.

#### 3:00–5:30 | Prepojenie prospecting → cold email pipeline
- **Povedať:** "Teraz spojíme výstup z Lekcie 1 so skillom `cold-email`."
- **Ukázať na obrazovke flow:**
  ```
  CSV s leadmi → Agent číta CSV → Pre každý riadok:
    1. Analyzuje firmu (web, LinkedIn)
    2. Nájde personalizačný háčik
    3. Vygeneruje email podľa šablóny
    4. Pridá do dávky
  → Výstup: personalizované emaily pre všetkých leadov
  ```
- **Praktický príklad promptu:**
  ```
  Prečítaj súbor /leads/berlin-saas-2025-08.csv.
  Pre každého leada vygeneruj cold email s predmetom a telom.

  O mne: Som founder ProduktX – nástroj na automatické code review 
  pre tímy používajúce Kubernetes. Pomáhame tímom znížiť chybovosť 
  deploymentov o 40 %.

  Personalizácia: Nájdi niečo špecifické o ich produkte alebo tíme
  (napr. používajú Kubernetes, nedávno hiring DevOp-ov).

  Tón: Neformálny, konzultačný, nie predajný.
  Výstup: Markdown tabuľka s leadom a emailom.
  ```

#### 5:30–7:30 | Generovanie variácií a A/B testovanie
- **Povedať:** "Jeden email nestačí. Agent ti vygeneruje viacero variácií pre A/B test."
- **Ukázať, ako požiadať o variácie:**
  ```
  Pre každého leada vytvor 2 verzie emailu:
  - Verzia A: krátka, priamočiara, value-first
  - Verzia B: zvedavostná otázka, problém-first

  Pridaj aj 2 varianty predmetu pre každú verziu.
  ```
- **Povedať:** "Toto je sila agenta – vie vygenerovať 40-60 personalizovaných emailov za pár sekúnd. Manuálne by to trvalo celý deň."
- **Spomenúť skill `ab-testing`:** "Ak chceš ísť ešte hlbšie do testovania, použi skill `ab-testing` na návrh experimentu pre celú kampaň."

#### 7:30–9:00 | Follow-up sekvencia
- **Povedať:** "80 % odpovedí prichádza až po follow-upoch. Agent ti vygeneruje celú sekvenciu."
- **Ukázať štruktúru sekvencie:**
  ```
  Deň 0:  Prvý email (value proposition)
  Deň 3:  Follow-up #1 (pridaná hodnota – článok, tip)
  Deň 7:  Follow-up #2 (social proof – case study)
  Deň 14: Follow-up #3 (posledný pokus – break-up email)
  ```
- **Povedať:** "Každý follow-up je iný – žiadne 'len pripomínam'. Agent pridá novú hodnotu v každom kroku."
- **Spomenúť:** "Detailne sa follow-upom venujeme v Lekcii 5 tohto modulu."

#### 9:00–10:00 | Best practices a záver
- **Povedať:** "Zopakujme si najdôležitejšie:"
  - Vždy daj agentovi kontext o sebe a svojom produkte
  - Personalizácia nie je 'Hi {meno}' – je to relevantný insight o ich biznise
  - Generuj variácie a testuj
  - Cold email je prvý dotyk – buď krátky a hodnotný
- **Povedať:** "V ďalšej lekcii sa pozrieme na to, ako agent zvláda zákaznícku podporu keď už leadov premeníš na zákazníkov."

### Kľúčové body
- Skill `cold-email` generuje personalizované emaily na základe dát o leadoch
- 5 princípov: personalizovaný predmet, stručnosť, konkrétny dôvod, jasná CTA, žiadne prílohy
- Agent generuje viacero variácií pre A/B testovanie
- Celá follow-up sekvencia: deň 0, 3, 7, 14 – každý krok s novou hodnotou
- Prepojenie s `prospecting` tvorí kompletnú pipeline

### Domáca úloha
1. Napíš svoj "o mne / o produkte" odsek (max 3 vety), ktorý dáš agentovi ako kontext
2. Vygeneruj cold emaily pre aspoň 10 leadov z Lekcie 1 – skús obe verzie A/B
3. Vyber 3 emaily a pošli ich manuálne (alebo cez GWS Gmail skill, ak máš nastavený)
4. Napíš si, ktoré predmety a prístupy ti prídu najsilnejšie – toto bude základ tvojej šablóny

---

## Lekcia 3: Agent pre customer support
**Dĺžka videa:** 12 minút

### Detailný obsah / scenár

#### 0:00–1:30 | Úvod a hook
- **Povedať:** "Koľko hodín týždenne tráviš odpovedaním na tie isté otázky? 'Ako resetnem heslo?', 'Kde nájdem faktúru?', 'Prečo mi nejde integrácia?' Dnes ťa týchto otázok zbavíme. Agent bude tvoj support tím."
- **Ukázať rýchle demo:** Agent dostane support ticket, analyzuje ho, nájde odpoveď v dokumentácii a vygeneruje personalizovanú odpoveď – za 15 sekúnd.

#### 1:30–3:30 | Ako agent rozumie support ticketom
- **Povedať:** "Agent nie je len vyhľadávač v dokumentácii. On ticketom rozumie – kategorizuje ich, prioritizuje a eskalizuje."
- **Ukázať pipeline spracovania ticketu:**
  ```
  [Ticket príde] → Agent:
    1. Kategorizuje (bug / feature request / how-to / billing / iné)
    2. Určí prioritu (urgent / high / normal / low)
    3. Vyhľadá odpoveď v znalostnej báze / dokumentácii
    4. Ak nájde → generuje odpoveď
    5. Ak nenájde → eskalizuje človeku s návrhom
  ```
- **Povedať:** "Toto všetko agent robí autonómne. Ty len kontroluješ eskalované tickety."

#### 3:30–6:00 | Vytvorenie znalostnej bázy pre agenta
- **Povedať:** "Agent potrebuje vedieť, čo má odpovedať. Vytvoríme mu knowledge base."
- **Tri zdroje znalostí:**
  1. **Dokumentácia produktu** – nechaj agenta prečítať tvoju docs stránku
  2. **FAQ a historické tickety** – nahraj CSV s minulými ticketmi a riešeniami
  3. **Produktový kontext** – použi skill `product-marketing` na vytvorenie `.agents/product-marketing.md`
- **Ukázať praktický setup:**
  ```
  # Krok 1: Vytvor produktový kontext
  "Použi skill product-marketing a vytvor kontext pre môj produkt."

  # Krok 2: Daj agentovi dokumentáciu
  "Prečítaj obsah https://docs.mojprodukt.sk a vytvor z neho 
  knowledge base pre support."

  # Krok 3: Nahraj historické tickety
  "Prečítaj support-tickets-2024.csv. Pre každú kategóriu 
  vytvor šablónu odpovede."
  ```
- **Povedať:** "Čím lepšia knowledge base, tým menej ticketov skončí u človeka."

#### 6:00–8:30 | Spracovanie reálnych ticketov
- **Ukázať live ukážku s 3 typmi ticketov:**

**Ticket 1 – How-to (jednoduchý):**
  ```
  "Ako nastavím SSO pre môj tím?"
  → Agent nájde v docs, vygeneruje krok-za-krokom odpoveď
  ```

**Ticket 2 – Bug report (stredný):**
  ```
  "Integrácia so Slackom prestala fungovať po update."
  → Agent kategorizuje ako bug, skontroluje changelog, 
    ponúkne workaround, eskalizuje vývojovému tímu
  ```

**Ticket 3 – Billing (komplexný):**
  ```
  "Prečo mi prišla faktúra na 199 € keď mám Basic plán za 49 €?"
  → Agent skontroluje billing históriu, identifikuje 
    prekročenie limitu API calls, vysvetlí zákazníkovi
  ```

#### 8:30–10:00 | Automatické odpovede vs. eskalácia
- **Povedať:** "Nie na všetko má agent odpovedať sám. Musí vedieť, kedy povedať 'toto už musí riešiť človek'."
- **Pravidlá eskalácie (nauč ich agenta):**
  - Zákazník je nahnevaný / žiada refund
  - Ticket obsahuje bezpečnostný incident
  - Problém sa týka citlivých údajov
  - Agent nenašiel relevantnú odpoveď v knowledge base
  - Ticket je od VIP/enterprise zákazníka
- **Ukázať, ako agent eskaluje:**
  ```
  "Ticket #1234 eskalovaný. Dôvod: Bezpečnostný incident.
  Návrh: Okamžite kontaktovať CISO. Tu je draft odpovede 
  zákazníkovi, že incident riešime s najvyššou prioritou."
  ```

#### 10:00–11:30 | Analýza support trendov
- **Povedať:** "Agent nie je len 'odpovedávač'. Je to aj analytik. Identifikuje trendy a problémy skôr, než sa stanú krízou."
- **Ukázať, čo agent dokáže zistiť z ticketov:**
  - Ktoré featury majú najviac problémov?
  - Ktorí zákazníci sú najviac nespokojní (najviac ticketov)?
  - Aké otázky sa opakujú? → návrh na nový help article
  - Sezónne výkyvy v podpore
- **Povedať:** "Tieto insighty dáš produktovému tímu a zlepšuješ produkt na základe dát."

#### 11:30–12:00 | Best practices a záver
- **Povedať:** "Agent pre support = tvoj 24/7 support tím. Ale pamätaj – agent podporuje ľudí, nenahrádza ich. Tie najťažšie prípady stále patria človeku."

### Kľúčové body
- Agent kategorizuje, prioritizuje a odpovedá na support tickety autonómne
- Znalostná báza = dokumentácia + FAQ + historické tickety + produktový kontext
- 3 zdroje: docs stránka, CSV s ticketmi, `product-marketing` skill
- Eskalačné pravidlá: refund, bezpečnosť, VIP zákazníci, neznáme problémy
- Agent analyzuje trendy a odporúča zlepšenia produktu

### Domáca úloha
1. Vytvor knowledge base pre svoj produkt – nechaj agenta prečítať tvoju dokumentáciu a vygenerovať súbor s FAQ
2. Napíš aspoň 10 rôznych support ticketov, ktoré by ti mohli prísť, a nechaj agenta na ne odpovedať
3. Definuj svoje eskalačné pravidlá – ktoré prípady musí vždy riešiť človek?
4. Ak máš reálne support tickety (napr. z Intercom, Zendesk), exportuj 20-30 z nich do CSV a nechaj agenta spraviť trendovú analýzu

---

## Lekcia 4: Agent pre analýzu predajných dát
**Dĺžka videa:** 10 minút

### Detailný obsah / scenár

#### 0:00–1:00 | Úvod a hook
- **Povedať:** "Dáta sú super, ale len ak im rozumieš. Agent ti dáta nielen zanalyzuje, ale povie ti, čo máš robiť – konkrétne akcie, ktoré zvýšia tvoje tržby."
- **Ukázať rýchle demo:** Agent dostane CSV s predajmi za posledný kvartál a do 30 sekúnd vráti: top 3 problémy, top 3 príležitosti a konkrétne odporúčania.

#### 1:00–3:30 | Aké dáta agent potrebuje a odkiaľ ich získať
- **Povedať:** "Agent vie pracovať s akýmikoľvek štruktúrovanými dátami. Cez MCP a API vie dáta aj sám ťahať."
- **Zdroje predajných dát:**
  - **CRM export** (HubSpot, Salesforce, Pipedrive) – CSV
  - **Google Sheets** – cez GWS Sheets skills
  - **Stripe / Paddle** – billing a revenue dáta
  - **Google Analytics** – konverzie a traffic
  - **SQL databáza** – agent môže spúšťať SQL queries
- **Ukázať, ako agent načíta dáta:**
  ```
  # Z CSV:
  "Prečítaj sales-q2-2025.csv a sprav analýzu."

  # Z Google Sheets:
  "Použi gws-sheets-read na tabuľku 'Sales Dashboard 2025'."

  # Z SQL (cez bash):
  "Spusti SELECT * FROM deals WHERE created_at > '2025-01-01' 
  a výsledky zanalyzuj."
  ```

#### 3:30–6:00 | Základná predajná analytika – čo všetko agent zistí
- **Povedať:** "Poďme si ukázať, čo všetko agent dokáže z predajných dát vyčítať."
- **Prejsť analýzu krok za krokom (ukázať na obrazovke):**

**1. Pipeline health:**
  - Koľko dealov je v jednotlivých fázach?
  - Aká je priemerná dĺžka predajného cyklu?
  - Kde sa dealy najčastejšie zasekávajú?

**2. Win/loss analýza:**
  - Win rate podľa segmentu, veľkosti dealov, produktu
  - Prečo prehrávame? (ak sú dostupné dôvody)
  - Ktorý rep má najlepšiu win rate?

**3. Revenue analýza:**
  - MRR/ARR trend
  - Priemerná hodnota deal-u (ASP)
  - Customer Acquisition Cost (CAC) a LTV
  - Churn rate podľa kohorty

**4. Forecast:**
  - Aký revenue očakávame tento kvartál?
  - Ktoré dealy sú v riziku?

- **Povedať:** "Toto všetko agent vygeneruje do jedného reportu za menej ako minútu."

#### 6:00–7:30 | Vizualizácia – grafy a dashboardy
- **Povedať:** "Čísla sú fajn, ale graf povie viac. Agent ti vygeneruje vizualizácie."
- **Ukázať príklady (agent používa matplotlib alebo generuje CSV pre Google Sheets):**
  - Pipeline funnel graf
  - Revenue trend (mesačný)
  - Win rate podľa repa (bar chart)
  - Churn kohortová analýza
- **Praktický prompt:**
  ```
  Z dát v sales-q2-2025.csv mi vygeneruj:
  1. Funnel graf – počet dealov v každej fáze
  2. Mesačný revenue trend za posledných 12 mesiacov
  3. Win rate podľa veľkosti dealov

  Ulož grafy ako PNG a vytvor z nich krátky sumár.
  ```
- **Povedať:** "Ak používaš Google Sheets, agent vie grafy vytvoriť priamo tam cez GWS Sheets API."

#### 7:30–9:00 | Od dát k akcii – agent ako predajný poradca
- **Povedať:** "Toto je tá najdôležitejšia časť. Agent ti nepovie len 'tu sú čísla'. Povie ti 'tu sú čísla a toto s tým sprav'."
- **Ukázať príklad výstupu agenta:**
  ```
  🔴 PROBLÉMY:
  1. Dealy sa zasekávajú vo fáze "Demo" – priemerná doba 14 dní
     (vs. benchmark 7 dní). Odporúčam: skrátiť follow-up cyklus.
  2. Win rate pre enterprise segment klesla z 35 % na 22 %.
     Odporúčam: preveriť konkurenciu v tomto segmente.
  3. Churn u zákazníkov, ktorí neprešli onboardingom, je 3x vyšší.
     Odporúčam: zapnúť onboarding agenta (Modul 5, Lekcia 4).

  🟢 PRÍLEŽITOSTI:
  1. Mid-market segment rastie najrýchlejšie – zdvojnásobiť outreach.
  2. Zákazníci, ktorí používajú integráciu X, majú o 60 % vyššie LTV.
     Odporúčam: promo integrácie X v onboardingu.
  3. Q3 pipeline je o 40 % väčší ako Q2 v rovnakom čase.
  ```
- **Povedať:** "Toto nie je analytický report. Toto je akčný plán."

#### 9:00–10:00 | Best practices a záver
- **Povedať:** "Agent ti dá analýzu za minútu. Ale tá analýza je len taká dobrá, ako dáta, ktoré do nej vstúpia."
- **Best practices:**
  - Udržuj CRM čistý – garbage in, garbage out
  - Pravidelne (týždenne) nechaj agenta spraviť pulse check
  - Kombinuj dáta z viacerých zdrojov pre kompletný obraz
  - Daj agentovi biznisový kontext – ciele, benchmarky, históriu

### Kľúčové body
- Agent analyzuje predajné dáta z CRM, Stripe, Google Sheets, SQL a ďalších zdrojov
- 4 oblasti analýzy: pipeline health, win/loss, revenue, forecast
- Agent generuje vizualizácie (grafy, funnel, kohortové analýzy)
- Kľúčová hodnota: odporúčania na konkrétne akcie, nielen reporting
- Pravidelná týždenná analýza = včasné odhalenie problémov

### Domáca úloha
1. Exportuj svoje predajné dáta z CRM (alebo si vytvor testovací CSV s 50+ riadkami) a nechaj agenta spraviť kompletnú analýzu
2. Nechaj agenta vygenerovať aspoň 3 grafy z tvojich dát
3. Napíš si top 3 odporúčania, ktoré ti agent dal – a vyber jedno, ktoré tento týždeň implementuješ
4. Nastav si týždenný report – nechaj agenta vytvoriť šablónu, ktorú budeš používať každý týždeň

---

## Lekcia 5: Agent pre follow-up sekvencie
**Dĺžka videa:** 11 minút

### Detailný obsah / scenár

#### 0:00–1:00 | Úvod a hook
- **Povedať:** "Vedeli ste, že 48 % obchodníkov nikdy nepošle ani jeden follow-up? A pritom 80 % dealov sa uzatvára až po 5. kontakte. Dnes si postavíme agenta, ktorý nikdy nezabudne – a vždy pošle ten správny follow-up v správny čas."
- **Ukázať rýchle demo:** Agent sleduje pipeline, identifikuje dealy bez follow-upu a vygeneruje personalizované správy.

#### 1:00–3:30 | Prečo follow-upy zlyhávajú a ako to agent rieši
- **Povedať:** "Ľudia zabúdajú. Alebo nevedia, čo napísať. Alebo sa boja, že budú otravní. Agent tieto problémy nemá."
- **Tri dôvody, prečo follow-upy zlyhávajú:**
  1. **Zabudnutie** – obchodník má 50 dealov, nevie, komu kedy naposledy písal
  2. **Prázdna správa** – 'len sa pripomínam' neprináša hodnotu
  3. **Nekonzistentnosť** – raz pošleš follow-up za 2 dni, inokedy za 2 týždne
- **Ako to agent rieši:**
  1. **Nikdy nezabudne** – sleduje pipeline a upozorní na dealy bez follow-upu
  2. **Vždy pridá hodnotu** – každý follow-up má nový dôvod (case study, článok, štatistika, nová featúra)
  3. **Dodržiava kadenciu** – presne podľa nastavenej sekvencie

#### 3:30–6:00 | Návrh follow-up sekvencie
- **Povedať:** "Dobrá follow-up sekvencia má štruktúru. Poďme si ju navrhnúť."
- **Prejsť celú sekvenciu krok za krokom:**

```
📧 KONTAKT 1 (Deň 0) – Prvý email (z Lekcie 2)
  Cieľ: Predstaviť hodnotu, získať pozornosť

📧 KONTAKT 2 (Deň 3) – Hodnotový follow-up
  Cieľ: Pridať novú informáciu, nie "len pripomínam"
  Príklady: "Mimochodom, tu je case study s firmou podobnou vašej..."
           "Všimol som si, že ste hiring DevOps – náš nástroj s tým pomáha..."

📧 KONTAKT 3 (Deň 7) – Social proof
  Cieľ: Ukázať, že to funguje u iných
  Príklady: "Práve sme vydali výsledky s klientom X: 40% menej incidentov..."
           "G2 recenzia od firmy v tvojom segmente..."

📧 KONTAKT 4 (Deň 14) – Alternatívny kanál
  Cieľ: Skúsiť inú cestu
  Príklady: LinkedIn message, Twitter DM, komentár na ich blogu

📧 KONTAKT 5 (Deň 21) – Break-up email
  Cieľ: Posledný pokus, bez tlaku
  Príklad: "Zdá sa, že teraz nie je správny čas. Nechám ťa – 
           ale ak by sa niečo zmenilo, som tu."
```

- **Povedať:** "Toto je štandardná B2B sekvencia. Agent ju vygeneruje celú za 30 sekúnd."

#### 6:00–8:00 | Agent ako follow-up automat
- **Ukázať kompletný setup pre automatizáciu:**
- **Krok 1: Daj agentovi pipeline dáta**
  ```
  "Prečítaj si pipeline.csv – obsahuje všetky aktívne dealy 
  s dátumom posledného kontaktu a fázou."
  ```
- **Krok 2: Agent identifikuje dealy potrebujúce follow-up**
  ```
  "Nájdi všetky dealy, kde posledný kontakt bol pred >3 dňami 
  a deal nie je označený ako 'closed-won' alebo 'closed-lost'."
  ```
- **Krok 3: Agent vygeneruje personalizované follow-upy**
  ```
  "Pre každý identifikovaný deal vygeneruj follow-up email 
  podľa štádia sekvencie. Ak je to 1. follow-up, pridaj 
  hodnotový obsah. Ak 3., použi social proof."
  ```
- **Krok 4: Uloženie a odoslanie**
  ```
  "Ulož vygenerované emaily do /follow-ups/2025-08-11.csv. 
  Pošli mi zoznam na schválenie."
  ```
- **Povedať:** "Celý tento proces trvá agentovi pár minút. Tebe by to trvalo hodiny."

#### 8:00–9:30 | Integrácia s kalendárom a CRM
- **Povedať:** "Follow-up nie sú len emaily. Agent vie sledovať aj to, či sa dohodnutý call naozaj stal."
- **Ukázať integrácie:**
  - **Google Calendar:** Agent skontroluje, či bol call po deme naplánovaný a či sa uskutočnil. Ak nie, pošle follow-up.
  - **CRM:** Agent aktualizuje stav dealov v CRM po každom follow-upe.
  - **Notifikácie:** "Agent ťa upozorní: 'Deal so Spoločnosťou X je 10 dní bez kontaktu. Tu je draft follow-upu.'"
- **Ukázať príklad konfigurácie:**
  ```
  Nastav mi follow-up agenta, ktorý:
  1. Každé ráno o 8:00 skontroluje pipeline
  2. Nájde dealy bez kontaktu >3 dni
  3. Vygeneruje draft follow-upov
  4. Pošle mi ich na schválenie do Gmailu
  5. Po schválení ich odošle (cez GWS Gmail)
  6. Zaloguje aktivitu do CRM
  ```
- **Povedať:** "Toto je už produkčný setup. V Module 7 sa naučíme, ako to celé naplánovať cez scheduling, aby to bežalo automaticky."

#### 9:30–11:00 | Best practices, meranie a záver
- **Povedať:** "Follow-up sekvencia je živý organizmus. Treba ju merať a vylepšovať."
- **Metriky, ktoré sledovať:**
  - Response rate po jednotlivých follow-upoch
  - V ktorom bode sekvencie ľudia najčastejšie odpovedajú?
  - Ktorý typ follow-upu funguje najlepšie (hodnotový vs. social proof vs. break-up)?
- **Povedať:** "Nechaj agenta spraviť mesačnú analýzu efektivity follow-upov a optimalizovať sekvenciu."
- **Zhrnutie modulu:**
  - "V tomto module si vybudoval kompletnú predajnú a support automatizáciu: od hľadania leadov, cez oslovenie, support, analýzu dát až po follow-upy."
  - "V Module 7 sa posunieme na vyššiu úroveň – pokročilé techniky, MCP integrácie, scheduling a nonstop bežiacich agentov."

### Kľúčové body
- 80 % dealov sa uzatvára po 5. kontakte, ale 48 % obchodníkov nepošle ani jeden follow-up
- 5-kroková sekvencia: prvý kontakt → hodnota → social proof → alternatívny kanál → break-up
- Agent sleduje pipeline, identifikuje dealy bez follow-upu a generuje personalizované správy
- Každý follow-up musí prinášať novú hodnotu – nikdy "len sa pripomínam"
- Integrácia s kalendárom a CRM pre plne automatizovaný proces
- Pravidelné meranie a optimalizácia – ktorý typ follow-upu funguje najlepšie?

### Domáca úloha
1. Navrhni vlastnú 5-krokovú follow-up sekvenciu pre svoj biznis – napíš, čo by mal obsahovať každý krok
2. Vytvor testovací CSV s 10 dealmi v rôznych fázach a nechaj agenta vygenerovať follow-upy
3. Vyber si jeden reálny deal, kde si dlho neposlal follow-up, a nechaj agenta napísať správu – pošli ju
4. Nastav si jednoduchý kontrolný mechanizmus: nechaj agenta vytvoriť skript, ktorý každý deň skontroluje pipeline CSV a vypíše dealy bez follow-upu

---
