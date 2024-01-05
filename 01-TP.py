import random
import statistics

#Donées : 

populations = [
    { "id" : 0, "name" : "Alan" },
    { "id" : 1, "name" : "Albert" },
    { "id" : 2, "name" : "Jhon" },
    { "id" : 3, "name" : "Brice" },
    { "id" : 4, "name" : "Alexendra" },
    { "id" : 5, "name" : "Brad" },
    { "id" : 6, "name" : "Carl" },
    { "id" : 7, "name" : "Dallas" },
    { "id" : 8, "name" : "Dennis" },
    { "id" : 9, "name" : "Edgar" },
    { "id" : 10, "name" : "Erika" },
    { "id" : 11, "name" : "Isaac" },
    { "id" : 12, "name" : "Brice" },
    { "id" : 13, "name" : "Alice" },
    { "id" : 14, "name" : "Sophia" },
    { "id" : 15, "name" : "Rasmus" },
    { "id" : 16, "name" : "Taylor" },
    { "id" : 17, "name" : "Olivia" },
    { "id" : 18, "name" : "Jessica" },
    { "id" : 19, "name" : "Anna" },
    { "id" : 20, "name" : "Samantha" },
    { "id" : 21, "name" : "Grace" },
    { "id" : 22, "name" : "Anna" },
    { "id" : 23, "name" : "Alexis" },
    { "id" : 24, "name" : "Madison" },
    { "id" : 25, "name" : "Nicole" },
    { "id" : 26, "name" : "Amanda" },
    { "id" : 27, "name" : "Haley" }  
]

#Question n°1 : Ajoutez un champ lenChar qui détermine la longueur de chaque nom.
# Ajout du champ lenChar pour chaque élément de la liste populations
for person in populations:
    person['lenChar'] = len(person['name'])

# Affichage des données mises à jour
print(f"Question n°1:")
for person in populations:
    print(person)

#Quesion n°2 : Ajoutez un champ rate, puis respectivement attribuer pour chaque personne, des valeurs aléatoires comprises entre 1 et 100.
# Attribution de valeurs aléatoires pour le champ 'rate' pour chaque personne
for person in populations:
    person['rate'] = random.randint(1, 100)

# Affichage des données mises à jour
print(f"Question n°2:")
for person in populations:
    print(person)

#Question n°3 : Déterminez les 4 personnes qui ont les meilleurs valeurs de rate.
# Trie des personnes par ordre décroissant de rate
trie_populations = sorted(populations, key=lambda x: x['rate'], reverse=True) #Reverse=True pour inversé l'ordre croissant en ordre decroissant

# Sélection des 4 premières personnes ayant les meilleures valeurs de rate
top_4 = trie_populations[:4]

# Affichage des 4 personnes ayant les meilleurs valeurs de rate
print(f"Question n°3:")
for person in top_4:
    print(person)

#Question n°4 : Attribuez une augmentation de 0.1% à chacune des valeurs.
# Augmentation de 0.1% pour chaque valeur de rate
for person in populations:
    newRate =  person['rate'] * 1.001 #Creation d'une nouvelle valeure pour augmenter de 0.1% la valeur de rate de person 
    person['rate'] = round(newRate,2) #On arrondi avec Round la somme obtenue dans newRate

# Affichage des données mises à jour
print(f"Question n°4:")
for person in populations:
    print(person)

#Question n°5 : Créez une fonction qui permet de tirer de manière aléatoire une personne.
def choix_personne_aleatoire(populations):
    return random.choice(populations) #Choix aléatoire d'une personne dans la liste de données de population avec random.choice.

personne_aleatoire = choix_personne_aleatoire(populations)
print(f"Question n°5:")
print(f"Personne choisie de manière aléatoire : {personne_aleatoire}")

#Question n°6 : Ordonnez par ordre croissant dans une liste s de tuples, les personnes en fonction de leur rate respectif.
# Trier les personnes par ordre croissant en fonction de leur rate
trie_croissant_populations = sorted(populations, key=lambda x: x['rate']) #Trie croissant avec sorted.

# Création d'une liste de tuples avec les informations triées
s = [(person['name'], person['rate']) for person in trie_croissant_populations]

# Affichage de la liste de tuples ordonnée par rate croissant
print(f"Question n°6:")
print(f"Liste ordonnée par rate croissant :{s} ")

#Question n°7 : Trouvez la valeur centrale, la valeur centrale partage en 2 la série de valeurs rates ordonnées.
# Obtenir une liste des valeurs de rate

# Calculer la médiane des valeurs de rate
halfLength = int(len(s)/2)
if halfLength % 2:
    median = round(s[halfLength][1],2)
else :
    value1 = s[halfLength][1]
    value2 = s[halfLength+1][1]
    median = round((value1 + value2)/2, 2)

# Affichage de la médiane
print(f"Question n°7:")
print(f"La valeur centrale (médiane) de la série de valeurs rates est : {median}")

#Question n°8 : Partionnez la liste s en quatre parties distinctes. Que représente à votre avis la valeur centrale déterminée dans la question précédente.
# `s` est votre liste de tuples triés contenant les noms et les valeurs `rate`

# Calculer la longueur de la liste `s`
n = len(s) #Taille de la liste s 

# Calculer les indices pour diviser la liste en quartiles
q1_index = n // 4  # Calcule l'indice du premier quartile (Q1) # divise en 4 la longueur de la liste s
q2_index = 2 * q1_index  # Calcule l'indice du deuxième quartile (Q2) # multiplie par 2 le Q1
q3_index = 3 * q1_index  # Calcule l'indice du troisième quartile (Q3) # multiplie par 2 le Q1

# Diviser la liste `s` en quartiles en utilisant les indices calculés
quartile_1 = s[:q1_index]  # Premier quartile (de l'index 0 à Q1) #Selectionne la premiere partie de données
quartile_2 = s[q1_index:q2_index]  # Deuxième quartile (de Q1 à Q2) #Selectionne la 2eme partie des données
quartile_3 = s[q2_index:q3_index]  # Troisième quartile (de Q2 à Q3) # #Selectionne la 3eme partie des données
quartile_4 = s[q3_index:]  # Quatrième quartile (de Q3 jusqu'à la fin) #Selectionne la 4eme partie des données

# Afficher les différentes parties (quartiles)
print(f"Question n°8:")
print("- Premier quartile (Q1) :", quartile_1)
print("- Deuxième quartile (Q2) :", quartile_2)
print("- Troisième quartile (Q3) :", quartile_3)
print("- Quatrième quartile (Q4) :", quartile_4)

#Question n°9 : Concluez sur la répartition de ces valeurs. Que pensez vous de la valeure centrale par rapport a la moyenne (à calculer) de la série de valeur rates.
#Calcul de la moyenne de tous les rates. 
somme_rates = sum(person['rate'] for person in populations) #calcul fait avec sum
#Diviser la somme par la longeur de s
moyenne = somme_rates // len(s)
print(f"Question n°9:")
print(f"La moyenne est : {moyenne}")
print(f"Comparaision entre la médiane et la moyenne est : médiane : {median} / moyenne : {moyenne}")

#Conclusion :
# La médiane divise en deux parts égales une série de valeurs.
# Tandis que la moyenne est la somme de toutes les valeurs, divisée par le nombre de valeurs.