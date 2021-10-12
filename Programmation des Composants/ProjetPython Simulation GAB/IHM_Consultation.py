#!/usr/bin/python
#-*- coding: utf-8 -*-
import tkinter
import sys
from Cnt_Transaction import Consultation
from IHM_Transaction import IHM_Transaction
from Cnt_Transaction import Cnt_Transaction as C_T

class IHM_Consultation:
    def __init__(self,Acces):
        self.Acces=Acces
        self.distr=C_T.ReturnerDistributeur()
        self.Acces.setTransaction_(Consultation())
        self.fenetre1=tkinter.Toplevel()
        self.fenetre1.iconbitmap('favicon.ico')
        print("11111111111111")
        C_T.EffectuerConsultation(self.Acces.Compte,self.distr)
        print("2222222222222")
        self.ExtraitSolde = "Extrait de solde"+"\n\n"+self.Acces.Compte.client.getNom()+" "+self.Acces.Compte.client.getPrenom()
        self.NumeroCompte = "Numéro de Compte :"+str(self.Acces.Compte.getNumeroCmpt())
        self.Solde = "Solde de Compte :"+str(self.Acces.Compte.getSolde())+" DA."
        self.DerniereAcces = "Dernière accés :"+self.Acces.getDate_ancienne()
        self.fenetre1.title("IHM_Consultation")
        self.fenetre1.minsize (980,420)
        font_1=("Times New Roman",40)
        font_2=("Times New Roman",40)
        couleurs=['red','#ccf9f9','#573281','#ccf9f9','#573281','yellow']
        self.fenetre1.config (bg=couleurs[0])
        self.fr_consult = tkinter.Frame (self.fenetre1 ,bg=couleurs[1],bd=3)
        self.lab=tkinter.Label (self.fr_consult,text=self.ExtraitSolde,fg=couleurs[2],bg=couleurs[3],font=font_1)
        self.lab.pack(side= tkinter.TOP) 
        self.label1=tkinter.Label (self.fr_consult,text=self.NumeroCompte,fg=couleurs[2],bg=couleurs[3],font=font_1)
        self.label1.pack() 
        self.label2=tkinter.Label (self.fr_consult,text=self.Solde,fg=couleurs[2],bg=couleurs[3],font=font_1)
        self.label2.pack() 
        self.label3=tkinter.Label (self.fr_consult,text=self.DerniereAcces,fg=couleurs[2],bg=couleurs[3],font=font_1)
        self.label3.pack()
        self.btn_terminer= tkinter.Button (self.fr_consult,text="Terminer",width=10,fg=couleurs[4],bg=couleurs[5],font=font_2,command=self.Terminer)
        self.btn_terminer.pack()
        self.ConsulterSolde()
        self.fenetre1.bind('<Escape>',sys.exit)
        self.fenetre1.mainloop()
        print("fin IHM_Consultation")
        self.fenetre1.destroy()

    def ConsulterSolde(self, ):
        self.fr_consult.pack()

    def EffectuerTransaction(self, ):
        pass
        
    def Terminer(self, ):
        self.fenetre1.iconify()
        IHM_Transaction(self.Acces,"consultation")
        self.fenetre1.quit()
        print("fin de consultation")
        pass
