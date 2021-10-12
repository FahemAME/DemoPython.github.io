#!/usr/bin/python
#-*- coding: utf-8 -*-
import tkinter
import sys
class IHM_Impression:
	def __init__(self):
		self.fenetre=tkinter.Tk()
		self.fenetre.iconbitmap('favicon.ico')
		self.MsgEchecImpression = "Echec d'impression de ticket."
		self.MsgImpression = "Transaction réussie.\n\n Voulez vous imprimer un ticket?"

		self.fenetre.title("IHM_Impression")    
		self.fenetre.minsize (980,420)
		font_1=("Times New Roman",50)
		font_2=("Times New Roman",40)
		couleurs=['#FAFFC5','white','black','#F0AFE5','blue','grey']
		self.fenetre.config (bg=couleurs[0])
		self.fr_imp = tkinter.Frame (self.fenetre ,bg=couleurs[1],bd=3)
		self.fr_imp.pack()
		self.lab=tkinter.Label (self.fr_imp,text=self.MsgImpression,fg=couleurs[2],bg=couleurs[3],font=font_1)
		self.lab.pack(side= tkinter.TOP)

		self.btn_oui_impr= tkinter.Button (self.fr_imp,text="Oui",width=10,fg=couleurs[4],bg=couleurs[5],font=font_2,command=self.ValiderImpression)
		self.btn_oui_impr.pack(side= tkinter.LEFT)

		self.btn_non_impr= tkinter.Button (self.fr_imp,text="Non",width=10,fg=couleurs[4],bg=couleurs[5],font=font_2,command=self.AnnulerImpression)
		self.btn_non_impr.pack(side= tkinter.RIGHT)

		self.fenetre.bind('<Escape>',sys.exit)
		self.fenetre.mainloop()
		print("fin IHM_Impression")
		self.fenetre.destroy()
	def ValiderImpression(self, ):

		pass

	def AnnulerImpression(self, ):
		self.fenetre.quit()
		print("fin de lllimpression\t btn_non_impr")
		pass

