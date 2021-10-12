#!/usr/bin/python
#-*- coding: utf-8 -*-
import mysql.connector

class Cnt_Distributeur:
	def ValiderRetrait( ):
		pass

	def VerifierModeService( ):
		pass

	def VerifierLesPannes( ):
		pass

	def CapturerLesPannes( ):
		pass

	def Ejectercarte( ):
		pass

	def VerifierEtatImpression( ):
		return False
		pass

	def ValiderImpression( ):
		pass

	def AnnulerImpression( ):
		pass

	def Verifier_etat_de_la_caisse( ):
		pass

	def Verifier_etat_de_l_encre( ):
		pass

	def Verifier_etat_du_papier( ):
		pass

	def ActualiserLaCaisse(e):
		pass

	def Actualiser_Etat_Papier( ):
		pass

	def Actualiser_Etat_Encre( ):
		pass

	def ImprimerTransaction( ):
		pass

	def CalculerBillets( ):
		print("CalculerBillets...")
		pass

	def EjecterBillets( ):
		print("EjecterBillets...")
		pass

	def VerifierEtatCarteAvalees( ):
		pass

class Distributeur:
	def __init__(self):
		self.NumeroDistr = None
		self.Etat_de_la_caisse = None
		self.Etat_des_cartes_avalees = None
		self.Etat_d_encre = None
		self.Etat_de_papier = None
	def getNumeroDistr(self):
		with open ("Distributeur.txt","r") as mon_fichier :
			contenu=mon_fichier.read().splitlines()
		return contenu[0]
	def getEtat_de_la_caisse(self):
		con =mysql.connector.connect(host='localhost',database='mydb',user='root', password='test')
		print("getEtat_de_la_caisse...\n\n")
		curs=con.cursor()
		print("test2\n\n\nppppppp getEtat_de_la_caisse",self.getNumeroDistr())
		req="select mydb.get_etat_caisse_distributeur("+self.getNumeroDistr()+");"    
		curs.execute(req)    
		rslt=curs.fetchall()
		print(str(rslt[0][0]))
		con.close()
		return rslt[0][0]	
	def getEtat_des_cartes_avalees(self):
		con =mysql.connector.connect(host='localhost',database='mydb',user='root', password='test')
		print("getEtat_des_cartes_avalees...\n\n")
		curs=con.cursor()
		print("test2\n\n\nppppppp012 getEtat_des_cartes_avalees",self.getNumeroDistr())
		req="select mydb.get_etat_carte_avalees_distributeur("+self.getNumeroDistr()+");"    
		curs.execute(req)    
		rslt=curs.fetchall()
		print(str(rslt[0][0]))
		con.close()
		return rslt[0][0]
	def getEtat_d_encre(self):
		with open ("Distributeur.txt","r") as mon_fichier :
			contenu=mon_fichier.read().splitlines()
		print("getEtat_d_encre:"+str(contenu[1]))
		return contenu[1]      
	def getEtat_de_papier(self):
		with open ("Distributeur.txt","r") as mon_fichier :
			contenu=mon_fichier.read().splitlines()
		print("getEtat_de_papier:"+str(contenu[2]))
		return contenu[2]
	def setEtat_de_la_caisse(self,e):
		con =mysql.connector.connect(host='localhost',database='mydb',user='root', password='test')
		print("setEtat_de_la_caisse...\n\n")
		curs=con.cursor()
		print("test2\n\n\nppppppp setEtat_de_la_caisse",self.getNumeroDistr())
		req="call mydb.set_etat_caisse_distributeur("+self.getNumeroDistr()+","+e+");"    
		curs.execute(req)    
		con.commit()
		con.close()
		self.Etat_de_la_caisse =e
		pass
	def setEtat_des_cartes_avalees(self,e):
		con =mysql.connector.connect(host='localhost',database='mydb',user='root', password='test')
		print("setEtat_des_cartes_avalees...\n\n",e)
		curs=con.cursor()
		print("test2\n\n\nppppppp setEtat_des_cartes_avalees",self.getNumeroDistr())
		req="call mydb.set_etat_carte_avalees_distributeur("+self.getNumeroDistr()+","+str(e)+");"    
		curs.execute(req)    
		con.commit()
		con.close()
		self.Etat_des_cartes_avalees=e
		pass
	def setEtat_d_encre(self,e):
		self.Etat_d_encre=e
		pass
	def setEtat_de_papier(self,e):
		self.Etat_de_papier=e
		pass
