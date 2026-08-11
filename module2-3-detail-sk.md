# Prime Agent Masterclass – Modul 2: Prvé kroky s agentom

## Prehľad modulu

**Cieľ modulu:** Po absolvovaní tohto modulu budeš vedieť písať efektívne prompty, ktoré z agenta dostanú maximum. Naučíš sa pracovať so súbormi, spúšťať Python a bash príkazy priamo cez agenta, vyhľadávať na webe a spracúvať informácie. Modul zavŕšiš praktickým projektom – automatickým prieskumom trhu, ktorý využiješ v reálnom biznise.

**Celková dĺžka:** 60 minút videa + domáce úlohy

---

## Lekcia 1: Písanie efektívnych promptov
**Dĺžka videa:** 12 minút

### Detailný obsah / scenár

#### 0:00–1:30 | Úvod – prečo na promptoch záleží
- **Povedať:** „Vitaj v Module 2. Toto je lekcia, ktorá ti ušetrí desiatky hodín. Písanie promptov pre agenta je úplne iná disciplína ako písanie pre chatbota. Chatbot len odpovedá – agent koná."
- **Ukázať na obrazovke porovnanie:**
  - Zlý prompt: „Oprav môj kód" → agent tápe, pýta sa, stráca čas
  - Dobrý prompt: „V súbore `app.py` na riadkoch 45–78 je funkcia `calculate_tax`. Tá vracia nesprávne hodnoty pre DPH nad 1000€. Nájdi chybu, oprav ju a napíš test, ktorý overí správnosť." → agent okamžite koná
- **Povedať:** „Rozdiel medzi 2-minútovou a 20-minútovou úlohou je v kvalite promptu."

#### 1:30–4:00 | Anatómia dobrého promptu – framework „Cieľ-Kontext-Formát-Obmedzenia"
- **Povedať:** „Každý dobrý prompt má štyri vrstvy. Nauč sa ich – budeš ich používať každý deň."
- **Rozpísať na slide / obrazovku:**

**1. Cieľ – ČO chceš dosiahnuť**
  - Buď konkrétny, nie vágny
  - Príklad zlý: „Sprav analýzu dát"
  - Príklad dobrý: „Vypočítaj priemerný mesačný rast tržieb za posledných 12 mesiacov a identifikuj 3 mesiace s najväčším prepadom"

**2. Kontext – KDE a Z ČOHO**
  - Aké súbory, aké dáta, aké prostredie
  - Príklad: „Použi súbor `sales_2024.csv` v aktuálnom priečinku, stĺpce: date, revenue, product"

**3. Formát – AKO má vyzerať výstup**
  - Definuj štruktúru, nie len „daj mi výsledok"
  - Príklad: „Vytvor Markdown tabuľku s mesiacom, tržbami a percentuálnou zmenou oproti predošlému mesiacu"

**4. Obmedzenia – ČO NESMIE alebo MUSÍ**
  - Technické limity, preferencie, „nepoužívaj knižnicu X", „všetko v slovenčine"
  - Príklad: „Nepoužívaj pandas, len čisté Python. Výstup v slovenčine."

- **Povedať:** „Zapamätaj si: **Cieľ-Kontext-Formát-Obmedzenia**. Keď sa budeš trápiť s agentom, skontroluj, či tvoj prompt má všetky štyri."

#### 4:00–6:30 | Praktické príklady – pred a po
- **Povedať:** „Poďme si ukázať transformáciu reálnych promptov."

**Príklad 1 – Analýza kódu:**
  - ❌ Zlý: „Pozri sa na tento kód a povedz mi čo je zle" (bez súboru, bez kontextu)
  - ✅ Dobrý: „Súbor `src/utils.py`, funkcia `validate_email` na riadkoch 23–45. Táto funkcia má validovať emailové adresy podľa RFC 5322, ale prepúšťa adresy bez TLD (napr. `user@domain`). Nájdi presnú chybu v regexe, oprav ju a napíš 5 testovacích prípadov, ktoré overia opravu. Výstup vo formáte: popis chyby, opravený kód, testy."

**Príklad 2 – Dátová úloha:**
  - ❌ Zlý: „Spracuj dáta v sales.csv" 
  - ✅ Dobrý: „Súbor `sales.csv` (UTF-8, čiarka ako oddeľovač). Nájdi všetky duplicitné záznamy podľa stĺpca `transaction_id`, zlúč ich podľa dátumu (`date`), a vytvor nový CSV `sales_deduped.csv`. Do výstupu pridaj stĺpec `total_revenue` (quantity × unit_price). Výstup zoraď chronologicky."

**Príklad 3 – Web scraping:**
  - ❌ Zlý: „Pozri sa na túto stránku a daj mi info"
  - ✅ Dobrý: „Prejdi všetky články na `https://example.com/blog?page=1` až po stranu 5. Z každého článku extrahuj: názov, autora, dátum publikácie, a prvých 200 slov textu. Ulož výsledky do `blog_posts.json` v štruktúre `[{title, author, date, excerpt}]`. Ignoruj články staršie ako 2024."

- **Povedať:** „Vidíš ten rozdiel? Pri dobrom prompte agent nemusí hádať. Vie presne čo, kde, ako."

#### 6:30–8:30 | Techniky pre pokročilých
- **Povedať:** „Teraz pár techník, ktoré ťa posunú na vyššiu úroveň."

**1. Chain of Thought prompting:**
  - „Pri zložitých úlohách povedz agentovi, aby premýšľal nahlas:"
  - Príklad: „Predtým než začneš kódovať, vysvetli mi svoj plán – čo všetko bude treba spraviť a v akom poradí. Potom to implementuj."
  - **Prečo to funguje:** Agent si sám rozvrhne úlohu a ty vieš skontrolovať logiku ešte pred exekúciou

**2. Few-shot prompting:**
  - „Ukáž agentovi príklad toho, čo chceš:"
  - Príklad: „Tu je príklad dobrého testu: `def test_add(): assert add(2,3) == 5`. Teraz vytvor podobné testy pre funkcie `subtract`, `multiply`, `divide`."

**3. Role prompting:**
  - „Daj agentovi rolu – ovplyvní to kvalitu aj štýl výstupu:"
  - Príklad: „Si senior Python vývojár špecializujúci sa na finančné aplikácie. Všetky premenné pomenuj v slovenčine a pridávaj validačné komentáre v štýle PEP 8."

**4. Negatívny prompting:**
  - „Povedz, čo NECHCEŠ:"
  - Príklad: „Nepoužívaj knižnicu pandas. Nepoužívaj OOP, len funkcie. Výstup nesmie obsahovať žiadne TODO komentáre."

- **Povedať:** „Tieto štyri techniky – Chain of Thought, Few-shot, Role a Negatívny prompting – si zapamätaj. Budeš ich používať denne."

#### 8:30–10:30 | Najčastejšie chyby pri promptovaní
- **Povedať:** „Poďme si prejsť, čo NEROBIŤ. Toto sú chyby, ktoré začínajúcich používateľov stoja najviac času."

**Chyba 1: Príliš vágne zadanie**
  - „Sprav niečo s dátami" – agent nevie, čo chceš
  - **Oprava:** Vždy špecifikuj súbor, formát, cieľ

**Chyba 2: Príliš veľa naraz**
  - „Refaktoruj celý projekt, pridaj testy, oprav dokumentáciu, a ešte..." 
  - **Oprava:** Rozdeľ na menšie úlohy. Jedna úloha = jeden prompt

**Chyba 3: Chýbajúci formát výstupu**
  - Agent ti dá technicky správny, ale nepoužiteľný výsledok
  - **Oprava:** Vždy definuj: „Výstup ulož do X. Formát: Y. Štruktúra: Z."

**Chyba 4: Ignorovanie limitov modelu**
  - „Nájdi všetkých 50 000 záznamov a spracuj ich" – model má kontextové okno
  - **Oprava:** „Spracuj prvých 100 záznamov, výsledok ulož, potom pokračuj ďalších 100..."

**Chyba 5: Neposkytnutie príkladu**
  - Agent nie je telepata. Ak chceš špecifický štýl, ukáž mu ho
  - **Oprava:** „Tu je príklad výstupu: ... Teraz sprav to isté pre..."

- **Povedať:** „Týchto 5 chýb ťa bude prenasledovať. Vytlač si ich a maj ich pred sebou pri každom prompte."

#### 10:30–12:00 | Zhrnutie a interaktívne cvičenie
- **Povedať:** „Poďme si to vyskúšať. Dám ti 3 scenáre a ty napíš, ako by si sformuloval prompt."

**Cvičenie 1:** „Máš priečinok s 50 obrázkami z dovolenky. Chceš ich všetky zmenšiť na šírku 1200px a skonvertovať do WebP."
  - *Účastníci píšu do chatu svoje prompty*
  - *Ukážka riešenia:* „V priečinku `./fotky` nájdi všetky obrázky (JPG, PNG, HEIC). Zmeň ich veľkosť na šírku 1200px pri zachovaní pomeru strán. Skonvertuj do formátu WebP s kvalitou 85%. Ulož do `./fotky/webp/`. Pôvodné súbory nechaj nedotknuté."

**Cvičenie 2:** „Chceš z GitHub repozitára stiahnuť posledných 20 issues a vytvoriť z nich prehľadnú správu."
  - *Účastníci píšu do chatu svoje prompty*
  - *Ukážka riešenia:* „Z GitHub repozitára `https://github.com/owner/repo` stiahni 20 najnovších issues (vrátane closed). Pre každé issue extrahuj: číslo, názov, autora, label-y, stav (open/closed), a prvý komentár. Vytvor Markdown súbor `github_issues_report.md` s prehľadnou tabuľkou a samostatnou sekciou pre open a closed issues."

**Cvičenie 3:** „Máš 200 MB CSV súbor s logmi servera. Chceš nájsť všetky chyby."
  - *Účastníci píšu do chatu svoje prompty*
  - *Ukážka riešenia:* „Súbor `server.log` má 200 MB. Prečítaj ho po častiach po 10 MB. Vyhľadaj všetky riadky obsahujúce `ERROR` alebo `CRITICAL`. Extrahuj timestamp, úroveň logu a správu. Chyby zoskup podľa typu (ERROR/CRITICAL) a spočítaj výskyty. Výsledok ulož do `error_summary.json`. Ak narazíš na pamäťový limit, spracuj súbor inkrementálne."

- **Záver:** „Gratulujem! Práve si sa naučil framework, ktorý ti ušetrí stovky hodín. Cieľ-Kontext-Formát-Obmedzenia – zapamätaj si to. Ideme na ďalšiu lekciu!"

### Kľúčové body
- Framework CKFO: Cieľ – Kontext – Formát – Obmedzenia
- Chain of Thought, Few-shot, Role a Negatívny prompting
- 5 najčastejších chýb: vágnosť, preťaženie, chýbajúci formát, ignorovanie limitov, chýbajúci príklad
- Dobrý prompt = presný, konkrétny, s definovaným výstupom

### Domáca úloha
1. Napíš 5 promptov podľa frameworku CKFO pre reálne úlohy, ktoré riešiš (práca, škola, hobby). Každý prompt musí mať všetky 4 zložky
2. Zober svoj najhorší prompt z minulosti (keď si s agentom bojoval) a prepíš ho podľa CKFO. Porovnaj výsledky – napíš krátku reflexiu (50 slov)
3. Vyskúšaj Chain of Thought prompting na komplexnej úlohe (napr. návrh architektúry, refaktoring). Opíš, ako sa zmenil výstup oproti bežnému promptu
4. Nájdi 3 príklady zlých promptov v online tutoriáloch/fórach a prepíš ich. Uverejni „pred a po" do diskusie kurzu

---

## Lekcia 2: Práca so súbormi a kontextom
**Dĺžka videa:** 12 minút

### Detailný obsah / scenár

#### 0:00–1:00 | Úvod – súbory ako palivo agenta
- **Povedať:** „Agent bez súborov je ako kuchár bez surovín. V tejto lekcii sa naučíš, ako agentovi efektívne dodať dáta – malé súbory, veľké súbory, celé projekty."
- **Ukázať rýchlu ukážku:** Agent pracuje s 50-súborovým projektom – číta, edituje, vytvára nové súbory – všetko v jednej session
- **Povedať:** „Toto je tá pravá sila agenta – nie odpovedať na otázky, ale reálne pracovať s tvojím kódom."

#### 1:00–3:30 | Ako agent „vidí" súbory – súborový systém očami agenta
- **Povedať:** „Prime Agent má niekoľko spôsobov, ako interagovať so súbormi. Každý má svoje využitie."
- **Prehľad metód:**

**1. Automatické uvedomenie si adresárovej štruktúry:**
  - Agent automaticky vidí working directory, v ktorom bol spustený
  - Príkaz: `ls`, alebo Python `os.listdir('.')`
  - **Pozor:** Nevie o súboroch mimo working directory, pokiaľ mu nepovieš

**2. Čítanie súborov:**
  - Malé súbory: Agent ich načíta celé do kontextu (`.py`, `.md`, `.txt`, `.json`, `.csv`)
  - Stredné súbory: Agent ich číta po častiach (chunks)
  - Veľké súbory: Treba špeciálny prístup – streaming, indexy, sumarizácia
  - **Limit:** Kontextové okno modelu – napr. Claude 200K tokenov ≈ 150 000 slov. Ak je súbor väčší, treba stratégie

**3. Zápis a editácia súborov:**
  - `edit` skill: Presná editácia – nájde a nahradí text v existujúcom súbore
  - Bash: `echo "nový obsah" > súbor.txt`, `cat << 'EOF' > súbor.txt`
  - Python: `open('súbor.txt', 'w').write(...)`
  - **Pravidlo palca:** Na malé zmeny použi `edit`. Na vytváranie nových – bash alebo Python

**4. Práca s binárnymi súbormi:**
  - Obrázky: Agent ich vie čítať ako base64 (cez `attach_image`), ale nevie ich „vidieť" bez vizuálneho modelu
  - PDF: Agent extrahuje text z PDF (cez bash nástroje ako `pdftotext`)
  - **Dôležité:** Pri binárnych súboroch špecifikuj, či chceš extrahovať text alebo pracovať s metadátami

- **Povedať:** „Zapamätaj si: malé súbory – celé do kontextu. Veľké súbory – po častiach. Binárne – extrakcia. Kontextové okno je tvoj strop."

#### 3:30–5:30 | Praktické techniky práce so súbormi
- **Povedať:** „Poďme si ukázať reálne scenáre."

**Scenár 1: Refaktoring naprieč projektom**
  - Úloha: „Mám 30 `.js` súborov, potrebujem premenovať všetky funkcie z `oldFunctionName` na `newFunctionName`"
  - **Správny postup:**
    1. Agent si urobí prehľad: `grep -r "oldFunctionName" --include='*.js'`
    2. Identifikuje všetky výskyty aj s okolitým kontextom (riadok)
    3. Použije `edit` skill na každý súbor – presné nahradenie
    4. Overí: znova spustí `grep`, či niekde nezostalo staré pomenovanie
  - **Prečo to funguje:** Agent sám nájde, zmení a overí – ty len zadáš cieľ

