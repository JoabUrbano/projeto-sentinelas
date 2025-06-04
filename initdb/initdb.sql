CREATE DATABASE IF NOT EXISTS sentinelas;

-- Usa o banco criado
USE sentinelas;

CREATE TABLE IF NOT EXISTS `tb_avistagem_deteccao` (
	`id` int AUTO_INCREMENT NOT NULL UNIQUE,
	`expedicao` varchar(255) NOT NULL,
	`pernada` varchar(255) NOT NULL,
	`navio` varchar(255) NOT NULL,
	`data` timestamp NOT NULL,
	`registro` varchar(255) NOT NULL,
	`tipo_som` varchar(255) NOT NULL,
	`especie` varchar(255) NOT NULL,
	`nome_comum` varchar(255) NOT NULL,
	`latitude` float NOT NULL,
	`longitude` float NOT NULL,
	`filhotes` int NOT NULL,
	`observacoes` varchar(255) NOT NULL,
	`tamanho_grupo_minimo` int NOT NULL,
	`tamanho_grupo_maximo` int NOT NULL,
	PRIMARY KEY (`id`)
);
