import json
import os
from datetime import datetime

DATA_DIR = "data"
PRIX_PATH = os.path.join(DATA_DIR, "prix.json")
INVENTAIRE_PATH = os.path.join(DATA_DIR, "inventaire.json")
TRESORERIE_PATH = os.path.join(DATA_DIR, "tresorerie.txt")


def enregistrer_tresorerie_historique(tresorerie, path="data/tresorerie_history.json"):
    historique = []
    if os.path.exists(path):
        with open(path, 'r') as f:
            try:
                historique = json.load(f)
            except:
                historique = []
    historique.append({"timestamp": datetime.now().isoformat(), "tresorerie": tresorerie})
    with open(path, 'w') as f:
        json.dump(historique, f)

def lire_tresorerie_historique(path="data/tresorerie_history.json"):
    if os.path.exists(path):
        with open(path, 'r') as f:
            try:
                return json.load(f)
            except:
                return []
    return []


def ouvrir_prix(path=PRIX_PATH):
    os.makedirs(DATA_DIR, exist_ok=True)
    if not os.path.exists(path):
        prix_defaut = {
            "bananes": 2,
            "mangues": 7,
            "ananas": 5,
            "noix de coco": 4,
            "papayes": 3
        }
        with open(path, 'w', encoding='utf-8') as fichier:
            json.dump(prix_defaut, fichier, ensure_ascii=False, indent=4)
    with open(path, 'r', encoding='utf-8') as fichier:
        return json.load(fichier)


def ouvrir_inventaire(path=INVENTAIRE_PATH):
    os.makedirs(DATA_DIR, exist_ok=True)
    if not os.path.exists(path):
        inventaire_defaut = {
            "bananes": 120,
            "mangues": 85,
            "ananas": 45,
            "noix de coco": 60,
            "papayes": 30
        }
        with open(path, 'w', encoding='utf-8') as fichier:
            json.dump(inventaire_defaut, fichier, ensure_ascii=False, indent=4)
    with open(path, 'r', encoding='utf-8') as fichier:
        return json.load(fichier)
    


def ecrire_inventaire(inventaire, path="data/inventaire.json"):
    with open(path, 'w', encoding='utf-8') as fichier:
        json.dump(inventaire, fichier, ensure_ascii=False, indent=4)


def ouvrir_tresorerie(path=TRESORERIE_PATH):
    os.makedirs(DATA_DIR, exist_ok=True)
    if not os.path.exists(path):
        tresorerie_initiale = 1000.0
        with open(path, 'w', encoding='utf-8') as fichier:
            json.dump(tresorerie_initiale, fichier, ensure_ascii=False, indent=4)
    with open(path, 'r', encoding="utf-8") as fichier:
        return json.load(fichier)
    


def ecrire_tresorerie(tresorerie, path="data/tresorerie.txt"):
    with open(path, 'w', encoding='utf-8') as fichier:
        json.dump(tresorerie, fichier, ensure_ascii=False, indent=4)


def afficher_tresorerie(tresorerie):
    print(f"\n💰 Tresorerie actuelle: {tresorerie:.2f} $")        


def afficher_inventaire(inventaire): 
    print("🍓 Inventaire actuel de la plantation:")
    for fruits, quantite in inventaire.items():
        print(f"- {fruits.capitalize()} : {quantite} unites")
  
        
def recolter(inventaire, fruit, quantite):
    try:
        # Validate input inventory
        if inventaire is None:
            inventaire = ouvrir_inventaire()  # Charger l'inventaire existant au lieu d'en créer un nouveau vide
            
        if not isinstance(inventaire, dict):
            print("Warning: inventaire was not a dictionary")
            inventaire = ouvrir_inventaire()
            
        # Update inventory
        inventaire[fruit] = inventaire.get(fruit, 0) + quantite
        
        # Save immediately after update
        ecrire_inventaire(inventaire)
        print(f"\n🍂 Recolte {quantite} {fruit} supplementaire")
        
        # Debug print
        print("Updated inventory:", inventaire)
        
        return inventaire    
        
    except Exception as e:
        print(f"Erreur lors de la récolte: {e}")
        return ouvrir_inventaire()  # Retourner l'inventaire existant en cas d'erreur



def vendre(inventaire, fruit, quantite, tresorerie, prix):
    if inventaire.get(fruit, 0) >= quantite:
        inventaire[fruit] -= quantite
        tresorerie += prix.get(fruit, 0) * quantite
        message = {'status': 'success', 'text': f"\n Vendu {quantite} {fruit} !"}
        enregistrer_tresorerie_historique(tresorerie)
        print(f"\n Vendue {quantite} {fruit} !")
        return inventaire, tresorerie  # Retourner seulement inventaire et tresorerie
    else:
        message = {'status': 'error', 'text': f"\n Pas assez de {fruit} pour en vendre {quantite} !"}
        return inventaire, tresorerie  # Retourner les valeurs inchangées

        

def vendre_tout(inventaire, tresorerie, prix):
    print("\n🛒 Vente de tout l'inventaire :")
    for fruit, quantite in list(inventaire.items()):
        if quantite > 0:
            revenu = prix.get(fruit, 0) * quantite
            tresorerie += revenu
            print(f"- {fruit.capitalize()} : vendu {quantite} unites pour {revenu:.2f} $")
            inventaire[fruit] = 0
    return inventaire, tresorerie


def valeur_stock(inventaire, prix):
    valeur = {}
    for fruit in inventaire:
        quantite = inventaire[fruit]
        prix_unitaire = prix.get(fruit, 0)
        valeur[fruit] = quantite * prix_unitaire
    return valeur

def dollar_to_euro(tresorerie, taux_conversion=0.85):
    tresorerie_euro = tresorerie * taux_conversion
    return tresorerie_euro


if __name__ == "__main__":
    inventaire = ouvrir_inventaire()
    tresorerie = ouvrir_tresorerie()
    prix = ouvrir_prix()
    
    afficher_inventaire(inventaire)
    afficher_tresorerie(tresorerie)
    
    recolter(inventaire, "bananes", 10)
    inventaire, tresorerie = vendre(inventaire, "bananes", 5, tresorerie, prix)
    
    ecrire_inventaire(inventaire)
    ecrire_tresorerie(tresorerie)
    