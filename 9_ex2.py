import csv

films = [["Top Gun","Risky Business","Minority Report"],["Titanic","The Revenant","Incepion"],["Training Day","Man on Fire","Flight"]]

with open("ex.csv", "w", newline='') as f:
    w = csv.writer(f,delimiter=",")
    for film in films:
        w.writerow(film)
        print(film)
