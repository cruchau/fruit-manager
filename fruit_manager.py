import json
import os

DATA_DIR = "data"
PRIX_PATH = os.path.join(DATA_DIR, "prix.json")
INVENTAIRE_PATH = os.path.join(DATA_DIR, "inventaire.json")
TRESORERIE_PATH = os.path.join(DATA_DIR, "tresorerie.txt")

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
        with open(path, 'r', encoding='utf-8') as fichier:
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
    inventaire[fruit] = inventaire.get(fruit,0) + quantite # r returns the value for the specified key if the key exists in the dictionary
    print(f"\n🍂 Recolte {quantite} {fruit} supplementaire")


def vendre(inventaire, fruit, quantite, tresorerie, prix):
    if inventaire.get(fruit, 0) >= quantite:
        inventaire[fruit] -= quantite
        tresorerie += prix.get(fruit, 0) * quantite
        print(f"\n Vendue {quantite} {fruit} !")
        return (inventaire, tresorerie)
    else:
        print(f"Pas assez de {fruit} pour vendre {quantite} unites.")
        

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
    