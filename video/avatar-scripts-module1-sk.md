# Modul 1: Úvod a inštalácia – AI Avatar Skripty

---

## Lekcia 1: Čo je Prime Agent a prečo teraz (5 min)

[00:00] (úsmev, energický, ruky široko)
Predstav si, že máš kolegu, ktorý nikdy nespí. [...] Nikdy sa nesťažuje. [...] A rozumie presne tomu, čo po ňom chceš.

[00:12] (pauza, ruky k sebe)
To nie je sci-fi. To je AI agent. A presne o tom je tento kurz.

[00:20] (krok bližšie ku kamere, dôverný tón)
Volám sa [tvoje meno] a toto je Prime Agent Masterclass. Vitaj v Module 1.

[00:28] (uvoľnený postoj)
Začnime úplne od základov. Čo to vlastne ten Prime Agent je?

[00:34] (ruky pred seba, vysvetľujúci postoj)
Prime Agent je tvoj vlastný AI agent, ktorý beží priamo na tvojom počítači. [...] Nie v cloude niekde v Kalifornii. U teba. Pod tvojou kontrolou.

[00:46] (dôraz prstom)
A to je obrovský rozdiel.

[00:50] (krok späť, rozhliadnutie)
Vie čítať súbory. Vie spúšťať kód. Vie prehľadávať web. Vie písať do terminálu. [...] A hlavne – vie rozmýšľať v krokoch.

[01:04] (spomalenie, vážnejší tón)
Dostane úlohu, rozloží si ju na podúlohy, spustí nástroje, pozrie sa na výsledok, vyhodnotí ho a rozhodne sa, čo ďalej. [...] Presne ako dobrý vývojár.

[01:17] (uvoľnenie, ľahký úsmev)
Len to robí za sekundy. A nikdy nezabudne, čo robil pred minútou.

[01:26] (tempo sa zrýchľuje, nadšenie)
A teraz tá dôležitejšia otázka: [...] Prečo práve teraz?

[01:32] (prsty na ruke – počítanie)
Tri dôvody.

[01:35] (jeden prst)
Po prvé – modely sú konečne dosť schopné. GPT-4, Claude, DeepSeek, Gemini. [...] Ešte pred dvoma rokmi by to nefungovalo. Modely nevedeli dostatočne dobre rozmýšľať v reťazcoch. Dnes? [...] Dnes ti agent rozloží komplexnú úlohu na dvadsať krokov a každý z nich vykoná.

[01:55] (dva prsty)
Po druhé – nástroje dozreli. Terminál, filesystém, web, API. [...] Agent už nie je len hlava. Má ruky. Môže naozaj niečo spraviť, nielen o tom hovoriť.

[02:10] (tri prsty)
A po tretie – [...] a toto je podľa mňa najdôležitejšie – [...] svet sa zrýchlil natoľko, že jednoducho nestíhaš.

[02:22] (osobný tón)
Koľkokrát si si povedal: "Toto by som mal zautomatizovať." [...] "Na toto potrebujem skript." [...] "Keby tak niekto urobil tú nudnú časť za mňa." [...] "Toto by mi trvalo celé popoludnie."

[02:38] (výrazné prikývnutie)
Presne na toto je Prime Agent. [...] Nie aby ťa nahradil. Ale aby ťa odbremenil.

[02:48] (nová energia, ruky do strán)
Na konci tohto kurzu budeš mať agenta, ktorý ti reálne pomáha. [...] Nie hračku. Nie chatbot, s ktorým sa rozprávaš, keď sa nudíš. [...] Kolegu. Ktorý maká, kým ty rozmýšľaš nad tým dôležitým.

[03:06] (ukľudnenie, štruktúra)
Tento prvý modul je základ. Zoznámime sa s tým, čo agent je, ako funguje, nainštalujeme ho, spustíme, nastavíme a dáme mu prvý príkaz.

[03:20] (pohľad priamo do kamery, úprimnosť)
Ak si nikdy nepracoval s terminálom, ak ťa desí príkazový riadok, ak si myslíš, že toto nie je pre teba – [...] zostaň so mnou.

[03:32] (ruky na srdce)
Pretože práve ty z toho vyťažíš najviac. [...] Kto nevie programovať, pre toho je agent najväčším skokom v produktivite.

[03:42] (energia stúpa)
Prime Agenta ovládaš v prirodzenom jazyku. Po slovensky. Po česky. Po anglicky. [...] Povieš mu, čo chceš. On spraví zvyšok.

[03:54] (pauza, úsmev)
Toto je budúcnosť práce s počítačom. A ty budeš pri tom. Nie za päť rokov. Teraz.

