#!/usr/bin/python
#-*- coding: utf-8 -*-
import tkinter
import sys
from IHM_Transaction import IHM_Transaction
from Cnt_Transaction import Cnt_Transaction as C_T
from Cnt_Transaction import Virement

class IHM_Virement:
    def __init__(self,Acces):
        self.Acces=Acces
        self.Acces.setTransaction_(Virement())
        self.fenetre=tkinter.Toplevel()     
        self.fenetre.iconbitmap('favicon.ico')
        self.ChampCompte = "Veuillez saisir le numéro\n de Compte bénéficiaire :"
        self.ChampMontant = ""
        self.Virement_vers_Acces= ""
        self.compte_n_existe_pas = "Le numéro de compte\n bénéficiaire que vous\n avez saisi n'existe pas."
        self.fenetre.title("IHM_Virement")
        self.fenetre.minsize (980,420)
        font_1=("Times New Roman",40)
        font_2=("Times New Roman",45)
        font_3=("Times New Roman",25)
        couleurs=['#ccf9f9','#ccf9f9','#573281','#ccf9f9','#573281','yellow']
        self.fenetre.config (bg=couleurs[0])
        self.fr_virm = tkinter.Frame (self.fenetre ,bg=couleurs[1],bd=3)
        self.fr_virm.pack()
        self.label1=tkinter.Label (self.fr_virm,text=self.ChampCompte,fg=couleurs[2],bg=couleurs[3],font=font_1)
        self.label_saisir_compte=tkinter.Label (self.fr_virm,text=" 20 chiffres restants.",fg=couleurs[2],bg=couleurs[3],font=font_3)

        self.val_compte=tkinter.StringVar()
        self.val_compte.trace('w',self.limite_size_compte)
        self.compte_saisi=tkinter.Entry( self.fr_virm,width=20,textvariable=self.val_compte,font=font_2)
        
        self.btn_valider_cmpt= tkinter.Button (self.fr_virm,text="Valider",width=7,fg=couleurs[4],bg=couleurs[5],font=font_2,command=self.ValiderCompte)
        self.btn_annuler= tkinter.Button (self.fr_virm,text="Annuler",width=7,fg=couleurs[4],bg=couleurs[5],font=font_2,command=self.Annuler)
        self.btn_valider_montant= tkinter.Button (self.fr_virm,text="Valider_",width=7,fg=couleurs[4],bg=couleurs[5],font=font_2,command=self.ValiderMontant)
        
        self.val_montant=tkinter.StringVar()
        self.val_montant.trace('w',self.limite_size_montant)
        self.montant_saisi=tkinter.Entry( self.fr_virm,width=20,textvariable=self.val_montant,font=font_2)
        
        self.SaisirCompte()


        self.fenetre.bind('<Escape>',sys.exit)
        self.fenetre.mainloop()
        print("fin IHM_Virement")
        self.fenetre.destroy()

    def SaisirMontant(self, ):
        self.ChampMontant = "Le numéro de compte bénéficiaire :\n"+str(self.compte_saisi.get())+"\nVeuillez saisir le montant:"
        self.label1.config(text=self.ChampMontant)
        self.compte_saisi.grid_forget()
        self.label_saisir_compte.grid_forget()
        self.btn_valider_cmpt.grid_forget()
        self.btn_annuler.grid_forget()
        self.btn_valider_montant.grid(row=4,column=1)
        self.montant_saisi.grid(row=2,column=1)
        self.montant_saisi.focus_force()
        pass

    def ValiderCompte(self, ):
        if C_T.VerifierExistenceCompte(self.compte_saisi.get(),self.Acces.Compte.getNumeroCmpt()):
            self.SaisirMontant()
            self.Acces.Transaction_.setNumero_compte_beneficiaire(self.compte_saisi.get())
        else :
            self.affichage_compte_n_existe_pas()
            self.Virement_vers_Acces="autre Transaction"
            self.fenetre.after(3000,self.fenetre.quit)
        pass

    def SaisirCompte(self, ):
        self.label1.grid(row=1,column=1)
        self.compte_saisi.grid(row=2,column=1)
        self.compte_saisi.focus_force()
        self.label_saisir_compte.grid(row=3,column=1)
        self.btn_valider_cmpt.grid(row=4,column=0)
        self.btn_annuler.grid(row=4,column=2)
        self.btn_valider_cmpt.config(state=tkinter.DISABLED)
        pass

    def ValiderMontant(self, ):
        print("ValiderMontant")
        self.fenetre.iconify()
        self.Acces.Transaction_.setMontant(self.montant_saisi.get())
        c=IHM_Transaction(self.Acces,"Virement")
        print("\n\n",self.Acces.Transaction_.getMontant(),"\t\t",self.Acces.Transaction_.getNumero_compte_beneficiaire(),"\n\n")
        print(c.transaction_vers_retrait_ou_virement)
        self.Virement_vers_Acces= c.transaction_vers_retrait_ou_virement
        self.fenetre.deiconify()
        print("que dois je faire?IHM_Virement ")
        self.fenetre.quit()
        pass

    def Annuler(self, ):
        self.Virement_vers_Acces="autre Transaction"
        self.fenetre.quit()
        pass
    def affichage_compte_n_existe_pas(self,):
        print("20\n\n")
        self.label1.config(text=self.compte_n_existe_pas)
        self.compte_saisi.grid_forget()
        self.label_saisir_compte.grid_forget()
        self.btn_valider_cmpt.grid_forget()
        self.btn_annuler.grid_forget()
    def limite_size_montant(self,*args):
        print("limite_size_montant")
        pass
    def limite_size_compte(self,*args):
        v=self.compte_saisi.get()
        print(20-len(v))
        self.label_saisir_compte.config(text=str(20-len(v))+" chiffres restants.")
        if len(v)>20:
            print("bluummm")
            self.label_saisir_compte.grid_forget()
            self.val_compte.set(v[:20])
        if len(v)==20:
            self.btn_valider_cmpt.config(state=tkinter.NORMAL)
            self.label_saisir_compte.grid_forget()
        if len(v)<20:
            print("bla bla bla")
            self.btn_valider_cmpt.config(state=tkinter.DISABLED)
            self.label_saisir_compte.grid(row=3,column=1)
                        
                                    

#IHM_Virement()