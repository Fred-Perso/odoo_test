#!/usr/bin/env python3

# Fonction de calcul du prix unitaire dans odoo
def calcul_prix(produit, quantite):
	
	A4 = [0.4, 0.3, 0.2, 0.15, 0.12]
	_135gr = [0.2, 0.2, 0.1, 0.1, 0.1]
	_170gr = [3, 4, 5, 6, 7]
	recto = [3, 4, 5, 6, 7]
	quantites = [1,10, 20, 30, 40]
	
	prix_unitaire = [0, 0, 0]
	
# Tableau des coefs
	coef=[0.5,1,2]

# on détermine le coef en fonction du format
	coefP=0
	if "A4" in str(produit):
		coefP = coef[1]
	elif "A3" in str(produit):
		coefP = coef[2]
	elif "A5" in str(produit):
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

	if "A4" in str(produit):
		prix_unitaire[0] = A4[Qt1]*coefP
	elif "A5" in str(produit):
		prix_unitaire[0] = A4[Qt1]*coefP
	elif "A3" in str(produit):
		prix_unitaire[0] = A4[Qt1]*coefP
	else:
		prix_unitaire[0] = 0
		
	if "135gr" in str(produit):
		prix_unitaire[1] = _135gr[Qt1]*coefP
	elif "150gr" in str(produit):
		prix_unitaire[1] = _170gr[Qt1]*coefP
	else:
		prix_unitaire[1] = 0
		
	if "recto" in str(produit):
		prix_unitaire[2] = recto[Qt1]*coefP
	else:
		prix_unitaire[0] = 0
		
	#somme de tout les prix unitaitaires qui va. remplacer la valeur du prix unitaire dans odoo

	prix_uni = sum(prix_unitaire)
	
	return prix_uni

for record in self:
	produit = record['name']
	quantite = int(record['product_uom_qty'])
	prix = calcul_prix(produit, quantite)
	record['x_studio_test'] = prix