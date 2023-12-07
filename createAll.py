import subprocess

# Spécifiez la commande que vous souhaitez exécuter
commande = "python fretboard.py"

# Spécifiez le nombre d'itérations
nombre_iterations = 10  # Vous pouvez ajuster le nombre selon vos besoins

# Boucle à travers la plage de 300 à 800
for parametre in range(300, 801):
    # Construit la commande complète en ajoutant le paramètre
    commande_complete = f"{commande} {parametre}"

    # Exécute la commande
    try:
        subprocess.run(commande_complete, shell=True, check=True)
        print(f"Commande exécutée avec succès avec le paramètre {parametre}")
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'exécution de la commande avec le paramètre {parametre}: {e}")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")

    # Pause facultative entre les itérations
    # Vous pouvez ajuster cette valeur en fonction de vos besoins
    # time.sleep(1)

