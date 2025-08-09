import json

def ouvrir_inventaire(path="data/inventaire.json"):
    with open(path, 'r', encoding='utf-8') as fichier:
        inventaire = json.load(fichier)
    return inventaire


def ecrire_inventaire(inventaire, path="data/inventaire.json"):
    with open(path, 'w', encoding='utf-8') as fichier:
        json.dump(inventaire, fichier, ensure_ascii=False, indent=4)


def ouvrir_tresorerie(path="data/tresorerie.txt"):
    with open(path, 'r', encoding="utf-8") as fichier:
        tresorerie = json.load(fichier)
    return tresorerie


def ecrire_tresorerie(tresorerie, path="data/tresorerie.txt"):
    with open(path, 'w', encoding='utf-8') as fichier:
        json.dump(tresorerie, fichier, ensure_ascii=False, indent=4)


def afficher_tresorerie(tresorerie):
    print(f"\n Tresorerie actuelle: {tresorerie:.2f} $")        


def afficher_inventaire(inventaire): 
    print("Inventaire actuel de la plantation:")
    for fruits, quantite in inventaire.items():
        print(f"- {fruits.capitalize()} : {quantite} unites")
  
        
def recolter(inventaire, fruit, quantite):
    inventaire[fruit] = inventaire.get(fruit,0) + quantite # r returns the value for the specified key if the key exists in the dictionary
    print(f"\n Recolte {quantite} {fruit} supplementaire")


def vendre(inventaire, fruit, quantite, tresorerie):
    if inventaire.get(fruit, 0) >= quantite:
        inventaire[fruit] -= quantite
        tresorerie += 1 * quantite
        print(f"\n Vendue {quantite} {fruit} !")
        return (inventaire, tresorerie)
    else:
        print(f"Pas assez de {fruit} pour vendre {quantite} unites.")


if __name__ == "__main__":
    inventaire = ouvrir_inventaire()
    tresorerie = ouvrir_tresorerie()
    afficher_inventaire(inventaire)
    afficher_tresorerie(tresorerie)
    
    recolter(inventaire, "bananes", 10)
    inventaire, tresorerie = vendre(inventaire, "bananes", 5, tresorerie)
    
    ecrire_inventaire(inventaire)
    ecrire_tresorerie(tresorerie)
    