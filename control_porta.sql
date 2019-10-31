-- --------------------------------------------------------
-- Servidor:                     127.0.0.1
-- Versão do servidor:           10.4.8-MariaDB - mariadb.org binary distribution
-- OS do Servidor:               Win64
-- HeidiSQL Versão:              10.2.0.5599
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- Copiando estrutura do banco de dados para control_porta
CREATE DATABASE IF NOT EXISTS `control_porta` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `control_porta`;

-- Copiando estrutura para tabela control_porta.porta
CREATE TABLE IF NOT EXISTS `porta` (
  `portaId` int(11) NOT NULL AUTO_INCREMENT,
  `NomeLab` varchar(255) DEFAULT NULL,
  `labCode` int(11) DEFAULT NULL,
  `horarioEntra` datetime DEFAULT NULL,
  `horarioSai` datetime DEFAULT NULL,
  `userId` int(11) DEFAULT NULL,
  PRIMARY KEY (`portaId`),
  KEY `fk_user_porta` (`userId`),
  CONSTRAINT `fk_user_porta` FOREIGN KEY (`userId`) REFERENCES `usuario` (`userId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Copiando dados para a tabela control_porta.porta: ~4 rows (aproximadamente)
/*!40000 ALTER TABLE `porta` DISABLE KEYS */;
INSERT INTO `porta` (`portaId`, `NomeLab`, `labCode`, `horarioEntra`, `horarioSai`, `userId`) VALUES
	(1, 'digital', 1, '2019-04-19 13:08:22', '2019-04-19 13:58:22', 3),
	(2, 'programação', 1, '2019-04-19 13:08:22', '2019-04-19 13:58:22', 1),
	(3, 'digital', 1, '2019-04-20 20:08:22', '2019-04-20 23:58:22', 1),
	(4, 'digital', 1, '2019-04-19 13:08:22', '2019-04-19 13:58:22', 3);
/*!40000 ALTER TABLE `porta` ENABLE KEYS */;

-- Copiando estrutura para tabela control_porta.usuario
CREATE TABLE IF NOT EXISTS `usuario` (
  `userId` int(11) NOT NULL AUTO_INCREMENT,
  `Nome_Completo` varchar(255) DEFAULT NULL,
  `login` varchar(255) DEFAULT NULL,
  `senha` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`userId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Copiando dados para a tabela control_porta.usuario: ~3 rows (aproximadamente)
/*!40000 ALTER TABLE `usuario` DISABLE KEYS */;
INSERT INTO `usuario` (`userId`, `Nome_Completo`, `login`, `senha`) VALUES
	(1, 'aluno', '8888', '8888'),
	(2, 'ademir', '4444', '4444'),
	(3, 'tiaxer', '555', '555');
/*!40000 ALTER TABLE `usuario` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
