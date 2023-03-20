#!/usr/bin/env python3

# ---------Fonction devis livre Atelier-----------#
def calcul_prix(produit, quantite, pages):
	
	base_A4 = [0.4, 0.3, 0.2, 0.15, 0.12]

	_80gr = [0.2, 0.2, 0.1, 0.1, 0.1]
	_90gr = [0.2, 0.2, 0.1, 0.1, 0.1]

	rv_quadri = [2.5, 4, 5, 6, 7]
	rv_nb = [3, 4, 5, 6, 7]


# nombres de pages du livre

# Déclaration de la variable prix unitaire
	prix_unitaire = [0, 0, 0, 0]
	
# Tableau des coéficiants de tarifs en fonction du A4
	coef=[0.3,0.4,0.5,1,2]

# on détermine le coef en fonction du format
	coefP=0
	if "A4" in str(produit):
		coefP = coef[3]
	elif "A5" in str(produit):
		coefP = coef[2]
	elif "A6" in str(produit):
		coefP = coef[1]

# on détermine la valeur du tableau quantité de pages	
	Quantite_pages = quantite * pages

	Qt1p = 0
	if Quantite_pages <= 51:
		Qt1p = 0
	elif Quantite_pages <= 101:
		Qt1p = 1
	elif Quantite_pages <= 251:
		Qt1p = 2
	elif Quantite_pages <= 501:
		Qt1p = 3
	else:
		Qt1p = 4	

# on détermine la valeur du tableau quantité pour les autres éléments	

		Qt1 = 0
	if quantite <= 1:
		Qt1 = 0
	elif quantite <= 10:
		Qt1 = 1
	elif quantite <= 20:
		Qt1 = 2
	elif quantite <= 30:
		Qt1 = 3
	else:
		Qt1 = 4	

# Conditions qui vont déterminer les éléments de calcul du prix unitaire	

# Attribut formats

	if "A4" in str(produit):
		prix_unitaire[0] = base_A4[Qt1p]*Quantite_pages
	elif "A5" in str(produit):
		prix_unitaire[0] = base_A4[Qt1p]*Quantite_pages
	elif "A6" in str(produit):
		prix_unitaire[0] = base_A4[Qt1p]*Quantite_pages
	else:
		prix_unitaire[0] = 0

	# Attribut support
		
	if "80gr" in str(produit):
		prix_unitaire[1] = (_80gr[Qt1p]*coefP)*Quantite_pages
	elif "90gr" in str(produit):
		prix_unitaire[1] = (_90gr[Qt1p]*coefP)*Quantite_pages
	elif "135gr" in str(produit):
		prix_unitaire[1] = (_135gr[Qt1p]*coefP)*Quantite_pages


	if "300gr" in str(produit):
		prix_unitaire[2] = _300gr[Qt1]*coefP
	elif "350gr" in str(produit):
		prix_unitaire[2] = _350gr[Qt1]*coefP
	else:
		prix_unitaire[2] = 0

	# Attribut type d'impression
		
	if "recto/verso" in str(produit) and "quadri" in str(produit):
		prix_unitaire[3] = rv_quadri[Qt1]
	else:
		prix_unitaire[3] = 0

	# Attribut finition


		
	#somme de tous les prix unitaitaires qui va remplacer la valeur du prix unitaire dans odoo

	prix_uni = sum(prix_unitaire)
	
	return prix_uni

def mise_en_forme(produit):
    # Chercher le produit entre les parenthèses
    start_index = produit.find("(")
    end_index = produit.find(")")
    if start_index == -1 or end_index == -1:
        # Si les parenthèses ne sont pas trouvées, retourner le produit inchangé
        return produit
    contenu_parentheses = produit[start_index+1:end_index]

    # Diviser le contenu entre les parenthèses en une liste de mots
    mots = contenu_parentheses.split(", ")

    # Récupérer les valeurs des différents paramètres
    format = ""
    impression = ""
    support = ""
    for mot in mots:
        if "Format" in mot:
            format = mot.replace("Format", "").strip()
        elif "Impression" in mot:
            impression = mot.replace("Impression", "").strip()
        elif "Support" in mot:
            support = mot.replace("Support", "").strip()

    # Remplacer le produit initial par le produit formaté
    produit_formate = "{}\nFormat : {}\nImpression : {}\nSupport : {}".format(produit[:start_index].strip(), format, impression, support)
    return produit_formate
#-----------------------Fin

#-----------------Fonction devis GF---------------------#

# Le code ci-dessous fait une boucle for pour récupérer les variables dont on a besoins
# prix est la ligne qui va récupérer le résultat de la fonction calcul_prix

for record in self:
	if record.x_studio_val_fontion == 0:
		produit = record['name']
		pages = record['x_studio_nbr_pages']
		quantite = int(record['product_uom_qty'])
		prix = calcul_prix(produit, quantite,pages)
		nomt = mise_en_forme(produit)
		record['price_unit'] = prix
		record['name'] = nomt
	else:
		record['x_studio_remise_suggrer_1'] = 1

