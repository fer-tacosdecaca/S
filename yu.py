from tkinter import *
import speedtest

awa = Tk()
awa.config(bg="red")
awa.title("caca")
awa.geometry("700x500")



label = Label(awa, text="Verificación de velocidad de Internet", font=("Lucida Sans Unicode", 17, "bold","italic"), fg="#5D6D7E", bg="#dee8f1")
label.place(relx=0.5, rely=0.1,anchor=CENTER)

label2 = Label(awa, text="Velocidad de descarga:", font=("Lucida Sans Unicode", 13, "bold","italic"), fg="#5D6D7E", bg="#dee8f1")
label2.place(relx=0.5, rely=0.2,anchor=CENTER)

vel = Label(awa, text=" ", font=("Lucida Sans Unicode", 14, "bold","italic"), fg="#5D6D7E", bg="#dee8f1")
vel.place(relx=0.5, rely=0.3,anchor=CENTER)

velo = Label(awa, text="Velocidad de subida:", font=("Lucida Sans Unicode", 13, "bold","italic"), fg="#5D6D7E", bg="#dee8f1")
velo.place(relx=0.5, rely=0.5,anchor=CENTER)



def showinfo():
    print("boton pulsado")
    st = speedtest.Speedtest()
    sped = round(st.download()/1000000,2)
    vel["text"] = str(sped) + " :mbps"
    usped = round(st.upload()/1000000,2)
    velo["text"] = str(usped) + " :mbps"
showinf = Button(awa, text="Mosatrar informacion", command=showinfo)
showinf.place(relx=0.5, rely=0.7,anchor=CENTER)






















































































awa.mainloop()