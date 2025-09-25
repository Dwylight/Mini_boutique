class Product:
    tous_les_produits = []

    def __init__(self, nom, prix, stock):
        self.nom = nom
        self.prix = prix
        self.stock = stock
        Product.tous_les_produits.append(self)

    def verifier_stock(self):
        return self.stock > 0

class Cart:
    def __init__(self):
        self.produits = []

    def ajouter_produit(self, produit):
        if produit.verifier_stock():
            self.produits.append(produit)
            produit.stock -= 1
            print(f"{produit.nom} a été ajouté à votre panier")
        else:
            print(f"Le stock de {produit.nom} est épuisé!")

    def retirer_produit(self, produit):
        if produit in self.produits:
            self.produits.remove(produit)
            produit.stock += 1
            print(f"Vous avez retiré {produit.nom} du panier")
        else:
            print(f"{produit.nom} n'est pas dans le panier.")

    def calculer_total(self):
        total = 0
        for produit in self.produits:
            total += produit.prix
        return total
    
    def voir_le_panier(self):
        if not self.produits:
            print("Votre panier est vide.")
        else:
            print("Contenu de votre panier:")
            for produit in self.produits:
                print(f"- {produit.nom} : {produit.prix} FCFA")
    
def afficher_tous_les_produits():
    for produit in Product.tous_les_produits:
        print(f"- {produit.nom}")
    


    





    
        


        