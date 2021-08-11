from os import read
from re import split
import csv
from pathlib import Path
from time import sleep

def calculator (project_name):
    
    print("\n>]=======================================================[<")
    print(f">] Valutiamo il progetto '{project_name}' ...")
    proj_file = open(str(Path.home())+"/"+project_name+".rmn","r")
    reader = csv.reader(proj_file)
    header = next(reader)
    header = header[1:-1]
    header = [(k[:-14]) for k in header]
    
    partecipants = {}
    for k in header:
        partecipants[k] = {"Payed":0,"Spent":0}
        
    for line in reader:
        pool = line[1:-1]
        for k,v in zip(header,pool):
            partecipants[k]["Payed"] += float(split("\|",v)[0])
            partecipants[k]["Spent"] += float(split("\|",v)[1])

    print(">] Calcolo dei delta per ciascun partecipante ...")
    sleep(1)
    for k in partecipants:
        partecipants[k]["Delta"] = partecipants[k]["Payed"] - partecipants[k]["Spent"]
        print("\t",k, partecipants[k])

    print("\n>] Verifica anti-cheat ...")
    sleep(1)
    if sum([(partecipants[k]["Delta"]) for k in partecipants]) != 0:
      print("\t>! ... Whoops! Qualcuno ha barato qui!")
      quit()
    else:
      print("\t>! ... a posto!")

    print("\n>] Inizio a calcolare ...")

    creditors = {}
    debitors = {}
    answers = []

    for k in partecipants:
      if partecipants[k]["Delta"] > 0:
        creditors[k] = partecipants[k]["Delta"]
      elif partecipants[k]["Delta"] < 0:
        debitors[k] = partecipants[k]["Delta"]
      else:
        continue
    
    print("\n>] Creditori:", creditors)
    print(">] Debitori:",debitors)

    
    for d in debitors:
      for c in creditors:
        if debitors[d] > creditors[c]:
          answers.append(f'{d} deve restituire {debitors[d]} a {c}')
          debitors[d] = debitors[d] - creditors[c]
          creditors.pop(c)
        elif debitors[d] == creditors[c]:
          answers.append(f'{d} deve restituire {debitors[d]} a {c}')
          creditors.pop(c)
          debitors.pop(d)

      
    
    print(answers)
    print("FINEEEEEEEEEEEEEEEEEEEEEEE")


    print(">]=======================================================[<")
