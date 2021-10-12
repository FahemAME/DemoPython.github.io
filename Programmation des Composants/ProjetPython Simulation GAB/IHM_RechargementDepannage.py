#!/usr/bin/python
#-*- coding: utf-8 -*-
import tkinter

class IHM_RechargementDepannage:
	def __init__(self,AccesMaintenance):
		self.AgentMaintenance=AccesMaintenance.AgentMaintenance
		self.distributeur=AccesMaintenance.Distributeur
		self.fenetre=tkinter.Toplevel()     
		self.fenetre.iconbitmap('favicon.ico')
		self.Etat_de_la_caisse = "Etat de la caisse des billets :"+str(self.distributeur.getEtat_de_la_caisse())
		self.Etat_d_encre = "Etat d'encre:"+str(self.distributeur.getEtat_d_encre())
		self.Etat_de_papier = "Etat de papier :"+str(self.distributeur.getEtat_de_papier())
		self.Etat_des_cartes_avalees ="Etat des cartes avalées :"+str(self.distributeur.getEtat_des_cartes_avalees())
		self.Etat_des_pannes = "Etatdes pannes :..."
		self.fenetre.title("IHM_RechargementDepannage")    
		self.fenetre.minsize (980,420)
		font_1=("Times New Roman",30)
		font_2=("Times New Roman",40)
		couleurs=['black','#ccf9f9','#573281','#ccf9f9','#573281','yellow']
		self.fenetre.config (bg=couleurs[0])
		self.fr_Rech_Depa = tkinter.Frame (self.fenetre ,bg=couleurs[1],bd=3)
		self.fr_Rech_Depa.pack(expand=tkinter.YES)
		self.label1=tkinter.Label (self.fr_Rech_Depa,text=self.Etat_de_la_caisse,fg=couleurs[2],bg=couleurs[3],font=font_1)
		self.label2=tkinter.Label (self.fr_Rech_Depa,text=self.Etat_d_encre,fg=couleurs[2],bg=couleurs[3],font=font_1)
		self.label3=tkinter.Label (self.fr_Rech_Depa,text=self.Etat_de_papier,fg=couleurs[2],bg=couleurs[3],font=font_1)
		self.label4=tkinter.Label (self.fr_Rech_Depa,text=self.Etat_des_cartes_avalees,fg=couleurs[2],bg=couleurs[3],font=font_1)
		self.label5=tkinter.Label (self.fr_Rech_Depa,text=self.Etat_des_pannes,fg=couleurs[2],bg=couleurs[3],font=font_1)
		
		self.label1.grid(row=1)
		self.label2.grid(row=2)
		self.label3.grid(row=3)
		self.label4.grid(row=4)
		self.label5.grid(row=5)

		self.btn1= tkinter.Button (self.fr_Rech_Depa,text="Recharger",fg=couleurs[4],bg=couleurs[5],font=font_2,command=self.Recharger1)
		self.btn2= tkinter.Button (self.fr_Rech_Depa,text="Recharger",fg=couleurs[4],bg=couleurs[5],font=font_2,command=self.Recharger2)
		self.btn3= tkinter.Button (self.fr_Rech_Depa,text="Recharger",fg=couleurs[4],bg=couleurs[5],font=font_2,command=self.Recharger3)
		self.btn_recuperer= tkinter.Button (self.fr_Rech_Depa,text="Recupérer",fg=couleurs[4],bg=couleurs[5],font=font_2,command=self.Recuperer)
		self.btn_depanner= tkinter.Button (self.fr_Rech_Depa,text=" Dépanner",fg=couleurs[4],bg=couleurs[5],font=font_2,command=self.Depanner)
		self.btn_terminer= tkinter.Button (self.fr_Rech_Depa,text="Terminer",fg=couleurs[4],bg=couleurs[5],font=font_2,command=self.Terminer)

		self.btn1.grid(row=1,column=2)
		self.btn2.grid(row=2,column=2)
		self.btn3.grid(row=3,column=2)
		self.btn_recuperer.grid(row=4,column=2)
		self.btn_depanner.grid(row=5,column=2)
		self.btn_terminer.grid(row=6,column=1)

		self.fenetre.mainloop()
		self.fenetre.destroy()

	def Recharger1(self, ):
		self.distributeur.setEtat_de_la_caisse(str(10000000))
		self.Etat_de_la_caisse = "Etat de la caisse des billets :"+str(self.distributeur.getEtat_de_la_caisse())
		self.label1.config(text=self.Etat_de_la_caisse)
		pass

	def Recharger2(self, ):
		pass

	def Recharger3(self, ):
		pass

	def Recuperer(self,):
		self.distributeur.setEtat_des_cartes_avalees(int(0))
		self.Etat_des_cartes_avalees="Etat des cartes avalées :"+str(self.distributeur.getEtat_des_cartes_avalees())
		self.label4.config(text=self.Etat_des_cartes_avalees)
		pass

	def Depanner(self, ):
		pass

	def Terminer(self, ):
		print(self.AgentMaintenance.getNumeroAgent(),"\n\n",self.AgentMaintenance.getCodeAgent())
		self.fenetre.quit()
		pass


