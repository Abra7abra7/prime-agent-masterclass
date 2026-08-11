# Prime Agent Masterclass – Detailná osnova kurzu

---

## Modul 1: Úvod a inštalácia

**Čo sa študent naučí:** Pochopí, čo je Prime Agent, aké sú jeho možnosti, a úspešne ho nainštaluje a nakonfiguruje na svojom systéme. Získa prehľad o architektúre agenta, jeho komponentoch a základnej terminológii.

### Lekcie

1. **Čo je Prime Agent a prečo ho potrebuješ**
   - Predstavenie platformy Prime Agent ako autonómneho AI agenta pre vývojárov a marketérov. Prehľad kľúčových schopností – od písania kódu cez automatizáciu marketingu až po produkčné nasadenie.

2. **Architektúra a kľúčové komponenty**
   - Vysvetlenie základných stavebných blokov: IPython kernel, skills, subagenti, continual harness, RLM runtime. Ako tieto komponenty spolupracujú pri vykonávaní úloh.

3. **Inštalácia na macOS, Linux a Windows**
   - Krok za krokom inštalácia Prime Agenta cez npm, vrátane kontroly Node.js verzie. Nastavenie systémových premenných a riešenie najčastejších inštalačných problémov.

4. **Konfigurácia API kľúčov a providerov**
   - Nastavenie poskytovateľov LLM (DeepSeek, OpenAI, Anthropic, Google Gemini). Konfigurácia API kľúčov cez `/login` a výber východiskového modelu.

5. **Prvé spustenie a orientácia v rozhraní**
   - Spustenie agenta v termináli, prvé privítanie, orientácia v CLI rozhraní. Základné príkazy a ako komunikovať s agentom.

---

## Modul 2: Prvé kroky s agentom

**Čo sa študent naučí:** Efektívne zadávať úlohy agentovi, čítať a interpretovať jeho výstupy, pracovať so súbormi a pochopiť, ako agent vykonáva kód a shell príkazy.

### Lekcie

1. **Ako správne formulovať úlohy (prompt engineering pre agentov)**
   - Zásady efektívneho zadávania úloh: špecifickosť, kontext, očakávaný formát výstupu. Ako sa agent rozhoduje a plánuje kroky.

2. **Práca s IPython kernelom – premenné, importy, perzistencia**
   - Vysvetlenie IPython kernelu ako dlhodobej pamäte agenta. Ako agent ukladá premenné, funkcie a výsledky medzi jednotlivými krokmi. Oživenie kernelu pri obnovení relácie.

3. **Shell príkazy a %%bash bunky**
   - Používanie `%%bash` buniek na spúšťanie shell príkazov. Rozdiel medzi shell a Python kontextom, zdieľanie stavu cez `%cd` a `os.environ`.

4. **Čítanie, vyhľadávanie a editácia súborov**
   - Ako agent pracuje so súborovým systémom – čítanie súborov v Pythone, vyhľadávanie vzorov, editácia cez skill `edit`. Best practices pre cielené úpravy namiesto prepisovania celých súborov.

5. **Interpretácia výstupov a debugging**
   - Ako čítať výsledky agenta, rozpoznávať chyby a iterovať. Ladenie úloh keď agent nevykoná presne to, čo chceme.

6. **Praktický projekt: Automatizovaná analýza repozitára**
   - Komplexné cvičenie: nechať agenta preskúmať neznámy repozitár, identifikovať jeho štruktúru, závislosti a vygenerovať prehľadný report.

---

## Modul 3: Skills a customizácia

**Čo sa študent naučí:** Rozumieť ekosystému skills, používať vstavané aj externé skilly, a vytvárať vlastné markdown a Python skilly pre opakované úlohy.

### Lekcie

1. **Čo sú skills a ako ich agent používa**
   - Definícia skillov ako rozšíriteľných inštrukcií a nástrojov. Ako agent objavuje a volá skilly na základe kontextu úlohy. Rozdiel medzi markdown a Python skillmi.

2. **Objavovanie a inštalácia skillov z knižnice**
   - Používanie skillu `find-skills` na vyhľadávanie dostupných skillov. Inštalácia nových skillov a ich aktivácia v agentovi.

3. **Markdown skilly – štruktúra SKILL.md**
   - Detailný rozbor SKILL.md súboru: metadáta, spúšťacie frázy, inštrukcie, referenčné materiály. Kedy použiť markdown skill namiesto Python skillu.

4. **Python skilly – importy, funkcie a CLI**
   - Vytváranie Python skillov s vlastnými funkciami. Ako agent importuje a volá Python skilly. Vystavenie CLI rozhrania cez konzolové skripty.

