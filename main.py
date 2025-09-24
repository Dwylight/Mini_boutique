import boutique

chaussure = boutique.Product("Air Force 1", 10000, 5)
parfum = boutique.Product("Touch", 500, 10 )
parfum_luxe = boutique.Product("Givenchy", 20000, 2)
pommade = boutique.Product("Vaseline", 3500, 3)
creme_solaire = boutique.Product("Eucerin", 15000, 4)
sac = boutique.Product("Hermès", 30000, 1)

produits_disponibles = {
    "Air Force 1": chaussure,
    "Touch": parfum,
    "Givenchy": parfum_luxe,
    "Vaseline": pommade,
    "Eucerin": creme_solaire,
    "Hermès": sac
}

def main():
    panier = boutique.Cart()

    print("Bienvenue dans la boutique en ligne DAMY SHOP")
    print()
    print("Voici la lste de nos articles: ")
    boutique.afficher_tous_les_produits()
    print()
    while True:
        print("--- MENU ---")
        print("1. Ajouter un article au panier")
        print("2. Retirer un article du panier")
        print("3. Voir le coût total du panier")
        print("4. Vérifier le stock d'un article")
        print("5. Valider le panier")
        print("6. Quitter")
        print()

        choix = input("Quel est votre choix?")
        print()

        if choix == "1":
            nom_produit = input("Entrez le nom exact de l'article")
            if nom_produit in produits_disponibles:
                produit = produits_disponibles[nom_produit]
                panier.ajouter_produit(produit)
            else:
                print("Cet article n'existe pas!")
        elif choix == "2":
            nom_article = input("Entrez le nom exact de l'article à retirer")
            if nom_article in produits_disponibles:
                article_a_retirer = produits_disponibles[nom_article]
                panier.retirer_produit(article_a_retirer)
        elif choix == "3":
            if panier == []:
                print("Vous n'avez aucun article dans votre panier")
            else:
                prix = panier.calculer_total()
                print(f"Le prx total du panier est {prix} FCFA")
        elif choix == "4":
            nom_produit = input("Entrez le nom exact de l'article")
            if nom_produit in produits_disponibles:
                produit = produits_disponibles[nom_produit]
                if produit.verifier_stock():
                    print(f"il reste {produit.stock} articles {produit.nom} en stock")
                else:
                    prix(f"Le stock {produit.nom} est epuisé")
        elif choix == "5":
            confirmation = input("Confirmer le paiement?(o/n)")
            if confirmation.lower() == "o":
                print("DAMY SHOP vous remercie pour votre achat")
                break
            else:
                print("Paiement non effectué")
        elif choix == "6":
            break
        else:
            print("Veuillez entrer un numéro valide!")

if __name__ == "__main__":
    main()


    



        









    