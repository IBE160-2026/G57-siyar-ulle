# PRD – Moldiz

## 1. Produktoversikt

Moldiz er en KI-basert studieassistent for studenter på høyskole og universitet.

Brukeren skal kunne lime inn fagtekst eller egne notater og bruke applikasjonen til å:

- lage sammendrag
- få enklere forklaringer
- generere quiz
- gjennomføre quiz
- få svar rettet
- se poengsum
- lagre tidligere notater og quizresultater

Målet er å gjøre repetisjon av fagstoff enklere og mer strukturert.

---

## 2. Problem

Studenter må ofte bruke mye tid på å:

- finne de viktigste punktene i en tekst
- lage egne sammendrag
- forstå vanskelige konsepter
- lage spørsmål for å teste seg selv
- holde orden på tidligere notater og resultater

Generelle KI-verktøy kan gjøre deler av dette, men brukeren må ofte selv skrive gode prompts og organisere resultatene.

Moldiz skal samle hele studieprosessen i én enkel arbeidsflyt.

---

## 3. Målgruppe

### Primærbruker

Student på høyskole eller universitet som skal repetere fagstoff før:

- prøve
- eksamen
- innlevering
- undervisning

Brukeren ønsker en enkel løsning uten å måtte skrive avanserte KI-prompts.

---

## 4. Hovedmål for v1

Første versjon av Moldiz skal støtte denne brukerflyten:

1. Brukeren limer inn fagtekst.
2. Brukeren kan lage et sammendrag.
3. Brukeren kan få teksten forklart enklere.
4. Brukeren kan generere en quiz med fem spørsmål.
5. Brukeren kan svare på spørsmålene.
6. Applikasjonen retter svarene.
7. Brukeren får poengsum og tilbakemelding.
8. Brukeren kan lagre notatet og resultatet.
9. Brukeren kan åpne tidligere lagrede notater.

---

## 5. Funksjonelle krav

### FR-1: Legge inn fagtekst

Brukeren skal kunne skrive eller lime inn tekst i et tekstfelt.

#### Akseptansekriterier

- tekstfeltet skal godta vanlig tekst
- tom tekst skal ikke kunne sendes til KI
- brukeren skal få en tydelig melding dersom feltet er tomt

---

### FR-2: Lage sammendrag

Brukeren skal kunne generere et kort sammendrag av fagteksten.

#### Akseptansekriterier

- sammendraget skal være basert på teksten brukeren har lagt inn
- resultatet skal vises tydelig på siden
- brukeren skal få en forståelig feilmelding dersom KI-tjenesten ikke svarer

---

### FR-3: Forklare fagstoff

Brukeren skal kunne få fagteksten forklart med enklere språk.

#### Akseptansekriterier

- forklaringen skal være basert på originalteksten
- resultatet skal vises separat fra sammendraget
- brukeren skal kunne bruke funksjonen uten å skrive egne prompts

---

### FR-4: Generere quiz

Moldiz skal kunne lage en quiz basert på fagteksten.

#### Akseptansekriterier

- quiz-en skal inneholde fem spørsmål
- hvert spørsmål skal ha en fasit
- spørsmålene skal være relevante for teksten
- quiz-data skal ha en struktur som applikasjonen kan bruke til retting

---

### FR-5: Gjennomføre quiz

Brukeren skal kunne svare på spørsmålene i applikasjonen.

#### Akseptansekriterier

- alle spørsmål skal vises tydelig
- brukeren skal kunne velge eller skrive svar
- brukeren skal kunne sende inn quiz-en når svarene er klare

---

### FR-6: Rette quiz

Applikasjonen skal kontrollere brukerens svar mot fasiten.

#### Akseptansekriterier

- riktig svar skal gi poeng
- feil svar skal ikke gi poeng
- brukeren skal få vite hvilke spørsmål som var riktige og feil
- korrekt svar skal vises ved feil svar

---

### FR-7: Vise poengsum

Etter gjennomført quiz skal brukeren få se resultatet.

#### Akseptansekriterier

- resultatet skal vise antall riktige av fem
- resultatet skal vises tydelig
- poengsummen skal kunne lagres sammen med notatet

---

### FR-8: Lagre notater

Brukeren skal kunne lagre tidligere arbeid.

Et lagret notat skal minimum kunne inneholde:

