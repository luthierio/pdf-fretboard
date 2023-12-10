import subprocess
import sys

commande = "python fretboard.py"

start = 600
end   = 700

if len(sys.argv) == 3:
  start = int(sys.argv[1])
  end = int(sys.argv[2])

# Boucle à travers la plage de 300 à 800
for parametre in range(start, end+1):
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

    # time.sleep(1)

