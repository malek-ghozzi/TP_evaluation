import tkinter as tk #importer la bibliothéque tkinter pour gérer l'interface graphique
from tkinter import Label,Entry #importer de la bibliothéque tkinter les labels et les entrés qu'on va l'utilisé 
import os, _thread
    

def run_proc():# la fonction "run_proc" va ouvrir le logiciel process explorer 
    
    os.system(r".\dos\procexp.exe") #le chemin de l'emplacement de logiciel process explorer 

def para_window(): #fonction para_window permet de 

    win_2 = tk.Tk() #creation d'une interface 2  avec la bibliothéque tkinter comme tk 
    win_2.title("Disk Banch paramétre") #titre de la fenetre quand on clique sur le bouton Dsik bench
    win_2.geometry("400x300")#taille de la fenetre
    frame_2 = tk.Frame(win_2)#creation  de la fentre 
    frame_2.pack()#regroupe les données de la fenetre .
    txt_2=Label(frame_2,text="Combien de Disk voulez-vous ?")#label contient le text "combien de disk coulez-vous?"
    txt_2.grid(row=0,column=3,pady=20,padx=100)#la gestion de la fentre : on graduer la fentre sous forme des lignes et des colonnes.Le text précedent prend la ligne0et la colonne 3
    box=Entry(frame_2) #le nombre de disk souhaité sera entré dans la variable box       
    box.grid(row=1,column=3)#l'emplacement de box dans la 1ére ligne et la 3éme colonne 
    btn_valide = tk.Button(frame_2,text="Valider",fg="red")#vreation de bouton "valider" coloré en rouge 
    btn_valide.grid(row=2,column=3,pady=10,padx=100)#l'emplacement de bouton valider dans la 2éme ligne et le 3éme colonne 

    try: #fonction essayé si bien excuté alors on avoir les fentres de disk bench si nn un mesg "non" sera affichié 
        
        def open_disk():#la fonction open_disk permet d'ouvrir le disk banch 
            os.system(r".\dos\DiskBench.exe")#le chemin de l'emplacement de logiciel disk bench

        def run_disk():#la fonction "run_disk" permet d'avoir la nombre de disk souhaité n  puis ouvrir n fentre  et enfin l'affihcgae 
            n=int(float(box.get()))#avoir la valeur entré de nmbre de disk souhaité 

            for i in range(1,n+1):#on execute le nombre de disk souhaité n  dansun boucle for n fois 
        
                _thread.start_new_thread(open_disk)#Pour la synchronisation on a utliser "_thread" c'est comme des processus ou tâches léger.On a Démarré un nouveau thread et renvoyé son identifiant.Le thread exécute la fonction la  open.disk()
            win_2.destroy()#la fonction ".destory()" permet de  détruire les composants de l'interface graphique pour libérer la mémoire et effacer l'écran
    
        btn_valide.config(command=run_disk)#la configuration de bouton valider
        
        
    except ValueError:#sil ya une erreur retourner "non"
       return "non"


win = tk.Tk()#creation d'une interface principale  avec la bibliothéque tkinter comme tk 
win.title("TP2 évaluation de performance")#titre de la fenetre quand on lance le programme 
win.geometry("400x300")#taille de la fenetre
frame = tk.Frame(win)#creation de la fentre 
frame.pack()#regroupe les données de la fenetre .
btn_cpu = tk.Button(frame,text="DISK BENCH",fg="red",height="5",command=para_window)#creation de bouton "Disk bench" et lorqu'on clique sur le bouton on excute la fonction "para_window"
btn_cpu.grid(row=0,column=3,pady=10,padx=100)#l'emplacement de bouton "Disk bench"
btn_disk = tk.Button(frame,text="Process Explorer",fg="blue",height="5",width="12",command=run_proc)#creation de bouton "Process explorer" et lorqu'on clique sur le bouton on excute la fonction "run_proc"
btn_disk.grid(row=1,column=3,pady=10,padx=100)#l'emplacement de bouton "Process Explorer"

txt=Label(frame,text="© Malek Ghozzi & Med Amine Boufares")#un text ecrit dans la fenetre 
txt.grid(row=3,column=3,pady=50,padx=100)#l'emplacemnt de ce text

win.mainloop()#affichier l'interface principale 