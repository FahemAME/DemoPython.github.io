-- -----------------------------------------------------
-- insertion des cartes

INSERT INTO `mydb`.`carte` (`numero_crt`, `date_peremption`) VALUES ('100000000000001', '2021-01-15');
INSERT INTO `mydb`.`carte` (`numero_crt`, `date_peremption`) VALUES ('100000000000002', '2021-06-15');
INSERT INTO `mydb`.`carte` (`numero_crt`, `date_peremption`) VALUES ('100000000000003', '2021-01-12');
INSERT INTO `mydb`.`carte` (`numero_crt`, `date_peremption`) VALUES ('100000000000004', '2019-01-12');

-- -----------------------------------------------------
-- insertion des clients

INSERT INTO `mydb`.`client` (`nom`, `prenom`) VALUES ('AMIR', 'Amir');
INSERT INTO `mydb`.`client` (`nom`, `prenom`) VALUES ('CRIS', 'Ronaldo');
INSERT INTO `mydb`.`client` (`nom`, `prenom`) VALUES ('MEQRAN', 'Yuba');
INSERT INTO `mydb`.`client` (`nom`, `prenom`) VALUES ('NOM1', 'Prenom1');

-- -----------------------------------------------------
-- insertion des comptes

INSERT INTO `compte` (`numero_cmpt`,`solde`, `code`, `numero_crt`, `id_client`) 
VALUES ('10000000000000100001','100000', '1111',
( SELECT numero_crt FROM carte where numero_crt='100000000000001'), 
(SELECT idclient FROM client where idclient='4'));
INSERT INTO `compte` (`numero_cmpt`,`solde`, `code`, `numero_crt`, `id_client`) 
VALUES ('10000000000000100002','200000', '2222',
(SELECT numero_crt FROM carte where numero_crt='100000000000002'), 
(SELECT idclient FROM client where idclient='6'));
INSERT INTO `compte` (`numero_cmpt`,`solde`, `code`, `numero_crt`, `id_client`) 
VALUES ('10000000000000100007','70000000', '7777',
(SELECT numero_crt FROM carte where numero_crt='100000000000003'),
(SELECT idclient FROM client where idclient= '5'));
INSERT INTO `compte` (`numero_cmpt`,`solde`, `code`, `numero_crt`, `id_client`) 
VALUES ('10000000000000100005','100', '1234',
(SELECT numero_crt FROM carte where numero_crt='100000000000004'), 
(SELECT idclient FROM client where idclient='7'));

-- -----------------------------------------------------
-- insertion des agents de maintenance

INSERT INTO `mydb`.`agentmaintenance` (`numero_agent`, `code_agent`, `nom`, `prenom`) 
VALUES ('100001', '1234567890', 'AGENT1', 'Agent1');
INSERT INTO `mydb`.`agentmaintenance` (`numero_agent`, `code_agent`, `nom`, `prenom`) 
VALUES ('100002', '1000012345', 'AGENT2', 'Agent2');

-- -----------------------------------------------------
-- insertion des distributeurs

INSERT INTO `mydb`.`distributeur` (`numero_distr`, `etat_caisse`,`etat_carte_avalees`) 
VALUES ('100123', '50000','0');
INSERT INTO `mydb`.`distributeur` (`numero_distr`, `etat_caisse`,`etat_carte_avalees`)
 VALUES ('100124', '5000','0');
