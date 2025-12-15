import streamlit as st

# Tytuł aplikacji
st.title("📦 Prosty Magazyn w Streamlit")

# 1. Inicjalizacja listy w pamięci sesji (session_state)
# Dzięki temu lista nie resetuje się przy każdym kliknięciu przycisku
if 'magazyn' not in st.session_state:
    st.session_state.magazyn = []

# --- SEKJA DODAWANIA ---
st.header("Dodaj nowy towar")
col1, col2 = st.columns([3, 1])

with col1:
    # Pole tekstowe do wpisania nazwy
    nowy_towar = st.text_input("Nazwa towaru", label_visibility="collapsed", placeholder="Wpisz nazwę...")

with col2:
    # Przycisk dodawania
    dodaj_btn = st.button("Dodaj", type="primary")

if dodaj_btn:
    if nowy_towar:
        st.session_state.magazyn.append(nowy_towar)
        st.success(f"Dodano: {nowy_towar}")
    else:
        st.warning("Nazwa towaru nie może być pusta!")

st.divider()

# --- SEKCJA LISTY I USUWANIA ---
st.header("Stan Magazynu")

if len(st.session_state.magazyn) > 0:
    # Wyświetlanie listy
    st.write(f"Liczba produktów: **{len(st.session_state.magazyn)}**")
    
    # Tworzymy dataframe (tabelę) dla ładniejszego wyglądu, lub prostą listę
    st.dataframe(st.session_state.magazyn, column_config={0: "Nazwa Towaru"}, use_container_width=True)

    st.subheader("Usuń towar")
    # Wybór towaru do usunięcia z listy rozwijanej
    towar_do_usuniecia = st.selectbox("Wybierz towar do usunięcia", st.session_state.magazyn)
    
    if st.button("Usuń wybrany towar"):
        if towar_do_usuniecia in st.session_state.magazyn:
            st.session_state.magazyn.remove(towar_do_usuniecia)
            st.success("Usunięto towar!")
            st.rerun() # Odświeża aplikację, aby zaktualizować listę natychmiast
else:
    st.info("Magazyn jest pusty. Dodaj pierwsze produkty powyżej.")

# Stopka
st.markdown("---")
st.caption("Prosty system magazynowy działający na listach Python.")
