import streamlit as st
import pandas as pd
from collections import Counter

# Konfiguracja strony (dodaje ikonkę w karcie przeglądarki)
st.set_page_config(page_title="Magazyn", page_icon="🙂")

# Tytuł z uśmieszkiem
st.title("📦 Prosty Magazyn z wykresem 🙂")
st.write("Witaj! Zarządzaj swoim towarem z uśmiechem.")

# 1. Inicjalizacja listy w pamięci sesji
if 'magazyn' not in st.session_state:
    st.session_state.magazyn = []

# --- SEKCJA DODAWANIA ---
st.subheader("Dodaj nowy towar")
col1, col2 = st.columns([3, 1])

with col1:
    nowy_towar = st.text_input("Nazwa towaru", label_visibility="collapsed", placeholder="np. Jabłko")

with col2:
    dodaj_btn = st.button("Dodaj ➕", type="primary")

if dodaj_btn:
    if nowy_towar:
        # Dodajemy towar do listy
        st.session_state.magazyn.append(nowy_towar)
        st.success(f"Dodano: {nowy_towar} 😉")
    else:
        st.warning("Musisz wpisać nazwę! 😐")

st.divider()

# --- SEKCJA STATYSTYK I WYKRESU ---
st.subheader("📊 Statystyki i Wykres")

if len(st.session_state.magazyn) > 0:
    # Zliczamy wystąpienia towarów (np. {'Jabłko': 2, 'Banany': 1})
    licznik = Counter(st.session_state.magazyn)
    
    # Tworzymy DataFrame dla wykresu
    df = pd.DataFrame.from_dict(licznik, orient='index', columns=['Ilość'])
    
    # Wyświetlamy wykres słupkowy
    st.bar_chart(df)
    
    st.caption("Powyższy wykres pokazuje ilość sztuk każdego towaru.")

else:
    st.info("Magazyn jest pusty. Wykres pojawi się po dodaniu towarów.")

st.divider()

# --- SEKCJA USUWANIA ---
st.subheader("Stan Magazynu i Usuwanie")

if len(st.session_state.magazyn) > 0:
    # Wyświetlenie surowej listy
    st.write(f"Wszystkie elementy na liście: {st.session_state.magazyn}")

    # Wybór do usunięcia
    towar_do_usuniecia = st.selectbox("Co chcesz usunąć?", options=list(set(st.session_state.magazyn)))
    
    if st.button("Usuń jedną sztukę 🗑️"):
        if towar_do_usuniecia in st.session_state.magazyn:
            st.session_state.magazyn.remove(towar_do_usuniecia)
            st.success("Usunięto! 👋")
            st.rerun()
else:
    st.write("Tu na razie jest pusto... 🦗")
