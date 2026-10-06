# Tilbakemelding på product brief

| | |
|---|---|
| **Gruppe** | G57 – G57-siyar-ulle |
| **Product brief** | `PRODUCT_BRIEF.md` (commit 0d46b68) |
| **Tilbakemelding fra** | Faglærer i IBE160 (utarbeidet med KI-støtte) |
| **Dato** | 2026-10-06 |

## Samlet vurdering

- **Bør revideres før dere går videre.** Rett punktene markert «Endre» før dere lager PRD og arkitektur.

**Det som er bra:**

1. Idéen er tydelig og realistisk: Moldiz lar studenten lime inn fagtekst og få sammendrag, forklaringer, spørsmål og quiz. MVP-lista i fem steg er konkret, og dere har allerede fått et første sammendrag med Gemini til å virke i `app.py`.
2. Teknologivalget (Python og Streamlit) er enkelt og godt egnet for nybegynnere, og lista «Mulig videreutvikling» gir gode kandidater til å utvide omfanget.

**De viktigste endringene:**

1. Omfanget i MVP-en er for lite. Lim inn tekst → sammendrag → noen spørsmål kan bli ferdig på svært kort tid, og dere har allerede laget en del av det. Da blir det lite å vise i funksjonalitet, testing og prosess. Flytt minst to punkter fra «Mulig videreutvikling» inn i v1, for eksempel quiz med retting og poeng, og lagring av tidligere notater.
2. Briefen mangler suksesskriterier som kan testes, og en ærlig vurdering av hva som skiller Moldiz fra eksisterende verktøy (ChatGPT, Quizlet, NotebookLM med flere). Lag briefen på nytt med BMAD (`bmad-product-brief`), slik at den får alle delene: problem, løsning, brukere, «What Makes This Different», suksesskriterier, scope og visjon.
3. Følg BMAD-flyten før dere bygger videre. Koden ble lagt inn samme dag som briefen. Lag PRD, arkitektur og stories først, slik at sensor kan spore funksjonene fra plan til kode.

## Vanskelighetsgrad og gjennomførbarhet

### Vurdert vanskelighetsgrad

- **Enkel**

**Sammenlignbart med:** 8) Foredragsnotater – sammendrag og quizgenerator (enkel). MVP-en i briefen er enda smalere enn forslaget, siden den ikke har quiz med fasit, filopplasting eller lagring.

**Begrunnelse:**

| Faktor | Nivå (lav / middels / høy) | Kommentar |
|---|---|---|
| Domenelogikk – hvor mange og hvor kompliserte regler og beregninger må stemme? | Lav | Nesten ingen egen logikk i MVP-en. Quiz med tilbakemelding (funksjon 4) ville gitt litt mer. |
| Datamodell – antall entiteter og relasjoner mellom dem | Lav | Ingen lagring i MVP-en. Med lagring av notater blir det notat, sammendrag, spørsmål og quizresultat. |
| Brukere, roller og innlogging | Lav | Én brukertype, ingen innlogging. |
| KI-funksjonalitet i appen, f.eks. kall til språkmodell, prompts i koden og håndtering av usikre svar | Middels | KI er sentral: sammendrag, forklaring og spørsmål. Strukturert utdata for quiz (spørsmål, alternativer, fasit) er det mest krevende. |
| Integrasjoner og eksterne tjenester, f.eks. API-er, betaling og e-post | Middels | Gemini-API med nøkkel. Gemini har et gratisnivå, men sensor må ha egen nøkkel eller en testmodus. |
| Sanntid, samtidighet eller flere brukere som påvirker hverandre | Lav | Ingen. |
| Filhåndtering, f.eks. opplasting, PDF-lesing og eksport | Lav | Bare innliming av tekst i MVP-en. PDF-opplasting er nevnt som videreutvikling. |
| Sikkerhet og personvern | Lav | Ingen personopplysninger. API-nøkkelen må holdes utenfor repoet. Dere bruker `.env`, og det er riktig. |

**Hva vanskelighetsgraden betyr for dere:**

- _Enkel:_ Et enkelt prosjekt gir stor sjanse for å bli ferdig. Vanskelighetsgraden inngår likevel i vurderingen, så for å nå helt opp må dere vise mer i gjennomføringen. Det betyr særlig et gjennomarbeidet design, grundig testing, en tydelig dokumentert prosess og en README som virker. For Moldiz bør dere i tillegg utvide omfanget, slik at det er nok funksjonalitet å vise.

