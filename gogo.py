import matplotlib .pyplot as pit
import psutil as p


appnl = []
appnpl = []
count = 0



for process in p.process_iter():
    count = count +1
    if count <= 6:
        name = process.name()
        cpuu= p.cpu_percent()
        print("nombre: ", name, "-- uso de cpu:", cpuu)
        appnl.append(name)
        appnpl.append(cpuu)




pit.figure(figsize=(7,12))
pit.xlabel("app")
pit.ylabel("Uso")
pit.bar(appnl, appnpl,width=0.6 ,color=("purple","green","red","blue","orange","pink"))
pit.show()
