#!/usr/bin/python
#-*- coding: utf-8 -*-
import tkinter
import sys
from IHM_Transaction import IHM_Transaction
from Cnt_Transaction import Retrait

class IHM_Retrait_argent:
	def __init__(self,Acces ):
		self.Acces=Acces
		self.compte=Acces.Compte
		self.Acces.setTransaction_(Retrait())
		self.retrait_vers_acces=""
		self.fenetre=tkinter.Toplevel()
		self.fenetre.iconbitmap('favicon.ico')
		self.MsgselectionnerMontant="Sélectionnez le montant désiré :"
		self.ChampMontant="Veuillez saisir le montant :"
		self.fenetre.title("IHM_Retrait_argent")    
		self.fenetre.minsize (980,420)
		font_1=("Times New Roman",50)
		font_2=("Times New Roman",40)
		couleurs=['#ccf9f9','#dcf9ff','#573281','#ccf9f9','#573281','yellow']
		self.fenetre.config (bg=couleurs[0])
		self.fr_Retr = tkinter.Frame (self.fenetre ,bg=couleurs[1],bd=3)
		self.fr_Retr.pack()

		self.fr_Autre = tkinter.Frame (self.fenetre ,bg=couleurs[1],bd=3)

		self.label1=tkinter.Label (self.fr_Retr,text=self.MsgselectionnerMontant,fg=couleurs[2],bg=couleurs[3],font=font_1)
		self.label1.grid(row=0 ,column=0 ,columnspan=3,padx=50)

		self.btn_montant_1000= tkinter.Button (self.fr_Retr,text="1000 DA",width=12,fg=couleurs[4],bg=couleurs[5],font=font_2,command=self.command_btn_1000)
		self.btn_montant_1000.grid(row=1 ,column=0 )
		self.btn_montant_2000= tkinter.Button (self.fr_Retr,text="2000 DA",width=12,fg=couleurs[4],bg=couleurs[5],font=font_2,command=self.command_btn_2000)
		self.btn_montant_2000.grid(row=2 ,column=0 )
		self.btn_montant_5000= tkinter.Button (self.fr_Retr,text="5000 DA",width=12,fg=couleurs[4],bg=couleurs[5],font=font_2,command=self.command_btn_5000)
		self.btn_montant_5000.grid(row= 3,column=0 )
		self.btn_montant_8000= tkinter.Button (self.fr_Retr,text="8000 DA",width=12,fg=couleurs[4],bg=couleurs[5],font=font_2,command=self.command_btn_8000)
		self.btn_montant_8000.grid(row=4 ,column=0 )
		self.btn_montant_10000= tkinter.Button (self.fr_Retr,text="10000 DA",width=12,fg=couleurs[4],bg=couleurs[5],font=font_2,command=self.command_btn_10000)
		self.btn_montant_10000.grid(row=1 ,column=2 )
		self.btn_montant_20000= tkinter.Button (self.fr_Retr,text="20000 DA",width=12,fg=couleurs[4],bg=couleurs[5],font=font_2,command=self.command_btn_20000)
		self.btn_montant_20000.grid(row=2 ,column= 2)
		self.btn_montant_50000= tkinter.Button (self.fr_Retr,text="50000 DA",width=12,fg=couleurs[4],bg=couleurs[5],font=font_2,command=self.command_btn_50000)
		self.btn_montant_50000.grid(row=3 ,column=2 )
		self.btn_montant_autre= tkinter.Button (self.fr_Retr,text="Autre montant",width=12,fg=couleurs[4],bg=couleurs[5],font=font_2,command=self.command_btn_autre_montant)
		self.btn_montant_autre.grid(row=4 ,column=2 )
		
		self.label2=tkinter.Label (self.fr_Autre,text=self.ChampMontant,fg=couleurs[2],bg=couleurs[3],font=font_1)
		self.label2.pack()
		self.val=tkinter.StringVar()
		self.val.trace('w',self.limite_size_montant)
		self.montant_saisi=tkinter.Entry( self.fr_Autre,width=10,textvariable=self.val,font=("Times New Roman",30))
		self.montant_saisi.pack()
		self.montant_saisi.focus_force()
		self.label3=tkinter.Label (self.fr_Autre,text="Montant maximal est 50000 Da.",fg=couleurs[2],bg=couleurs[3],font=font_1)
		self.fenetre.bind('<Escape>',sys.exit)
		self.fenetre.mainloop()
		print("fin IHM_Retrait_argent")
		self.fenetre.destroy()

	def ValiderMontant(self, ):
		self.SaisirMontant()
		pass
	def command_btn_1000(self, ):
		self.val.set("1000")
		print("command_btn_1000")
		self.SaisirMontant()
		pass
	def command_btn_2000(self, ):
		self.val.set("2000")
		self.SaisirMontant()
		pass
	def command_btn_5000(self, ):
		self.val.set("5000")
		self.SaisirMontant()
		pass
	def command_btn_8000(self, ):
		self.val.set("8000")
		self.SaisirMontant()
		pass
	def command_btn_10000(self, ):
		self.val.set("10000")
		self.SaisirMontant()
		pass
	def command_btn_20000(self, ):
		self.val.set("20000")
		self.SaisirMontant()
		pass
	def command_btn_50000(self, ):
		self.val.set("50000")
		self.SaisirMontant()
		pass
	def command_btn_autre_montant(self, ):
		print(self.compte.client.getPrenom())
		print("\n\n")
		print("\n\n bbb")
		print(self.compte.getNumeroCmpt())
		print("\n\n....")
		self.fr_Retr.forget()
		self.fr_Autre.pack()
		pass
	def SaisirMontant(self, *args):
		self.fenetre.iconify()
		self.Acces.Transaction_.setMontant(self.montant_saisi.get())
		c=IHM_Transaction(self.Acces,"Retrait argent")
		print(c.transaction_vers_retrait_ou_virement)
		print("\n\n",self.Acces.Transaction_.getMontant(),"\n\n")
		print("\n\nretrait_vers_acces=c.transaction_vers_retrait")
		self.retrait_vers_acces=c.transaction_vers_retrait_ou_virement
		self.fenetre.deiconify()
		print("que dois je faire?IHM_Retrait_argent ")
		self.fenetre.quit()
		pass
	def limite_size_montant(self,*args):
		print("ttttttttttttttttt")
		self.montant_saisi.bind('<Return>',self.SaisirMontant)
		v=self.montant_saisi.get()
		if len(v)>5:
			self.val.set(v[:5])
		if len(v)<5 :
			self.label3.forget()
		print("self.montant_saisi.get()")
		if int(v)>50000 and len(v)==5:
			self.label3.pack()
			self.montant_saisi.delete(4,len(self.montant_saisi.get()))
			self.montant_saisi.bind('<Return>',None)
		if int(v)>50000 and len(v)>5:
			self.label3.pack()
			self.montant_saisi.delete(5,len(self.montant_saisi.get()))
			self.montant_saisi.bind('<Return>',None)