### Gjennomførbarhet med BMAD og Claude Code

Dere skal planlegge med BMAD (product brief → PRD → arkitektur → epics og stories) og implementere med Claude Code. Vurderingen under tar hensyn til at det må være tid til hele denne flyten, og til testing, retting og README til slutt.

| Spørsmål | Vurdering (OK / risiko / stor risiko) | Kommentar |
|---|---|---|
| **Tid og omfang** – kan v1 realistisk bli ferdig og stabil i løpet av semesteret, med tid til flere iterasjoner? | Risiko | Risikoen er motsatt av det vanlige: MVP-en er så liten at den blir ferdig lenge før semesteret er over, og gir lite å vise. |
| **BMAD-flyten** – er briefen konkret nok til at PRD, arkitektur og stories kan lages uten store hull, og blir det overkommelig mange stories? | Risiko | Funksjonene er listet, men suksesskriterier og avgrensning mangler, og briefen er ikke laget med BMAD-malen. PRD-en får lite å bygge på. |
| **Egnet for Claude Code** – bruker løsningen en vanlig, godt dokumentert teknologistakk som Claude Code håndterer godt, eller krever den nisjeteknologi, spesialmaskinvare eller mye manuell konfigurasjon? | OK | Python, Streamlit og Gemini-API er godt dokumentert. |
| **Kontroll på KI-ens arbeid** – kan gruppen selv avgjøre om koden gjør det riktige? Krever domenet kunnskap gruppen ikke har, f.eks. avanserte beregninger eller fagregler, så er det vanskelig å kvalitetssikre. | OK | Koden er enkel å kontrollere. Kvaliteten på KI-svarene kan dere vurdere mot fagtekster dere kjenner. Briefen nevner selv «kvalitetssikring av KI-genererte svar», og det er bra. |
| **Testbarhet** – finnes det tydelige regler og forventede resultater som tester kan skrives mot? | Risiko | Uten suksesskriterier og egen logikk er det lite å teste utover at kallet til Gemini virker. Quiz med retting og poeng gir tydelige regler å teste mot. |
| **Kjørbar for sensor** – kan appen kjøres lokalt etter README, uten gruppens nøkler, betalte kontoer eller egen infrastruktur? | Risiko | Krever Gemini-nøkkel. Beskriv i README hvordan sensor lager en gratis nøkkel, legg ved `.env.example`, og vurder en testmodus med ferdige svar. |
| **Avhengigheter og kostnader** – krever løsningen betalte API-er, f.eks. språkmodeller, og finnes det en plan for kostnad, testmodus eller mock-data? | Risiko | Gemini er valgt, men briefen nevner ikke kostnad, gratisnivå eller testmodus. |

**Konklusjon om gjennomførbarhet:**

- **Gjennomførbart med justert omfang.** Se forslagene under.

**Forslag til justering av omfang eller vanskelighetsgrad:**

1. Utvid v1 med quiz med retting og poeng (funksjon 4 i briefen, men med tydelige regler) og lagring av tidligere notater med tilhørende sammendrag og quizresultater.
2. Legg til PDF-opplasting eller flashcards som et tydelig trinn 2, slik at dere har en plan for hva som kommer når v1 er ferdig og testet.

## Hvorfor product brief er viktig for mappen

Product brief er utgangspunktet for PRD, arkitektur, stories og til slutt koden. Del 1 av mappen vurderes blant annet på om sensor kan følge en sporbar vei fra plan til ferdig app. Den vurderes også på om appen gjør det dere har beskrevet, om den er testet, om den er godt designet, og om den kan kjøres etter README. Et uklart, for stort eller for lite brief gjør alt dette vanskeligere senere. Det er mye enklere å rette nå enn sent i semesteret.

## 1. Gjennomgang av briefens deler