**Scenár 2: Spracovanie CSV bez pandas**
  - Úloha: „Mám 150 MB CSV, nemôžem použiť pandas (prostredie bez knižníc)"
  - **Správny postup:**
    1. Agent použije Python `csv` modul
    2. Číta po riadkoch: `for row in csv.reader(file)`
    3. Spracúva inkrementálne, nezapisuje celý súbor do pamäte
    4. Výsledky priebežne zapisuje do výstupného súboru
  - **Prečo to funguje:** Memory-efficient spracovanie, vhodné pre akékoľvek veľké CSV

**Scenár 3: Vytvorenie projektu z viacerých zdrojov**
  - Úloha: „Spoj dokumentáciu z 10 `.md` súborov do jedného `docs.md` s obsahom"
  - **Správny postup:**
    1. Agent načíta všetky `.md` súbory
    2. Extrahuje nadpisy (## Heading) z každého
    3. Vytvorí obsah s odkazmi na začiatku
    4. Spojí všetky súbory do jedného, zachová formátovanie
  - **Prečo to funguje:** Agent kombinuje čítanie, analýzu a zápis – tri rôzne fázy

- **Povedať:** „Všimni si vzorec: **identifikuj → spracuj → over.** Agent to robí automaticky, keď mu dáš dobrý prompt."

#### 5:30–7:30 | Kontextové okno – manažment a stratégie
- **Povedať:** „Kontextové okno je najväčšie obmedzenie agenta. Musíš mu rozumieť, inak ťa bude brzdiť."
- **Vysvetlenie:**
  - Každý model má limit: Claude 200K, GPT-4 128K, DeepSeek V4 128K, Gemini 2.5 1M tokenov
  - 1 token ≈ 0.75 slova v angličtine, ≈ 0.5 slova v slovenčine (kvôli diakritike)
  - Do kontextu sa počíta: systém prompt + história konverzácie + výstupy nástrojov + súbory
  - Keď sa blížiš k limitu, agent začne „zabúdať" začiatok konverzácie

**Stratégie pre veľké projekty:**
  1. **Chunking:** „Spracuj prvých 500 riadkov, výsledok ulož, potom pokračuj..."
  2. **Sumarizácia:** „Sumarizuj doterajší priebeh (200 slov) a pokračuj v úlohe"
  3. **Indexovanie:** „Vytvor index všetkých funkcií/tried v projekte, potom spracúvaj podľa indexu"
  4. **Kontextové súbory:** „Vytvor `context.md` s kľúčovými informáciami, ktoré agent potrebuje"

- **Ukázať praktický príklad:**
  - Projekt s 200 `.py` súbormi, celkovo 50 000 riadkov
  - Agent vytvorí index: `grep -rn "def \|class " --include='*.py' > symbols.txt`
  - Index má len 3 000 riadkov namiesto 50 000
  - Agent používa index na navigáciu – hľadá v indexe, potom číta len relevantné súbory

- **Povedať:** „Indexovanie je tvoj najlepší priateľ pri veľkých projektoch. Nauč sa ho používať."

#### 7:30–9:00 | Práca s adresármi a štruktúrou projektu
- **Povedať:** „Agent nie je obmedzený len na jeden priečinok. Vie prechádzať štruktúrou, vytvárať nové adresáre, reorganizovať súbory."

**Užitočné bash príkazy pre agenta:**
  - `find . -name '*.py'` – nájde všetky Python súbory
  - `tree -L 2` – zobrazí stromovú štruktúru (ak je nainštalovaný)
  - `wc -l *.py` – spočíta riadky v každom `.py` súbore
  - `du -sh *` – zobrazí veľkosť podadresárov

**Python pre štruktúru:**
  - `os.walk('.')` – prechádza všetky podadresáre
  - `pathlib.Path` – moderné API pre cesty k súborom
  - `glob.glob('**/*.py', recursive=True)` – nájde všetky `.py` súbory rekurzívne

- **Praktický tip:** „Ak chceš, aby agent rozumel štruktúre projektu, nechaj ho vygenerovať prehľad:"

```
Vytvor súbor `project_structure.md` s kompletnou stromovou štruktúrou projektu (len názvy súborov a adresárov, max 2 úrovne). Potom podľa tejto štruktúry identifikuj všetky Python moduly a ich závislosti.
```

- **Povedať:** „Agent získa mapu projektu a môže sa v ňom inteligentne pohybovať."

#### 9:00–10:30 | Best practices: čo robiť a čo NEROBIŤ
- **Povedať:** „Rýchly súhrn pravidiel, ktoré ti ušetria bolesť hlavy."

**✅ ROB:**
  - Vždy špecifikuj cestu k súborom (absolútnu alebo relatívnu voči working directory)
  - Pri veľkých súboroch použi chunking: „Spracuj po 500 riadkov"
  - Vytváraj medzivýstupy: „Ulož priebežný výsledok do X, potom pokračuj"
  - Používaj indexovanie pre veľké projekty: „Vytvor index funkcií/tried"
  - Pri binárnych súboroch špecifikuj formát extrakcie: „Extrahuj text z PDF, ignoruj obrázky"

**❌ NEROB:**
  - Nepokúšaj sa načítať 50 MB súbor naraz do kontextu – agent sa zasekne
  - Nenechávaj agenta hádať, ktorý súbor myslíš – „tamten súbor" nefunguje
  - Nezabúdaj na working directory – agent nevidí mimo neho
  - Needituj binárne súbory priamo – najprv extrahuj text, potom pracuj

- **Povedať:** „Toto si zapamätaj: **identifikuj – spracuj – over.** A pri veľkých dávkach: **indexuj a chunkuj.**"

#### 10:30–12:00 | Zhrnutie a mini-cvičenie
- **Povedať:** „Poďme si to vyskúšať. Máš priečinok s 20 `.txt` súbormi logov. Každý má 10 MB. Potrebuješ nájsť všetky riadky s 'ERROR' a 'CRITICAL', zlúčiť ich a zoradiť podľa času."
- *Účastníci navrhujú postup*
- **Ukážka riešenia:** 
  1. Agent: `grep -rh "ERROR\|CRITICAL" *.txt > all_errors.txt`
  2. Agent: „Súbor all_errors.txt má X MB. Spracujem ho po častiach. Extrahujem timestamp z každého riadku, zoradím chronologicky. Výsledok uložím do `errors_sorted.json`."
  3. Agent iteruje, kým nespracuje všetky súbory

- **Záver:** „Toto je presne ten pattern: identifikuj súbory, extrahuj relevantné dáta, spracuj a zoraď. Rovnako budeš pracovať s akýmikoľvek veľkými datasetmi."

### Kľúčové body
- Agent pracuje so súbormi cez čítanie, editáciu, zápis a indexovanie
- Kontextové okno je limit – chunking, sumarizácia, indexovanie sú riešenia
- Vždy špecifikuj cesty k súborom presne
- Pri veľkých dátach: identifikuj → spracuj po častiach → over výsledok

### Domáca úloha
1. Vytvor priečinok s 10 rôznymi súbormi (txt, csv, json, md, py). Nechaj agenta spraviť kompletnú analýzu: nájdi duplicitné slová, spočítaj výskyty, výsledok ulož ako report
2. Nájdi vo svojom existujúcom projekte 3 súbory väčšie ako 1000 riadkov. Nechaj agenta vytvoriť ich index a vysvetliť štruktúru každého z nich
3. Vyskúšaj chunking: Daj agentovi 5 MB CSV a nechaj ho spracovať po 100-riadkových dávkach. Porovnaj čas spracovania s jednorazovým načítaním
4. Vytvor Markdown súbor s prehľadom všetkých súb  

borov v tvojom projekte (stromová štruktúra + stručný popis každého súboru)

---

## Lekcia 3: Python a bash – agent ako vývojár
**Dĺžka videa:** 15 minút

### Detailný obsah / scenár

#### 0:00–1:30 | Úvod – prečo Python a bash v agentovi
- **Povedať:** „Toto je lekcia, ktorá ťa naučí agenta programovať. Nie odpovedať na otázky o kóde, ale reálne ho spúšťať, testovať, ladiť."
- **Ukázať rýchlu ukážku:** Agent v IPython kernel-i – spúšťa Python skript, vidí chybu, opravuje ju, spúšťa znova. Celý cyklus vývoja.
- **Povedať:** „Prime Agent nie je glorifikovaný ChatGPT. Je to skutočné vývojové prostredie. A Python + bash sú jeho ruky."

#### 1:30–3:30 | IPython kernel – mozog za operáciou
- **Povedať:** „IPython kernel je to, čo odlišuje Prime Agenta od všetkých ostatných. Nie je to len 'spusti kód a vráť výsledok'. Je to perzistentné Python prostredie."
- **Čo to znamená v praxi:**
  - **Premenné prežívajú naprieč krokmi:** Definuješ `x = 5` v kroku 1, v kroku 10 stále existuje
  - **Importy zostávajú:** `import pandas as pd` – načíta sa raz, používaš celú session
  - **Helper funkcie:** Definuješ si `def calculate_tax(amount): ...` a voláš ju opakovane
  - **Výstupy sa kumulujú:** Agent vidí všetky predošlé výstupy a stavia na nich
  - **Chybové hlásenia sú spätná väzba:** Agent spustí kód, vidí `NameError: name 'x' is not defined`, opraví a spustí znova
- **Ukázať na obrazovke reálnu session:**
  ```python
  # Krok 1: Agent definuje premennú
  data = [1, 2, 3, 4, 5]

  # Krok 5: Agent používa tú istú premennú
  average = sum(data) / len(data)
  print(f"Priemer: {average}")

  # Krok 10: Agent pridáva ďalšie výpočty
  import statistics
  median = statistics.median(data)
  ```
- **Povedať:** „Toto je zásadný rozdiel oproti ChatGPT. Tam každá správa začína od nuly. Tu všetko pretrváva."

#### 3:30–5:30 | Čo agent dokáže s Pythonom
- **Povedať:** „Poďme si prejsť praktické kategórie úloh, ktoré agent zvládne s Pythonom."

**1. Spracovanie dát:**
  - CSV, JSON, XML parsovanie
  - Analýza textu – regex, NLP, spracovanie reťazcov
  - Matematické výpočty – `math`, `statistics`, `decimal`
  - Vizualizácia – `matplotlib`, `seaborn` (ukladá obrázky, nezobrazuje interaktívne)
  - Príklad: „Načítaj sales.csv, vypočítaj kĺzavý priemer 7 dní, vykresli graf a ulož ako sales_trend.png"

**2. Súborové operácie:**
  - Hromadné premenovanie: `os.rename()`, `pathlib.Path.rename()`
  - Konverzia formátov: CSV → JSON, Markdown → HTML, XML → YAML
  - Generovanie kódu: Vytváranie boilerplate, šablón, config súborov
  - Príklad: „Skonvertuj všetky `.csv` súbory v priečinku na `.json` s rovnakou štruktúrou"

**3. Web scraping a API volania:**
  - `requests`, `httpx` – HTTP requesty
  - Parsovanie HTML: `BeautifulSoup`, `lxml`
  - Práca s REST API: GET, POST, autentifikácia, headers
  - Príklad: „Získaj dáta z API `https://api.example.com/v1/orders`, transformuj JSON odpoveď do CSV"

**4. Automatizácia a scripting:**
  - Automatizácia buildu: `subprocess`, `os.system`
  - Testovanie: `pytest`, `unittest`
  - Code quality: `black`, `flake8`, `mypy`
  - Príklad: „Spusti testy v `tests/`, nájdi failing testy, oprav kód, spusti znova"

- **Povedať:** „Python v agentovi = tvoje dáta, tvoje nástroje, tvoja automatizácia. Všetko v jednom prostredí."

#### 5:30–7:30 | Bash v agentovi – systémová sila
- **Povedať:** „Bash dopĺňa Python. Nie všetko potrebuje Python – niekedy je bash rýchlejší, jednoduchší, priamočiarejší."
- **Kedy použiť bash namiesto Pythonu:**
  - **Inštalácia balíčkov:** `uv pip install pandas` – rýchlejšie ako Python `subprocess`
  - **Súborové operácie:** `grep`, `find`, `sed`, `awk` – roky optimalizované UNIX nástroje
  - **Git operácie:** `git log`, `git diff`, `git blame` – natívne, bez knižníc
  - **System info:** `top`, `df -h`, `free -m` – monitoring zdrojov
  - **Refaktoring naprieč súbormi:** `grep -r "oldFunction" --include='*.js' | wc -l` – nájde všetky výskyty
- **Ukázať praktický príklad – refaktoring s bash:**
  ```
  # Nájdi všetky súbory s deprecated API volaniami
  grep -rn "oldAPI.call\|oldAPI.query" --include='*.ts' src/

  # Spočítaj výskyty
  grep -rc "oldAPI" --include='*.ts' src/ | sort -t: -k2 -rn

  # Nahraď vo všetkých súboroch
  find src/ -name '*.ts' -exec sed -i 's/oldAPI/newAPI/g' {} +
  ```
- **Povedať:** „Bash je najrýchlejší spôsob, ako spracovať stovky súborov naraz. Agent ho používa prirodzene."

#### 7:30–9:30 | Python + bash spolu – synergia
- **Povedať:** „Skutočná sila prichádza, keď agent kombinuje Python a bash v jednej úlohe."
- **Ukázať reálny workflow:**

**Príklad 1: Spracovanie logov s Python + bash:**
  1. **Bash:** `grep "ERROR" app.log | cut -d' ' -f1,3,5- > errors_raw.txt`
     (Extrahuje timestamp, level a message z logu – rýchlejšie ako Python)
  2. **Python:** Načíta `errors_raw.txt`, parsuje timestamp-y, zoskupí podľa hodín, vykreslí graf
     ```python
     from collections import Counter
     import matplotlib.pyplot as plt

     hours = Counter()
     with open('errors_raw.txt') as f:
         for line in f:
             hour = line.split()[0].split(':')[0]
             hours[hour] += 1

     plt.bar(hours.keys(), hours.values())
     plt.savefig('error_distribution.png')
     ```
  3. Výsledok: Graf rozloženia chýb počas dňa – kombinácia bash rýchlosti a Python flexibility

**Príklad 2: Príprava datasetu pre ML:**
  1. **Bash:** `find data/ -name '*.csv' -exec wc -l {} + | sort -rn`
     (Zistí veľkosti všetkých CSV súborov)
  2. **Python:** Načíta len súbory s >1000 riadkami, spojí ich, vyčistí
     ```python
     import pandas as pd
     import glob

     files = glob.glob('data/**/*.csv', recursive=True)
     dfs = [pd.read_csv(f) for f in files if os.path.getsize(f) > 10000]
     combined = pd.concat(dfs, ignore_index=True)
     ```
  3. Výsledok: Spojený dataset pripravený na trénovanie

- **Povedať:** „Bash = rýchlosť. Python = flexibilita. Spolu = neobmedzené možnosti."

#### 9:30–11:00 | Inštalácia balíčkov – uv a dependency management
- **Povedať:** „Keď agent potrebuje novú knižnicu, vie si ju nainštalovať sám. Nemusíš opúšťať session."
- **Ukázať:**
  ```bash
  # Agent sám zistí, že potrebuje pandas
  uv pip install pandas

  # Alebo konkrétnu verziu
  uv pip install pandas==2.0.3

  # Alebo z requirements.txt
  uv pip install -r requirements.txt
  ```
- **Povedať:** „Prime Agent používa `uv` – rýchly Python package manager. Inštalácia trvá sekundy, nie minúty."
- **Dôležité upozornenie:**
  - Nainštalované balíčky sú lokálne pre danú session – po reštarte neprežijú
  - Ak chceš perzistentné knižnice, vytvor si `requirements.txt` a nechaj agenta inštalovať na začiatku session
  - Alebo použi projektové virtuálne prostredie (`.venv`)

#### 11:00–13:00 | Debugging s agentom – ako na to
- **Povedať:** „Agent nie je neomylný. Občas spraví chybu. Ale vie ich aj opraviť – keď mu dáš správny feedback."
- **Debugging workflow:**
  1. **Agent spustí kód → dostane chybu**
  2. **Agent prečíta chybovú hlášku** – `TypeError`, `NameError`, `ImportError`...
  3. **Agent opraví kód** – sám, bez tvojho zásahu
  4. **Agent spustí znova** – overí opravu
  5. **Ak stále zlyhá:** Skúsi iný prístup, inú logiku

- **Ako mu pomôcť:**
  - Daj mu kontext: „Tento kód padá na `NoneType`, asi nie sú dáta. Skontroluj, či súbor existuje a nie je prázdny."
  - Špecifikuj expected behavior: „Funkcia by mala vrátiť dictionary, nie list."
  - Daj mu test case: „Otestuj s `test_input = [1, 2, 3]`, očakávaný výstup `6`."

- **Ukázať praktickú ukážku debugging session:**
  - Agent vytvorí skript, spustí ho, dostane `IndexError: list index out of range`
  - Agent sám pridá kontrolu dĺžky poľa: `if len(data) > index:`
  - Spustí znova – funguje
  - **Povedať:** „Vidíš? Agent = napíše → otestuje → opraví → otestuje. Rovnako ako skutočný vývojár."

#### 13:00–14:00 | Best practices pre Python a bash v agentovi
- **Povedať:** „Pár pravidiel pre efektívne používanie Pythonu a bashu."

**✅ ROB:**
  - Používaj Python na spracovanie dát, analýzu, complex logic
  - Používaj bash na súborové operácie, inštalácie, systémové príkazy
  - Kombinuj: Bash pre rýchlu extrakciu, Python pre hlbkové spracovanie
  - Inštaluj len to, čo potrebuješ – `uv pip install` je tvoj priateľ
  - Uchovávaj si `requirements.txt` pre opakovateľné sessiony

**❌ NEROB:**
  - Nepoužívaj Python na čisté súborové operácie (grep, find sú rýchlejšie)
  - Neinštaluj ťažké knižnice (CUDA, PyTorch) ak nepotrebuješ – majú veľké dependencies
  - Nezabúdaj, že premenné prežívajú naprieč krokmi – vyčisti ich, ak treba
  - Nespúšťaj kód naslepo bez testovania – vždy over výstup

#### 14:00–15:00 | Zhrnutie a mini-cvičenie
- **Povedať:** „Máš CSV s 50 000 riadkami predajných dát. Potrebuješ:
  1. Nájsť top 10 produktov podľa tržieb
  2. Vypočítať medzimesačný rast
  3. Vytvoriť graf trendu
  4. Všetko uložiť do prehľadného reportu"
- *Účastníci navrhujú postup – kedy Python, kedy bash*
- **Riešenie:**
  - Bash: `wc -l sales.csv` – rýchle overenie veľkosti
  - Python: Načítať pandas, groupby + sum, sort, head(10)
  - Python: Vypočítať `pct_change()` pre medzimesačný rast
  - Python: `matplotlib` graf, `plt.savefig()`
  - Python: Vygenerovať Markdown report s tabuľkami a grafom

- **Záver:** „Toto je reálny analytický workflow. Spustil by si ho jediným promptom. V Module 3 sa naučíš, ako z tohto spraviť opakovateľný skill."

### Kľúčové body
- IPython kernel = perzistentné Python prostredie – premenné, importy, helper funkcie prežívajú
- Python = dáta, analýza, komplexná logika
- Bash = rýchlosť, súborové operácie, systémové príkazy
- Kombinácia Python + bash = maximálna produktivita
- Debugging = napíš → otestuj → oprav → otestuj (cyklus agenta)

### Domáca úloha
1. Vytvor Python skript, ktorý spracuje CSV s 10 000+ riadkami – nechaj agenta napísať, spustiť a odladiť celý kód
2. Napíš bash one-liner, ktorý nájde 5 najväčších súborov v tvojom projekte. Potom ho nechaj agenta vysvetliť, čo robí
3. Kombinuj Python a bash: Nechaj agenta extrahovať dáta z log súborov bash-om, spracovať Pythonom a vygenerovať report
4. Nainštaluj cez agenta knižnicu, ktorú ešte nemáš (napr. `rich`, `typer`, `pydantic`) a nechaj ho napísať demo skript, ktorý ju používa

---

## Lekcia 4: Web search a research
**Dĺžka videa:** 12 minút

### Detailný obsah / scenár

#### 0:00–1:30 | Úvod – internet ako zdroj nekonečných dát
- **Povedať:** „Agent bez prístupu na web je ako knižnica bez kníh. V tejto lekcii sa naučíš, ako z agenta spraviť výskumníka, ktorý vie nájsť, overiť a syntetizovať informácie z internetu."
- **Ukázať rýchlu ukážku:** Agent vyhľadáva na webe, nachádza 15 zdrojov, porovnáva informácie, vytvára research report s citáciami
- **Povedať:** „Toto je jeden z najsilnejších skillov agenta – schopnosť pracovať s internetom v reálnom čase."

#### 1:30–3:30 | Ako web search funguje v Prime Agentovi
- **Povedať:** „Prime Agent používa `websearch` skill. Je to Python funkcia, ktorú agent volá priamo z IPython kernelu."
- **Ako to funguje technicky:**
  - Agent dostane tvoj dotaz (napr. „Najlepšie Python knižnice pre data science 2025")
  - Zavolá `await websearch("query")` – odošle dotaz do Google Search API (cez Serper)
  - Dostane výsledky: titulok, URL, snippet (krátky popis), prípadne knowledge graph
  - Výsledky sa vrátia do kontextu agenta ako štruktúrované dáta
  - Agent ich použije na zodpovedanie otázky alebo ďalší research
- **Čo web search NErobí:**
  - Neotvára stránky (nescrapuje) – vracia len search results (názov + snippet)
  - Neprehľadáva hlboký web – len verejne indexované stránky
  - Nevracia obrázky, videá, ani dynamický obsah
- **Povedať:** „Web search = rýchly prehľad. Na hĺbkový prieskum stránok treba scraping. K tomu sa dostaneme."

#### 3:30–5:30 | Kedy použiť web search vs scraping
- **Povedať:** „Web search a scraping sú dve rozdielne veci. Musíš vedieť, kedy ktoré použiť."

**Web search (websearch):**
  - Rýchla odpoveď na otázku: „Aká je aktuálna cena Bitcoinu?"
  - Prehľad zdrojov: „Top 10 Python knižníc pre ML v 2025"
  - Overenie faktov: „Je `library X` stále maintainovaná?"
  - Trendy a novinky: „Čo je nové v React 19?"
  - Konkurenčná analýza: „Kto sú hlavní konkurenti `company Y`?"

**Web scraping (priamy prístup na stránky):**
  - Extrakcia špecifických dát zo stránok: ceny produktov, zoznamy, tabuľky
  - Získanie plného textu článkov (nie len snippet)
  - Monitorovanie zmien na konkrétnych stránkach
  - Zber dát pre datasety (napr. všetky blog posty za posledný rok)
  - Hĺbková analýza obsahu (nielen search snippet)

- **Praktický príklad rozdielu:**
  - Web search: „Aké sú hlavné výhody Kubernetes?" → 10 odkazov s popismi
  - Web scraping: „Prejdi všetkých 10 odkazov, extrahuj kompletný text každého článku, porovnaj argumenty, nájdi spoločné témy" → hĺbková analýza

- **Povedať:** „Web search = šírka (veľa zdrojov, rýchlo). Scraping = hĺbka (detailné dáta z menšieho počtu zdrojov)."

#### 5:30–7:30 | Ako správne používať web search
- **Povedať:** „Web search vyzerá jednoducho, ale sú triky, ktoré ťa posunú od nováčika k profíkovi."

**1. Presné vyhľadávanie s operátormi:**
  - Presná fráza: `"prime agent" skills` – hľadá presne „prime agent" ako frázu
  - Vylúčenie: `prime agent -reddit` – vynechá výsledky z Redditu
  - Doména: `site:github.com prime agent` – len z GitHubu
  - Kombinácia: `"AI agent" (terminal OR CLI) site:github.com -chatgpt`
  - Časové obmedzenie: Agent môže požiadať o výsledky za posledný rok/mesiac/týždeň

**2. Štruktúrované vyhľadávanie:**
  - Namiesto jedného širokého dotazu rozdeľ na viacero špecifických
  - Zlý: „Všetko o Prime Agent"
  - Dobrý: 3 separátne vyhľadávania:
    1. „Prime Agent features and capabilities"
    2. „Prime Agent vs Cursor vs Copilot comparison"
    3. „Prime Agent pricing and setup guide"

**3. Krížové overenie:**
  - Jeden zdroj = jeden názor
  - Nechaj agenta vyhľadať viacero zdrojov a porovnať ich
  - Príklad: „Nájdi 5 zdrojov o TOP 10 Python AI knižniciach. Porovnaj ich odporúčania, nájdi zhodu (spomenuté vo viacerých) a vytvor syntézu."

**4. Iteratívne vyhľadávanie:**
  - Prvé vyhľadávanie → zanalyzuj výsledky → identifikuj medzery → druhé vyhľadávanie
  - Príklad: 
    1. „Nájdi hlavné výhody Kubernetes" → 10 zdrojov
    2. „Z týchto 10 zdrojov vidím, že často spomínajú 'scaling' a 'orchestration'. Teraz nájdi konkrétne príklady Kubernetes scaling failures a porovnaj s Docker Swarm."
    3. Výsledok: Hlbšia, nuansovanejšia analýza

- **Povedať:** „Tieto 4 techniky – operátory, štruktúrovanie, krížové overenie a iterácia – ťa naučia používať web search ako profesionál."

#### 7:30–9:30 | Výskumný workflow krok za krokom
- **Povedať:** „Poďme si ukázať kompletný výskumný workflow na reálnom príklade."
- **Zadanie:** „Potrebujem zistiť, či sa oplatí investovať do Kubernetes pre náš startup. Sme 5-členný tím, produkt je monolit v Node.js, nasadený na AWS EC2."

**Krok 1: Prvotný prieskum (broad search)**
  - Agent: `websearch("Kubernetes pros and cons for small teams 2025")`
  - Agent: `websearch("Kubernetes vs AWS ECS vs Docker Swarm comparison")`
  - Agent: `websearch("Kubernetes total cost of ownership small team")`
  - Výsledok: 30 odkazov s rôznymi pohľadmi

**Krok 2: Analýza a syntéza**
  - Agent vyhodnotí:
    - Výhody: Škálovanie, ekosystém, community, managed options (EKS, GKE)
    - Nevýhody: Zložitosť, náklady na réžiu, learning curve pre tím
    - Zistenie: Pre 5-členný tím s monolitom je pravdepodobne overkill

**Krok 3: Hĺbkový prieskum alternatív**
  - Agent: `websearch("AWS ECS Fargate vs Kubernetes for Node.js monolith")`
  - Agent: `websearch("ECS Fargate pricing calculator small team")`
  - Agent: `websearch("migrating from monolith to microservices when to do it")`

**Krok 4: Záverečná správa**
  - Agent vytvorí štruktúrovaný report:
    - Executive summary
    - Porovnávacia tabuľka (K8s vs ECS vs Docker Swarm vs zostať pri EC2)
    - Nákladová analýza (1 rok, 3 roky)
    - Odporúčanie s kontextom (5-členný tím, monolit Node.js, AWS)
    - Riziká a mitigácie

- **Povedať:** „Toto je výskumný workflow. Jeden prompt, 4 fázy, komplexný výstup. Agent robí všetko – ty len čítaš výsledok."

#### 9:30–11:00 | Ako zadať dokonalý research prompt
- **Povedať:** „Framework pre research prompt:"

**Šablóna research promptu:**
  ```
  Preskúmaj [TÉMA]. Potrebujem:
  1. [ČO konkrétne zistiť]
  2. [AKÉ zdroje použiť / obmedzenia]
  3. [FORMÁT výstupu – report, tabuľka, zoznam]
  4. [ČASOVÝ RÁMEC – posledný rok, mesiac, vždy aktuálne]
  ```

**Príklad:**
  ```
  Preskúmaj trh s AI coding agentmi v roku 2025. Potrebujem:
  1. Zoznam všetkých významných hráčov (Cursor, Copilot, Cody, Codeium, Prime Agent...)
  2. Pre každého: cena, kľúčové features, integrované modely, target audience
  3. Porovnávaciu tabuľku vo formáte Markdown s columns: Nástroj, Cena, Features, Modely, Vhodné pre
  4. Len nástroje aktívne udržiavané v roku 2025 – ignoruj ukončené/mŕtve projekty
  5. Na záver: odporúčanie pre sólového vývojára vs malý tím (3-10 ľudí)
  ```

- **Povedať:** „Všimni si: Cieľ je jasný. Zdroje špecifikované. Formát definovaný. Časový rámec stanovený. Plus akčné odporúčanie na konci."

#### 11:00–12:00 | Zhrnutie a best practices
- **Povedať:** „Rýchly prehľad toho najdôležitejšieho:"

**✅ ROB:**
  - Používaj operátory pre presné vyhľadávanie (quotes, site:, -exclude)
  - Rozdeľ široké témy na viacero špecifických dotazov
  - Vždy krížovo overuj – viacero zdrojov, porovnanie, syntéza
  - Iteruj – prvé výsledky použi na lepšie otázky
  - Definuj formát výstupu (report, tabuľka, odporúčanie)

**❌ NEROB:**
  - Nestaň sa len na jeden zdroj
  - Nezabúdaj na časový kontext (aktuálne dáta)
  - Nemiešaj web search s web scraping – sú to rôzne veci
  - Nenechávaj agenta bez štruktúry – research bez formátu je nehľadaný chaos

- **Záver:** „Web search a research s agentom = rýchlosť, šírka a hĺbka. V Module 3 sa naučíš, ako z tohto workflowu spraviť automatizovaný skill. Ale to už predbiehame..."

### Kľúčové body
- Web search = rýchly prehľad, scraping = hĺbková analýza
- Operátory: quotes, site:, -exclude pre presné vyhľadávanie
- Krížové overenie: viacero zdrojov → porovnanie → syntéza
- Iteratívny research: prvé výsledky → lepšie otázky → hlbšia analýza
- Research prompt = téma + čo zistiť + zdroje + formát + časový rámec

### Domáca úloha
1. Vykonaj kompletný research na tému „najlepšie techniky prompt engineeringu pre AI agentov 2025". Použi 3+ iterácií web search a vytvor syntézu
2. Porovnaj 3 konkurenčné produkty vo svojom odvetví. Nechaj agenta nájsť informácie, vytvoriť porovnávaciu tabuľku a napísať odporúčanie
3. Vyskúšaj time-bound research: „Najlepšie CSS frameworky za posledných 6 mesiacov" vs „CSS frameworky 2023" – porovnaj výsledky, napíš rozdiely
4. Vytvor research prompt podľa šablóny z lekcie pre tému, ktorá ťa reálne zaujíma. Zdieľaj výsledok v diskusii

---

## Lekcia 5: Praktický projekt – Automatický prieskum trhu
**Dĺžka videa:** 9 minút

### Detailný obsah / scenár

#### 0:00–1:00 | Úvod – všetko dokopy
- **Povedať:** „Toto je moment, na ktorý sme celý modul čakali. Všetko, čo si sa doteraz naučil – prompt writing, práca so súbormi, Python, bash, web search – dáme do jedného reálneho projektu."
- **Ukázať výsledok:** Agent spustí automatický prieskum trhu – od zadania až po finálny report
- **Povedať:** „Toto nie je cvičenie. Toto je reálna úloha, ktorú budeš robiť pre svoj biznis. Poďme na to."

#### 1:00–3:00 | Definícia projektu – čo budeme robiť
- **Povedať:** „Zadanie nášho projektu:"

**Cieľ:** Automatický prieskum trhu pre fiktívny SaaS produkt „CloudFlow" – nástroj na správu cloudových zdrojov pre malé a stredné firmy.

**Čo potrebujeme zistiť:**
  1. Kto sú naši hlavní konkurenti? (minimálne 5)
  2. Aké sú ich kľúčové features? Čo odlišuje lídrov?
  3. Aká je cenová stratégia na trhu? (freemium, per-seat, usage-based)
  4. Čo hovoria zákazníci? (recenzie, hodnotenia, časté sťažnosti)
  5. Aké sú trendy v industry? (trh rastie/klesá, nové technológie)
  6. Kde sú medzery na trhu? (príležitosti pre náš produkt)

**Výstup:** Komplexný Markdown report `market_research.md` obsahujúci:
  - Executive summary (max 300 slov)
  - Profily top 5 konkurentov (názov, URL, features, cena, target audience, silné/slabé stránky)
  - Porovnávacia tabuľka (features matrix: my vs konkurenti)
  - Cenová analýza (rozsah cien, priemer, medián, najčastejší model)
  - Analýza zákazníckych sentimentov (zhrnutie recenzií, top 5 pain points)
  - Trendy a predikcie (3 kľúčové trendy na nasledujúci rok)
  - Odporúčanie pre positioning (3 konkrétne odporúčania)

- **Povedať:** „Toto nie je len 'search a hotovo'. Je to plnohodnotný prieskum. A agent ho spraví za 9 minút."

#### 3:00–5:30 | Krok 1 – Identifikácia konkurentov a zber dát
- **Povedať:** „Prvý krok: zistiť, kto sú hráči na trhu."
- **Ukázať live (alebo detailný screen recording):**

**Prompt 1 – Nájdenie konkurentov:**
  ```
  Preskúmaj trh s nástrojmi na správu cloudových zdrojov (cloud resource management) 
  pre malé a stredné firmy (SMB, 10-500 zamestnancov). Nájdi aspoň 8 nástrojov, 
  ktoré priamo konkurujú fiktívnemu produktu "CloudFlow" (multi-cloud dashboard, 
  cost optimization, resource monitoring). Pre každý nástroj zisti: 
  presný názov, URL, krátky popis (1-2 vety). 
  Výstup: číslovaný zoznam.
  ```

**Čo agent robí:**
  1. `websearch("cloud resource management tools SMB 2025")`
  2. `websearch("multi-cloud management platforms comparison")`  
  3. `websearch("cloud cost optimization tools for startups")`
  4. Zozbiera názvy z viacerých zdrojov (G2, Capterra, Product Hunt, blogy)
  5. Vyfiltruje duplicity, vyberie top 8 podľa relevancie
  6. Výstup: Zoznam konkurentov s URL a popismi

**Prompt 2 – Detailné profily:**
  ```
  Pre každého z týchto 8 konkurentov vytvor detailný profil. 
  Pre každého zisti:
  - Presný názov produktu a spoločnosti
  - Webová stránka (URL)
  - Kľúčové features (aspoň 5)
  - Cenový model (freemium/paid/enterprise) a približná cena (ak dostupná)
  - Cieľová skupina (SMB, enterprise, developers, DevOps)
  - Silné stránky a slabé stránky (aspoň 2 každé)
  Formát: Markdown profil pre každého konkurenta.
  ```

**Čo agent robí:**
  1. Pre každého konkurenta: navštívi stránku (alebo vyhľadá info)
  2. Extrahuje features z product pages, pricing pages
  3. Hľadá recenzie na G2, Capterra, TrustRadius
  4. Vytvorí štruktúrovaný profil
  5. Uloží do `competitors/competitor_N.md`

- **Povedať:** „Všimni si: 2 prompty, 8 konkurentov, detailné profily. Agent pracuje systematicky."

#### 5:30–7:00 | Krok 2 – Cenová analýza a zákaznícke sentimenty
- **Povedať:** „Teraz ideme hlbšie. Ceny a čo hovoria zákazníci."

**Prompt 3 – Cenová analýza:**
  ```
  Vytvor cenovú analýzu trhu cloud resource management nástrojov.
  Pre každého z 8 konkurentov zisti:
  - Presný cenový model (freemium, per-user, per-resource, usage-based)
  - Konkrétne ceny (ak dostupné – free tier, starter, pro, enterprise)
  - Skryté poplatky (support, onboarding, overages)
  - Celkový rozsah cien (minimum po maximum)

  Vypočítaj:
  - Priemernú cenu pre starter tier
  - Medián ceny
  - Najčastejší cenový model

  Výstup: Markdown sekcia do market_research.md s tabuľkou a sumárom.
  ```

**Čo agent robí:**
  1. Pre každého konkurenta: hľadá pricing page, dokumentáciu
  2. Extrahuje čísla z pricing tables
  3. Počíta štatistiky (priemer, medián, modus)
  4. Identifikuje pattern-y (väčšina používa per-seat? alebo usage-based?)
  5. Formátuje prehľadnú tabuľku

**Prompt 4 – Zákaznícke sentimenty:**
  ```
  Analyzuj zákaznícke recenzie a sentiment pre top 5 konkurentov 
  z nášho prieskumu. Pre každého konkurenta:
  - Nájdi recenzie na G2, Capterra a TrustRadius (ak dostupné)
  - Identifikuj top 3 veci, ktoré zákazníci chvália (strengths)
  - Identifikuj top 3 veci, na ktoré sa sťažujú (weaknesses)
  - Zhrň celkový sentiment (prevažne pozitívny/zmiešaný/negatívny)
  - Daj tomu skóre 1-5

  Na záver:
  - Top 5 najčastejších pain points naprieč všetkými produktmi
  - Čo zákazníci najviac oceňujú (spoločné themes)
  - Čo im najviac chýba (spoločné gaps)

  Výstup: Markdown sekcia do market_research.md
  ```

**Čo agent robí:**
  1. Pre každého z top 5 konkurentov:
     - `websearch("konkurent G2 reviews")`
     - `websearch("konkurent Capterra reviews")`
  2. Extrahuje rating (hviezdičky), číta review text
  3. Identifikuje opakujúce sa témy („easy to use", „great support", „expensive")
  4. Vytvorí sentiment summary
  5. Zozbiera pain points a wishes

- **Povedať:** „Ceny + recenzie = kompletný obraz trhu. Vieš, za koľko sa predáva a čo si zákazníci myslia."

#### 7:00–8:30 | Krok 3 – Trendy, predikcie a finálny report
- **Povedať:** „Posledný krok: kam trh smeruje a čo to znamená pre nás."

**Prompt 5 – Trendy a predikcie:**
  ```
  Preskúmaj aktuálne trendy v cloud resource management pre SMB segment.
  Identifikuj:
  - 3-5 kľúčových trendov na najbližších 12-24 mesiacov
  - Pre každý trend: popis, dopad na trh, príležitosti/hrozby
  - Ktoré technológie získavajú trakciu? (AI-driven, serverless, FinOps)
  - Aký je predpokladaný rast trhu? (CAGR, market size)

  Výstup: Markdown sekcia s:
  - Popis trendov (1 odstavec na trend)
  - Trakcia a momentum (early/adopting/mature)
  - Odporúčanie: na ktoré trendy sa zamerať a prečo
  ```

**Čo agent robí:**
  1. `websearch("cloud management market trends 2025 2026")`
  2. `websearch("FinOps adoption SMB 2025")`
  3. `websearch("AI in cloud management trends")`
  4. `websearch("cloud management market size CAGR forecast")`
  5. Syntetizuje z viacerých zdrojov (Gartner, Forrester, industry blogs)
  6. Vytvorí predikcie s kontextom pre náš segment

**Prompt 6 – Finálna kompilácia:**
  ```
  Zober všetky predošlé analýzy a vytvor kompletný market_research.md:

  Štruktúra:
  # Prieskum trhu: Cloud Resource Management pre SMB (2025)
  ## Executive Summary (max 300 slov)
  ## Profily konkurentov (top 5, detailné)
  ## Porovnávacia tabuľka (features matrix)
  ## Cenová analýza (štatistiky, modely)
  ## Zákaznícke sentimenty (recenzie, pain points)
  ## Trendy a predikcie (3 kľúčové trendy)
  ## Positioning odporúčanie (3 konkrétne odporúčania)

  Všetko v slovenčine, profesionálny tón, ready na prezentáciu.
  ```

**Čo agent robí:**
  1. Načíta všetky podklady z predošlých krokov
  2. Vytvorí štruktúrovaný Markdown dokument
  3. Pridá formátovanie (tabuľky, bold, headings)
  4. Napíše executive summary (syntéza všetkých zistení)
  5. Sformuluje 3 konkrétne, akčné odporúčania
  6. Uloží ako `market_research.md`

- **Povedať:** „Hotovo. 6 promptov. 9 minút. Kompletný prieskum trhu. Toto je sila agenta."

#### 8:30–9:00 | Zhrnutie modulu a čo ďalej
- **Povedať:** „Gratulujem! Práve si dokončil Modul 2. Poďme si zhrnúť, čo všetko si sa naučil:"
  - ✅ Framework CKFO pre dokonalé prompty
  - ✅ Práca so súbormi – čítanie, editácia, chunking, indexovanie
  - ✅ Python a bash – perzistentný kernel, kombinácia nástrojov
  - ✅ Web search a research – vyhľadávanie, scraping, syntéza
  - ✅ Praktický projekt – kompletný prieskum trhu
- **Povedať:** „V Module 3 sa naučíš, ako všetky tieto schopnosti zabaliť do skills – opakovateľných, zdieľateľných modulov. Automatizácia na úplne novej úrovni."

### Kľúčové body
- Kompletný prieskum trhu = identifikácia konkurentov + profily + ceny + recenzie + trendy + odporúčania
- Systematický prístup: 6 cielených promptov, každý stavia na predošlom
- Agent zvládne celý workflow od vyhľadávania až po finálny report
- Výstup je pripravený na prezentáciu – profesionálny, štruktúrovaný, akčný

### Domáca úloha
1. **Povinné:** Spusti kompletný prieskum trhu pre svoj vlastný produkt/projekt. Použi rovnakú štruktúru: konkurenti, profily, ceny, recenzie, trendy, report
2. Porovnaj výsledky svojho prieskumu s aspoň 2 konkurentmi manuálne – over presnosť a doplň, čo agent nenašiel
3. Vytvor skrátenú verziu prieskumu (5 minút namiesto 9) pre rýchle rozhodovanie – ktoré časti by si vypustil a prečo?
4. Zdieľaj svoj `market_research.md` v diskusii – získaj spätnú väzbu od komunity

---

## Kontrolný zoznam Modulu 2

Odškrtni si po splnení:

- [ ] Lekcia 1: Ovládam framework CKFO a viem napísať efektívny prompt pre agenta
- [ ] Lekcia 2: Viem pracovať so súbormi – čítanie, editácia, chunking veľkých súborov, indexovanie
- [ ] Lekcia 3: Ovládam Python a bash v agentovi – perzistentný kernel, kombinácia nástrojov, debugging
- [ ] Lekcia 4: Ovládam web search a research – vyhľadávanie, scraping, syntéza, iterácia
- [ ] Lekcia 5: Dokončil som praktický projekt – kompletný prieskum trhu s 6 promptami
- [ ] Všetky domáce úlohy odovzdané / splnené

---

*Prime Agent Masterclass © 2025 – Modul 2/6*

---

# Prime Agent Masterclass – Modul 3: Skills a customizácia

## Prehľad modulu

**Cieľ modulu:** Po absolvovaní tohto modulu budeš vedieť rozširovať schopnosti Prime Agenta pomocou skills – znovupoužiteľných modulov, ktoré menia jednorazové úlohy na opakovateľné workflowy. Naučíš sa skills nájsť, nainštalovať, používať a hlavne vytvárať vlastné – od jednoduchých markdown inštrukcií až po plnohodnotné Python moduly.

**Celková dĺžka:** 55 minút videa + domáce úlohy

---

## Lekcia 1: Čo sú skills a kde ich nájsť
**Dĺžka videa:** 10 minút

### Detailný obsah / scenár

#### 0:00–1:30 | Úvod – skills ako super-schopnosti agenta
- **Povedať:** „Vitaj v Module 3. Toto je modul, ktorý z teba spraví skutočného power-usera. Skills sú to, čo mení Prime Agenta z univerzálneho nástroja na tvojho osobného špecialistu."
- **Metafora:** „Ak je Prime Agent smartfón, skills sú appky. Bez nich je to skvelý hardvér, ale s nimi je to zariadenie, ktoré rieši presne TVOJE problémy."
- **Ukázať rýchlu ukážku:** Agent bez skillov: snaží sa, ale tápe. Agent so skillom: presne vie, čo robiť, má pripravené inštrukcie, postupy, integrácie.
- **Povedať:** „Skills = znovupoužiteľné balíčky expertízy. Vytvoríš raz, používaš navždy."

#### 1:30–3:00 | Čo presne je skill?
- **Povedať:** „Skill v Prime Agentovi je balíček inštrukcií, ktorý agentovi hovorí, AKO niečo robiť. Nie ČO robiť – to povieš ty. Skill definuje POSTUP."
- **Technická definícia:**
  - Skill = adresár so súborom `SKILL.md` (povinný)
  - Voliteľne: Python kód (`skill.py`), assety (šablóny, konfigurácie), závislosti
  - Skill sa aktivuje, keď používateľ spomenie kľúčové slová alebo explicitne zavolá názov skillu
  - Agent dostane inštrukcie zo skillu a aplikuje ich na tvoju úlohu
- **Čo skill obsahuje (SKILL.md štruktúra):**
  - **Názov a popis:** Kedy skill použiť
  - **Trigger phrases:** Aké frázy skill spúšťajú (napr. „A/B test", „experiment")
  - **Inštrukcie:** Krok-za-krokom postup, čo má agent robiť
  - **Príklady:** Konkrétne príklady použitia pre agenta
  - **Obmedzenia:** Na čo si dať pozor, čo nerobiť
- **Povedať:** „Skill = expertný postup zabalený do súboru. Agent ho načíta, aplikuje a ty dostaneš konzistentný výsledok – vždy."

#### 3:00–5:00 | Ako skills fungujú v praxi
- **Povedať:** „Poďme si ukázať, ako skill reálne funguje na príklade."

**Príklad 1: Skill na code review**
  - Používateľ: „Sprav code review môjho Pull Requestu"
  - Agent načíta `code-review/SKILL.md`
  - Skill hovorí:
    - Pozri sa na zmenené súbory (git diff)
    - Skontroluj: naming conventions, DRY principle, error handling, test coverage
    - Napíš feedback v tóne: konštruktívny, konkrétny, s príkladmi
    - Výstup formát: Markdown s checkboxami
  - Agent aplikuje inštrukcie na tvoj kód
  - Výsledok: Konzistentné code review – vždy rovnaká štruktúra, kvalita, tón

**Príklad 2: Skill na tvorbu blog postov**
  - Používateľ: „Napíš blog post o našom novom featur-e"
  - Agent načíta `blog-post/SKILL.md`
  - Skill hovorí:
    - Štruktúra: Hook → Problém → Riešenie → Features → Výhody → CTA
    - Tón: Konverzačný, prístupný, technický ale nie suchý
    - Dĺžka: 800-1200 slov
    - Vždy pridaj: meta description (max 155 znakov), 3 social media blurbs
    - Výstup: Markdown súbor pripravený na publikovanie
  - Agent vytvorí blog post podľa šablóny
  - Výsledok: Blog post, ktorý je ready-to-publish – nie len surový text

- **Povedať:** „Vidíš ten rozdiel? Bez skillu agent vytvorí generický text. So skillom vytvorí text podľa tvojej presnej šablóny – tón, štruktúra, dĺžka, všetko sedí."

#### 5:00–7:00 | Ekosystém skillov – čo je k dispozícii
- **Povedať:** „Prime Agent má zabudovanú knižnicu skills, ktoré sú pripravené na použitie hneď po inštalácii. A potom je tu obrovský ekosystém komunitných skillov."
- **Zabudované (built-in) skills:**
  - `edit` – Presná editácia súborov (nájdi a nahraď)
  - `websearch` – Google vyhľadávanie (Serper API)
  - `attach_image` – Načítanie obrázkov do kontextu
  - `agent_message` – Komunikácia medzi agentmi (parent-child-sibling)
  - `agent_observe` – Pozorovanie iných agentov
  - `compact` – Manažment kontextového okna
  - `goal` – Sledovanie a manažment cieľov
  - `rlm_heartbeat` – Plánovanie opakovaných úloh

- **Komunitné skills (dostupné cez inštaláciu):**
  - **Marketing:** copywriting, SEO audit, social media, email campaigns, A/B testing, ads, competitor analysis
  - **Vývoj:** code review, testing, CI/CD, database migrations, API design
  - **Biznis:** financial modeling, pitch deck creation, market research, product strategy
  - **Dizajn:** UI/UX review, design systems, accessibility audit
  - **Dáta:** data analysis, visualization, ETL pipelines, reporting

- **Kde skills nájsť:**
  - `/skills` príkaz v Prime Agentovi – zobrazí všetky nainštalované skilly
  - `~/.prime/agent/skills/` – lokálny adresár s tvojimi skillmi
  - `~/.agents/skills/` – zdieľané skilly z agenta do agenta (.agents adresár)
  - Online repozitáre: GitHub, komunitné fóra, Prime Intellect hub

- **Povedať:** „Desiatky skills sú už pripravené. Marketing, vývoj, biznis, dizajn, dáta. Nájdeš ich cez `/skills` alebo v `.agents` priečinku."

#### 7:00–9:00 | Ako skill objaviť a vyhodnotiť
- **Povedať:** „Nie každý skill je kvalitný. Musíš vedieť rozoznať dobrý skill od zlého."

**Kritériá kvalitného skillu:**
  1. **Jasný trigger:** Presne vieš, kedy skill použiť („A/B test", nie „marketing")
  2. **Detailné inštrukcie:** Krok-za-krokom, nie vágne „sprav to dobre"
  3. **Konkrétne príklady:** 2-3 príklady použitia – ako presne má výstup vyzerať
  4. **Definovaný výstup:** Aký formát, štruktúra, kvalita
  5. **Obmedzenia a edge cases:** Na čo si dať pozor

**Varovné signály zlého skillu:**
  - Príliš široký trigger: „marketing", „writing", „code"
  - Vágne inštrukcie: „write good code", „make it better"
  - Žiadne príklady – agent nevie, čo očakávaš
  - Žiadny definovaný výstupný formát
  - Nejasné, kedy skill prestáva byť relevantný

- **Praktický príklad evaluácie:**
  - **Dobrý skill:** `seo-audit/SKILL.md` – „Spusť SEO audit webstránky. Skontroluj: meta tags, headings, content quality, technical SEO, backlinks. Výstup: skóre 0-100, zoznam issues, prioritizované odporúčania."
  - **Zlý skill:** `marketing-help/SKILL.md` – „Pomôžem ti s marketingom. Opýtaj sa ma čokoľvek." (nič konkrétne)

- **Povedať:** „Kvalitný skill = vieš presne, čo dostaneš, kedy a v akej kvalite. Ak to nie je jasné z SKILL.md, skill je zlý."

#### 9:00–10:00 | Zhrnutie a objavovanie
- **Povedať:** „Poďme preskúmať, aké skilly už máš k dispozícii."
- **Live ukážka v termináli:**
  ```bash
  prime-agent
  # V Prime Agent TUI:
  /skills
  ```
- **Čo vidíš:**
  - Zoznam všetkých nainštalovaných skillov
  - Každý s názvom, popisom, trigger phrases
  - Rozdelenie: built-in vs custom
- **Úloha pre účastníkov:** „Pozri sa na `/skills`, nájdi 3 skilly, ktoré by si vedel použiť vo svojej práci, a prečítaj si ich SKILL.md"
- **Záver:** „Toto je tvoja vstupná brána do sveta skillov. V ďalšej lekcii sa naučíš, ako ich nainštalovať a používať. A v Lekcii 3 si vytvoríš vlastný."

### Kľúčové body
- Skill = znovupoužiteľný balíček inštrukcií (SKILL.md + voliteľne kód a assety)
- Skills menia generického agenta na špecialistu pre TVOJE úlohy
- Built-in skills: edit, websearch, attach_image, agent_message, compact, goal...
- Komunitné skills: marketing, vývoj, biznis, dizajn, dáta
- Kvalitný skill = jasný trigger + detailné inštrukcie + príklady + definovaný výstup

### Domáca úloha
1. Preskúmaj všetky built-in skills cez `/skills`. Pre každý si prečítaj SKILL.md a napíš, na čo slúži
2. Nájdi v `.agents/skills/` aspoň 5 skillov, ktoré by si vedel použiť vo svojej práci. Ohodnoť ich podľa kritérií z lekcie
3. Vyber si jeden skill z knižnice a vyskúšaj ho na reálnej úlohe. Napíš krátku recenziu: čo fungovalo, čo chýbalo, čo by si zlepšil
4. Nájdi online 3 komunitné skilly mimo Prime Agent ekosystému (GitHub, fóra) a porovnaj ich kvalitu s built-in skillmi

---

## Lekcia 2: Ako nainštalovať a používať skills
**Dĺžka videa:** 12 minút

### Detailný obsah / scenár

#### 0:00–1:30 | Úvod – skills v akcii
- **Povedať:** „V prvej lekcii si zistil, čo sú skills a kde ich nájsť. Teraz sa naučíš, ako ich nainštalovať a hlavne používať. Toto je praktická lekcia – všetko si ukážeme live."
- **Ukázať rýchlu ukážku:** Inštalácia skillu, jeho aktivácia, použitie – od začiatku do konca
- **Povedať:** „Inštalácia skillu = 1 príkaz. Použitie = stačí spomenúť kľúčové slovo. Poďme na to."

#### 1:30–3:30 | Spôsoby inštalácie skillov
- **Povedať:** „Prime Agent ponúka niekoľko spôsobov, ako skills nainštalovať. Každý má svoje využitie."

**Metóda 1: Inštalácia cez `/skills` (najjednoduchšia)**
  - Otvor Prime Agent TUI: `prime-agent`
  - Napíš `/skills` – zobrazí sa interaktívny zoznam
  - Vyber skill z knižnice → Enter → potvrď inštaláciu
  - Skill sa stiahne a nainštaluje do `~/.prime/agent/skills/`
  - Hotovo! Skill je pripravený na použitie
  - **Výhoda:** Najrýchlejšie, žiadne manuálne sťahovanie

**Metóda 2: Manuálna inštalácia z adresára**
  - Vytvor alebo stiahni skill adresár
  - Umiestni ho do `~/.prime/agent/skills/`
  - Štruktúra: `skills/moj-skill/SKILL.md`
  - Reštartuj Prime Agenta (alebo použi `/skills` na obnovenie)
  - Skill je automaticky detegovaný a pripravený
  - **Výhoda:** Full kontrola, offline inštalácia, vlastné skilly

**Metóda 3: Inštalácia z `.agents` adresára (zdieľané skilly)**
  - `.agents` adresár v tvojom projekte
  - Skilly v `.agents/skills/` sú automaticky dostupné pre všetkých, ktorí projekt používajú
  - Tímová spolupráca: jeden vytvorí, všetci používajú
  - **Výhoda:** Zdieľanie v tíme, version control (Git), konzistencia

**Metóda 4: Inštalácia z URL**
  - `prime-agent --install-skill https://example.com/skill.tar.gz`
  - Priama inštalácia z URL (ak skill provider poskytuje priamy link)
  - **Výhoda:** Distribúcia, inštalácia na diaľku

- **Povedať:** „Štyri spôsoby: `/skills` (najrýchlejšie), manuálne (plná kontrola), `.agents` (tímové zdieľanie), URL (vzdialená distribúcia). Vyber si ten, ktorý ti vyhovuje."

#### 3:30–5:30 | Inštalácia krok za krokom – live demo
- **Povedať:** „Poďme nainštalovať prvý skill. Použijeme `/skills`, pretože je to najjednoduchšie."
- **Live demo na obrazovke:**
  1. `prime-agent` – spustenie
  2. `/skills` – otvorenie knižnice
  3. Výber skillu: napr. „SEO Audit" (seo-audit)
  4. Enter – potvrdenie
  5. Agent stiahne a nainštaluje
  6. Hotovo – skill je pripravený
- **Čo sa stalo v pozadí:**
  - Skill sa stiahol do `~/.prime/agent/skills/seo-audit/`
  - Súbory: `SKILL.md`, prípadne `skill.py`, assety
  - Agent ho zaregistroval a teraz ho vie používať
- **Povedať:** „Jeden príkaz. 10 sekúnd. Skill je pripravený."

**Poďme nainštalovať ďalší – manuálne:**
  - Ukážeme manuálnu inštaláciu:
    ```bash
    mkdir -p ~/.prime/agent/skills/my-custom-skill
    # Vytvoríme SKILL.md
    cat > ~/.prime/agent/skills/my-custom-skill/SKILL.md << 'EOF'
    # My Custom Skill
    Trigger: custom analysis
    Description: Moja vlastná analýza
    ...
    EOF
    ```
  - Reštart Prime Agenta
  - `/skills` – vidíme náš nový skill
  - **Povedať:** „Manuálna inštalácia = plná kontrola. Vytvoríš si vlastný, dáš do priečinka, hotovo."

#### 5:30–7:30 | Ako skills používať
- **Povedať:** „Skill je nainštalovaný. Ako ho teraz použiť?"

**Tri spôsoby aktivácie skillu:**

**1. Automatická aktivácia (najbežnejšia):**
  - Napíšeš správu, ktorá obsahuje trigger phrase definovanú v SKILL.md
  - Príklad: Skill `seo-audit` má trigger „SEO audit", „SEO check", „SEO analysis"
  - Napíšeš: „Sprav SEO audit mojej stránky https://moja-stranka.sk"
  - Agent automaticky rozpozná trigger a načíta skill
  - **Výhoda:** Prirodzené, nemusíš myslieť na to, ktorý skill použiť

**2. Explicitné zavolanie:**
  - Použi názov skillu ako command: `@seo-audit`
  - Alebo: „Použi skill seo-audit na..."
  - Agent vie, že chceš presne tento skill – preskočí vyhľadávanie triggerov
  - **Výhoda:** Presná kontrola, žiadna ambiguity

**3. Reťazenie skillov:**
  - „Najprv použi skill `competitor-analysis` na nájdenie konkurentov. Potom použi `seo-audit` na audit ich stránok. Nakoniec použi `report-generator` na vytvorenie finálneho reportu."
  - Agent spustí skills v poradí, každý s vlastnými inštrukciami
  - Výstupy z prvého skillu sa stanú vstupmi pre druhý
  - **Výhoda:** Komplexné workflowy z jednoduchých skillov

- **Povedať:** „Automaticky, explicitne, alebo v reťazci. Skills sa prispôsobia tvojmu štýlu práce."

#### 7:30–9:00 | Praktické príklady použitia
- **Povedať:** „Poďme si ukázať reálne scenáre."

**Scenár 1: SEO audit webstránky**
  - Používateľ: „Sprav SEO audit https://moja-firma.sk"
  - Agent aktivuje `seo-audit` skill
  - Skill inštrukcie:
    1. Stiahni HTML stránky (curl)
    2. Skontroluj meta tags (title, description, OG tags)
    3. Analyzuj headings štruktúru (H1-H6)
    4. Skontroluj content quality (dĺžka, keywords, readability)
    5. Otestuj technical SEO (SSL, mobile, rýchlosť načítania)
    6. Vytvor report so skóre 0-100 a prioritizovanými odporúčaniami
  - Výsledok: `seo-audit-report.md` s kompletnou analýzou

**Scenár 2: Analýza konkurencie**
  - Používateľ: „Analyzuj konkurentov pre môj startup" (spustí sa `competitor-profiling`)
  - Skill inštrukcie:
    1. Identifikuj konkurentov (web search)
    2. Pre každého zisti: produkt, ceny, features, target audience
    3. Vytvor SWOT analýzu pre každého
    4. Porovnaj v tabuľke (features matrix)
    5. Napíš positioning odporúčanie
  - Výsledok: Profesionálna analýza konkurencie

**Scenár 3: Generovanie reportu**
  - Používateľ: „Vytvor report z prieskumu trhu"
  - Skill `report-generator`:
    1. Načíta všetky podklady (súbory, predošlé výstupy)
    2. Štruktúruje podľa šablóny: executive summary → detaily → závery
    3. Formátuje ako profesionálny dokument
    4. Exportuje do PDF/HTML/Markdown
  - Výsledok: Report pripravený na prezentáciu

- **Povedať:** „Každý skill rieši špecifickú časť problému. Spolu tvoria kompletný workflow."

#### 9:00–10:30 | Best practices pre používanie skillov
- **Povedať:** „Pár pravidiel pre efektívne používanie."

**✅ ROB:**
  - Nauč sa trigger phrases svojich skillov – šetrí to čas
  - Používaj explicitné volanie (`@skill-name`) keď chceš presne tento skill
  - Reťaz skills pre komplexné úlohy (jeden skill = jeden krok)
  - Čítaj SKILL.md pred prvým použitím – vieš, čo skill robí
  - Kombinuj skills s vlastnými inštrukciami: „Použi SEO audit skill, ale zameraj sa hlavne na technical SEO"

**❌ NEROB:**
  - Nepoužívaj skill, ktorému nerozumieš – vždy si prečítaj SKILL.md
  - Nenechávaj skill bez dohľadu pri dlhých operáciách – skills majú svoje limity
  - Nezabúdaj, že skills sú generické – vždy ich prispôsob svojmu kontextu
  - Nemiešaj príliš veľa skillov naraz – 2-3 na úlohu je optimum

- **Povedať:** „Skills = ušetrený čas a konzistentná kvalita. Používaj ich múdro."

#### 10:30–12:00 | Zhrnutie a troubleshooting
- **Povedať:** „Bežné problémy a ako ich vyriešiť:"

**Problém 1: Skill sa neaktivuje**
  - Riešenie: Skontroluj, že používaš presnú trigger phrase definovanú v SKILL.md
  - Skús explicitné zavolanie: `@skill-name`
  - Over, že skill je naozaj nainštalovaný: `/skills`

**Problém 2: Skill produkuje zlé výsledky**
  - Riešenie: Skill je generický, prispôsob ho svojmu kontextu: „Použi skill X, ale..." 
  - Ak je skill trvalo zlý, edituj jeho SKILL.md – uprav inštrukcie podľa svojich potrieb

**Problém 3: Konflikt medzi skillmi**
  - Riešenie: Použi explicitné volanie, aby agent presne vedel, ktorý skill chceš
  - Pre komplexné úlohy: jeden skill na jeden krok, nezlučuj ich

**Problém 4: Skill potrebuje API kľúč/nástroj, ktorý nemám**
  - Riešenie: Prečítaj SKILL.md pred inštaláciou – sekcia „Prerequisites/Dependencies"
  - Niektoré skilly vyžadujú externé API (napr. Serper pre web search, GWS pre Google Workspace)

- **Záver:** „Skills sú jednoduché, ale majú svoje pravidlá. Keď ich pochopíš, tvoja produktivita vyletí o 200%. Ideme na Lekciu 3 – vytvoríš si vlastný skill!"

### Kľúčové body
- 4 spôsoby inštalácie: `/skills`, manuálna, `.agents` (tímová), URL
- 3 spôsoby aktivácie: automatická (trigger phrase), explicitná (`@skill`), reťazenie
- Vždy čítaj SKILL.md pred použitím – poznaj skill, ktorý používaš
- Prispôsob skills svojmu kontextu – nie sú to dogmy
- Reťaz skills pre komplexné workflowy: jeden skill = jeden krok

### Domáca úloha
1. Nainštaluj 3 skilly z knižnice (rôzne kategórie: marketing, vývoj, dáta) a vyskúšaj ich na reálnych úlohách
2. Vytvor `.agents/skills/` priečinok v tvojom projekte a nainštaluj tam jeden zdieľaný skill – otestuj, že funguje
3. Vyskúšaj reťazenie: spoj 2-3 skilly do workflowu. Napríklad: `competitor-profiling` → `seo-audit` → manuálna syntéza. Opíš výsledok
4. Nájdi skill, ktorý čiastočne nespĺňa tvoje potreby, a uprav jeho SKILL.md. Porovnaj výstup pred a po úprave

---

## Lekcia 3: Vytvorenie vlastného markdown skillu
**Dĺžka videa:** 15 minút

### Detailný obsah / scenár

#### 0:00–1:30 | Úvod – staň sa tvorcom
- **Povedať:** „Toto je lekcia, ktorá ťa posunie od konzumenta k tvorcovi. Vytvoríš si vlastný skill – od nuly. Naučíš sa štruktúru, best practices a hlavne spôsob myslenia, ktorý ti umožní vytvárať skills pre čokoľvek."
- **Ukázať hotový skill:** „Toto je skill, ktorý si vytvoríš. Volá sa `tyzdenny-report`. Automaticky vygeneruje týždenný biznis report z tvojich dát."
- **Povedať:** „Na konci tejto lekcie budeš mať funkčný, použiteľný skill. A hlavne – budeš vedieť vytvoriť ďalší a ďalší."

#### 1:30–4:00 | Anatómia SKILL.md – čo musí obsahovať
- **Povedať:** „Každý skill začína súborom SKILL.md. Toto je jeho DNA. Poďme si rozobrať, čo presne musí obsahovať."

**Štruktúra SKILL.md:**
  ```
  # Názov skillu
  Jasný, výstižný názov

  ## Trigger phrases
  Zoznam fráz, ktoré spúšťajú tento skill:
  - "týždenný report"
  - "weekly report" 
  - "vygeneruj report"
  - "týždenné zhrnutie"

  ## Popis
  Kedy sa má skill použiť a čo rieši.

  ## Inštrukcie / Postup
  Detailný krok-za-krokom postup, čo má agent robiť.
  Toto je NAJDÔLEŽITEJŠIA časť.

  ## Formát výstupu
  Ako má vyzerať výsledok. Štruktúra, formát, príklady.

  ## Obmedzenia
  Čo nerobiť, na čo si dať pozor, edge cases.

  ## Príklady
  2-3 konkrétne príklady vstupu a očakávaného výstupu.
  ```

- **Povedať:** „Toto je minimálna štruktúra. Čím detailnejšie inštrukcie, tým lepší výstup. Nikdy nepodceňuj príklady – sú to pre agenta zlatý štandard."

#### 4:00–7:00 | Live tvorba – Skill „Týždenný report"
- **Povedať:** „Poďme vytvoriť reálny skill. Bude sa volať `tyzdenny-report`."
- **Live coding na obrazovke:**

**Krok 1: Vytvorenie adresárovej štruktúry**
  ```bash
  mkdir -p ~/.prime/agent/skills/tyzdenny-report
  touch ~/.prime/agent/skills/tyzdenny-report/SKILL.md
  ```

**Krok 2: Písanie SKILL.md (ukazujeme naživo, vysvetľujeme každú časť)**

  ```markdown
  # Týždenný biznis report

  ## Trigger phrases
  - "týždenný report"
  - "týždenné zhrnutie"
  - "weekly report"
  - "vygeneruj report za týždeň"
  - "týždenný biznis report"
  - "sprav report"

  ## Popis
  Skill na automatické generovanie týždenného biznis reportu.
  Použi, keď používateľ chce sumarizovať aktivity, predaje alebo 
  metriky za uplynulý týždeň. Vstupom sú dáta (CSV, JSON) alebo 
  textový popis aktivít. Výstupom je štruktúrovaný report 
  pripravený na zdieľanie.

  ## Inštrukcie

  1. **Zisti zdroj dát:**
     - Ak používateľ poskytol súbor (CSV, JSON), načítaj ho
     - Ak nie, opýtaj sa, odkiaľ získať dáta (súbor, API, manuálny vstup)
     - Ak je veľa dát, spracúvaj po častiach

  2. **Analyzuj dáta:**
     - Identifikuj kľúčové metriky (tržby, počet zákazníkov, konverzie...)
     - Porovnaj s predošlým týždňom (ak sú dostupné historické dáta)
     - Vypočítaj percentuálne zmeny
     - Nájdi top 3 víťazstvá a top 3 problémy

  3. **Vytvor report v tejto presnej štruktúre:**
     ```
     # Týždenný report [dátumový rozsah]

     ## 📊 Kľúčové čísla
     - Metrika 1: hodnota (+X% oproti minulému týždňu)
     - Metrika 2: hodnota (+X% oproti minulému týždňu)
     - ...

     ## 🏆 Top 3 víťazstvá
     1. Konkrétne víťazstvo s vysvetlením
     2. ...
     3. ...

     ## ⚠️ Top 3 výzvy
     1. Konkrétny problém s kontextom
     2. ...
     3. ...

     ## 📈 Trendy
     - Popis kľúčového trendu 1
     - Popis kľúčového trendu 2

     ## 🎯 Akčné kroky na ďalší týždeň
     - [ ] Konkrétna akcia 1
     - [ ] Konkrétna akcia 2
     - [ ] Konkrétna akcia 3

     ## 💡 Postreh týždňa
     Jeden hlbší insight alebo learning z tohto týždňa.
     ```

  4. **Tón a štýl:**
     - Profesionálny, ale priateľský a priamy
     - Vecný, žiadne zbytočné prívlastky
     - Dáta prezentuj jasne, ideálne v tabuľkách
     - Používaj emoji len v nadpisoch (ako v štruktúre)
     - Všetko v slovenčine (ak používateľ nešpecifikuje inak)

  5. **Uloženie:**
     - Ulož report ako `tyzdenny-report-YYYY-MM-DD.md`
     - Pridaj dátum vygenerovania do hlavičky reportu

  ## Formát výstupu
  Markdown súbor s vyššie uvedenou štruktúrou. 
  Dĺžka: primeraná dátam, zvyčajne 1-2 strany.

  ## Obmedzenia
  - Neuhádaj metriky – ak chýbajú dáta, opýtaj sa
  - Pri veľkých datasetoch (>10 MB) spracúvaj inkrementálne
  - Nepoužívaj externé API bez overenia dostupnosti
  - Ak nie sú dostupné historické dáta, vynechaj porovnanie (%)
  - Nesnaž sa vkladať obrázky priamo do Markdownu 
    (pokiaľ to nie je URL)

  ## Príklady

  ### Príklad 1: Report pre e-shop
  Používateľ: "Sprav týždenný report z predajov. Dáta v sales.csv"
  Očakávaný výstup: Report s metrikami: celkové tržby, počet objednávok, 
  priemerná hodnota objednávky, top 3 produkty. Porovnanie s minulým 
  týždňom. Top víťazstvá a výzvy.

  ### Príklad 2: Report pre marketingový tím
  Používateľ: "Týždenný report – tento týždeň: 1500 návštev webu, 
  120 nových leadov, 8 demo hovorov. Minulý týždeň: 1200 návštev, 
  95 leadov, 5 demo hovorov."
  Očakávaný výstup: Report s vypočítanými percentuálnymi zmenami, 
  identifikovanými trendmi a akčnými krokmi.

  ### Príklad 3: Report z log súboru
  Používateľ: "Vygeneruj týždenný report z errors.log"
  Očakávaný výstup: Report s počtom chýb podľa typu, najčastejšie 
  chyby, porovnanie s minulým týždňom, odporúčanie na opravy.
  ```

- **Povedať:** „Vidíš tú štruktúru? Trigger phrases – jasné. Inštrukcie – detailné. Formát – presne definovaný. Príklady – konkrétne. Toto je recept na dokonalý skill."

#### 7:00–10:00 | Testovanie skillu – iteratívne vylepšovanie
- **Povedať:** „Skill je napísaný. Teraz ho otestujeme a vylepšíme."

**Krok 1: Prvé spustenie**
  - Reštartovať Prime Agenta: `prime-agent`
  - Overiť, že skill je viditeľný: `/skills` → nájsť „Týždenný biznis report"
  - Spustiť: „Vytvor týždenný report. Tento týždeň: tržby 25000€, 85 zákazníkov, 12 vrátení. Minulý týždeň: tržby 21000€, 72 zákazníkov, 8 vrátení."
  - Pozorovať výstup

**Krok 2: Analýza výstupu**
  - Čo fungovalo: Štruktúra reportu, výpočty
  - Čo treba zlepšiť: Chýba jasnejšie oddelenie víťazstiev od obyčajných metrík, možno pridať grafický prvok (ASCII chart?)

**Krok 3: Iterácia – úprava SKILL.md**
  - „Vidíš, že prvá verzia nie je dokonalá. To je normálne. Upravíme inštrukcie:"
  - Pridáme do inštrukcií:
    ```
    - Pre každé víťazstvo napíš KONKRÉTNY dôvod, 
      prečo k nemu došlo (nielen "vyššie tržby", 
      ale "vyššie tržby vďaka email kampani z utorka")
    - Pridaj sekciu "🔥 Rýchle víťazstvo" – 
      jedna vec, ktorú môže tím spraviť hneď zajtra
    ```
  - Uložíme, reštartujeme, otestujeme znova

**Krok 4: Finálna verzia**
  - Po 2-3 iteráciách je skill vyladený
  - Povedať: „Všimni si pattern: **vytvor → otestuj → analyzuj → vylepši → otestuj**. Rovnako ako pri programovaní. Skills nie sú nikdy hotové na prvýkrát."

- **Povedať:** „Iterácia je kľúč. Prvý skill nikdy nie je dokonalý. Testuj, vylepšuj, testuj."

#### 10:00–12:00 | Tipy pre profesionálne skills
- **Povedať:** „Pár tipov, ktoré odlišujú amatérske skills od profesionálnych:"

**1. Buď hyper-špecifický v inštrukciách**
  - ❌ Zlé: „Napíš dobrý report"
  - ✅ Dobré: „Report musí mať: presne 5 sekcií, každá s 2-3 odrážkami, prvá veta každej sekcie je bold sumár"

**2. Používaj kontrolné zoznamy (checklists)**
  - V inštrukciách daj agentovi checklist:
    ```
    Pred odovzdaním výstupu skontroluj:
    - [ ] Všetky percentá sú vypočítané správne
    - [ ] Dátumy sú vo formáte DD.MM.YYYY
    - [ ] Report má všetky povinné sekcie
    - [ ] Jazyk je slovenčina (bez anglicizmov)
    ```

**3. Definuj „Done" podmienky**
  - Agent musí vedieť, kedy je úloha dokončená
  - „Skill je dokončený, keď: report je uložený ako .md súbor, všetky sekcie sú vyplnené, a používateľovi je oznámená cesta k súboru"

**4. Pridaj fallback inštrukcie**
  - Čo robiť, keď niečo chýba alebo zlyhá
  - „Ak chýbajú historické dáta: napíš 'Porovnanie s minulým obdobím nie je k dispozícii' namiesto vynechania sekcie"

**5. Verzionuj svoje skills**
  - Pridaj do SKILL.md: `version: 1.2.0`
  - Udržuj changelog: `## Zmeny vo v1.2: pridaná sekcia Trendy, vylepšené formátovanie`
  - Umožní ti to vrátiť sa k staršej verzii, ak nová nefunguje

- **Povedať:** „Týchto 5 tipov – špecifickosť, checklisty, done podmienky, fallbacky, verzionovanie – ťa odlíši od 90% tvorcov skillov."

#### 12:00–14:00 | Pokročilé techniky – parametrizácia a podmienené správanie
- **Povedať:** „Keď ovládaš základy, poďme na pokročilé techniky."

**1. Parametrizovateľné skills:**
  - Skill môže akceptovať parametre od používateľa
  - Príklad: „Sprav týždenný report, ale zameraj sa len na marketingové metriky. Formát: Google Slides."
  - V SKILL.md:
    ```
    ## Parametre
    - `zameranie`: ktoré metriky zahrnúť (všetky | marketing | predaj | technické)
    - `format`: výstupný formát (md | pdf | google-slides)
    - `jazyk`: slovenčina | angličtina | čeština
    ```
  - Agent aplikuje parametre na základné inštrukcie

**2. Podmienené správanie:**
  - Skill môže mať vetvy podľa typu vstupu
  - Príklad:
    ```
    Ak používateľ poskytne CSV súbor:
      → Parsuj CSV, extrahuj stĺpce

    Ak používateľ poskytne textový popis:
      → Extrahuj čísla z textu, štruktúruj ich

    Ak používateľ neposkytne nič:
      → Opýtaj sa, odkiaľ získať dáta
    ```

**3. Multi-step workflow v jednom skille:**
  - Jeden skill môže orchestráciu viacerých podúloh
  - Príklad `market-research` skill:
    1. Identifikácia zdrojov (web search)
    2. Zber dát (scraping, API volania)
    3. Analýza (Python – štatistika, NLP)
    4. Syntéza (LLM – sumarizácia, odporúčania)
    5. Výstup (formátovanie, uloženie)

- **Povedať:** „Parametrizácia, podmienené správanie, multi-step workflow. Toto sú techniky, ktoré ti umožnia vytvárať skills na profesionálnej úrovni."

#### 14:00–15:00 | Zhrnutie a zadanie domácej úlohy
- **Povedať:** „Poďme si zhrnúť, čo si sa naučil:"
  - ✅ Štruktúra SKILL.md: názov, triggery, popis, inštrukcie, formát, obmedzenia, príklady
  - ✅ Ako vytvoriť skill od nuly (tyzdenny-report)
  - ✅ Iteratívne vylepšovanie: vytvor → otestuj → analyzuj → vylepši
  - ✅ Profesionálne techniky: špecifickosť, checklisty, done podmienky, fallbacky
  - ✅ Pokročilé: parametrizácia, podmienené správanie, multi-step workflow

- **Záver:** „Toto je možno najdôležitejšia lekcia celého kurzu. Vytváranie skillov = tvoja super-schopnosť. Každý manuálny proces, ktorý robíš opakovane, môže byť skill. V ďalšej lekcii sa naučíš, kedy pridať Python kód."

### Kľúčové body
- SKILL.md štruktúra: názov → triggery → popis → inštrukcie → formát → obmedzenia → príklady
- Inštrukcie sú NAJDÔLEŽITEJŠIA časť – čím detailnejšie, tým lepší výstup
- Iterácia je kľúč: vytvor → otestuj → analyzuj → vylepši → otestuj
- Profi tipy: špecifickosť, checklisty, done podmienky, fallbacky, verzionovanie
- Pokročilé: parametrizácia, podmienené správanie, multi-step workflow

### Domáca úloha
1. **Povinné:** Vytvor vlastný markdown skill podľa štruktúry z lekcie. Téma: čokoľvek, čo robíš aspoň 2× týždenne (napr. analýza emajlov, generovanie faktúr, príprava meeting notes)
2. Otestuj svoj skill na 3 rôznych vstupoch a zdokumentuj, čo fungovalo a čo treba zlepšiť. Uprav SKILL.md aspoň 2× na základe testovania
3. Nájdi 2 existujúce skilly z knižnice a navrhni vylepšenia ich SKILL.md. Čo by si pridal, upravil alebo odstránil?
4. Vytvor „skill template" – prázdnu šablónu SKILL.md s komentármi, ktorú budeš používať na rýchle vytváranie ďalších skillov. Zdieľaj ju v diskusii

---

## Lekcia 4: Python skills – kedy a ako
**Dĺžka videa:** 12 minút

### Detailný obsah / scenár

#### 0:00–1:30 | Úvod – kedy markdown nestačí
- **Povedať:** „Markdown skills sú skvelé na 80% prípadov. Ale čo keď potrebuješ volať API, spracovať komplexné dáta, alebo integrovať externú knižnicu? Vtedy prichádza Python skill."
- **Ukázať rýchlu ukážku:** Python skill, ktorý volá REST API, spracuje JSON odpoveď a vytvorí interaktívny report
- **Povedať:** „Python skill = markdown inštrukcie + spustiteľný Python kód. Agent ho môže volať ako funkciu."

#### 1:30–4:00 | Architektúra Python skillu
- **Povedať:** „Python skill sa skladá z dvoch častí: SKILL.md (inštrukcie) a Python súbor (kód)."
- **Adresárová štruktúra:**
  ```
  skills/moj-python-skill/
  ├── SKILL.md          # Inštrukcie pre agenta (POVINNÉ)
  └── skill.py          # Python kód (VOLITEĽNÉ, ale pre Python skill nutné)
  ```

- **Ako to funguje:**
  1. Používateľ napíše trigger phrase
  2. Agent načíta SKILL.md – získa inštrukcie
  3. Agent zistí, že skill má Python kód
  4. Agent importuje modul: `import moj_python_skill` (názov adresára)
  5. Agent volá funkcie definované v `skill.py`
  6. Výsledok sa vráti do kontextu agenta

- **SKILL.md pre Python skill – čo treba navyše:**
  - Typ: `python` (namiesto `markdown`)
  - Python import: názov modulu, ktorý sa má importovať
  - API dokumentácia: aké funkcie sú k dispozícii, ich parametre, návratové hodnoty
  - Príklady volania Python funkcií

- **Príklad SKILL.md hlavičky pre Python skill:**
  ```yaml
  ---
  name: weather-report
  type: python
  python_import: weather_report
  description: Získa počasie pre dané mesto a vytvorí report
  ---
  ```

- **Povedať:** „Python skill = SKILL.md hovorí agentovi KEDY a AKO volať kód. skill.py obsahuje KONKRÉTNU implementáciu."

#### 4:00–7:00 | Live tvorba – Python skill „Počasie report"
- **Povedať:** „Poďme vytvoriť reálny Python skill. Bude získavať počasie z API a vytvárať report."

**Krok 1: Vytvorenie štruktúry**
  ```bash
  mkdir -p ~/.prime/agent/skills/weather-report
  touch ~/.prime/agent/skills/weather-report/SKILL.md
  touch ~/.prime/agent/skills/weather-report/skill.py
  ```

**Krok 2: SKILL.md (ukážeme na obrazovke)**
  ```markdown
  # Weather Report Skill

  ## Typ
  Python skill – poskytuje funkcie na získanie počasia.

  ## Python import
  ```python
  import weather_report
  ```

  ## Trigger phrases
  - "počasie"
  - "weather report"
  - "aké je počasie"
  - "predpoveď počasie"
  - "teplota v"

  ## Popis
  Python skill na získavanie aktuálneho počasia a predpovede 
  pomocou Open-Meteo API (zadarmo, bez API kľúča).

  ## API – dostupné funkcie

  ### `get_current_weather(city: str) -> dict`
  Získa aktuálne počasie pre dané mesto.
  Vracia: `{"city": str, "temperature": float, "humidity": int, 
  "wind_speed": float, "description": str}`

  ### `get_forecast(city: str, days: int = 3) -> list[dict]`
  Získa predpoveď na daný počet dní.
  Vracia: list dní, každý s `{"date": str, "temp_max": float, 
  "temp_min": float, "precipitation": float, "description": str}`

  ### `create_weather_report(city: str) -> str`
  Vytvorí kompletný Markdown report počasia (aktuálne + predpoveď).

  ## Inštrukcie pre agenta

  Keď používateľ požiada o počasie:
  1. Zavolaj `get_current_weather(city)` pre aktuálne dáta
  2. Zavolaj `get_forecast(city, days=3)` pre predpoveď
  3. Zavolaj `create_weather_report(city)` pre kompletný report
  4. Vráť výsledok používateľovi v peknom formáte

  ## Príklady

  Používateľ: "Aké je počasie v Bratislave?"
  Agent zavolá:
  ```python
  current = weather_report.get_current_weather("Bratislava")
  forecast = weather_report.get_forecast("Bratislava", days=3)
  ```

  ## Obmedzenia
  - Používa Open-Meteo API (zadarmo, bez kľúča)
  - Geokódovanie miest je približné – pre presnosť použi súradnice
  - API limit: 10 000 volaní/deň (dostatok pre bežné použitie)
  ```

**Krok 3: skill.py (ukážeme na obrazovke)**
  ```python
  """
  Weather Report Skill – získava počasie cez Open-Meteo API.
  """
  import requests
  from datetime import datetime, timedelta

  # Cache pre geokódovanie (mesto → súradnice)
  _geo_cache = {}

  def _geocode(city: str) -> dict:
      """Prevedie názov mesta na súradnice (latitude, longitude)."""
      if city in _geo_cache:
          return _geo_cache[city]

      # Open-Meteo geocoding API
      url = f"https://geocoding-api.open-meteo.com/v1/search"
      params = {"name": city, "count": 1, "language": "sk"}
      resp = requests.get(url, params=params, timeout=10)
      data = resp.json()

      if "results" not in data or not data["results"]:
          raise ValueError(f"Mesto '{city}' nebolo nájdené.")

      result = data["results"][0]
      geo = {
          "name": result["name"],
          "country": result.get("country", "??"),
          "lat": result["latitude"],
          "lon": result["longitude"],
      }
      _geo_cache[city] = geo
      return geo

  def _get_weather_code_description(code: int) -> str:
      """Prevedie WMO weather code na slovenský popis."""
      codes = {
          0: "Jasno ☀️",
          1: "Prevažne jasno 🌤️",
          2: "Polooblačno ⛅",
          3: "Zamračené ☁️",
          45: "Hmla 🌫️",
          51: "Slabé mrholenie 🌧️",
          61: "Slabý dážď 🌧️",
          63: "Mierny dážď 🌧️",
          71: "Slabé sneženie ❄️",
          80: "Prehánky 🌦️",
          95: "Búrka ⛈️",
      }
      return codes.get(code, f"Neznáme (kód {code})")

  def get_current_weather(city: str) -> dict:
      """Získa aktuálne počasie pre dané mesto."""
      geo = _geocode(city)
      url = "https://api.open-meteo.com/v1/forecast"
      params = {
          "latitude": geo["lat"],
          "longitude": geo["lon"],
          "current": "temperature_2m,relative_humidity_2m,"
                     "wind_speed_10m,weather_code",
          "timezone": "Europe/Bratislava",
      }
      resp = requests.get(url, params=params, timeout=10)
      data = resp.json()["current"]

      return {
          "city": f"{geo['name']}, {geo['country']}",
          "temperature": data["temperature_2m"],
          "humidity": data["relative_humidity_2m"],
          "wind_speed": data["wind_speed_10m"],
          "description": _get_weather_code_description(
              data["weather_code"]
          ),
          "time": data["time"],
      }

  def get_forecast(city: str, days: int = 3) -> list[dict]:
      """Získa predpoveď počasia na daný počet dní."""
      geo = _geocode(city)
      url = "https://api.open-meteo.com/v1/forecast"
      params = {
          "latitude": geo["lat"],
          "longitude": geo["lon"],
          "daily": "temperature_2m_max,temperature_2m_min,"
                   "precipitation_sum,weather_code",
          "forecast_days": days,
          "timezone": "Europe/Bratislava",
      }
      resp = requests.get(url, params=params, timeout=10)
      daily = resp.json()["daily"]

      forecast = []
      for i in range(days):
          forecast.append({
              "date": daily["time"][i],
              "temp_max": daily["temperature_2m_max"][i],
              "temp_min": daily["temperature_2m_min"][i],
              "precipitation": daily["precipitation_sum"][i],
              "description": _get_weather_code_description(
                  daily["weather_code"][i]
              ),
          })
      return forecast

  def create_weather_report(city: str) -> str:
      """Vytvorí kompletný Markdown report počasia."""
      current = get_current_weather(city)
      forecast = get_forecast(city, days=3)

      # Slovenská hlavička
      report = f"""# 🌤️ Počasie: {current['city']}

  ## 📍 Aktuálne počasie ({current['time']})
  - **Teplota:** {current['temperature']}°C
  - **Vlhkosť:** {current['humidity']}%
  - **Vietor:** {current['wind_speed']} km/h
  - **Stav:** {current['description']}

  ## 📅 Predpoveď na 3 dni

  | Dátum | Max | Min | Zrážky | Stav |
  |-------|-----|-----|--------|------|
  """
      for day in forecast:
          report += (
              f"| {day['date']} "
              f"| {day['temp_max']}°C "
              f"| {day['temp_min']}°C "
              f"| {day['precipitation']} mm "
              f"| {day['description']} |\n"
          )

      report += "\n---\n*Dáta: Open-Meteo API (zadarmo, bez API kľúča)*"
      return report
  ```

- **Povedať:** „Vidíš ten rozdiel oproti markdown skillu? Máme reálny Python kód, ktorý volá API, spracováva JSON, cachuje výsledky. Agent to celé vie použiť."

#### 7:00–9:00 | Ako agent používa Python skill
- **Povedať:** „Poďme si ukázať, ako agent reálne používa tento skill."
- **Live demo:**
  1. Reštartovať Prime Agenta
  2. `/skills` – vidíme `weather-report` (Python)
  3. Zadať: „Aké je počasie v Košiciach?"
  4. Agent:
     - Rozpozná trigger „počasie"
     - Načíta SKILL.md
     - Zistí, že má Python kód
     - Importuje modul: `import weather_report`
     - Zavolá: `weather_report.get_current_weather("Košice")`
     - Zavolá: `weather_report.get_forecast("Košice", days=3)`
     - Zavolá: `weather_report.create_weather_report("Košice")`
     - Vypíše Markdown report
  5. Výsledok: Profesionálny report počasia

- **Povedať:** „Agent všetko spravil sám. Importoval modul, zavolal správne funkcie, použil výstup. Ty si len povedal 'aké je počasie'."

#### 9:00–10:30 | Kedy použiť markdown skill vs Python skill
- **Povedať:** „Toto je dôležité rozhodnutie. Nie vždy potrebuješ Python."

**Použi MARKDOWN skill keď:**
  - Úloha je o POSTUPE a ŠTRUKTÚRE (nie o výpočtoch)
  - Nepotrebuješ volať externé API alebo knižnice
  - Agent môže všetko spraviť pomocou `bash` a `python` v IPython kerneli
  - Chceš skill rýchlo vytvoriť a zdieľať (žiadny kód)
  - Príklady: code review, blog post, email template, meeting notes

**Použi PYTHON skill keď:**
  - Potrebuješ integrovať externé API (REST, GraphQL, SDK)
  - Máš komplexné výpočty, ktoré by boli v Markdown-e neprehľadné
  - Chceš zapuzdriť logiku (napr. cachovanie, retry, error handling)
  - Potrebuješ spracovať špecifický formát (napr. binárne dáta, XML, protobuf)
  - Vytváraš skill, ktorý budú používať iní – Python umožňuje type hints, testy
  - Príklady: API integrácie, dátové pipeline-y, ML inferencia, komplexná vizualizácia

**Hybridný prístup:**
  - SKILL.md + voliteľné Python utility funkcie
  - Markdown definuje workflow, Python poskytuje helper funkcie
  - Agent používa Python funkcie v rámci markdown-om definovaného postupu

- **Povedať:** „80% skillov bude markdown. Python si nechaj na prípady, kde markdown jednoducho nestačí."

#### 10:30–11:30 | Debugging Python skillov
- **Povedať:** „Python skills môžu padať. Tu je ako ich ladiť."

**1. Testuj funkcie manuálne:**
  - V Prime Agent IPython kerneli:
    ```python
    import weather_report
    result = weather_report.get_current_weather("Bratislava")
    print(result)  # skontroluj výstup
    ```

**2. Čítaj error messages:**
  - Agent ti ich ukáže priamo v chate
  - `ImportError` – skontroluj názov súboru/adresára
  - `AttributeError` – funkcia neexistuje, preklep?
  - `requests.exceptions.Timeout` – API neodpovedá, pridaj timeout/retry

**3. Pridávaj logovanie:**
  - V skill.py: `print(f"[DEBUG] Geocoding {city}...")` 
  - Agent uvidí výstup v konzole

**4. Verzionuj a rollback:**
  - Udržuj staršiu verziu: `skill.py.bak`
  - Ak nová verzia nefunguje, vráť sa

- **Povedať:** „Debugging Python skillov je rovnaký ako debugging akéhokoľvek Python kódu. Len beží v kontexte agenta."

#### 11:30–12:00 | Zhrnutie a odporúčania
- **Povedať:** „Poďme si zhrnúť:"
  - ✅ Python skill = SKILL.md (inštrukcie) + skill.py (kód)
  - ✅ Agent importuje modul a volá funkcie priamo
  - ✅ Použi Python skill na API integrácie, komplexné výpočty, enkapsuláciu
  - ✅ Debugging = testuj manuálne, čítaj errory, loguj, verzionuj

- **Záver:** „Python skills sú výkonné, ale komplexnejšie. Zační s markdown skillom. Keď narazíš na limit, pridaj Python. V poslednej lekcii tohto modulu sa pozrieme na najdôležitejšie skills z knižnice."

### Kľúčové body
- Python skill = SKILL.md + skill.py (samostatný Python modul)
- Agent importuje modul a volá funkcie podľa inštrukcií v SKILL.md
- Použi Python skill na: API integrácie, komplexné výpočty, enkapsuláciu logiky
- 80% skillov vystačí s markdown – Python si nechaj na špeciálne prípady
- Debugging: testuj funkcie manuálne v IPython kerneli, čítaj errory, loguj

### Domáca úloha
1. Vytvor Python skill, ktorý integruje akékoľvek verejné API (napr. GitHub, OpenWeather, pokéAPI). Musí obsahovať SKILL.md aj skill.py
2. Porovnaj svoj Python skill s markdown verziou rovnakej úlohy. Ktorá bola jednoduchšia na vytvorenie? Ktorá dáva lepšie výsledky? Napíš krátku analýzu (100 slov)
3. Pridaj error handling a retry logiku do svojho Python skillu. Otestuj ho na zlyhanie API (napr. zlý API endpoint) – skontroluj, že skill elegantne zlyhá a nie crashne
4. Nájdi existujúci Python skill v ekosystéme Prime Agenta a naštuduj si jeho kód. Čo sa ti páči, čo by si zlepšil?

---

## Lekcia 5: Skill library – najdôležitejšie skills pre biznis
**Dĺžka videa:** 6 minút

### Detailný obsah / scenár

#### 0:00–1:00 | Úvod – skills, ktoré ťa posunú
- **Povedať:** „Toto je rýchla prehliadka najdôležitejších skillov z knižnice Prime Agenta. Nie je to hĺbková lekcia – je to mapa. Mapa, ktorá ti ukáže, čo všetko môžeš robiť hneď teraz, bez toho aby si čokoľvek programoval."
- **Ukázať `/skills` v TUI – scrollovať zoznamom**
- **Povedať:** „Toto nie sú všetky. Vybral som top skills, ktoré reálne používam každý týždeň. Rozdelil som ich do kategórií."

#### 1:00–2:30 | Marketingové skills – tvoja marketingová agentúra
- **Povedať:** „Toto sú skills, ktoré nahradia marketingovú agentúru za 5000€ mesačne."

**1. `copywriting` – Píše texty, ktoré konvertujú**
  - Na čo: homepage, landing pages, pricing pages, CTA
  - Trigger: „napíš copy", „vylepši text", „potrebujem headline"
  - **Best use:** „Napíš hero section pre SaaS produkt, ktorý šetrí firmám 20 hodín mesačne na manuálnych úlohách. Tón: profesionálny, priamy, benefit-focused."

**2. `seo-audit` – SEO doktor**
  - Na čo: audit stránky, technické SEO, on-page optimalizácia
  - Trigger: „SEO audit", „SEO kontrola", „prečo ma nevidno v Google"
  - **Best use:** „Sprav SEO audit https://moja-stranka.sk a daj mi top 5 vecí, ktoré mám opraviť."

**3. `content-strategy` – Čo písať**
  - Na čo: plánovanie obsahu, topic clustre, obsahový kalendár
  - Trigger: „content strategy", „čo mám písať", „blog témy"
  - **Best use:** „Vytvor 3-mesačnú obsahovú stratégiu pre B2B SaaS v oblasti HR tech."

**4. `competitor-profiling` – Špiónska agentúra**
  - Na čo: analýza konkurencie, profily, SWOT
  - Trigger: „analyzuj konkurenta", „profil konkurencie"
  - **Best use:** „Vytvor detailné profily top 5 konkurentov v segmente AI recruitment nástrojov."

**5. `emails` – Automatické sekvencie**
  - Na čo: welcome, nurture, re-engagement, onboarding emaily
  - Trigger: „emailová sekvencia", „drip kampaň", „welcome email"
  - **Best use:** „Vytvor 5-emailovú welcome sekvenciu pre nových používateľov nášho SaaS nástroja."

- **Povedať:** „Týchto 5 skillov = tvoja marketingová agentúra. Každý rieši jednu špecifickú časť marketingu."

#### 2:30–3:30 | Biznis a stratégia skills
- **Povedať:** „Teraz skills pre biznisové rozhodovanie a stratégiu."

**6. `pricing` – Koľko si pýtať**
  - Na čo: cenová stratégia, tier štruktúra, value metric
  - Trigger: „pricing", „koľko účtovať", „cenová stratégia"
  - **Best use:** „Navrhni 3-tier cenovú štruktúru pre B2B SaaS s value metric 'počet projektov'."

**7. `offers` – Neodolateľná ponuka**
  - Na čo: konštrukcia ponuky, bonusy, garancie, value stacking
  - Trigger: „offer", „ponuka", „grand slam offer"
  - **Best use:** „Navrhni neodolateľnú ponuku pre náš konzultačný balík za 5000€."

**8. `ab-testing` – Experimenty**
  - Na čo: návrh a vyhodnotenie A/B testov
  - Trigger: „A/B test", „experiment", „otestovať", „split test"
  - **Best use:** „Navrhni A/B test pre homepage – chceme otestovať benefit-focused headline vs feature-focused headline."

**9. `launch` – Produktový launch**
  - Na čo: launch stratégia, checklist, Product Hunt, koordinácia
  - Trigger: „launch", „spustenie", „product launch", „Product Hunt"
  - **Best use:** „Vytvor 30-dňový launch plán pre náš nový AI produkt."

**10. `marketing-plan` – Komplexný marketingový plán**
  - Na čo: 90-dňový plán, AARRR framework, budget alokácia
  - Trigger: „marketingový plán", „growth plán"
  - **Best use:** „Vytvor 90-dňový marketingový plán pre B2B SaaS startup s budgetom 5000€."

- **Povedať:** „Pricing, offers, A/B testing, launch, marketing plan. Toto sú strategické skills – tie, ktoré ťa posunú od vykonávateľa k stratégovi."

#### 3:30–4:30 | Predajné a growth skills
- **Povedať:** „Skills, ktoré priamo generujú revenue."

**11. `cold-email` – Studený outreach**
  - Na čo: cold email kampane, follow-up sekvencie
  - Trigger: „cold email", „outreach", „osloviť", „prospecting"
  - **Best use:** „Napíš 3-emailovú cold sekvenciu pre B2B SDR – target sú CIO v stredných firmách."

**12. `prospecting` – Hľadanie leadov**
  - Na čo: zoznamy prospectov, kvalifikácia, ICP-fit
  - Trigger: „nájdi leadov", „prospecting", „zoznam firiem"
  - **Best use:** „Nájdi 50 B2B SaaS firiem v Európe s 50-200 zamestnancami, ktoré používajú AWS."

**13. `sales-enablement` – Výzbroj pre sales**
  - Na čo: pitch deck, one-pager, objection handling, demo script
  - Trigger: „sales deck", „pitch deck", „ako odpovedať na námietku"
  - **Best use:** „Vytvor one-pager pre náš produkt, ktorý sales team môže poslať po discovery call."

**14. `referrals` – Virálny rast**
  - Na čo: referral program, affiliate, ambasádori
  - Trigger: „referral", „affiliate", „odporúčací program"
  - **Best use:** „Navrhni referral program pre B2B SaaS – odmena 20% z prvého roka."

**15. `churn-prevention` – Záchrana zákazníkov**
  - Na čo: cancel flow, save offers, win-back, dunning
  - Trigger: „churn", „odchádzajú zákazníci", „cancel flow"
  - **Best use:** „Navrhni cancel flow, ktorý zníži churn aspoň o 15%."

- **Povedať:** „Cold email, prospecting, sales enablement, referrals, churn prevention. Toto je tvoj growth stack."

#### 4:30–5:30 | Špeciálne a technické skills
- **Povedať:** „Na záver pár špeciálnych skillov, ktoré sú jedinečné."

**16. `customer-research` – Čo si myslia zákazníci**
  - Na čo: analýza rozhovorov, survey analýza, review mining, Reddit mining
  - Trigger: „customer research", „čo hovoria zákazníci", „VOC"
  - **Best use:** „Analyzuj podporové tickety za posledný mesiac a identifikuj top 5 pain pointov."

**17. `ai-seo` – SEO pre AI vyhľadávače**
  - Na čo: optimalizácia pre ChatGPT, Perplexity, AI Overviews
  - Trigger: „AI SEO", „LLM optimalizácia", „objaviť sa v ChatGPT"
  - **Best use:** „Ako mám upraviť obsah, aby ma citovali AI vyhľadávače?"

**18. `programmatic-seo` – SEO na škále**
  - Na čo: generovanie stoviek SEO stránok podľa šablón
  - Trigger: „programmatic SEO", „pSEO", „vygeneruj stránky"
  - **Best use:** „Vytvor šablónu pre '[názov nástroja] alternative' stránky."

**19. `image` – Vizuálny obsah**
  - Na čo: blog hero images, social media grafika, OG images
  - Trigger: „vytvor obrázok", „hero image", „social media grafika"
  - **Best use:** „Vytvor hero image pre blog post o AI agentoch – štýl: moderný, tech, modrá+purpurová."

**20. `social` – Social media manažér**
  - Na čo: LinkedIn posty, Twitter thready, content kalendár
  - Trigger: „LinkedIn post", „Twitter thread", „social media"
  - **Best use:** „Napíš 5 LinkedIn postov na tento týždeň – téma: AI v biznise."

- **Povedať:** „Toto je moja top 20. Každý z týchto skillov som reálne použil. Každý z nich šetrí hodiny."

#### 5:30–6:00 | Zhrnutie modulu a čo ďalej
- **Povedať:** „Gratulujem! Práve si dokončil Modul 3. Čo všetko si sa naučil:"
  - ✅ Čo sú skills, kde ich nájsť, ako vyhodnotiť kvalitu
  - ✅ Ako skilly inštalovať a používať – 4 spôsoby inštalácie, 3 spôsoby aktivácie
  - ✅ Ako vytvoriť vlastný markdown skill – od štruktúry po iteratívne vylepšovanie
  - ✅ Python skills – kedy ich použiť, ako ich postaviť, ako ladiť
  - ✅ Prehľad top 20 skillov z knižnice pre biznis a marketing
- **Povedať:** „V Module 4 sa naučíš o automatizácii – kontinuálny harness, heartbeat-y, sub-agenti. Ale to je už iná kapitola..."

### Kľúčové body
- Top 5 marketing skills: copywriting, seo-audit, content-strategy, competitor-profiling, emails
- Top 5 biznis skills: pricing, offers, ab-testing, launch, marketing-plan
- Top 5 growth skills: cold-email, prospecting, sales-enablement, referrals, churn-prevention
- Špeciálne: customer-research, ai-seo, programmatic-seo, image, social
- Každý skill = hodiny ušetreného času. Zační s tými, ktoré riešia tvoj najväčší problém

### Domáca úloha
1. Nainštaluj a vyskúšaj aspoň 5 skillov z tohto zoznamu, ktoré si ešte nepoužil. Pre každý napíš 1-vetovú recenziu
2. Identifikuj 3 manuálne procesy vo svojej práci, ktoré by sa dali pokryť existujúcimi skillmi z knižnice. Implementuj ich
3. Vytvor si vlastný „osobný stack" – zoznam 10 skillov, ktoré budeš používať najčastejšie. Zoraď ich podľa priority
4. Zdieľaj svoj stack v diskusii – porovnaj s ostatnými, inšpiruj sa, diskutuj

---

## Kontrolný zoznam Modulu 3

Odškrtni si po splnení:

- [ ] Lekcia 1: Viem, čo sú skills, kde ich nájsť, a ako vyhodnotiť ich kvalitu
- [ ] Lekcia 2: Ovládam inštaláciu skillov (4 spôsoby) a ich používanie (3 spôsoby aktivácie)
- [ ] Lekcia 3: Viem vytvoriť vlastný markdown skill – ovládam štruktúru SKILL.md a iteratívne vylepšovanie
- [ ] Lekcia 4: Rozumiem Python skillom – viem, kedy ich použiť a ako ich postaviť
- [ ] Lekcia 5: Poznám top 20 skillov z knižnice a viem, ktoré riešia moje najväčšie problémy
- [ ] Všetky domáce úlohy odovzdané / splnené

---

*Prime Agent Masterclass © 2025 – Modul 3/6*
