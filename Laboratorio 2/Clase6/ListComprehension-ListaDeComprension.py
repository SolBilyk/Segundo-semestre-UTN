names=["Paolo","Rodrigo","Lupe","Pepe"]
alongP=[p for p in names if p[0]=="P"] #Rerotna una lista solo con los nombres que empiezan con "P"
print(alongP)

bottleC=[{"name":"Quilmes", "Country":"Arg"},
        {"name":"Corona","Country":"Mx"},
        {"name":"Stella Artois","Country":"Belgium"}]

Arg= [b for b in bottleC if b["Country"]=="Arg"]
print(Arg)
print(bottleC)