import csv, re, os
from pathlib import Path

def projectCreator():
    home = str(Path.home())
    name = input(">! Come lo chiamiamo questo nuovo progetto?")
    partecipants = input(">! Inserisci i nomi dei partecipanti, separali con la virgola: ")
    partecipants = re.split(",",partecipants)
    print(partecipants)
    
    with open(home+"/"+name+".rmn","w") as file:
        file.write("Transazione,")
        for n in partecipants:
            if partecipants.index(n) != len(partecipants)+1:
              stringa = n+","
              file.write(stringa)
            else:
              file.write(stringa)
        file.write("\n")
    print(">! Progetto creato!")

def projectLookup():
    print(">! Ho trovato questi progetti:")
    for file in os.listdir(Path.home()):
        if file.endswith(".rmn"):
            print(file[:-4])
     
def projectAdder(project_name):
    try:
        with open(str(Path.home())+"/"+project_name+".rmn") as file:
            print(f">! Progetto {project_name} aperto!")
            reader = csv.reader(file,delimiter=",")
            head = next(reader)
            transactions = []
            trans_name = input(">! Inserisci descrizione transazione: ")
            transactions.append(trans_name)
            for name in head[1:-1]:
                insertion = input(f">! Aggiungi movimento per {name} nella forma <importo pagato|spesa effettiva>")
                transactions.append(insertion)
        print(">! Inserisco nel progetto!")
        with open(str(Path.home())+"/"+project_name+".rmn","a") as file:
            for t in transactions:
                s = t+","
                file.write(s)
            file.write("\n")
            print(">! Fatto!")

    except Exception as error:
        print(">! Qualcosa è andato storto",error)

def projectReader(project_name):
  home = str(Path.home())+"/"+project_name+".rmn"
  with open(home,"r") as file:
    reader = file.readlines()
    for l in reader:
      print(l)

def projectEval(project_name):
  print(f">] Inizio a valutare il progetto '{project_name}'")
  proj_file = open(str(Path.home())+"/"+project_name+".rmn","r")
  reader = csv.reader(proj_file)
  header = next(reader)

  list_of_transactions = []
  transaction_map = {}
  for line in reader:
    for n in range(1,len(header)-1):
      transaction_map["transaction_name"] = line[0]
      print(re.split("\|",line[n]))
      transaction_map[header[n]] = {"payed":re.split("\|",line[n])[0],"spent":re.split("\|",line[n])[1]}
    list_of_transactions.append(transaction_map)
    print(transaction_map)

  

print('''
>[ ================================================= ]<
    | Benvenuto in LaRomana. Cosa vuoi fare oggi? |
>[ ================================================= ]<    ''')
while True:
    print('''
>] new - Crea nuovo progetto
>] see - Vedi i progetti attivi
>] see <name> - Vedi progetto <name>
>] add <name> - Aggiungi movimenti al progetto <name>
>] calculate <name> - Restituisce i risultati del progetto <name>
>] clear - Pulisce lo schermo
>] quit - Chiudi
''')

    ans = input()

    if ans == "new":
        projectCreator()
    elif ans == "clear":
      os.system('cls' if os.name == 'nt' else 'clear')
    elif ans == "see":
        projectLookup()
    elif "see" in ans:
        projectReader(ans[4:])
    elif "add" in ans:
        projectAdder(ans[4:])
    elif "calculate" in ans:
        projectEval(ans[10:])
    elif ans == "quit":
        print(">! Arrivederci!")
        quit()
    elif ans == "egg":
        print('''
,___,     ,___,
[O.o]     [O.o]
/)__)     /)__)
-"--"------"--"----
        ''')
