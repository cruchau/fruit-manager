import streamlit as st
import matplotlib.pyplot as plt
from fruit_manager import *
import matplotlib.dates as mdates
import pandas as pd

st.title("🍇 Dashboard de la plantation")

inventaire = ouvrir_inventaire()
tresorerie = ouvrir_tresorerie()
prix = ouvrir_prix()

with st.sidebar:
    st.header("🛒 Vendre des Fruits")
    fruit_vendre = st.selectbox("Choisissez un fruit", list(inventaire.keys()))
    quantite_vendre = st.number_input("Quantité à vendre", min_value=1, step=1)
    
    if st.button("Vendre"):
        inventaire, tresorerie = vendre(inventaire, fruit_vendre, quantite_vendre, tresorerie, prix)
    
    st.header("🌾 Récolter des Fruits")
    fruit_recolter = st.selectbox("Choisissez un fruit à récolter", list(inventaire.keys()), key="recolter")
    quantite_recolter = st.number_input("Quantité à récolter", min_value=1, step=1, key="quantite_recolter")
    
    if st.button("Récolter"):
        inventaire = recolter(inventaire, fruit_recolter, quantite_recolter)
        if inventaire:  # Vérifier que l'inventaire est valide
            ecrire_inventaire(inventaire)
        else:
            st.error("Erreur lors de la récolte")

        
st.header("💰 Tresorerie")
st.metric(label="Montant disponible", value=f"{tresorerie:.2f} $")

st.header("📈 Evolution de la tresorerie")
historique = lire_tresorerie_historique()
if historique:

    df = pd.DataFrame(historique).tail(20)
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df = df.sort_values("timestamp")

    fig, ax = plt.subplots()
    ax.plot(df["timestamp"], df["tresorerie"], marker="o")
    ax.set_xlabel("Date")
    ax.set_ylabel("Tresorerie ($)")
    ax.set_title("Evolution de la tresorerie")
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m %H:%M'))
    fig.autofmt_xdate()
    _, mid_col, _ = st.columns([1,2,1])
    mid_col.pyplot(fig)
else:
    st.info("Aucune donnee d'historique de la tresorerie pour le moment.")

st.header("📦 Inventaire")
# Inventaire sous forme de tableau
st.table(inventaire)
# Inventaire sous forme de graphique
fig, ax = plt.subplots()
# Trier l'inventaire par quantite decroissante
inventaire = dict(sorted(inventaire.items(), key=lambda item: item[1], reverse=True))
ax.bar(inventaire.keys(), inventaire.values(), edgecolor='k')
ax.set_xlabel("Fruits")
ax.set_ylabel("Quantité")
ax.set_title("Inventaire des Fruits")
st.pyplot(fig)


ecrire_inventaire(inventaire)
ecrire_tresorerie(tresorerie)

