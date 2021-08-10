from os import read
import re, csv
from pathlib import Path

def calculator (project_name):
    
    print(f">] Inizio a valutare il progetto '{project_name}'")
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
            partecipants[k]["Payed"] += float(re.split("\|",v)[0])
            partecipants[k]["Spent"] += float(re.split("\|",v)[1])

    for k in partecipants:
        print(k, partecipants[k])