5. **Vytváranie vlastného skillu pomocou skill-creator**
   - Praktický návod na tvorbu vlastného skillu od nuly. Validácia, testovanie a nasadenie skillu do agenta.

6. **Organizácia a správa knižnice skillov**
   - Best practices pre štruktúrovanie skill adresárov, verzionovanie, a zdieľanie skillov medzi projektmi. Využitie globálnych vs. lokálnych skillov.

---

## Modul 4: Subagenti a delegovanie

**Čo sa študent naučí:** Vytvárať a riadiť hierarchiu subagentov, delegovať komplexné úlohy na špecializované podriadené jednotky a zbierať od nich výsledky.

### Lekcie

1. **Koncept subagentov – prečo a kedy delegovať**
   - Vysvetlenie hierarchickej architektúry agentov. Kedy má zmysel vytvoriť subagenta namiesto volania skillu. Izolácia kontextu, špecializácia a paralelné spracovanie.

2. **Vytváranie subagenta cez `rlm('úloha')`**
   - Praktické vytváranie subagentov priamo z IPython kernelu. Ako formulovať task prompt pre subagenta. Čo sa vracia po spustení – `rlm_child_id`, `name`, `session_dir`.

3. **Komunikácia medzi agentmi – `agent_message.send()`**
   - Ako subagent posiela výsledky rodičovi cez `agent_message.send(message, receiver_role='parent')`. Komunikácia medzi súrodencami. Best practices pre správu a odpovede.

4. **Pozorovanie a monitoring subagentov**
   - Používanie `agent_observe` na sledovanie stavu subagentov. Čítanie logov a session súborov. Ako zistiť, či subagent stále pracuje alebo skončil.

5. **Pokročilé delegovanie – reťazenie a špecializácia**
   - Vytváranie reťazcov subagentov pre viacstupňové pipeline. Špecializované subagenty pre konkrétne domény (kód, marketing, analýza). Ako odovzdávať kontext medzi úrovňami.

6. **Praktický projekt: Tím agentov pre prieskum trhu**
   - Vybudovanie hierarchického tímu: hlavný agent deleguje prieskum konkurencie, analýzu zákazníkov a SEO audit trom špecializovaným subagentom paralelne.

---

## Modul 5: Automatizácia marketingu

**Čo sa študent naučí:** Využívať marketingové skilly Prime Agenta na tvorbu obsahu, SEO, prieskum trhu, emailové kampane, sociálne siete a ďalšie marketingové aktivity – všetko autonómne.

### Lekcie

1. **Prehľad marketingových skillov a ich orchestrácia**
   - Mapovanie dostupných marketingových skillov: copywriting, SEO audit, social, emails, ads, content strategy, CRO, AB testing a ďalšie. Ako ich kombinovať do ucelených workflowov.

2. **Tvorba marketingového obsahu na mieru**
   - Použitie skillov `copywriting`, `copy-editing`, `content-strategy` na generovanie landing pages, blog postov, emailov a reklamných textov. Ako dávať agentovi správny brandový kontext.

3. **SEO a AI viditeľnosť**
   - Automatizovaný SEO audit cez `seo-audit`, nasadenie štruktúrovaných dát cez `schema`, a optimalizácia pre AI vyhľadávače cez `ai-seo`. Tvorba programatických SEO stránok.

4. **Emailové kampane a marketingové slučky**
   - Vytváranie celých emailových sekvencií (welcome, nurture, re-engagement) cez skill `emails`. Nastavenie automatických marketingových slučiek (`marketing-loops`), ktoré bežia na týždennej báze.

5. **Prieskum trhu a zákaznícka analytika**
   - Použitie `customer-research` a `competitor-profiling` na hĺbkový prieskum. Mining recenzií, analýza sentimentu, tvorba person a JTBD.

6. **Sociálne siete a obsahový kalendár**
   - Generovanie a plánovanie príspevkov na LinkedIn, Twitter/X, Instagram cez skill `social`. Tvorba carouselov, vlákien a krátkych video skriptov. Automatizovaný obsahový kalendár.

---

## Modul 6: Automatizácia predaja a supportu

**Čo sa študent naučí:** Automatizovať predajné procesy, tvorbu sales collateralov, zákaznícku podporu, onboarding a retenčné stratégie pomocou Prime Agenta.

### Lekcie

1. **Sales enablement – battle cards, decky, one-pagery**
   - Tvorba predajných materiálov cez `sales-enablement`: pitch decky, objection handling, demo skripty, ROI analýzy. Automatické generovanie personalizovaných proposalov.

