import streamlit as st
import pandas as pd
from collections import Counter

# Konfiguracja strony (dodaje ikonkę w karcie przeglądarki)
st.set_page_config(page_title="Wesoły Magazyn", page_icon="🙂", layout="wide")

# --- PANEL BOCZNY (SIDEBAR) - NASZ "CHŁOP" ---
with st.sidebar:
    st.header("Twój pomocnik magazynowy 👋")
    
    # Używamy markdown # (nagłówków), żeby emojis były duże
    st.markdown("# 👨‍🌾😁") # Uśmiechnięty chłop
    st.markdown("### 👋🖐️6️⃣") # Ręka macha, ręka trzyma 6
    st.markdown("### 🖐️7️⃣") # Druga ręka trzyma 7
    
    st.caption("„Patrz! Mam szóstkę i siódemkę! I macham!”")
    st.divider()
    st.write("Tutaj zarządzasz swoim magazynem z uśmiechem.")

# --- GŁÓWNA CZĘŚĆ STRONY ---

st.title("📦 Prosty Magazyn z wykresem 🙂")

# 1. Inicjalizacja listy w pamięci sesji
if 'magazyn' not in st.session_state:
    st.session_state.magazyn = []

# --- SEKCJA DODAWANIA ---
st.subheader("1. Dodaj nowy towar")
col1, col2 = st.columns([3, 1])

with col1:
    nowy_towar = st.text_input("Nazwa towaru", label_visibility="collapsed", placeholder="np. Jabłko")

with col2:
    dodaj_btn = st.button("Dodaj ➕", type="primary", use_container_width=True)

if dodaj_btn:
    if nowy_towar:
        # Dodajemy towar do listy
        st.session_state.magazyn.append(nowy_towar)
        st.success(f"Dodano: {nowy_towar} 😉")
        st.rerun() # Odświeżamy, żeby od razu zaktualizować wykres
    else:
        st.warning("Musisz wpisać nazwę! 😐")

st.divider()

# Tworzymy dwie kolumny na głównej stronie dla lepszego układu
main_col1, main_col2 = st.columns(2)

with main_col1:
    # --- SEKCJA STATYSTYK I WYKRESU ---
    st.subheader("📊 2. Statystyki i Wykres")

    if len(st.session_state.magazyn) > 0:
        # Zliczamy wystąpienia towarów
        licznik = Counter(st.session_state.magazyn)
        
        # Tworzymy DataFrame dla wykresu
        df = pd.DataFrame.from_dict(licznik, orient='index', columns=['Ilość Sztuk'])
        
        # Wyświetlamy wykres słupkowy
        st.bar_chart(df)
        st.caption("Wykres pokazuje ilość sztuk każdego towaru.")
    else:
        st.info("Magazyn jest pusty. Dodaj towary, aby zobaczyć wykres.")

with main_col2:
    # --- SEKCJA USUWANIA ---
    st.subheader("🗑️ 3. Usuwanie towaru")

    if len(st.session_state.magazyn) > 0:
        st.write(f"Łącznie produktów w magazynie: **{len(st.session_state.magazyn)}**")

        # Lista unikalnych nazw do wyboru w selectboxie
        unikalne_towary = sorted(list(set(st.session_state.magazyn)))
        
        # Wybór do usunięcia
        towar_do_usuniecia = st.selectbox("Wybierz co chcesz usunąć:", options=unikalne_towary)
        
        # Informacja ile sztuk tego konkretnego towaru mamy
        ilosc_tego_towaru = st.session_state.magazyn.count(towar_do_usuniecia)
        st.caption(f"Masz {ilosc_tego_towaru} szt. tego produktu.")

        if st.button(f"Usuń jedną sztukę '{towar_do_usuniecia}' 🚮", type="secondary"):
            if towar_do_usuniecia in st.session_state.magazyn:
                st.session_state.magazyn.remove(towar_do_usuniecia)
                st.success("Usunięto! 👋")
                st.rerun()
    else:
        st.write("Tu na razie jest pusto... 🦗")
        st.write("Skorzystaj z sekcji 1, aby coś dodać.")
