import xlrd

def lister_noms_feuilles(chemin):  # Indique le "chemin" comme dans l'exemple suivant : C:\\Users\\hdf-msi\\Robot Framework\\Robot Excel\\lapin
    fichier_excel = xlrd.open_workbook(chemin)
    feuille = fichier_excel.sheet_names()
    msg = feuille
    resultat_log = print(msg)
    return resultat_log

def Rechercher_information_nom_feuille(chemin, nom_de_feuille, recherche):  # Indique le "chemin" comme dans l'exemple suivant : C:\\Users\\hdf-msi\\Robot Framework\\Robot Excel\\lapin
    fichier_excel = xlrd.open_workbook(chemin)
    feuille = fichier_excel.sheet_by_name(nom_de_feuille)
    nb_ligne_feuille = feuille.nrows
    for i in range(nb_ligne_feuille):
        filtre_ligne_excel = str(feuille.row(i)).replace("text:'", "").replace("empty:''", "").replace(", ", "").replace("[", "").replace("]", "").split("'")
        liste_ligne_excel = list(filter(None, filtre_ligne_excel))
        verif = recherche in liste_ligne_excel
        print(liste_ligne_excel)
    msg = verif
    resultat_log = print(msg)
    return resultat_log

def Rechercher_information_index_feuille(chemin, index_de_feuille, recherche):  # Indique le "chemin" comme dans l'exemple suivant : C:\\Users\\hdf-msi\\Robot Framework\\Robot Excel\\lapin
    fichier_excel = xlrd.open_workbook(chemin)
    feuille = fichier_excel.sheet_by_index(index_de_feuille)
    nb_ligne_feuille = feuille.nrows
    for i in range(nb_ligne_feuille):
        filtre_ligne_excel = str(feuille.row(i)).replace("text:'", "").replace("empty:''", "").replace(", ", "").replace("[", "").replace("]", "").split("'")
        liste_ligne_excel = list(filter(None, filtre_ligne_excel))
        verif = recherche in liste_ligne_excel
        print(liste_ligne_excel)
    msg = verif
    resultat_log = print(msg)
    return resultat_log
