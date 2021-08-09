import csv, re, os
from pathlib import Path


def projectCreator():
    home = str(Path.home())
    name = input("Come lo chiamiamo questo nuovo progetto?")
    partecipants = input("Inserisci i nomi dei partecipanti, separali con la virgola: ")
    partecipants = re.split(",",partecipants)
    
    with open(home+"/"+name+".rmn","w") as file:
        file.write("Transazione,")
        for n in partecipants:
            print(n)
            stringa = n+","
            file.write(stringa)
        file.write("\n")
    print("Progetto creato!")

def projectLookup():
    print("\nHo trovato questi progetti:")
    for file in os.listdir(Path.home()):
        if file.endswith(".rmn"):
            print(file[:-4])
     
def projectAdder(project_name):
    try:
        with open(str(Path.home())+"/"+project_name+".rmn") as file:
            print(f"Progetto {project_name} aperto!")
            reader = csv.reader(file,delimiter=",")
            head = next(reader)
            transactions = []
            for name in head[1:]:
                insertion = input(f"Aggiungi movimento per {name} nella forma <spesa_effettiva;pagamento>")
                transactions.append(insertion)
        print("Inserisco nel progetto!")
        with open(str(Path.home())+"/"+project_name+".rmn","a") as file:
            for t in transactions:
                s = t+","
                file.write(s)
            print("fatto!")

    except Exception as error:
        print("Qualcosa è andato storto",error)


print("\nBenvenuto in LaRomana. Cosa vuoi fare oggi?")
while True:
    print('''

new - Crea nuovo progetto
see - Vedi i progetti attivi
add <name> - Aggiungi movimenti al progetto <name>
cmd - Vedi comandi disponibili
quit - Chiudi
''')

    ans = input()

    if ans == "new":
        projectCreator()
    elif ans == "see":
        projectLookup()
    elif "add" in ans:
        projectAdder(ans[4:])
    elif ans == "quit":
        quit()