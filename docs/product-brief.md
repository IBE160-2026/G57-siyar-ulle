# Product Brief – Moldiz

## Gruppe

G57 – Siyar og Ulle

## Executive Summary

Moldiz er en KI-basert studieassistent som skal hjelpe studenter med å forstå, repetere og teste seg selv på fagstoff.

Brukeren kan lime inn fagtekst eller egne notater. Moldiz bruker kunstig intelligens til å lage sammendrag, forklare vanskelig fagstoff på en enklere måte og generere quizspørsmål.

I første versjon skal brukeren også kunne gjennomføre en quiz, få svarene rettet, se poengsummen sin og lagre tidligere notater med tilhørende sammendrag og quizresultater.

Målet er å samle flere nyttige studieaktiviteter i én enkel applikasjon.

---

## The Problem

Studenter må ofte lese store mengder pensum, forelesningsnotater og annet fagstoff.

En typisk situasjon kan være en student som skal repetere et kapittel før en prøve eller eksamen. Studenten må først finne de viktigste delene av teksten, lage et sammendrag, forstå vanskelige konsepter og deretter lage spørsmål for å teste seg selv.

Dette tar tid og kan være vanskelig å gjøre systematisk.

Eksisterende KI-verktøy kan hjelpe med enkelte av disse oppgavene, men studenten må ofte selv formulere gode prompts, organisere svarene og holde oversikt over tidligere arbeid.

Moldiz skal gjøre denne arbeidsflyten enklere og mer strukturert.

---

## Who This Serves

### Primærbruker

Den viktigste brukeren er en student på høyskole eller universitet som skal repetere fagstoff før en prøve, innlevering eller eksamen.

Brukeren ønsker å kunne:

- få et raskt sammendrag av fagstoff
- få vanskelige konsepter forklart enklere
- teste seg selv med quiz
- få umiddelbar tilbakemelding på svar
- se poengsum
- lagre tidligere notater og resultater
- komme tilbake til tidligere fagstoff senere

---

## The Solution

Moldiz skal ha en enkel arbeidsflyt.

### 1. Legge inn fagtekst

Brukeren skriver eller limer inn fagtekst i applikasjonen.

### 2. Lage sammendrag

KI analyserer teksten og lager et kort sammendrag med de viktigste punktene.

### 3. Forklare fagstoff

Brukeren kan be Moldiz forklare teksten eller vanskelige begreper på en enklere måte.

### 4. Lage quiz

Moldiz genererer en quiz basert på fagteksten.

Quiz-en skal i første versjon bestå av for eksempel fem spørsmål.

### 5. Rette quiz og vise poeng

Brukeren svarer på spørsmålene.

Moldiz sammenligner svarene med fasiten og viser:

- hvilke svar som var riktige
- hvilke svar som var feil
- korrekt svar
- samlet poengsum

### 6. Lagre tidligere arbeid

Brukeren skal kunne lagre tidligere notater med:

- original fagtekst eller tittel
- sammendrag
- quiz
- quizresultat

Brukeren skal senere kunne åpne dette igjen.

---

## What Makes This Different

Moldiz konkurrerer ikke med store generelle KI-verktøy som ChatGPT, Quizlet eller NotebookLM når det gjelder antall funksjoner.

Forskjellen er at Moldiz skal være laget for én bestemt og enkel studieprosess.

I stedet for at brukeren selv må skrive prompts og organisere svarene, skal Moldiz gi en fast arbeidsflyt:

**fagtekst → sammendrag → forklaring → quiz → retting → poeng → lagring**

Moldiz skal derfor være enklere å bruke for en student som bare ønsker å repetere fagstoff uten å måtte lære hvordan man bruker et generelt KI-verktøy effektivt.

Fordelen skal være enkelhet, struktur og fokus på aktiv læring.

---

## Version 1 Scope

Følgende funksjoner skal være med i første fungerende versjon:

### Fagtekst

- brukeren kan skrive eller lime inn tekst
- applikasjonen skal håndtere vanlige fagtekster på norsk

### Sammendrag

- KI lager et kort sammendrag
- sammendraget skal fremheve de viktigste punktene

### Enkel forklaring

- KI kan forklare fagstoffet med enklere språk

### Quiz

- KI genererer fem spørsmål basert på teksten
- spørsmålene skal ha en tydelig fasit

### Quizretting

- brukeren kan svare på spørsmålene
- svarene blir rettet
- brukeren får vite hvilke svar som var riktige og feil
- brukeren får en poengsum

### Lagring

- brukeren kan lagre et notat
- lagrede notater skal kunne inneholde sammendrag og quizresultat
- brukeren skal kunne åpne tidligere lagrede notater

