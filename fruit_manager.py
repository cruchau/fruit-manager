inventaire = {
    "bananes":120, 
    "mangues":85,
    "ananas":45,
    "noix de coco":60,
    "papayes":30,

}


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
    