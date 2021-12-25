import os
import shutil

def creer_dossier(chemin):  # Indique le "chemin" comme dans l'exemple suivant : C:\\Users\\hdf-msi\\Robot Framework\\Robot Excel\\lapin
    os.mkdir(chemin)
    msg = "Dossier crée"
    resultat_log = print(msg)
    return resultat_log

def supprimer_dossier_vide(chemin):  # # Indique le "chemin" comme dans l'exemple suivant : C:\\Users\\hdf-msi\\Robot Framework\\Robot Excel\\lapin
        os.rmdir(chemin)
        msg = "Dossier suprimé"
        resultat_log = print(msg)
    return resultat_log

def supprimer_dossier_non_vide(chemin):  # # Indique le "chemin" comme dans l'exemple suivant : C:\\Users\\hdf-msi\\Robot Framework\\Robot Excel\\lapin
        shutil.rmtree(chemin)
        msg = "Dossier suprimé"
        resultat_log = print(msg)
    return resultat_log

def supprimer_fichier(chemin):  # # Indique le "chemin" comme dans l'exemple suivant : C:\\Users\\hdf-msi\\Robot Framework\\Robot Excel\\lapin
        os.remove(chemin)
        msg = "Fichier suprimé"
        resultat_log = print(msg)
    return resultat_log

def copier_fichier(chemin_fichier_copier, chemin_destination_fichier_copier):  # Indique le "chemin_fichier_copier" et "chemin_destination_fichier_copier" comme dans l'exemple suivant : C:\\Users\\hdf-msi\\Robot Framework\\Robot Excel\\lapin
        source = chemin_fichier_copier
        destination = chemin_destination_fichier_copier
        shutil.copy2(source, destination)   # Pourquoi utiliser la fonction "copy2" ? puisque par rapport aux autres fonction de copie, le "copie2" copie les metadatas
        msg = "Fichier copié"
        resultat_log = print(msg)
    return resultat_log

def copier_dossier(chemin_dossier_copier, chemin_destination_dossier_copier):  # Indique le "chemin_fichier_copier" et "chemin_destination_fichier_copier" comme dans l'exemple suivant : C:\\Users\\hdf-msi\\Robot Framework\\Robot Excel\\lapin
        source = chemin_dossier_copier
        destination = chemin_destination_dossier_copier
        shutil.copytree(source, destination)
        msg = "Dossier copié"
        resultat_log = print(msg)
    return resultat_log

def deplacer_renommer_dossier_fichier(chemin_dossier_copier, chemin_destination_dossier_copier):  # Indique le "chemin_fichier_copier" et "chemin_destination_fichier_copier" comme dans l'exemple suivant : C:\\Users\\hdf-msi\\Robot Framework\\Robot Excel\\lapin
        source = chemin_dossier_copier
        destination = chemin_destination_dossier_copier
        shutil.move(source, destination)
        msg = "Fichier copié"
        resultat_log = print(msg)
    return resultat_log