| Del av brief | Status | Kommentar |
|---|---|---|
| Executive Summary – er det klart hva appen er, og hvilket problem den løser? | OK | «Produktidé» forklarer tydelig hva Moldiz er og gjør. |
| The Problem – er problemet konkret, med reelle situasjoner og brukere? | Juster | Problemet er riktig, men generelt. Beskriv en konkret situasjon, for eksempel en student som skal repetere et kapittel før en prøve. |
| The Solution – beskriver løsningen brukeropplevelsen, ikke bare teknologi? | OK | De fire funksjonene beskriver hva brukeren gjør. |
| What Makes This Different – er vurderingen ærlig og realistisk? | Endre | Mangler. Hvorfor skal en student bruke Moldiz i stedet for å lime teksten inn i ChatGPT? Skriv en ærlig vurdering. |
| Who This Serves – er primærbrukerne tydelige, og vet vi hva de trenger? | Juster | «Studenter på høyskole og universitet» er bredt. Velg én konkret primærbruker. |
| Success Criteria – kan kriteriene faktisk sjekkes eller testes? | Endre | Mangler. «Mål for prosjektet» handler om hva dere skal lære, ikke om hva appen skal klare. Legg til kriterier som «brukeren kan ta en quiz på 5 spørsmål og se antall riktige». |
| Scope – er det klart hva som er med i første versjon, og hva som ikke er det? | Endre | MVP og videreutvikling er listet, men MVP-en er for liten, og «Forklaring av fagstoff» og «Quiz» står som hovedfunksjoner uten å være med i MVP-en. Gjør scope konsistent. |
| Vision – henger visjonen sammen med resten uten å blåse opp omfanget? | Juster | «Mulig videreutvikling» fungerer som visjon, men flere av punktene bør heller inn i v1. |

## 2. Utgangspunkt for del 1 av mappen

Punktene følger kriteriene i sensorveiledningen for del 1. Vektene i parentes viser hvor mye hvert kriterium teller i del 1.

| Kriterium i del 1 | Hva briefen bør legge til rette for | Status | Kommentar |
|---|---|---|---|
| **1. Prosess og KI-styring** (30 %) | Brief som er presis nok til at PRD og stories kan bygges direkte på den, slik at krav kan spores fra brief til kode. | Endre | Briefen er ikke laget med BMAD, og koden kom før PRD og stories. Lag brief, PRD og stories med BMAD nå, og lagre prompts og KI-økter. |
| **2. Funksjonalitet og omfang** (20 %) | Realistisk omfang for gruppen og semesteret: en tydelig kjerneflyt som kan bli ferdig og stabil, og nok innhold til å vise reell funksjonalitet. | Endre | For lite omfang til å vise reell funksjonalitet. Utvid som foreslått over. |
| **3. Kvalitetssikring og testing** (15 %) | Suksesskriterier og funksjoner som er konkrete nok til å bli testtilfeller. | Endre | Ingen suksesskriterier å teste mot. Quizretting og lagring gir testbar logikk. |
| **4. Design og brukeropplevelse** (10 %) | Tydelige brukere og brukssituasjoner som designet kan bygges rundt, gjerne med de viktigste skjermbildene eller flytene skissert. | Juster | Streamlit gir et ryddig utgangspunkt. Beskriv brukssituasjonen og skisser hvordan sammendrag, spørsmål og quiz vises. |
| **5. Kodekvalitet og arkitektur** (10 %) | Teknologivalg som er begrunnet og ikke mer komplekse enn appen trenger. | OK | Python og Streamlit er et enkelt og passende valg. Samle KI-kallene i én modul når appen vokser. |
| **6. README og kjørbarhet** (10 %) | Løsning som andre kan kjøre lokalt uten betalte kontoer, og uten tilgang til gruppens egne tjenester og nøkler. | Juster | Krever Gemini-nøkkel. README mangler foreløpig oppskrift. Legg til `requirements.txt`, `.env.example` og trinnvis oppstart. |
| **7. Ryddighet i repoet** (5 %) | En plan for hvor hemmeligheter, testdata og dokumentasjon skal ligge. | Juster | Bruk av `.env` er riktig. Sjekk at `.env` står i `.gitignore`, og legg planleggingsdokumenter i en egen mappe. |

## 3. Neste steg for gruppen

1. Lag briefen på nytt med `bmad-product-brief`, med suksesskriterier, «What Makes This Different» og et utvidet, konsistent scope for v1.
2. Utvid v1 med quiz med retting og poeng og lagring av notater, og planlegg testmodus for Gemini.
3. Gå videre til PRD, arkitektur og stories før dere bygger mer kode, og commit planleggingsdokumentene underveis.

Oppdater product brief i repoet når dere har gjort endringene, slik at historikken viser hvordan planen utviklet seg. Det er en del av prosessen sensor ser etter.
