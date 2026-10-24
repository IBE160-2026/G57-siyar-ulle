# Epics and User Stories – Moldiz

## 1. Formål

Dette dokumentet deler kravene i PRD-en opp i epics og user stories.

Målet er å gjøre utviklingen sporbar fra:

Product Brief → PRD → Architecture → Stories → Code → Testing

---

# Epic 1 – Legge inn og behandle fagtekst

## Story 1.1 – Legge inn tekst

Som student  
vil jeg kunne skrive eller lime inn fagtekst  
slik at jeg kan bruke teksten videre i Moldiz.

### Akseptansekriterier

- brukeren kan skrive eller lime inn tekst
- tekstfeltet skal være tydelig synlig
- tom tekst skal ikke kunne sendes videre
- brukeren skal få en tydelig advarsel dersom feltet er tomt

---

## Story 1.2 – Lage sammendrag

Som student  
vil jeg kunne lage et sammendrag av fagteksten  
slik at jeg raskt kan se de viktigste punktene.

### Akseptansekriterier

- sammendraget skal være basert på brukerens tekst
- resultatet skal vises tydelig i appen
- brukeren skal kunne se at systemet arbeider mens KI-svaret genereres
- feil fra Gemini API skal håndteres uten at appen krasjer

---

## Story 1.3 – Få enklere forklaring

Som student  
vil jeg kunne få vanskelig fagstoff forklart enklere  
slik at jeg lettere kan forstå teksten.

### Akseptansekriterier

- forklaringen skal være basert på originalteksten
- brukeren skal ikke måtte skrive egne KI-prompts
- forklaringen skal vises separat fra sammendraget
- API-feil skal gi en forståelig feilmelding

---

# Epic 2 – Quiz

## Story 2.1 – Generere quiz

Som student  
vil jeg kunne generere en quiz fra fagteksten  
slik at jeg kan teste hva jeg har lært.

### Akseptansekriterier

- quiz-en skal inneholde fem spørsmål
- hvert spørsmål skal ha svaralternativer eller tydelig svarformat
- hvert spørsmål skal ha en fasit
- spørsmålene skal være relevante for fagteksten
- quiz-data skal kunne behandles av programmet

---

## Story 2.2 – Svare på quiz

Som student  
vil jeg kunne svare på quizspørsmålene  
slik at jeg kan teste min egen forståelse.

### Akseptansekriterier

- alle fem spørsmål skal vises
- brukeren skal kunne velge eller skrive svar
- svarene skal lagres midlertidig mens quiz-en gjennomføres
- brukeren skal kunne sende inn quiz-en

---

## Story 2.3 – Rette quiz

Som student  
vil jeg få vite hvilke svar som er riktige og feil  
slik at jeg kan lære av resultatet.

### Akseptansekriterier

- brukerens svar sammenlignes med fasiten
- riktig svar gir poeng
- feil svar gir ikke poeng
- korrekt svar vises dersom brukeren svarer feil
- rettingen skal gjøres av vanlig Python-logikk, ikke av KI

---

## Story 2.4 – Vise poengsum

Som student  
vil jeg se poengsummen min etter quiz-en  
slik at jeg kan vurdere hvor godt jeg kan fagstoffet.

### Akseptansekriterier

- resultatet skal vise antall riktige av fem
- poengsummen skal beregnes korrekt
- resultatet skal vises tydelig
- poengsummen skal kunne lagres

---

# Epic 3 – Lagring av notater

## Story 3.1 – Lagre notat

Som student  
vil jeg kunne lagre arbeidet mitt  
slik at jeg kan komme tilbake til det senere.

### Akseptansekriterier

Et lagret notat skal kunne inneholde:

- tittel
- original fagtekst
- sammendrag
- forklaring
- quiz
- quizresultat

Data skal lagres lokalt.

---

## Story 3.2 – Se lagrede notater

Som student  
vil jeg kunne se en liste over tidligere notater  
slik at jeg raskt finner tidligere arbeid.

### Akseptansekriterier

- lagrede notater skal vises i en liste
- hvert notat skal ha en tydelig tittel
- brukeren skal kunne velge et notat

---

## Story 3.3 – Åpne tidligere notat

Som student  
vil jeg kunne åpne et tidligere lagret notat  
slik at jeg kan repetere tidligere fagstoff.

### Akseptansekriterier

