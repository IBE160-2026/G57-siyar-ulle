# Product Brief – Moldiz

**Gruppe:** G57 – G57-siyar-ulle  
**Gruppemedlemmer:** Siyar og Ulle  
**Revidert:** 7. oktober 2026, på bakgrunn av faglærerens tilbakemelding.

## Executive Summary – produktidé

Moldiz er en KI-basert studieassistent for studenter som vil repetere egne fagtekster. Studenten limer inn et utdrag, får et kort sammendrag og en enkel forklaring, gjennomfører en quiz og lagrer notatet med resultater til senere repetisjon. Første versjon skal ha en komplett og testbar studieøkt, med quizretting og lokal lagring som egen funksjonalitet.

Dette dokumentet er revidert etter delene faglæreren etterspør i BMAD. Det er ikke et bevis på at `bmad-product-brief` er kjørt. Gruppen må gjennomføre og dokumentere den faktiske BMAD-flyten før videre funksjonsutvikling.

## The Problem – konkret brukssituasjon

En IT-student ved Høgskolen i Molde skal repetere et kapittel før en prøve. Studenten har forelesningsnotater, men bruker mye tid på å finne hovedpunktene og lage spørsmål. Å lese et sammendrag viser heller ikke om studenten faktisk har forstått stoffet. Notater og øvingsresultater blir lett spredt over ulike verktøy.

Behovet er en enkel arbeidsflyt for å forstå et avgrenset tekstutdrag, teste egen forståelse og finne igjen samme økt senere. Dette er en problemhypotese som skal undersøkes med studenttester, ikke et dokumentert funn fra brukerintervjuer.

## Who This Serves – primærbruker

Primærbrukeren er en bachelorstudent i IT og digitalisering ved HiMolde som repeterer norske fagnotater før en prøve. Studenten kan lime inn digital tekst, men ønsker å slippe å utforme egne KI-prompts og rette flervalgsspørsmål manuelt.

Andre studenter kan bruke løsningen, men v1 utformes for denne primærbrukeren. Det finnes én brukertype og ingen innlogging i v1.

## The Solution – brukeropplevelse

1. Studenten skriver en tittel og limer inn fagtekst.
2. Studenten velger «Lag studieøkt» og får sammendrag, en enkel forklaring og fem flervalgsspørsmål basert på teksten.
3. Sammendrag og forklaring vises først. Quizfasiten skjules til svarene er levert.
4. Studenten besvarer alle spørsmål og leverer quizen. Appen viser antall riktige, prosent, fasit og en kort forklaring til hvert svar.
5. Studenten lagrer økten. En oversikt over tidligere notater lar studenten åpne tekst, generert innhold og quizresultater igjen eller slette et notat.

Grensesnittet skal ha tydelige områder for tekst, sammendrag/forklaring, quiz og tidligere notater. Feil og venting vises der handlingen skjer. Teksten beholdes dersom generering mislykkes.

## What Makes This Different – ærlig vurdering

ChatGPT, Quizlet og NotebookLM er relevante eksisterende alternativer. Vi har ikke dokumentert at Moldiz gir bedre KI-svar eller har unike funksjoner sammenlignet med disse verktøyene.

Moldiz sin foreslåtte verdi er en avgrenset, norsk studieøkt med faste steg: egen tekst, sammendrag, forklaring, fem spørsmål, automatisk retting og lokal historikk. Studenten trenger ikke skrive en prompt eller beregne poeng selv. Om målgruppen foretrekker denne flyten, skal undersøkes i brukertesting. Prosjektet konkurrerer på enkel arbeidsflyt, ikke på en egen eller bedre språkmodell.

## Scope – første versjon (v1)

| ID | Funksjon | Avgrensning |
|---|---|---|
| F1 | Tekstinnlegging | Tittel og innlimt tekst på 100–15 000 tegn etter trimming. Tom tekst avvises. |
| F2 | Sammendrag | Kort norsk sammendrag av hovedpunktene i kildeteksten. |
| F3 | Forklaring | En enklere forklaring av sentrale begreper i samme tekst. |
| F4 | Quiz med retting og poeng | Nøyaktig fem spørsmål med fire alternativer og ett riktig svar per spørsmål. Ett poeng per riktig svar, ingen minuspoeng. Resultat 0–5 og 0–100 %. Alle spørsmål må besvares før levering. Fasit vises først etter levering. |
| F5 | Lagring og historikk | Lokal lagring av tittel, originaltekst, sammendrag, forklaring, quiz og quizforsøk med tidspunkt og resultat. Åpne og slette tidligere notater. Nye forsøk legges til historikken. |
| F6 | Demo og feilhåndtering | En fast eksempeltekst med ferdige, tydelig merkede svar uten API-nøkkel eller nettverk. KI-feil gir forståelig melding uten å miste teksten. |

Quiz og lagring er obligatoriske deler av v1, ikke valgfrie utvidelser. Generering av spørsmål inngår i quizen; andre spørsmålstyper er utenfor v1.

### Utenfor v1

PDF-opplasting, flashcards, flere språk, justerbar vanskelighetsgrad, innlogging, deling, skysynkronisering og flere brukerroller. Appen skal ikke brukes til sensitive personopplysninger eller som en autoritativ fasit på pensum.

## Success Criteria – testbare mål

Kriteriene under er mål for ferdig v1, ikke påstander om dagens prototype.

