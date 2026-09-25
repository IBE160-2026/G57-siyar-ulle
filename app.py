import streamlit as st
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client()

st.set_page_config(page_title="Moldiz", page_icon="📚")

st.title("📚 Moldiz")
st.subheader("KI-basert studieassistent")

st.write(
    "Lim inn fagtekst eller notater under. "
    "Moldiz kan lage et sammendrag ved hjelp av KI."
)

tekst = st.text_area(
    "Skriv eller lim inn tekst:",
    height=250
)

if st.button("Lag sammendrag"):
    if not tekst.strip():
        st.warning("Du må skrive inn tekst først.")
    else:
        with st.spinner("Lager sammendrag..."):
            try:
                response = client.models.generate_content(
                    model="gemini-3.5-flash-lite",
                    contents=(
                        "Lag et kort og lett forståelig sammendrag på norsk "
                        "av teksten nedenfor. Ta med de viktigste punktene.\n\n"
                        + tekst
                    ),
                )

                st.subheader("Sammendrag")
                st.write(response.text)

            except Exception as e:
                st.error(f"Noe gikk galt: {e}")