- original tekst skal kunne vises
- sammendrag skal kunne vises
- quizresultat skal kunne vises
- data skal fortsatt finnes etter at appen har blitt startet på nytt

---

# Epic 4 – Feilhåndtering og sikkerhet

## Story 4.1 – Håndtere Gemini-feil

Som bruker  
vil jeg få en forståelig melding dersom KI-tjenesten ikke fungerer  
slik at jeg vet hva som har skjedd.

### Akseptansekriterier

Appen skal håndtere:

- manglende API-nøkkel
- ugyldig API-nøkkel
- utilgjengelig Gemini API
- ugyldig KI-respons

Appen skal ikke krasje.

---

## Story 4.2 – Beskytte API-nøkkel

Som utvikler  
vil jeg holde API-nøkkelen utenfor GitHub  
slik at hemmelig informasjon ikke blir offentlig.

### Akseptansekriterier

- `.env` skal ligge i `.gitignore`
- ingen ekte nøkkel skal ligge i kildekoden
- `.env.example` skal vise hvordan variabelen settes opp

---

# Epic 5 – Testing

## Story 5.1 – Teste poengberegning

Som utvikler  
vil jeg teste quizpoeng automatisk  
slik at jeg vet at riktig og feil svar behandles korrekt.

### Akseptansekriterier

- riktig svar gir riktig poeng
- feil svar gir null poeng
- totalscore beregnes korrekt
- testen kan kjøres uten Gemini API

---

## Story 5.2 – Teste lagring

Som utvikler  
vil jeg teste lagring og lasting av notater  
slik at brukerdata ikke forsvinner.

### Akseptansekriterier

- et notat kan lagres
- samme notat kan hentes igjen
- relevante felt beholdes
- testene kan kjøres lokalt

---

# Epic 6 – Kjørbarhet for sensor

## Story 6.1 – Requirements

Som sensor  
vil jeg kunne installere nødvendige Python-pakker  
slik at appen kan kjøres lokalt.

### Akseptansekriterier

- repositoryet inneholder `requirements.txt`
- filen inneholder alle nødvendige pakker

---

## Story 6.2 – Miljøkonfigurasjon

Som sensor  
vil jeg forstå hvordan API-nøkkelen konfigureres  
slik at jeg kan teste KI-funksjonene.

### Akseptansekriterier

- repositoryet inneholder `.env.example`
- README forklarer hvordan Gemini-nøkkel opprettes
- ingen ekte API-nøkkel ligger i repositoryet

---

## Story 6.3 – README

Som sensor  
vil jeg kunne følge en enkel oppskrift for å starte Moldiz  
slik at prosjektet kan vurderes.

### Akseptansekriterier

README skal forklare:

1. hvordan repositoryet klones
2. hvordan avhengigheter installeres
3. hvordan `.env` opprettes
4. hvordan Gemini API-nøkkel legges inn
5. hvordan appen startes
6. hvordan tester kjøres

---

# Prioritering

## Må være med i v1

- Story 1.1
- Story 1.2
- Story 1.3
- Story 2.1
- Story 2.2
- Story 2.3
- Story 2.4
- Story 3.1
- Story 3.2
- Story 3.3
- Story 4.1
- Story 4.2
- Story 5.1
- Story 5.2
- Story 6.1
- Story 6.2
- Story 6.3

---

# Foreslått implementeringsrekkefølge

1. Strukturere prosjektet i moduler
2. Flytte eksisterende Gemini-kall til `ai_service.py`
3. Lage enklere forklaring
4. Lage quizgenerering
5. Lage quizretting og poeng
6. Lage SQLite-lagring
7. Lage visning av tidligere notater
8. Lage tester
9. Lage `.env.example`
10. Lage `requirements.txt`
11. Oppdatere README
12. Gjennomføre slutt-testing

---

# Sporbarhet mot PRD

| Story | PRD-krav |
|---|---|
| 1.1 | FR-1 |
| 1.2 | FR-2 |
| 1.3 | FR-3 |
| 2.1 | FR-4 |
| 2.2 | FR-5 |
| 2.3 | FR-6 |
| 2.4 | FR-7 |
| 3.1 | FR-8 |
| 3.2–3.3 | FR-9 |
| 4.1 | NFR-3 |
| 4.2 | NFR-4 |
| 6.1–6.3 | NFR-5 |

Denne koblingen gjør det mulig å følge kravene fra PRD til implementasjon og testing.
