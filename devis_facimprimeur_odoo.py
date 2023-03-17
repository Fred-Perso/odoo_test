#!/usr/bin/env python3

# Fonction de calcul du prix unitaire dans odoo
# Cette fonction reçois 2 arguments (valeurs) qui récupèrent depuis odoo le nom du produit et la quantité
def calcul_prix(produit, quantite):
	
	base_A4 = [0.4, 0.3, 0.2, 0.15, 0.12]

	_80gr = [0.2, 0.2, 0.1, 0.1, 0.1]
	_90gr = [0.2, 0.2, 0.1, 0.1, 0.1]
	_135gr = [0.2, 0.2, 0.1, 0.1, 0.1]
	_170gr = [0.2, 0.2, 0.1, 0.1, 0.1]
	_200gr = [0.2, 0.2, 0.1, 0.1, 0.1]
	_250gr = [0.2, 0.2, 0.1, 0.1, 0.1]
	_300gr = [0.2, 0.2, 0.1, 0.1, 0.1]
	_350gr = [0.2, 0.2, 0.1, 0.1, 0.1]

	recto_quadri = [1.5, 4, 5, 6, 7]
	rv_quadri = [2.5, 4, 5, 6, 7]
	recto_nb = [3, 4, 5, 6, 7]
	rv_nb = [3, 4, 5, 6, 7]

# Déclaration de la variable prix unitaire
	prix_unitaire = [0, 0, 0]
	
# Tableau des coéficiants de tarifs en fonction du A4
	coef=[0.3,0.4,0.5,1,2]

# on détermine le coef en fonction du format
	coefP=0
	if "A4" in str(produit):
		coefP = coef[3]
	elif "A3" in str(produit):
		coefP = coef[4]
	elif "A5" in str(produit):
		coefP = coef[2]
	elif "A6" in str(produit):
		coefP = coef[1]
	elif "10x21" in str(produit):
		coefP = coef[0]

# on détermine la valeur du tableau quantité	
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

	if "A3" in str(produit):
		prix_unitaire[0] = base_A4[Qt1]
	elif "A4" in str(produit):
		prix_unitaire[0] = base_A4[Qt1]
	elif "A5" in str(produit):
		prix_unitaire[0] = base_A4[Qt1]
	elif "A6" in str(produit):
		prix_unitaire[0] = base_A4[Qt1]
	elif "10x21" in str(produit):
		prix_unitaire[0] = base_A4[Qt1]
	else:
		prix_unitaire[0] = 0

	# Attribut support
		
	if "80gr" in str(produit):
		prix_unitaire[1] = _80gr[Qt1]*coefP
	elif "90gr" in str(produit):
		prix_unitaire[1] = _90gr[Qt1]*coefP
	elif "135gr" in str(produit):
		prix_unitaire[1] = _135gr[Qt1]*coefP
	elif "170gr" in str(produit):
		prix_unitaire[1] = _170gr[Qt1]*coefP
	elif "200gr" in str(produit):
		prix_unitaire[1] = _200gr[Qt1]*coefP
	elif "250gr" in str(produit):
		prix_unitaire[1] = _250gr[Qt1]*coefP
	elif "300gr" in str(produit):
		prix_unitaire[1] = _300gr[Qt1]*coefP
	elif "350gr" in str(produit):
		prix_unitaire[1] = _350gr[Qt1]*coefP
	else:
		prix_unitaire[1] = 0

	# Attribut type d'impression
		
	if "recto" in str(produit) and "quadri" in str(produit):
		prix_unitaire[2] = recto_quadri[Qt1]
	else:
		prix_unitaire[0] = 0

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


# Le code ci-dessous fait une boucle for pour récupérer les variables dont on a besoins
# prix est la ligne qui va récupérer le résultat de la fonction calcul_prix

for record in self:
	if record.x_studio_val_fontion == 0:
		produit = record['name']
		quantite = int(record['product_uom_qty'])
		prix = calcul_prix(produit, quantite)
		nomt = mise_en_forme(produit)
		record['price_unit'] = prix
		record['name'] = nomt
	else:
		record['x_studio_remise_suggrer_1'] = 1

