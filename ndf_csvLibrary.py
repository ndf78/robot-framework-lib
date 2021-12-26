import csv

def lister_noms_feuilles(chemin):  # Indique le "chemin" comme dans l'exemple suivant : C:\\Users\\hdf-msi\\Robot Framework\\Robot Excel\\lapin
    fichier_excel = xlrd.open_workbook(chemin)
    feuille = fichier_excel.sheet_names()
    msg = feuille
    resultat_log = print(msg)
    return resultat_log

    def read_csv_file(self, name, target):
        data = []
        with open(name, 'rt') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            for row in reader:
                data.append(row)
            nbligne = len(data)
            for i in range(nbligne):
                a = data[i]
                # print(a)
                if target in a == True:
                    find = a
                else:
                    print(a)
            search = a      #data[31]
        return target in search