---

## Out of Scope for Version 1

Følgende funksjoner er ikke nødvendige i første versjon:

- brukerkonto og innlogging
- deling mellom flere brukere
- mobilapp
- betaling
- avansert statistikk
- samarbeid mellom studenter
- automatisk synkronisering mellom enheter

Disse funksjonene kan vurderes senere dersom prosjektet får tid og behov.

---

## Success Criteria

Version 1 regnes som vellykket dersom følgende kan demonstreres og testes:

1. Brukeren kan lime inn en fagtekst og få et sammendrag.
2. Brukeren kan få fagteksten forklart med enklere språk.
3. Brukeren kan generere en quiz med fem spørsmål.
4. Quiz-en inneholder svar eller fasit som kan brukes til retting.
5. Brukeren kan svare på spørsmålene og få vite hvilke svar som er riktige og feil.
6. Brukeren kan se en samlet poengsum etter quiz-en.
7. Brukeren kan lagre minst ett notat med sammendrag og quizresultat.
8. Et lagret notat kan åpnes igjen senere.
9. Appen gir en forståelig feilmelding dersom KI-tjenesten ikke er tilgjengelig.
10. En ny bruker kan starte applikasjonen ved å følge README-en.

---

## Quality and Testing Goals

Prosjektet skal ha tester for funksjonalitet som kan kontrolleres uten å stole på KI-svaret alene.

Dette gjelder spesielt:

- beregning av quizpoeng
- kontroll av riktige og feil svar
- lagring av notater
- lasting av tidligere notater
- håndtering av tom tekst
- håndtering av feil fra KI-API-et

KI-genererte svar skal også vurderes manuelt på noen utvalgte fagtekster for å se om sammendrag og spørsmål er relevante.

---

## AI Usage

KI er en sentral del av løsningen.

Gemini API brukes til:

- sammendrag
- enklere forklaringer
- generering av quizspørsmål og fasit

API-nøkkelen skal ikke ligge i GitHub-repositoryet.

Den lagres lokalt i `.env`.

Prosjektet skal ha en `.env.example` som viser hvilken variabel brukeren må opprette uten å inneholde en ekte API-nøkkel.

Det skal også vurderes en testmodus eller mock-data slik at deler av applikasjonen kan demonstreres selv om Gemini API ikke er tilgjengelig.

---

## Technology

Vi planlegger å bruke:

- Python
- Streamlit
- Gemini API
- Git og GitHub
- enkel lokal lagring, for eksempel JSON eller SQLite
- pytest eller tilsvarende for testing

Python brukes til hovedlogikken.

Streamlit brukes til brukergrensesnittet.

Gemini brukes til KI-funksjonene.

Lagringsløsningen skal holdes enkel slik at prosjektet ikke blir unødvendig komplisert.

---

## User Experience

Moldiz skal være enkel å forstå uten forklaring.

En typisk brukerflyt skal være:

1. Åpne Moldiz.
2. Lime inn fagtekst.
3. Velge sammendrag eller forklaring.
4. Generere quiz.
5. Gjennomføre quiz.
6. Se resultat og poeng.
7. Lagre notatet og resultatet.
8. Åpne tidligere notater senere.

Brukeren skal ikke måtte skrive egne KI-prompts.

---

## Risks and Limitations

### KI kan gi feil svar

Språkmodellen kan lage sammendrag eller spørsmål som inneholder feil.

Derfor skal appen informere brukeren om at KI-generert innhold bør kontrolleres mot originalteksten.

### Ekstern API-tjeneste

Gemini kan være utilgjengelig eller ha begrensninger.

Applikasjonen må håndtere dette uten å krasje.

### API-nøkkel

Sensor og andre brukere vil ikke ha tilgang til gruppens API-nøkkel.

README skal derfor forklare hvordan man oppretter og konfigurerer en egen nøkkel.

---

## Future Vision

Når første versjon er stabil og testet, kan Moldiz videreutvikles med:

- PDF-opplasting
- flashcards
- flere typer quiz
- valg av vanskelighetsgrad
- automatisk genererte læringsplaner
- statistikk over quizresultater
- støtte for flere språk
- eksport av sammendrag og flashcards

PDF-opplasting eller flashcards vil være naturlige kandidater til neste utviklingstrinn etter v1.

---

## Project Goal

Målet med Moldiz er å utvikle en enkel, fungerende og testbar KI-basert studieassistent.

Prosjektet skal samtidig dokumentere hele utviklingsprosessen fra:

**Product Brief → PRD → Architecture → Epics and Stories → Implementation → Testing**

På denne måten skal det være mulig å følge kravene fra den første planen og helt frem til den ferdige funksjonaliteten.
