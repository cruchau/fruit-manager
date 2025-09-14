# 🥝 Fruit Manager

Bienvenue sur **Fruit Manager**, un tableau de bord interactif pour gerer votre plantation de fruit ! Ce projet, developpe avec streamlit, vous permet de suivre votre inventaire, vendre et recolter des fruits, et surveiller votre tresorerie en temps reel.

## 🛠️ Installation 

Creation de l'environnement virtuel
``` bash
poetry install
```

Lancez votre projet avec poetry:
``` bash
poetry run streamlit run app.py
```

## 🚀 Fonctionnalite

- **Vendre des fruits**: Selectionnez un fruit, indiquez la quantite a vendre et mettez a jour votre tresorerie automatiquement.
- **Recolte**: Ajoutez facilement de nouveaux fruits a votre inventaire apres chaque recolte
-**Suivi de la tresorerie**: Visualisez le montant disponible apres chaque operations.


## 📂 Structure du projet

- app.py : Interface principale streamlit
- fruit_manager.py : Fonctions de gestion de l'inventaire, des ventes, des recoltes et de la tresorerie.
- `data/` : Fichiers de donnees (inventaire, prix du marche, tresorerie).


## 🌟 Exemple d'utilisation

- Accedez a l'interface web generee par streamlit
- Utilisez la barre laterale pour vendre ou recolter des fruits.
- Consultez l'inventaire et la tresorerie mis a jour en temps reel. 


---

**Bonnes recoltes et bonnes ventes !**
🥭🍈🍉