[04:05] (vážnejší, sústredený)
Dnes sa pozrieme na to, čo dokáže, a prečo vznikol. [...] Potom si ho nainštalujeme. A na konci modulu mu dáš jeho prvý príkaz.

[04:18] (prechodový moment)
Ale najprv – poďme pochopiť, čím sa agent líši od bežného chatbota. Lebo to je úplne zásadný rozdiel. A keď ho pochopíš, všetko ostatné začne dávať zmysel.

[04:32] (gesto smerom k obrazovke, pohľad vedľa kamery)
Poďme sa na to pozrieť. Na obrazovke ti ukážem, ako vyzerá agent v akcii oproti klasickému chatu.

[04:42] (posledný pohľad do kamery, úsmev)
Toto ťa bude baviť. Poďme na to.

[04:48] (odchod od kamery, prechod na screen demo)
---

## Lekcia 2: Ako funguje AI agent vs chatbot (4 min)

[00:00] (stojí, ruky v bok, sebavedomý postoj)
Použil si niekedy ChatGPT? [...] Jasné, že áno. Všetci sme.

[00:07] (ruky pred seba, paralelné gesto)
Napíšeš otázku. On odpovie. Napíšeš ďalšiu. On znova odpovie. [...] Je to ako ping-pong. Loptička sem, loptička tam.

[00:18] (zastavenie, dôraz)
A teraz si predstav toto: [...] Povieš mu – "sprav mi analýzu všetkých PDF súborov v tomto priečinku, porovnaj čísla, vytvor graf a pošli ho mailom šéfovi."

[00:30] (pauza, zdvihnuté obočie)
Chatbot ti povie: "Super nápad! Tu je návod ako na to. Najprv otvor PDF, potom extrahuj dáta..." [...] A máš pred sebou pätnásť krokov, ktoré musíš spraviť ty.

[00:42] (ticho, potom dôraz)
Agent to spraví.

[00:46] (rozhodenie rukami)
Toto je ten rozdiel. Jeden rozpráva. Druhý koná.

[00:52] (krok vpred, dôverný tón)
Chatbot je konverzačný partner. Je to ako mať múdreho kamaráta, ktorý ti vždy poradí. [...] Agent je vykonávateľ. Je to ako mať zamestnanca, ktorý tú radu aj zrealizuje.

[01:06] (ukľudnenie, vysvetľujúci postoj)
Pozrime sa na to zvnútra. Čo sa deje, keď agent dostane úlohu?

[01:13] (počítanie na prstoch, pomaly)
Krok jedna: [...] Premýšľa. [...] Rozloží zadanie na menšie časti. [...] Spýta sa sám seba: "Čo všetko musím spraviť, aby som toto dokončil? V akom poradí? Čo potrebujem vedieť?"

[01:32] (dva prsty)
Krok dva: [...] Koná. Spustí príkaz. Otvorí súbor. Zavolá API. Niečo reálne urobí vo svete. Nie len vygeneruje text.

[01:46] (tri prsty)
Krok tri: [...] Pozoruje. Pozrie sa na výsledok. Vyhodnotí ho. [...] "Vyšlo to? Je to správne? Dáva to zmysel? Musím niečo opraviť alebo skúsiť inak?"

[02:02] (štyri prsty, kruhový pohyb)
A krok štyri: [...] Opakuje. Vráti sa ku kroku jedna s novou informáciou. [...] A znova. A znova. Kým nie je hotovo.

[02:16] (zastavenie, pohľad do kamery)
Toto je tá slučka: [...] Think → Act → Observe → Repeat.

[02:24] (gesto rukou – kolobeh)
A v tom je celé kúzlo. Agent nielen rozpráva. Agent robí. A učí sa z vlastných výsledkov.

[02:34] (praktický príklad, uvoľnený postoj)
Dám ti príklad z reálneho sveta. [...] Povedzme, že chceš zistiť, či tvoja webstránka funguje správne.

[02:44] (simulácia rozhovoru)
Chatbotu povieš: "Ako skontrolovať webstránku?" [...] On ti odpovie: "Použi PageSpeed Insights, skontroluj meta tagy, pozri sa na mobilnú verziu, over SSL certifikát..." [...] Super rady. Fakt. Ale musíš ich ísť spraviť ty. Jednu po druhej.

[03:00] (zmena tónu, energickejšie)
Agentovi povieš to isté. [...] A on: [...] otvorí stránku. [...] spustí audit. [...] prezrie meta tagy. [...] skontroluje rýchlosť na mobile aj desktope. [...] nájde rozbité linky. [...] overí certifikát. [...] A vráti sa ti s kompletnou správou aj s odporúčaniami, čo opraviť.

