# Architecture – Moldiz

## 1. Formål

Dette dokumentet beskriver den tekniske arkitekturen for Moldiz.

Moldiz er en KI-basert studieassistent bygget med Python og Streamlit. Applikasjonen skal kunne:

- ta imot fagtekst
- lage sammendrag
- forklare fagstoff enklere
- generere quiz
- rette quiz
- beregne poeng
- lagre notater og quizresultater
- åpne tidligere lagret arbeid

Arkitekturen skal være enkel nok for prosjektets omfang, men strukturert slik at funksjonene kan testes og videreutvikles.

---

## 2. Arkitekturprinsipper

Prosjektet skal følge disse prinsippene:

- enkel struktur
- tydelig separasjon mellom brukergrensesnitt, logikk, KI og lagring
- hemmelige API-nøkler skal ikke ligge i repositoryet
- funksjoner som poengberegning skal være testbare uten KI
- feil fra eksterne API-er skal håndteres uten at appen krasjer
- koden skal være lett å forstå for gruppen og sensor

---

## 3. Teknologistakk

### Programmeringsspråk

Python

### Brukergrensesnitt

Streamlit

### KI-tjeneste

Google Gemini API

### Lagring

SQLite anbefales for v1.

SQLite er valgt fordi:

- databasen lagres lokalt
- ingen ekstern databaseserver er nødvendig
- Python har god støtte for SQLite
- data kan bevares mellom oppstarter
- det passer godt til et lite studentprosjekt

### Testing

pytest

### Versjonskontroll

Git og GitHub

---

## 4. Overordnet arkitektur

Applikasjonen deles inn i fire hoveddeler:

1. User Interface
2. Application Logic
3. AI Service
4. Data Storage

Flyten er:

Bruker  
→ Streamlit UI  
→ applikasjonslogikk  
→ Gemini API eller lokal logikk  
→ SQLite  
→ resultat tilbake til bruker

---

## 5. Foreslått prosjektstruktur

```text
G57-siyar-ulle/
│
├── app.py
├── requirements.txt
├── .env
├── .env.example
├── .gitignore
├── README.md
│
├── docs/
│   ├── product-brief.md
│   ├── prd.md
│   ├── architecture.md
│   └── stories.md
│
├── moldiz/
│   ├── __init__.py
│   ├── ai_service.py
│   ├── quiz_service.py
│   ├── storage.py
│   └── models.py
│
└── tests/
    ├── test_quiz.py
    └── test_storage.py