2. **Prospecting a cold outreach**
   - Vyhľadávanie a kvalifikácia leadov cez `prospecting`. Tvorba personalizovaných cold email sekvencií s `cold-email`. A/B testovanie outreach kampaní.

3. **Riadenie zákazníckej podpory**
   - Automatizácia ticketovania, kategorizácie a odpovedí na časté otázky. Analýza support ticketov na identifikáciu trendov a produktových problémov.

4. **Onboarding a aktivácia používateľov**
   - Optimalizácia onboarding toku cez skill `onboarding`. Tvorba in-app správ, checklistov a sprievodcov. Meranie a zvyšovanie aktivačnej miery.

5. **Retencia, churn prevencia a win-back**
   - Návrh a implementácia retenčných stratégií cez `churn-prevention`. Automatizované win-back kampane, cancel flows a save offers. Recovery neúspešných platieb.

6. **Praktický projekt: End-to-end sales a support pipeline**
   - Vybudovanie kompletnej pipeline: od vyhľadania leadov, cez oslovenie, zaslanie materiálov, onboarding, až po retenčné kampane – všetko riadené agentom.

---

## Modul 7: Pokročilé techniky (MCP, API, scheduling)

**Čo sa študent naučí:** Rozširovať schopnosti agenta o externé API, MCP integrácie, Google Workspace, plánovanie úloh a pokročilé techniky orchestrácie.

### Lekcie

1. **Model Context Protocol (MCP) – čo to je a ako ho používať**
   - Vysvetlenie MCP štandardu a jeho úlohy v ekosystéme Prime Agent. Konfigurácia MCP Connections cez `/login`. Ako agent komunikuje s externými službami cez MCP server.

2. **Google Workspace integrácia – Gmail, Drive, Calendar, Sheets**
   - Praktické použitie GWS skillov: odosielanie emailov, správa kalendára, čítanie a zápis do Google Sheets/Docs. Automatizácia pracovných postupov naprieč Workspace.

3. **Volanie externých API z Python skillov**
   - Ako v rámci vlastných Python skillov volať REST API, spracovávať JSON odpovede a integrovať externé služby. Autentifikácia, rate limiting a error handling.

4. **Plánovanie úloh – heartbeaty a cron joby**
   - Nastavenie periodických úloh cez `rlm-heartbeat`. Ako nechať agenta bežať na pozadí a vykonávať úlohy v stanovených intervaloch (denné reporty, týždenné audity).

5. **Pokročilá orchestrácia – paralelné spracovanie a pipeline**
   - Spúšťanie viacerých subagentov paralelne, synchronizácia výsledkov, spracovanie chýb. Budovanie komplexných pipeline s podmienenými vetvami.

6. **Custom nástroje a rozšírenia – beyond skills**
   - Integrácia vlastných CLI nástrojov, Docker kontajnerov a externých skriptov do workflowu agenta. Ako rozšíriť agenta nad rámec štandardných skillov.

---

## Modul 8: Produkčné nasadenie a best practices

**Čo sa študent naučí:** Prevádzkovať Prime Agenta v produkčnom prostredí – bezpečnosť, monitoring, škálovanie, continual harness manažment a osvedčené postupy z reálnej praxe.

### Lekcie

1. **Bezpečnosť – API kľúče, permissions, sandboxing**
   - Best practices pre správu API kľúčov a citlivých údajov. Obmedzenie prístupu agenta k súborovému systému. Sandboxing a izolácia prostredia.

2. **Continual harness – pamäť, skilly a prompt manažment**
   - Hĺbkový pohľad na continual harness: vytváranie a správa memories, skills, subagent specs a prompt notes. Kedy používať `global_=True` pre cross-session znalosti. Refinement workflow.

3. **Monitoring a logovanie agenta v produkcii**
   - Sledovanie výkonu agenta, čítanie session logov, analýza chýb. Nastavenie notifikácií pri zlyhaní úloh. Ako merať efektivitu a náklady.

4. **Škálovanie – viacero agentov, load balancing**
   - Architektúra pre beh viacerých agentov súčasne. Rozdeľovanie úloh medzi agentov, fronty správ. Koordinácia väčších tímov agentov.

5. **Verzionovanie skillov a CI/CD pre agenta**
   - Správa verzií skillov, testovanie zmien pred nasadením. Automatizované nasadzovanie nových skillov a prompt notes. Rollback pri problémoch.

6. **Best practices a lessons learned z praxe**
   - Súhrn najdôležitejších odporúčaní z reálnych nasadení: ako písať dobré task prompty, kedy delegovať, ako štruktúrovať skilly, čomu sa vyhnúť. Odporúčaná cesta od experimentu k produkcii.
