import json

def ouvrir_inventaire(path="inventaire.json"):
    with open(path, 'r', encoding='utf-8') as fichier:
        inventaire = json.load(fichier)
    return inventaire

def ecrire_inventaire(inventaire, path="inventaire.json"):
    with open(path, 'w', encoding='utf-8') as fichier:
        json.dump(inventaire, fichier, ensure_ascii=False, indent=4)
        

def afficher_inventaire(inventaire): 
    print("Inventaire actuel de la plantation:")
    for fruits, quantite in inventaire.items():
        print(f"- {fruits.capitalize()} : {quantite} unites")
  
        
def recolter(inventaire, fruit, quantite):
    inventaire[fruit] = inventaire.get(fruit,0) + quantite # r returns the value for the specified key if the key exists in the dictionary
    print(f"\n Recolte {quantite} {fruit} supplementaire")


def vendre(inventaire, fruit, quantite):
    if inventaire.get(fruit, 0) >= quantite:
        inventaire[fruit] -= quantite
        print(f"\n Vendue {quantite} {fruit} !")
    else:
        print(f"Pas assez de {fruit} pour vendre {quantite} unites.")


if __name__ == "__main__":
    afficher_inventaire(inventaire)
    recolter(inventaire, "bananes", 10)
    vendre(inventaire, "bananes", 5)
    afficher_inventaire(inventaire)
    