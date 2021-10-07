/*
create  database SJQ07_M1
create table Article_Stock
(
ID_Article int primary key,
Nom_Article varchar(30) not null,
Categorie varchar(30) not null,
Quantite int not null
)
--insertion des donnees dans la table Article_Stock pour test
insert into Commande values(1,'Ordinateur','Electromenager',5)
insert into Commande values(2,'Pelle','Construction',2)
insert into Commande values(3,'Tapis','Decoration',4)
*/
create database BD__GAB;
	create table Compte_Client (
		Id_Compte_Client int(10),
		nom varchar(20),
		prenom varchar(20),
		numero_comp int(20),
		solde int(10),
		code_carte int(4)
		)
	create table Distributeurs (
		numero_distributeur int(5),
		Etat_Caisse int(6)
		)
	create table Transactions (
		Id_Transaction int(10),
		etat_transaction boolean,
		date_effectuer date,
		#Compte_Client int(10),
		#Distributeur int(5)
		)
	create table Retraits (
		montant_retrait int(5),
		#Transaction int(10)
		)
	create table Virements (
		montant_virement int(10),
		#numero_comp_beneficiaire int(10),
		#Transaction int(10)
		)
	create table Consultations (
		solde int(10),
		#Transaction int(10)
		)
	create table Agents_Maintenance (
		numero_agent int(5),
		code_agent int(10)
		)
	create table Acces_Agents (
		Id_Acces_Agent int(10),
		date_acces_agent date,
		#Agent_Maintenance int(5),
		#Distributeur int(5)
		)

"""
Client (id_client, nom, prénom)
Carte (numero_crt, date_peremption)
Compte (numero_cmpt, solde, code, #numero_crt, #id_client)
Transaction_ (id_transaction_, etat_validation, #numero_cmpt)
Acces (#id_transaction_, #numero_cmpt, date)
Virement (#id_transaction_, #numero_cmpt, montant, cpmt_beneficiaire)
Retrait (#id_transaction_, #numero_cmpt, montant)
Consultation (#id_transaction_, #numero_cmpt, solde)	

Distributeur (numero_distr, etat_caisse, etat_encre, etat_papier, etat_carte_avalees)
AgentMaintenance (numero_agent, code_agent, nom, prénom)
AccesMaintenance (#numero_distr, #numero_agent, date)
Effectuer (#id_transaction_, #numero_distr)
"""