- tittel
- original fagtekst
- sammendrag
- quiz
- quizresultat

#### Akseptansekriterier

- informasjonen skal kunne lagres lokalt
- applikasjonen skal bekrefte at lagringen var vellykket
- data skal være tilgjengelig etter at applikasjonen startes på nytt

---

### FR-9: Åpne tidligere notater

Brukeren skal kunne se og åpne lagrede notater.

#### Akseptansekriterier

- en liste over lagrede notater skal kunne vises
- brukeren skal kunne velge et notat
- lagret sammendrag og quizresultat skal kunne vises igjen

---

## 6. Ikke-funksjonelle krav

### NFR-1: Enkel brukeropplevelse

Applikasjonen skal være enkel å forstå uten opplæring.

### NFR-2: Ytelse

Vanlige handlinger i brukergrensesnittet skal oppleves som raske.

Ventetid på KI-svar kan avhenge av Gemini API.

### NFR-3: Feilhåndtering

Appen skal ikke krasje dersom Gemini API gir feil.

Brukeren skal få en forståelig feilmelding.

### NFR-4: Sikkerhet

API-nøkkelen skal ikke lagres i GitHub.

Den skal hentes fra en lokal `.env`-fil.

### NFR-5: Kjørbarhet

En ny bruker eller sensor skal kunne starte prosjektet ved å følge README.

---

## 7. Teknisk retning

Planlagt teknologi:

- Python
- Streamlit
- Gemini API
- Git og GitHub
- lokal lagring med JSON eller SQLite
- pytest for testing

Endelig arkitektur beskrives i `architecture.md`.

---

## 8. Datamodell – foreløpig

Følgende data må kunne lagres:

### Note

- id
- title
- original_text
- summary
- created_at

### Quiz

- id
- note_id
- questions
- answers

### QuizResult

- id
- quiz_id
- score
- total_questions
- completed_at

Den endelige datamodellen bestemmes i arkitekturdokumentet.

---

## 9. KI-funksjonalitet

Gemini API skal brukes til:

- sammendrag
- enkel forklaring
- generering av quiz og fasit

KI skal ikke brukes til selve poengberegningen.

Poeng og retting skal håndteres av vanlig programlogikk slik at funksjonen kan testes.

---

## 10. Testkrav

Prosjektet skal minimum teste:

- tomt tekstfelt
- poengberegning
- riktige og feil quizsvar
- lagring av notat
- lasting av notat
- håndtering av feil fra Gemini API

KI-kvalitet skal også vurderes manuelt ved bruk av utvalgte fagtekster.

---

## 11. Kjørbarhet for sensor

Repositoryet skal inneholde:

- `README.md`
- `requirements.txt`
- `.env.example`
- instruksjoner for opprettelse av Gemini API-nøkkel
- trinn for å starte Streamlit-appen

Det skal vurderes en enkel testmodus eller mock-data dersom KI-tjenesten ikke er tilgjengelig.

---

## 12. Utenfor scope for v1

Følgende er ikke krav i første versjon:

- innlogging
- flere brukere
- deling mellom studenter
- mobilapp
- betaling
- avansert analyse
- automatisk synkronisering

---

## 13. Mulig videreutvikling

Etter at v1 er stabil kan prosjektet utvides med:

- PDF-opplasting
- flashcards
- vanskelighetsgrader
- flere typer quiz
- statistikk over utvikling
- støtte for flere språk
- eksport av notater

---

## 14. Suksesskriterier

Prosjektet regnes som en fungerende v1 dersom:

1. brukeren kan lime inn tekst
2. brukeren kan få et sammendrag
3. brukeren kan få en enklere forklaring
4. applikasjonen kan lage fem quizspørsmål
5. brukeren kan gjennomføre quiz-en
6. svarene blir rettet
7. poengsummen vises korrekt
8. notater og quizresultater kan lagres
9. lagrede notater kan åpnes igjen
10. appen kan startes etter README-instruksjonene
11. API-feil håndteres uten at appen krasjer

---

## 15. Neste steg

Etter at PRD-en er godkjent internt i gruppen skal vi lage:

1. `architecture.md`
2. epics og stories
3. testplan
4. deretter videre implementasjon

Rekkefølgen skal gjøre det mulig å spore funksjonalitet fra plan til ferdig kode.
