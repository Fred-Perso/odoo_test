# Fonction de calcul du prix unitaire en fonction de la surface dans odoo

def calcul_prix_GF(produit,quantite,longueur,largeur):
	
	surface1 = ((longueur*largeur)/10000)*quantite
	surface = ((longueur*largeur)/10000)
	
	
	_150gr_satin = [16, 14, 12,11]
	_80gr_plan = [12, 10, 5,4]
	_Vinyle_monomere_dos_gris = [40,25, 20, 18, 16]
	_Vinyle_monomere_dos_blanc = [45,25, 20, 18, 16]
	_Vinyle_polymere_dos_gris = [30, 25, 20,18]
	_Vinyle_polyomere_dos_blanc = [30, 25, 20,18]
	_Bache_440gr = [28, 25, 20,18]
	_Bache_510gr = [28, 25, 20,18]

	_unite = [1.5, 1.3, 1, 0.6, 0.5]
	_michair = [1.5, 1.3, 1, 0.6, 0.5]
	_monomere = [15, 10, 1, 0.6, 0.5]
	_polymere = [20, 12, 1, 0.6, 0.5]

# Déclaration de la variable prix unitaire
	prix_unitaire = [0, 0, 0]
	
# on détermine le degressif surface à appliquer aux différents attributs en fonction de la surface totale de la ligne de commande
	Qt1 = 0
	if surface1 <= 0.5:
		Qt1 = 0
	elif surface1 <= 1:
		Qt1 = 1
	elif surface1 <= 5:
		Qt1 = 2
	elif surface1 <= 10:
		Qt1 = 3
	elif surface1 <= 300:
		Qt1 = 4
	else:
		Qt1 = 4	
		
# calcul du prix unitaire en fonction des éléments des différentes variables de surface
# le but étant de convertir une tarification à la surface en un affichage de vente à l'unité 

	# Attribut support
	if "80gr" in str(produit):
		prix_unitaire[0] = _80gr_plan[Qt1]*surface
	elif "150gr" in str(produit):
		prix_unitaire[0] = _150gr_satin[Qt1]*surface
	elif "Mono" in str(produit):
		prix_unitaire[0] = _Vinyle_monomere_dos_gris[Qt1]*surface
	else:
		prix_unitaire[0] = 0

	# Attribut de decoupe	
	if "unité" in str(produit):
		prix_unitaire[1] = _unite[Qt1]*surface
	elif "mi-chair" in str(produit):
		prix_unitaire[1] = _michair[Qt1]*surface
	else:
		prix_unitaire[1] = 0

	# Attribut finition
	if "Monom" in str(produit):
		prix_unitaire[2] = _monomere[Qt1]*surface
	elif "Poly" in str(produit):
		prix_unitaire[2] = _polymere[Qt1]*surface
	else:
		prix_unitaire[2] = 0


	# Sur le grand format, le problème va se poser sur les petites QT des petits stickers, c'est un problème qui était présent sur le site 
	# par exemple 100 sticker de 3 cm on est en dessous de 8 euros. il faudra ajouter une ligne au devis pour les frais de calage.
	# somme de tous les prix unitaitaires qui va remplacer la valeur du prix unitaire dans odoo
	prix_uni = sum(prix_unitaire)
	
	return prix_uni


def mise_en_forme_GF(produit,longueur, largeur):
    # Chercher le produit entre les parenthèses
    start_index = produit.find("(")
    end_index = produit.find(")")
    if start_index == -1 or end_index == -1:
		
        return produit
        
    contenu_parentheses = produit[start_index+1:end_index]
    
    # Diviser le contenu entre les parenthèses en une liste de mots
    mots = contenu_parentheses.split(", ")

    # Récupérer les valeurs des différents paramètres
    
    support = ""
    lamination = ""
    decoupe = ""
    for mot in mots:
        
        if "Support" in mot:
            support = mot.replace("Support", "").strip()
        elif "Lamination" in mot:
            lamination = mot.replace("Lamination", "").strip()
        elif "Découpe" in mot:
            decoupe = mot.replace("Découpe", "").strip()

    # Remplacer le produit initial par le produit formaté - la taille en cm ds le champ name sera renseignée manuellement
    produit_formate = "{}\nTaille en cm :\nSupport :{}\nLamination : {}\nDécoupe : {}".format(produit[:start_index].strip(),support, lamination, decoupe)
    
    return produit_formate
    

# Le code ci-dessous fait une boucle for pour récupérer les variables dont on a besoins
# prix est la ligne qui va récupérer le résultat de la fonction calcul_prix

for record in self:
	if record.x_studio_val_fontion == 0:
		produit = record['name']
		quantite = int(record['x_studio_qtu'])
		longueur = record['x_studio_bord_long']
		largeur = record['x_studio_bord_court']
		prix = calcul_prix_GF(produit,quantite,longueur,largeur)
		nomt = mise_en_forme_GF(produit,longueur, largeur)
		record['price_unit'] = prix
		record['name'] = nomt
	else:
		record['x_studio_remise_suggrer_1'] = 1