[03:20] (ruky otvorené)
Ty si medzitým vypil kávu. [...] Alebo robil niečo, čo naozaj vyžaduje tvoj mozog.

[03:28] (úsmev, uvoľnenie)
Toto nie je sci-fi. Toto je dnes. A ty sa to naučíš ovládať.

[03:36] (vážnejší, štruktúrovaný)
Samozrejme, nie je to mágia. Agent nie je dokonalý. [...] Môže sa pomýliť. Môže ísť zlým smerom. Môže niečo zle pochopiť. Preto je dôležité rozumieť tomu, ako premýšľa. Ako ho viesť.

[03:52] (povzbudenie)
A presne to sa naučíme v ďalších moduloch – ako agenta viesť, kontrolovať, opravovať a dostať z neho maximum.

[04:01] (prechodový moment, gesto k obrazovke)
Ale teraz – poďme sa pozrieť na obrazovku. Ukážem ti reálny príklad. [...] Rovnaká úloha. Chatbot verzus agent. Uvidíš ten rozdiel na vlastné oči.

[04:15] (úsmev, energia)
Poďme na to.

[04:18] (prechod na screen demo)
---

## Lekcia 3: Inštalácia krok za krokom (3 min)

[00:00] (energický, ruky spolu)
Dosť bolo teórie. [...] Poďme si zašpiniť ruky.

[00:06] (pauza, úsmev)
Ideme nainštalovať Prime Agenta na tvoj počítač.

[00:12] (upokojujúci tón, ruky pred seba)
A viem, čo si možno myslíš. [...] "Inštalácia. Terminál. Príkazy. To znie komplikovane." [...] Ale sľubujem ti – je to jednoduchšie, než si myslíš.

[00:25] (jeden prst)
Jeden príkaz. [...] Jeden riadok do terminálu. [...] A hotovo.

[00:33] (krok späť, priznanie)
Pamätám si, keď som prvýkrát niečo inštaloval cez terminál. [...] Mal som strach, že niečo pokazím. [...] Že sa mi rozbije počítač. [...] Že uvidím červené chyby a nebudem vedieť, čo s nimi.

[00:46] (povzbudenie, úsmev)
Ale vieš čo? [...] Je to len kopírovanie a vkladanie. [...] A ak to zvládli tisíce ľudí pred tebou, zvládneš to aj ty.

[00:57] (vážnejší, štruktúrovaný)
Predtým, než začneme, rýchla kontrola. Potrebuješ tri veci:

[01:03] (prvý prst)
Node.js na počítači. [...] To je ten runtime, v ktorom agent beží. Ak ho nemáš, neboj sa – na obrazovke ti ukážem, ako ho nainštalovať. Trvá to dve minúty.

[01:15] (druhý prst)
Terminál. [...] Alebo príkazový riadok. Na Macu je to Terminal, na Windowse PowerShell alebo CMD. Je to priamo v systéme, nemusíš nič inštalovať.

[01:26] (tretí prst)
A tretia vec? [...] Odvaha. [...] Prvý krok je vždy najťažší. Ale keď ho spravíš, zvyšok už pôjde sám.

[01:38] (energia späť)
Celá inštalácia je v podstate toto: [...] Otvoríš terminál. Napíšeš jeden príkaz. [...] Stlačíš Enter. [...] A čakáš pár sekúnd.

[01:50] (gesto – hotovo)
A potom? [...] Máš vlastného AI agenta. Na svojom počítači. Pripraveného pracovať.

[01:58] (pauza, pohľad do kamery)
Je to jeden z tých momentov, keď si povieš: [...] "Počkať. To je ono? [...] To bolo všetko?"

[02:08] (úsmev)
Áno. To je ono. [...] A teraz máš super silu, ktorú väčšina ľudí ešte neobjavila.

[02:16] (prechod na demo)
A teraz ti to ukážem naživo. [...] Krok za krokom. Od kontroly Node.js až po úspešnú inštaláciu.

[02:25] (gesto k obrazovke)
Každý krok uvidíš na obrazovke. [...] Čo napísať. Čo očakávať. [...] A keď niečo nevyjde, ukážem ti, ako to opraviť. [...] Nie si v tom sám.

[02:38] (záverečný pohľad do kamery)
Pripravený? [...] Poďme nainštalovať tvojho prvého AI agenta.

[02:45] (prechod na screen demo)
---

## Lekcia 4: Prvé spustenie a orientácia (3 min)

[00:00] (nadšený, ruky hore)
Máš ho! [...] Prime Agent je na tvojom počítači. Výborne!