-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`client`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`client` (
  `idclient` INT(11) NOT NULL AUTO_INCREMENT,
  `nom` VARCHAR(20) NULL,
  `prenom` VARCHAR(20) NULL,
  PRIMARY KEY (`idclient`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`carte`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`carte` (
  `numero_crt` INT(16) NOT NULL AUTO_INCREMENT,
  `date_peremption` DATE NULL,
  PRIMARY KEY (`numero_crt`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Compte`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Compte` (
  `numero_cmpt` INT(20) NOT NULL,
  `solde` INT(11) NULL,
  `code` INT(4) NULL,
  `numero_crt` INT(16) NULL,
  `id_client` INT(11) NULL,
  PRIMARY KEY (`numero_cmpt`),
  INDEX `numero_crt_idx` (`numero_crt` ASC) VISIBLE,
  INDEX `id_client_idx` (`id_client` ASC) VISIBLE,
  CONSTRAINT `numero_crt`
    FOREIGN KEY (`numero_crt`)
    REFERENCES `mydb`.`carte` (`numero_crt`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `id_client`
    FOREIGN KEY (`id_client`)
    REFERENCES `mydb`.`client` (`idclient`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Transaction_`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Transaction_` (
  `id_transaction_` BIGINT(25) NOT NULL,
  `numero_cmpt` INT(20) NOT NULL,
  `etat_validation` ENUM('valide', 'non valide') NULL,
  PRIMARY KEY (`id_transaction_`, `numero_cmpt`),
  INDEX `numero_cmpt_idx` (`numero_cmpt` ASC) VISIBLE,
  CONSTRAINT `numero_cmpt`
    FOREIGN KEY (`numero_cmpt`)
    REFERENCES `mydb`.`Compte` (`numero_cmpt`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Acces`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Acces` (
  `id_transaction_` BIGINT(25) NOT NULL,
  `numero_cmpt` INT(20) NOT NULL,
  `date` DATETIME(12) NULL,
  PRIMARY KEY (`id_transaction_`, `numero_cmpt`),
  INDEX `numero_cmpt_idx` (`numero_cmpt` ASC) VISIBLE,
  CONSTRAINT `numero_cmpt`
    FOREIGN KEY (`numero_cmpt`)
    REFERENCES `mydb`.`Compte` (`numero_cmpt`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT ``
    FOREIGN KEY (`id_transaction_`)
    REFERENCES `mydb`.`Transaction_` (`id_transaction_`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Virement`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Virement` (
  `id_transaction_` BIGINT(25) NOT NULL,
  `numero_cmpt` INT(20) NOT NULL,
  `montant` INT(11) NULL,
  `cpmt_beneficiaire` INT(20) NULL,
  INDEX `id_transaction__idx` (`id_transaction_` ASC) VISIBLE,
  INDEX `numero_cmpt_idx` (`numero_cmpt` ASC) VISIBLE,
  PRIMARY KEY (`id_transaction_`, `numero_cmpt`),
  INDEX `cpmt_beneficiaire_idx` (`cpmt_beneficiaire` ASC) VISIBLE,
  CONSTRAINT `id_transaction_`
    FOREIGN KEY (`id_transaction_`)
    REFERENCES `mydb`.`Transaction_` (`id_transaction_`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `numero_cmpt`
    FOREIGN KEY (`numero_cmpt`)
    REFERENCES `mydb`.`Compte` (`numero_cmpt`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `cpmt_beneficiaire`
    FOREIGN KEY (`cpmt_beneficiaire`)
    REFERENCES `mydb`.`Compte` (`numero_cmpt`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Retrait`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Retrait` (
  `id_transaction_` BIGINT(25) NOT NULL,
  `numero_cmpt` INT(20) NOT NULL,
  `montant` INT(11) NULL,
  INDEX `id_transaction__idx` (`id_transaction_` ASC) VISIBLE,
  INDEX `numero_cmpt_idx` (`numero_cmpt` ASC) VISIBLE,
  PRIMARY KEY (`numero_cmpt`, `id_transaction_`),
  CONSTRAINT `id_transaction_`
    FOREIGN KEY (`id_transaction_`)
    REFERENCES `mydb`.`Transaction_` (`id_transaction_`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `numero_cmpt`
    FOREIGN KEY (`numero_cmpt`)
    REFERENCES `mydb`.`Compte` (`numero_cmpt`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Consultation`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Consultation` (
  `id_transaction_` BIGINT(25) NOT NULL,
  `numero_cmpt` INT(20) NOT NULL,
  `solde` INT(11) NULL,
  PRIMARY KEY (`id_transaction_`, `numero_cmpt`),
  INDEX `numero_cmpt_idx` (`numero_cmpt` ASC) VISIBLE,
  CONSTRAINT `id_transaction_`
    FOREIGN KEY (`id_transaction_`)
    REFERENCES `mydb`.`Transaction_` (`id_transaction_`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `numero_cmpt`
    FOREIGN KEY (`numero_cmpt`)
    REFERENCES `mydb`.`Compte` (`numero_cmpt`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Distributeur`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Distributeur` (
  `numero_distr` INT(6) NOT NULL,
  `etat_caisse` INT(11) NULL,
  `etat_encre` INT(2) NULL,
  `etat_papier` INT(3) NULL,
  `etat_carte_avalees` INT(4) NULL,
  PRIMARY KEY (`numero_distr`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`AgentMaintenance`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`AgentMaintenance` (
  `numero_agent` INT(6) NOT NULL,
  `code_agent` INT(10) NULL,
  `nom` VARCHAR(20) NULL,
  `prenom` VARCHAR(20) NULL,
  PRIMARY KEY (`numero_agent`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`AccesMaintenance`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`AccesMaintenance` (
  `numero_distr` INT(6) NOT NULL,
  `numero_agent` INT(6) NOT NULL,
  `date _acces` DATE NULL,
  PRIMARY KEY (`numero_distr`, `numero_agent`),
  INDEX `numero_agent _idx` (`numero_agent` ASC) VISIBLE,
  CONSTRAINT `numero_distr `
    FOREIGN KEY (`numero_distr`)
    REFERENCES `mydb`.`Distributeur` (`numero_distr`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `numero_agent `
    FOREIGN KEY (`numero_agent`)
    REFERENCES `mydb`.`AgentMaintenance` (`numero_agent`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Effectuer`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Effectuer` (
  `id_transaction_,` BIGINT(25) NOT NULL,
  `numero_distr` INT(6) NOT NULL,
  PRIMARY KEY (`id_transaction_,`, `numero_distr`),
  INDEX `numero_distr _idx` (`numero_distr` ASC) VISIBLE,
  CONSTRAINT `id_transaction_, `
    FOREIGN KEY (`id_transaction_,`)
    REFERENCES `mydb`.`Transaction_` (`id_transaction_`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `numero_distr `
    FOREIGN KEY (`numero_distr`)
    REFERENCES `mydb`.`Distributeur` (`numero_distr`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