| ID | Kriterium | Hvordan det kontrolleres |
|---|---|---|
| S1 | Tekst under 100 eller over 15 000 tegn avvises før API-kall. Gyldig tekst godtas. | Grensetester med 0, 99, 100, 15 000 og 15 001 tegn. |
| S2 | En gyldig studieøkt inneholder sammendrag, forklaring og fem spørsmål med fire alternativer og én gyldig fasit hver. | Test av strukturert utdata. Ugyldig eller ufullstendig KI-svar avvises med mulighet til å prøve igjen. |
| S3 | Quizrettingen gir 0/5 = 0 %, 3/5 = 60 % og 5/5 = 100 %. | Automatiserte tester mot kjent fasit. Ubesvarte spørsmål hindrer levering og fasit er skjult på forhånd. |
| S4 | Et lagret notat og tilhørende quizforsøk finnes igjen etter omstart. Sletting fjerner notatet og forsøkene. | Integrasjonstest med midlertidig database og manuell omstart. |
| S5 | Demo kan gjennomføres uten nøkkel og nettverk, med samme eksempelresultat hver gang. | Test med API-kall blokkert og uten miljøvariabler. |
| S6 | Manglende nøkkel, tjenestefeil og ugyldige svar gir en forståelig melding; innlimt tekst beholdes. | Simulerte feil og manuell kontroll av brukergrensesnittet. |
| S7 | Sammendrag, forklaringer og quiz bygger på kildeteksten. | Gruppen kontrollerer minst tre kjente fagtekster mot en sjekkliste: hovedpunkter, støtte i teksten, tydelige spørsmål og riktig fasit. Avvik dokumenteres og rettes. |
| S8 | Minst tre av fire teststudenter klarer å generere, ta og lagre en studieøkt uten veiledning. | Observerte brukertester med samme oppgave; funn og endringer dokumenteres. |
| S9 | Sensor kan starte appen fra et rent miljø etter README og prøve demo uten gruppens nøkkel. | En annen person følger oppstartsinstruksjonen. |

## Teknologi, KI og personvern

Python og Streamlit beholdes fordi de passer en liten lokal app og gruppens kompetanse. Gemini brukes til tekstbearbeiding. Modellnavn skal kunne konfigureres, og tilgjengelighet kontrolleres ved oppsett. Vi lover ikke at en bestemt modell eller et gratisnivå er tilgjengelig gjennom hele prosjektet.

API-kall skal samles bak én avgrenset funksjon/modul. V1 trenger strukturert quizutdata og validering før visning eller lagring. Quizretting og poeng beregnes i Python, ikke av KI. SQLite foreslås til lokal lagring; endelig datamodell og moduldeling bestemmes i arkitekturen. Foreløpige entiteter er notat, tilhørende generert innhold, quizspørsmål og quizforsøk.

Bare teksten som studenten velger å bearbeide, sendes til KI-tjenesten. Brukeren skal få beskjed om dette før generering. API-nøkkel lagres i `.env` eller lokale secrets og skal aldri legges i repoet, databasen eller feilmeldinger. Notater og resultater lagres lokalt og kan slettes. Lokal v1 forutsetter én bruker per installasjon; en delt installasjon krever ny vurdering av tilgangskontroll.

Demo skal fungere uten kostnad. Levende KI-kall avhenger av egen nøkkel, gjeldende kvoter og prisvilkår. Gruppen skal kontrollere vilkårene, begrense tekstlengde og unngå automatiske kall ved hvert tastetrykk.

## Prosess og sporbarhet

Den opprinnelige `app.py` ble laget før PRD og stories og behandles som en teknisk prototype. Revisjonen gjør prototypen testbar med en fast demo, tydelig konfigurasjon og tryggere feilhåndtering. Quiz, forklaring og lagring er fortsatt planlagt funksjonalitet.

Før nye v1-funksjoner bygges skal gruppen:

1. Gjennomføre `bmad-product-brief` med denne revisjonen som grunnlag og lagre faktisk økt/prompt og resultat.
2. Lage PRD med F1–F6 og S1–S9 som utgangspunkt.
3. Lage arkitektur for KI-integrasjon, validering, lagring, grensesnitt og feil.
4. Lage epics og stories med akseptansekriterier, og koble hver story til krav, kode og tester.
5. Implementere stories med Claude Code etter emnets arbeidsflyt, kontrollere endringer og dokumentere testing og KI-bruk.

Planleggingsdokumentene bør ligge i `docs/planning/`. Gruppen må committe dem i faktisk rekkefølge; dokumentene skal ikke gi inntrykk av at planleggingen skjedde før prototypen.

README, `requirements.txt`, `.env.example` og `.gitignore` skal lages i repoet. README skal beskrive installasjon, `streamlit run app.py`, demo, nøkkeloppsett, modellvalg, datalagring og begrensninger. `.gitignore` skal utelate `.env`, lokale secrets og databasen. Disse støttefilene er ikke vedlagt denne revisjonen av de to filene.

## Vision – videre utvikling

Når v1 er ferdig og testet, er trinn 2 tekstbasert PDF-opplasting eller flashcards, valgt etter brukertestene og tilgjengelig tid. Senere kan språk og vanskelighetsgrad vurderes. Nye funksjoner skal ikke gå på bekostning av stabil quizretting, lagring, kjørbarhet og dokumentert prosess.

## Mål for gruppens læring

Gruppen skal få erfaring med Python, API-integrasjon, strukturert KI-utdata, datalagring, testing, Git/GitHub og brukergrensesnitt. Læringsmålene supplerer produktets målbare suksesskriterier og erstatter dem ikke.