[00:07] (ukľudnenie, poďme na vec)
A teraz – čo s ním? Poďme ho prvýkrát spustiť a pozrieť sa, čo všetko vidíš.

[00:16] (gesto – predstavenie)
Keď napíšeš `prime-agent` do terminálu a stlačíš Enter, otvorí sa pred tebou úplne nový svet.

[00:24] (opis, ruky pred seba)
Uvidíš terminálové okno, ktoré je rozdelené na niekoľko častí. [...] Na prvý pohľad to môže vyzerať technicky. Ale nie je to zložité.

[00:35] (štruktúra, počítanie)
Sú to v podstate tri časti, ktoré potrebuješ poznať:

[00:40] (prvý prst)
Po prvé – konverzačné okno. [...] To je tvoje hlavné miesto. Tam píšeš, čo chceš. A tam vidíš, čo agent robí a ako rozmýšľa. [...] Celý jeho myšlienkový proces. Transparentne. Krok za krokom.

[00:56] (druhý prst)
Po druhé – pracovný adresár. [...] To je miesto, odkiaľ agent štartuje. Tam má prístup k tvojim súborom. Nastavíš si ho podľa toho, na čom práve pracuješ. [...] Môže to byť tvoj projekt, tvoj dokumenty, čokoľvek.

[01:11] (tretí prst)
A po tretie – [...] nič viac. Naozaj. [...] Žiadne zložité menu. Žiadne desiatky tlačidiel. Žiadne nastavenia, v ktorých sa stratíš. Len ty a tvoj agent.

[01:24] (filozofia, dôraz)
A to je zámer. [...] Prime Agent je minimalistický. Robí jednu vec – rozumie ti a koná. Bez rozptyľovania. Bez zbytočností.

[01:36] (praktické, pokojný tón)
Keď agenta spustíš prvýkrát, privíta ťa. Opýta sa, s čím ti môže pomôcť. [...] Je to presne ako prvý rozhovor s novým kolegom. Len tento kolega je pripravený pracovať okamžite.

[01:50] (uistenie)
A neboj sa – nemôžeš nič pokaziť. [...] Agent pracuje len v tom adresári, ktorý mu dáš. Nezmazáva súbory, kým mu to explicitne nepovieš. A vždy sa ho môžeš spýtať: "Čo presne spravíš?" [...] A on ti to vysvetlí.

[02:05] (prechodový moment)
V ďalšej lekcii si nastavíme model a API kľúč, aby agent naozaj vedel rozmýšľať. [...] Ale najprv – poďme sa pozrieť, ako to celé vyzerá naživo.

[02:18] (gesto k obrazovke, energia)
Na obrazovke ti ukážem prvé spustenie. [...] Čo uvidíš. Čo kam napísať. Ako sa v tom zorientovať. [...] Krok za krokom.

[02:30] (úsmev)
Si pripravený na prvý kontakt so svojím agentom? Poďme na to.

[02:37] (prechod na screen demo)
---

## Lekcia 5: Nastavenie modelu a API kľúča (3 min)

[00:00] (pokojný, ruky pred seba)
Tvoj agent je nainštalovaný. Spustil si ho. [...] Ale ešte mu chýba mozog.

[00:08] (pauza, vysvetlenie)
Prime Agent sám o sebe je len kostra. [...] Aby vedel rozmýšľať, potrebuje model. A na to, aby sa k modelu pripojil, potrebuje API kľúč.

[00:19] (zjednodušenie)
Predstav si to takto: [...] Agent je auto. Model je motor. A API kľúč sú kľúče od zapaľovania. [...] Bez motora auto nejde. Bez kľúčov motor nenaštartuješ.

[00:33] (pokojný, vecný)
Aké modely môžeš použiť? [...] Možností je viacero a je to jedna z najväčších výhod Prime Agenta – nie si viazaný na jedného poskytovateľa.

[00:45] (počítanie na prstoch)
Claude od Anthropicu. [...] GPT-4o od OpenAI. [...] DeepSeek. [...] Gemini od Googlu. [...] A dokonca lokálne modely cez Ollama.

[00:58] (dôležité rozlíšenie)
A tu je kľúčová vec: [...] Niektoré modely sú platené – platíš za to, čo reálne využiješ. Iné ponúkajú kredity zadarmo na začiatok. A lokálne modely [...] tie sú úplne zadarmo, bežia priamo na tvojom hardvéri.

[01:14] (odporúčanie, úprimný tón)
Moja rada na začiatok? [...] Choď do DeepSeeku. Je lacný, extrémne schopný, a za pár eur prejdeš celý tento kurz. [...] Je to momentálne najlepší pomer cena/výkon na trhu.

