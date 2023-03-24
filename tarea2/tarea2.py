import csv

def import_data():
    archivo = input("Ingrese el nombre del archivo:")
    # Pasar datos a una lista de diccionarios por fila
    dictListStr = []
    with open(archivo, newline='') as data:
        fileRead = csv.DictReader(data, delimiter=';')

        for row in fileRead:
            dictListStr.append(row)

    #T ransformar los siguientes strings a ints para facilitar el trabajo
    listInts = ['Nro. RegiÃ³n', 'Circ. Senatorial', 'Distrito', 'Nro. Mesa', 'Electores', 'Nro. en Voto', 'Votos TRICEL'] 
    j = 0
    dictList = []
    for i in dictListStr:
        dictRow = dictListStr[j] 
        
        for key in dictRow: 
            if key in listInts:
                dictRow[key] = int(dictRow[key])
            else:
                continue
        j += 1

        dictList.append(dictRow)
              
    return dictList


def export_tables_by_region(data, filename):
    # Crea un diccionario vacio
    dictRegions = {}

    # Cuenta las veces que aparece cada región y lo añade al diccionario
    for dict in data:
        region = dict['RegiÃ³n']
        
        if region not in dictRegions:
            dictRegions[region] = 1
        elif region in dictRegions:
            dictRegions[region] += 1
            

    # Genera y escribe en el archivo csv 
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=' ')

        for key, value in dictRegions.items():
            valueFinal = int(value/4) #dividido en 4 para calzar con los candidatos
            text = (key + ';', valueFinal) 
            writer.writerow(text)


def export_general_results(data, filename):
    # Basicamente la misma funcion que la anterior pero utilizando candidatos.

    # Crea un diccionario vacio
    dictCandidato = {}

    # Por cada aparicion de un candidato se suma la cantidad de votos respectivos.
    for dict in data:
        candidato = dict['Candidato']
        votos = dict['Votos TRICEL']
        
        if candidato not in dictCandidato:
            dictCandidato[candidato] = votos
        elif candidato in dictCandidato:
            dictCandidato[candidato] += votos
            
    # Genera y escribe en el archivo csv 
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=' ')

        for key, value in dictCandidato.items():
            text = (key + ';', value)
            writer.writerow(text)


def export_count_by_local(data, filename):
    # Generamos lista vacia
    listLocal = []
    local = input("Ingrese el nombre del local:")

    # Ciclo que llena la lista anterior con los diccionarios solo del local dado
    j = 0
    for i in data:
        row = data[j]
        if local not in row['Local']:
            j += 1
        elif local in row['Local']:
            listLocal.append(row)
            j += 1

    # Finalmente utilizamos la lista obtenida en export_general_results
    export_general_results(listLocal, filename)


main = import_data()

export_count_by_local(main, 'output,csv')






    


        