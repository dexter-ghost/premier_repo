nombre1 = "10"
nombre2 = "8"

# Vérifier si nombre1 est numérique
if not nombre1.isnumeric():
    raise SystemExit("Fin du programme")

# Vérifier si nombre2 est numérique
if not nombre2.isnumeric():
    raise SystemExit("Fin du programme")

# Si on arrive ici, c'est que les deux sont numériques
print("Les deux valeurs sont numériques !")

nombre1 = int(nombre1)
nombre2 = int(nombre2)

test = 0