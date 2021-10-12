#!/usr/bin/python
#-*- coding: utf-8 -*-
import tkinter
import sys
from Cnt_Transaction import Cnt_Transaction as C_T
from IHM_Impression import IHM_Impression
from Cnt_Distributeur import Cnt_Distributeur as C_D

class IHM_Transaction():
    def __init__(self,acces,type_de_transaction):
        self.type_de_transaction=type_de_transaction
        self.acces=acces
        self.distr=C_T.ReturnerDistributeur()
        self.fenetre2=tkinter.Tk()
        self.fenetre2.iconbitmap('favicon.ico')
        self.Montant=""
        self.transaction_vers_retrait_ou_virement="Sortir"
        self.MsgEchecImpression = "\n\nEchec d'impression de ticket."
        self.TransactionValide = "Transaction réussie.\n\n Voulez vous imprimer un ticket?"
        self.EchecTransaction = "Echec de la transaction.\n\n Voulez vous effectuer \nune autre transaction?"
        self.fenetre2.title("IHM_Transaction")    
        self.fenetre2.minsize (980,420)
        font_1=("Times New Roman",50)
        font_2=("Times New Roman",40)
        couleurs=['#ccf9f9','#ccf9f9','#573281','#ccf9f9','#573281','yellow']
        self.fenetre2.config (bg=couleurs[0])
        
        self.fr_trn = tkinter.Frame (self.fenetre2 ,bg=couleurs[1],bd=3)
        self.lab=tkinter.Label (self.fr_trn,text=self.EchecTransaction,fg=couleurs[2],bg=couleurs[3],font=font_1)
        self.lab.pack(side= tkinter.TOP)
        self.btn_oui_= tkinter.Button (self.fr_trn,text="Oui",width=10,fg=couleurs[4],bg=couleurs[5],font=font_2,command=self.EffectuerAutreTransaction1)
        self.btn_non_= tkinter.Button (self.fr_trn,text="Non",width=10,fg=couleurs[4],bg=couleurs[5],font=font_2,command=self.fenetre2.quit)
        self.btn_non_.pack(side= tkinter.RIGHT)
        self.btn_oui_.pack(side= tkinter.LEFT)

        self.fr_imp=tkinter.Frame (self.fenetre2 ,bg=couleurs[1],bd=3)
        self.lab2=tkinter.Label (self.fr_imp,text=self.TransactionValide,fg=couleurs[2],bg=couleurs[3],font=font_1)
        self.lab2.pack(side= tkinter.TOP)
        self.btn_oui_impr= tkinter.Button (self.fr_imp,text="Oui",width=10,fg=couleurs[4],bg=couleurs[5],font=font_2,command=self.ValiderImpression)
        self.btn_oui_impr.pack(side= tkinter.LEFT)

        self.btn_non_impr= tkinter.Button (self.fr_imp,text="Non",width=10,fg=couleurs[4],bg=couleurs[5],font=font_2,command=self.AnnulerImpression)
        self.btn_non_impr.pack(side= tkinter.RIGHT)

        self.fenetre2.bind('<Escape>',sys.exit)
        if self.type_de_transaction=="Retrait argent" :
            self.EffectuerTransactionRetrait(self.acces)
        if self.type_de_transaction=="Virement" :
            self.EffectuerTransactionVirement(self.acces)       
        if self.type_de_transaction=="consultation" :
            self.fr_imp.pack()
        self.fenetre2.mainloop()
        print("gdfert")
        self.fenetre2.destroy()
    def EffectuerTransactionVirement(self, Montant):
        print(C_T.VerifierTransactionMontant(Montant,self.distr))
        if  C_T.VerifierTransactionMontant(Montant,self.distr) :
            self.fr_imp.pack()
            print(self.transaction_vers_retrait_ou_virement)
            C_T.AutorisationTransaction(self.acces.Compte,self.distr)
            C_T.EffectuerVirement(self.acces)
        else:
            C_T.RefuserTransaction(self.acces.Compte,self.distr)
            self.fr_trn.pack()
            print(self.transaction_vers_retrait_ou_virement)
        pass
    def EffectuerTransactionRetrait(self, Montant):
        print(C_T.VerifierTransactionMontant(Montant,self.distr))
        if  C_T.VerifierTransactionMontant(Montant,self.distr) :
            self.fr_imp.pack()
            print(self.transaction_vers_retrait_ou_virement)
            C_T.AutorisationTransaction(self.acces.Compte,self.distr)
            C_T.EffectuerRetrait(self.acces)
            print("...mon teste....\n",self.distr.getEtat_de_la_caisse(),Montant.Transaction_.getMontant())
            self.distr.setEtat_de_la_caisse(str(int(self.distr.getEtat_de_la_caisse())-int(Montant.Transaction_.getMontant())))
        else:
            C_T.RefuserTransaction(self.acces.Compte,self.distr)
            self.fr_trn.pack()
            print(self.transaction_vers_retrait_ou_virement)
        pass

    def ValiderImpression(self, ):
        self.btn_non_impr.forget()
        self.btn_oui_impr.forget()
        if C_D.VerifierEtatImpression():
            print("impression de transaction...")
        else:
            self.lab2.config(text=self.MsgEchecImpression)
            self.fenetre2.after(3000,self.fenetre2.quit)
        pass

    def AnnulerImpression(self, ):
        self.fenetre2.quit()
        print("fin de lllimpression\t btn_non_impr")
        pass

    def EffectuerAutreTransaction1(self,):
        self.transaction_vers_retrait_ou_virement="autre Transaction"
        self.fenetre2.quit()
        print("EffectuerAutreTransaction")
        pass