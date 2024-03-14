import os

def supprimer_dossiers_vides(chemin):
    for dossier in os.listdir(chemin):
        chemin_complet = os.path.join(chemin, dossier)
        if os.path.isdir(chemin_complet):
            try:
                if not os.listdir(chemin_complet):
                    os.rmdir(chemin_complet)
                    print(f"Dossier vide supprimé : {chemin_complet}")
                else:
                    supprimer_dossiers_vides(chemin_complet)
            except Exception as e:
                print(f"Erreur lors de la suppression du dossier {chemin_complet} : {e}")

# Remplacez 'chemin_dossier' par le chemin absolu du dossier que vous souhaitez nettoyer
chemin_dossier = "/Users/youcef-badjadi/Pictures"
supprimer_dossiers_vides(chemin_dossier)



