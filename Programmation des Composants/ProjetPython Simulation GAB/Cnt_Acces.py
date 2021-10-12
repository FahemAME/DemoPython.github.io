#!/usr/bin/python
#-*- coding: utf-8 -*-
import mysql.connector
from datetime import date, time, datetime

import Cnt_Distributeur as C_D 

from Transaction_ import Transaction_

class Cnt_Acces:
    def ReturnerAgent():
        return AgentMaintenance()
    def ReturnerAcces( ):
        return Acces()    
    def ReturnerAccesMaintenance( ):
        return AccesMaintenance()

    def VerifierCode( e):
        con =mysql.connector.connect(host='localhost',database='mydb',user='root', password='test')
        print("VerifierCode\t",e.Compte.getCode(),"\t",e.Compte.client.getNom(),"\t",e.Compte.carte.getNumeroCrt())
        curs=con.cursor()
        print("test2")
        req="select c.numero_cmpt,c.solde,max(a.date_acces) from compte c,client cl,carte cr,acces a where c.code="+str(e.Compte.getCode())+" and cl.nom='"+str(e.Compte.client.getNom())+"' and cl.prenom='"+str(e.Compte.client.getPrenom())+"' and cr.numero_crt="+str(e.Compte.carte.getNumeroCrt())+" and c.numero_crt=cr.numero_crt and c.id_client=cl.idclient;"
        curs.execute(req)
        rslt=curs.fetchall()
        mon_test=bool(rslt[0][0])
        if(mon_test):
            e.Compte.setNumeroCmpt(rslt[0][0])
            e.Compte.setSolde(rslt[0][1])
            e.setDate_ancienne(rslt[0][2])
            print("code valide DB....")
            return True
        else:
            print("code non valide DB....")
            return False
        con.close()
        print("fin de VerifierCode....")
    def VerifierNumeroEtCodeAgent(e):
            con =mysql.connector.connect(host='localhost',database='mydb',user='root', password='test')
            print("test")        
            curs=con.cursor()
            print("test2")
            req="SELECT * FROM agentmaintenance a where a.numero_agent="+e.getNumeroAgent()+" and a.code_agent="+e.getCodeAgent()+";"
            curs.execute(req)
            rslt=curs.fetchall()
            mon_test=bool(rslt)
            print(mon_test,"   ",rslt)
            if mon_test:
                print("acces valide a l'Agent")
                for i in rslt:
                    print(i)
                return True
            else:
                print("acces non valide a l'Agent")
                return False
    def VerifierTypeCarte( ):
        with open ("Lecture de carte.txt","r") as mon_fichier :
            contenu=mon_fichier.read().splitlines()
        if(contenu[0] =='Type de carte valide'):
            print(contenu[0],"VerifierTypeCarte")
            return True
        else: 
            return False
        pass
    def VerifierDatePeremption( ):
        print("VerifierDatePeremption",Carte().getDatePeremption())
        if(Carte().getDatePeremption() <datetime.now().date()):
            print("(Carte().getDatePeremption() <datetime.now().date()) veut dire expirée....")
            return True
        else: 
            return False
        pass
    def AvalerCarte(e):
        e.setEtat_des_cartes_avalees(int(e.getEtat_des_cartes_avalees())+1)
        print("AvalerCarte....write...")       
    def VerifierModeService(e):
            if(int(e.getEtat_de_la_caisse()) >=50000):
                return True
            else:
                return False
            pass
    def EjecterCarte( ):
            pass
    def EnregistrerAccesAgent(e):
        con =mysql.connector.connect(host='localhost',database='mydb',user='root', password='test')
        print("EnregistrerAccesAgent\t",str(e.AgentMaintenance.getNumeroAgent()),"\t",str(e.Distributeur.getNumeroDistr()))
        curs=con.cursor()
        print("test2")
        req="call mydb.procedure_acces_agent("+str(e.AgentMaintenance.getNumeroAgent())+","+str(e.Distributeur.getNumeroDistr())+");"        
        curs.execute(req)
        con.commit()
        con.close()
        pass
    def EnregistrerAccesClient(e):
        con =mysql.connector.connect(host='localhost',database='mydb',user='root', password='test')
        print("EnregistrerAccesClient\t")
        curs=con.cursor()
        print("test2")
        req="call mydb.procedure_acces_client("+str(e.Compte.getNumeroCmpt())+");"        
        curs.execute(req)
        con.commit()
        con.close()
        pass

class Client:
    def __init__(self):
        self.Nom = None
        self.Prenom = None
    def getNom( self):
        with open ("Lecture de carte.txt","r") as mon_fichier :
            contenu=mon_fichier.read().splitlines()
        return contenu[2]
    def getPrenom( self):
        with open ("Lecture de carte.txt","r") as mon_fichier :
            contenu=mon_fichier.read().splitlines()
        return contenu[3]

class Carte:
    def __init__(self):
        self.NumeroCrt = None
        self.Date_peremption = None

    def getNumeroCrt(self ):
        with open ("Lecture de carte.txt","r") as mon_fichier :
            contenu=mon_fichier.read().splitlines()
        return contenu[4]
        
    def getDatePeremption( self):
        with open ("Lecture de carte.txt","r") as mon_fichier :
            contenu=mon_fichier.read().splitlines()
        return datetime.strptime(contenu[1],'%Y-%m-%d').date()


class Compte:
    def __init__(self):
        self.NumeroCmpt = None
        self.Solde = None
        self.Code = None
        self.client=Client()
        self.carte=Carte()
    
    def setNumeroCmpt(self,e):
        self.NumeroCmpt=e
    def setSolde(self,e):
        self.Solde=e
    def setCode(self,e):
        self.Code=e

    def getNumeroCmpt(self):
        return self.NumeroCmpt
    def getSolde(self):
        print("Cnt_Acces")
        return self.Solde
    def getCode(self):
        return self.Code



class Acces:
    def __init__(self):
        self.Date_ancienne = None
        self.Compte=Compte()
        self.Transaction_=Transaction_()
    def setTransaction_(self,e):
        self.Transaction_=e 
        pass
    def setDate_ancienne(self,e):
        self.Date_ancienne=e 
        pass
    def getDate_ancienne(self):
        return self.Date_ancienne.strftime('%Y-%m-%d   %H:%M')



class AgentMaintenance:
    def __init__(self):
        self.NumeroAgent = 0
        self.CodeAgent = 0
    def setNumeroAgent(self,nmr_agent):
        self.NumeroAgent=nmr_agent  
    def setCodeAgent(self,code_agent):
        self.CodeAgent=code_agent

    def getNumeroAgent(self):
        return self.NumeroAgent     
    def getCodeAgent(self):
        return self.CodeAgent

class AccesMaintenance:
    def __init__(self):
        self.Date = None
        self.AgentMaintenance=AgentMaintenance()
        self.Distributeur=C_D.Distributeur()
    def getDate(self):
        return self.Date_ancienne.strftime('%Y-%m-%d   %H:%M')
 