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
  `horarioEntra` datetime DEFAULT NULL,
  `horarioSai` datetime DEFAULT NULL,
  PRIMARY KEY (`portaId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Copiando dados para a tabela control_porta.porta: ~0 rows (aproximadamente)
/*!40000 ALTER TABLE `porta` DISABLE KEYS */;
/*!40000 ALTER TABLE `porta` ENABLE KEYS */;

-- Copiando estrutura para tabela control_porta.usuario
CREATE TABLE IF NOT EXISTS `usuario` (
  `userId` int(11) NOT NULL AUTO_INCREMENT,
  `Nome_Completo` varchar(255) DEFAULT NULL,
  `login` varchar(255) DEFAULT NULL,
  `senha` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`userId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Copiando dados para a tabela control_porta.usuario: ~0 rows (aproximadamente)
/*!40000 ALTER TABLE `usuario` DISABLE KEYS */;
/*!40000 ALTER TABLE `usuario` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
