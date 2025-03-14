#########Code Moritz#############################
leistungstests = []            #leere List erstellen

first_experiment_id = input("Zahl, wo Leistungstest beginnen soll: ")         #first_experiment_id per user input definieren

try:
    first_experiment_id : int = int(first_experiment_id)                     #Überprüfen ob es sich bei first_experiment_id um einen intatcher handelt

    for i in range(10):                                                    #Zehn Leistungstests erstellen
        test = {
            "Versuchsleiter": "Moritz",
            "Erstelldatum": "14.03.2025",
            "id_nummer": i+int(first_experiment_id)
        }
        leistungstests.append(test)                       #Leistungstests in Liste hinzufügen

    for test in leistungstests[:5]:                     #ersten 5 Leistungstests ausgeben
        print(test)
            
    print("Experimente mit gerader id:",sum(1 for test in leistungstests if test["id_nummer"] % 2 == 0))       #Ausgeben, Anzahl Leistungstests mit gerader id

except ValueError:                                                 #Fehler ausgeben, falls first_experiment_id kein intatcher ist, um Absturz zu verhinern
    print("Fehler: Bitte gib eine gültige ganze Zahl ein.")
