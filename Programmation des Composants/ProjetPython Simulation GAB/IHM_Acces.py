#!/usr/bin/python
#-*- coding: utf-8 -*-
import tkinter
import sys
from Cnt_Acces import Cnt_Acces as C_A
from IHM_Consultation import IHM_Consultation 
from IHM_Retrait_argent import IHM_Retrait_argent 
from IHM_Virement import IHM_Virement 
from IHM_RechargementDepannage import IHM_RechargementDepannage 
class IHM_Acces:
	def __init__(self,):
		self.Acces=C_A.ReturnerAcces()
		self.AccesMiantenance=C_A.ReturnerAccesMaintenance()
		self.nmbr_fois=0
		self.fenetre=tkinter.Tk()
		self.fenetre.iconbitmap('favicon.ico')
		self.MsgModeService = "Mode service.\nVeuillez insérer votre carte\n S.V.P"
		self.MsgInsertionCode = "Inserer votre code :"
		self.AvalerCarte = "Votre carte est avalée."
		self.MsgReinsertionCode = "Réinserer votre code :"
		self.CarteEjectee = "Veuillez retirer votre carte \nS.V.P"
		self.OpertionTerminer = "Operation terminer.\n"+self.CarteEjectee
		self.CarteNonValide = "Operation terminer.\nType de carte non valide.\n"+self.CarteEjectee
		self.CodeIncorrecte = "Operation terminer.\nCode non valide.\n"+self.AvalerCarte
		self.CartePerimee = "Operation terminer.\nCarte éxpirée.\n"+self.AvalerCarte
		self.ChampNumeroAgent = "Numéro d'agent :  "
		self.ChampCodeAgent = "Code d'agent :  "
		self.MsgModeHorsService = "Mode hors service.\nVous ne pouvez pas effectuer \ndes transactions."
		self.MsgInsertionInvalide = "Numéro d'agent \nou \nCode d'agent est \ninvalide."
		self.fenetre.title("IHM_Acces")
		self.fenetre.minsize (980,420)
		font_1=("Times New Roman",50)
		font_2=("Times New Roman",40)
		font_3=("Times New Roman",30)

		couleurs=['#ccf9f9','#dcf9ff','#573281','#ccf9f9','#573281','yellow']
		self.fenetre.config (bg=couleurs[0])
		self.fr_mode_service = tkinter.Frame (self.fenetre ,bg=couleurs[1],bd=3)
		self.label1=tkinter.Label (self.fr_mode_service,text="",fg=couleurs[2],bg=couleurs[3],font=font_1)
		self.btn= tkinter.Button (self.fr_mode_service,text="Inserer votre carte",fg=couleurs[4],bg=couleurs[5],font=font_2,command=self.InsererCarte)
		self.value=tkinter.StringVar()
		self.value.trace('w',self.limite_size)
		self.code_saisi=tkinter.Entry(self.fr_mode_service, textvariable=self.value,show='*',width=4,font=("Times New Roman",30))
		self.btn_retrait= tkinter.Button (self.fr_mode_service,text="Retrait",width=17,fg=couleurs[4],bg=couleurs[5],font=font_2,command=self.command_btn_retrait)
		self.btn_virement= tkinter.Button (self.fr_mode_service,text="Virement",width=17,fg=couleurs[4],bg=couleurs[5],font=font_2,command=self.command_btn_virement)
		self.btn_consultation= tkinter.Button (self.fr_mode_service,text="Consultation",width=17,fg=couleurs[4],bg=couleurs[5],font=font_2,command=self.command_btn_consultation)
		self.fr_identification= tkinter.Frame (self.fr_mode_service ,bg=couleurs[1],bd=3)
		self.fr_mode_service.pack(expand=tkinter.YES)

		self.l1=tkinter.Label (self.fr_identification,text="Accés seulement aux agents \nde maintenance.",fg=couleurs[2],bg=couleurs[3],font=font_2)
		self.l2=tkinter.Label (self.fr_identification,text=self.ChampNumeroAgent,fg=couleurs[2],bg=couleurs[3],font=font_3)
		self.l3=tkinter.Label (self.fr_identification,text=self.ChampCodeAgent,fg=couleurs[2],bg=couleurs[3],font=font_3)
		self.l1.grid(row=0 ,column=0 ,columnspan=3,rowspan=2)
		self.l2.grid(row=2 ,column=0)
		self.l3.grid(row=3 ,column=0)

		self.value1=tkinter.StringVar()
		self.value2=tkinter.StringVar()
		self.value1.trace('w',self.limite_size1)
		self.value2.trace('w',self.limite_size2)

		self.numero_saisi_agent=tkinter.Entry(self.fr_identification,show='*',textvariable=self.value1,width=10,font=("Times New Roman",30))
		self.code_saisi_agent=tkinter.Entry(self.fr_identification,show='*',textvariable=self.value2,width=10,font=("Times New Roman",30))
		self.numero_saisi_agent.grid(row=2 ,column=1 ,columnspan=5)
		self.code_saisi_agent.grid(row=3 ,column=1 ,columnspan=5)
		self.numero_saisi_agent.focus_force()
		self.fr_mode_service.pack(expand=tkinter.YES)
		self.Accueil()
		self.fenetre.bind('<Escape>',sys.exit)
		self.fenetre.mainloop()
		print("fin IHM_Acces")
		self.fenetre.destroy()


	def Accueil(self,):
		self.label1.pack (side= tkinter.TOP)
		if C_A.VerifierModeService(self.AccesMiantenance.Distributeur) :
			self.fr_identification.forget()
			self.label1.config(text=self.MsgModeService)
			self.btn.pack (fill=tkinter.X)
			self.btn.focus_set()
			self.nmbr_fois=0
		else :
			self.btn.forget()
			self.label1.config(text=self.MsgModeHorsService)
			self.fr_identification.pack()
			self.numero_saisi_agent.delete(0,tkinter.END)
			self.code_saisi_agent.delete(0,tkinter.END)
			self.numero_saisi_agent.focus_force()

	def Inserer_code(self, ):
		self.code_saisi.delete(0,tkinter.END)
		self.code_saisi.focus_force()
	def ReinsererCode(self, ):
		self.code_saisi.delete(0,tkinter.END)
		self.label1.config(text=self.MsgReinsertionCode)
		self.code_saisi.focus_force()
		pass
	def SaisirNumeroAgentCodeAgent(self, ):
		self.AccesMiantenance.AgentMaintenance.setNumeroAgent(self.numero_saisi_agent.get())
		self.AccesMiantenance.AgentMaintenance.setCodeAgent(self.code_saisi_agent.get())
		print(self.numero_saisi_agent.get(),"\t rr",self.code_saisi_agent.get())
		if C_A.VerifierNumeroEtCodeAgent(self.AccesMiantenance.AgentMaintenance) :
			print("_____________________________________\n\n ")
			self.fenetre.iconify()
			ma_fenetre=IHM_RechargementDepannage(self.AccesMiantenance)
			print("_____________________________________\n\n ")
			C_A.EnregistrerAccesAgent(self.AccesMiantenance)
			self.fenetre.deiconify()
			self.Accueil()    

		else :
			self.label1.config(text=self.MsgInsertionInvalide)
			self.fr_identification.forget()
			self.fenetre.after(3000,self.Accueil)    
		pass

	def Valider(self, ):
		self.nmbr_fois+=1
		self.Acces.Compte.setCode(int(self.code_saisi.get()))
		if C_A.VerifierCode(self.Acces) :
			self.EffectuerAutreTransaction()
		else :
			print(".VerifierCode(int(self.code_saisi.get")
			if self.nmbr_fois<3:    
				self.ReinsererCode()
			else:
				self.label1.config(text=self.CodeIncorrecte)
				C_A.AvalerCarte(self.AccesMiantenance.Distributeur)
				self.code_saisi.forget()
				self.fenetre.after(3000,self.Accueil)    
	def Terminer(self, ):
		pass
	def InsererCarte( self,):
		self.btn.forget()
		if C_A.VerifierTypeCarte():
			if C_A.VerifierDatePeremption() :
				print ("crt expiree")
				C_A.AvalerCarte(self.AccesMiantenance.Distributeur)
				self.label1.config(text=self.CartePerimee)
				self.fenetre.after(3000,self.Accueil)
			else:
				print ("crt non expiree")
				self.label1.config(text=self.MsgInsertionCode)
				self.code_saisi.pack ()
				self.Inserer_code()
		else:
			print ("type crt nn valide")
			self.label1.config(text=self.CarteNonValide)
			self.fenetre.after(3000,self.Accueil)
		pass

	def EffectuerAutreTransaction(self, ):
		print ("code valide")
		self.code_saisi.forget()
		self.label1.config(text="Quelle transaction désirez-vous?")
		self.btn_retrait.pack ()
		self.btn_virement.pack ()
		self.btn_consultation.pack ()
		self.btn_retrait.focus_set()
		pass
	def limite_size(self,*args):
	   v=self.value.get()
	   if len(v)>4:self.value.set(v[:4])
	   if len(v)==4:self.Valider()
	def limite_size1(self,*args):
	   v=self.value1.get()
	   if len(v)>6:self.value1.set(v[:10])
	   if len(v)==6:self.code_saisi_agent.focus_force()
	def limite_size2(self,*args):
	   v=self.value2.get()
	   if len(v)>10:self.value2.set(v[:6])
	   if len(v)==10:self.SaisirNumeroAgentCodeAgent()
	def command_btn_consultation(self,):
		print("apres destruction")
		self.fenetre.iconify()
		IHM_Consultation(self.Acces)
		print(" IHM_Consultation vers IHM_Acces")
		C_A.EnregistrerAccesClient(self.Acces)
		self.fenetre.deiconify()
		self.label1.config(text=self.OpertionTerminer)
		self.btn_retrait.forget ()
		self.btn_virement.forget ()
		self.btn_consultation.forget ()
		self.fenetre.after(3000,self.Accueil)
		pass
	def command_btn_virement(self,):
		self.fenetre.iconify()
		print("8888 ")
		v=IHM_Virement(self.Acces) 
		self.fenetre.deiconify()
		if (v.Virement_vers_Acces=="autre Transaction"):
			self.EffectuerAutreTransaction()
			print("fahem\n\n\n")
		else:
			self.label1.config(text=self.OpertionTerminer)
			self.btn_retrait.forget ()
			self.btn_virement.forget ()
			self.btn_consultation.forget ()
			self.fenetre.after(3000,self.Accueil)
		pass
	def command_btn_retrait(self,):
		print("_____________________________________\n\n ")
		self.fenetre.iconify()
		b=IHM_Retrait_argent(self.Acces)
		print("_____________________________________\n\n ")
		print(b.retrait_vers_acces)
		self.fenetre.deiconify()
		
		if(b.retrait_vers_acces=="autre Transaction"):
			self.EffectuerAutreTransaction()
			print("fahem\n\n\n")
		else:
			print("Salvaaadooor")
			self.label1.config(text=self.OpertionTerminer)
			self.btn_retrait.forget()
			self.btn_virement.forget()
			self.btn_consultation.forget()
			self.fenetre.after(3000,self.Accueil)
			print("4441111111mm ")        
		pass
IHM_Acces()
