#!/usr/bin/python
#-*- coding: utf-8 -*-

from Transaction_ import Transaction_
import Cnt_Distributeur as C_D 

import mysql.connector



class Cnt_Transaction:
 
	def ReturnerDistributeur():
		return C_D.Distributeur()
	def RefuserTransaction(c,d ):
		con =mysql.connector.connect(host='localhost',database='mydb',user='root', password='test')
		print("RefuserTransaction")
		curs=con.cursor()
		print("test2\n\n\npppppppRefuserTransaction")
		req="call mydb.procedure_refuser_transaction("+str(c.getNumeroCmpt())+", "+str(d.getNumeroDistr())+");"        
		curs.execute(req)
		con.commit()
		con.close()
		pass

	def AutorisationTransaction( c,d):
		con =mysql.connector.connect(host='localhost',database='mydb',user='root', password='test')
		print("AutorisationTransaction")
		curs=con.cursor()
		print("test2\n\n\npppppppAutorisationTransaction")
		req=" call procedure_autoriser_transaction("+str(c.getNumeroCmpt())+", "+str(d.getNumeroDistr())+");"        
		curs.execute(req)
		con.commit()
		con.close()
		pass
	def VerifierExistenceCompte(CompteBeneficiaire,mon_compt):
		con =mysql.connector.connect(host='localhost',database='mydb',user='root', password='test')
		print("VerifierExistenceCompte\t",str(CompteBeneficiaire))
		curs=con.cursor()
		print("test2")
		req=" select c.numero_cmpt from compte c where c.numero_cmpt="+str(CompteBeneficiaire)+" and c.numero_cmpt !="+str(mon_compt)+";"        
		curs.execute(req)
		rslt=curs.fetchall()
		mon_test=bool(rslt)
		print(mon_test,"   ",rslt)
		if(mon_test):
			print("numero_cmpt existe DB....")
			return True
		else:
			print("numero_cmpt n'existe pas DB....")
			return False
		print("fin VerifierExistenceCompte......")
		con.close()
	def VerifierTransactionMontant(e,dist):
		print("VerifierTransactionMontant\t",str(e.Transaction_.getMontant()),str(e.Compte.getNumeroCmpt()),str(e.Compte.getSolde()))
		if(int( e.Transaction_.getMontant()) <= int(e.Compte.getSolde())+20) and (int( e.Transaction_.getMontant()) <= int(dist.getEtat_de_la_caisse())):
			print("yessss")
			return True
		else:            
			print("nooooo")
			return False

	def EffectuerRetrait(e):
		con =mysql.connector.connect(host='localhost',database='mydb',user='root', password='test')
		print("EffectuerRetrait...\n\n")
		curs=con.cursor()
		print("test2\n\n\nppppppp EffectuerRetrait")
		req="call mydb.procedure_Retrait("+str(e.Compte.getNumeroCmpt())+","+str(e.Transaction_.getMontant())+");"        
		curs.execute(req)
		con.commit()
		con.close()
		C_D.Cnt_Distributeur.CalculerBillets()
		C_D.Cnt_Distributeur.EjecterBillets()
		pass

	def EffectuerVirement(e ):
		con =mysql.connector.connect(host='localhost',database='mydb',user='root', password='test')
		print("EffectuerVirement...\n\n",e.Compte.getNumeroCmpt(),"\t",e.Transaction_.getMontant(),"\t",e.Transaction_.getNumero_compte_beneficiaire())
		curs=con.cursor()
		print("test2\n\n\npppppppEffectuerVirement")
		req="call mydb.procedure_virement("+str(e.Compte.getNumeroCmpt())+","+str(e.Transaction_.getMontant())+", "+str(e.Transaction_.getNumero_compte_beneficiaire())+");"        
		curs.execute(req)
		con.commit()
		con.close()
		pass

	def EffectuerConsultation(c,d):
		con =mysql.connector.connect(host='localhost',database='mydb',user='root', password='test')
		print("EffectuerTransaction")
		curs=con.cursor()
		print("test2\n\n\nppppppp")
		req="call mydb.procedure_consultation("+str(c.getNumeroCmpt())+", "+str(d.getNumeroDistr())+");"        
		curs.execute(req)
		con.commit()
		con.close()
		pass


class Consultation(Transaction_):
	def __init__(self):
		self.Solde = None
		print("creer Consultation.....db")
	def getSolde(self):
		return self.Solde

class Retrait(Transaction_):
	def __init__(self):
		self.Montant = None
	def setMontant(self,e):
		self.Montant=e
	def getMontant(self):
		return self.Montant

class Virement(Transaction_):
	def __init__(self):
		self.Montant = None
		self.Numero_compte_beneficiaire = None
	def setMontant(self,e):
		self.Montant=e
	def setNumero_compte_beneficiaire(self,e):
		self.Numero_compte_beneficiaire=e
	def getMontant(self):
		return self.Montant
	def getNumero_compte_beneficiaire(self):
		return self.Numero_compte_beneficiaire
