import os
import json

# --- SCRIPT AUTOMATIQUE ---
# Il cherche le notebook tout seul dans le dossier courant ou dans "notebooks"

print("🔍 Recherche du fichier notebook...")

# Liste des endroits où chercher
chemins_possibles = [
    "01_FineTuning_Pipeline.ipynb",              # Si à la racine
    "notebooks/01_FineTuning_Pipeline.ipynb",    # Si dans le dossier notebooks
    "notebooks\\01_FineTuning_Pipeline.ipynb"    # Variante Windows
]

fichier_trouve = None

for chemin in chemins_possibles:
    if os.path.exists(chemin):
        fichier_trouve = chemin
        break

if not fichier_trouve:
    # Recherche manuelle large si les noms exacts ne marchent pas
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(".ipynb") and "checkpoint" not in file:
                fichier_trouve = os.path.join(root, file)
                break
        if fichier_trouve: break

if fichier_trouve:
    print(f"✅ Fichier trouvé : {fichier_trouve}")
    
    try:
        with open(fichier_trouve, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Correction
        if 'metadata' in data and 'widgets' in data['metadata']:
            del data['metadata']['widgets']
            print("🔧 Section 'widgets' supprimée avec succès !")
            
            with open(fichier_trouve, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=1)
            print("💾 Fichier sauvegardé et propre.")
        else:
            print("ℹ️ Le fichier est déjà propre (pas de widgets trouvés).")
            
    except Exception as e:
        print(f"❌ Erreur lors de la lecture du fichier : {e}")
else:
    print("❌ IMPOSSIBLE de trouver le fichier .ipynb. Vérifiez qu'il est bien dans le dossier.")