[01:29] (uistenie)
A ak nechceš platiť vôbec? [...] Dá sa to. Ukážem ti aj lokálnu možnosť cez Ollama. Ale úprimne – na prvé kroky je cloudový model pohodlnejší a rýchlejší.

[01:42] (bezpečnosť, dôraz)
Ešte jedna zásadná vec, kým pôjdeme ďalej. [...] API kľúč.

[01:48] (vážny tón)
API kľúč je tvoje heslo k modelu. [...] Nikdy ho nezdieľaj. Nikdy ho nedávaj do kódu, ktorý nahrávaš na GitHub. [...] Nikdy ho neposielaj cez chat. [...] Toto je pravidlo číslo jeden.

[02:01] (upokojenie)
Prime Agent ho ukladá bezpečne. V špeciálnom konfiguračnom súbore, ktorý je len na tvojom počítači. Nikam sa neposiela. Tak to má byť.

[02:13] (prechod, energia)
Ale toto všetko sú len slová. [...] Poďme si to nastaviť. Na obrazovke ti ukážem:

[02:21] (počítanie, rýchlejšie tempo)
Kde získať API kľúč – pre každého poskytovateľa zvlášť. [...] Ako ho bezpečne uložiť do Prime Agenta. [...] Ako vybrať ten správny model pre tvoje potreby. [...] A ako celé nastavenie otestovať, aby si vedel, že to funguje.

[02:38] (gesto k obrazovke)
Všetko krok za krokom. Bez zbytočných komplikácií.

[02:44] (záverečný pohľad, povzbudenie)
Po tejto lekcii bude tvoj agent nielen stáť v garáži. [...] Bude naštartovaný. Pripravený. [...] S plnou nádržou.

[02:55] (úsmev)
Poďme mu dať mozog.

[02:58] (prechod na screen demo)
---

## Lekcia 6: Tvoj prvý command (2 min)

[00:00] (slávnostný tón, ruky spolu)
Toto je ten moment. [...] Moment, na ktorý sme celý tento modul pracovali.

[00:08] (pauza, pohľad do kamery)
Tvoj agent je nainštalovaný. Má model. Má API kľúč. [...] Je pripravený.

[00:16] (budovanie napätia, pomaly)
A teraz mu dáš jeho úplne prvý príkaz.

[00:21] (uvoľnenie, praktický tón)
Čo mu povedať? [...] Môže to byť hocičo. Ale odporúčam začať jednoducho. Nechaj veľké úlohy na neskôr.

[00:31] (príklady, počítanie na prstoch)
"Ukáž mi, čo je v tomto adresári." [...] "Vytvor mi súbor s básničkou." [...] "Nájdi na webe päť najlepších reštaurácií v Bratislave." [...] "Spočítaj, koľko slov je v tomto dokumente."

[00:43] (dôraz)
Čokoľvek z toho. [...] Dôležité je, aby si videl, čo sa stane. Aby si zažil ten pocit.

[00:52] (opis procesu, vzrušenie)
Keď stlačíš Enter, stane sa niečo magické. [...] Agent začne rozmýšľať. Uvidíš, ako si rozkladá úlohu na menšie časti. [...] Potom spustí príkaz. Vráti výsledok. Vyhodnotí ho. [...] A možno spraví ďalší krok. A ďalší.

[01:08] (pauza, dôraz)
Toto nie je chatbot, čo ti odpovie jedným textom a hotovo. [...] Toto je agent, ktorý koná. A ty celý proces uvidíš v reálnom čase.

[01:18] (osobný tón)
Pamätám si svoj prvý command. [...] Bol to jednoduchý príkaz – "sprav mi prieskum konkurencie pre môj startup". [...] Agent strávil desať minút prehľadávaním webu, porovnávaním cien, hľadaním recenzií. [...] Priniesol mi správu, ktorú by som sám robil hodiny.

[01:34] (odmlka, úsmev)
Vtedy som pochopil. [...] Toto mení všetko.

[01:41] (prechod, energia)
Ale dosť bolo môjho rozprávania. [...] Poďme to spraviť. Poďme mu dať tvoj prvý príkaz.

[01:49] (gesto k obrazovke, nadšenie)
Na obrazovke uvidíš celý proces. Čo napísať. Čo sa stane. Ako čítať výstup. [...] Celý ten moment od začiatku do konca.

[01:59] (posledný pohľad do kamery)
Si pripravený? [...] Tak poďme na to. Tvoj prvý command.

[02:05] (prechod na screen demo)
