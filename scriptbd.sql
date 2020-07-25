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
CREATE SCHEMA IF NOT EXISTS `startwars` DEFAULT CHARACTER SET utf8 ;
-- -----------------------------------------------------
-- Schema indice_ejemplo
-- -----------------------------------------------------
USE `startwars` ;

-- -----------------------------------------------------
-- Table `mydb`.`peliculas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `startwars`.`peliculas` (
  `idPl` INT NOT NULL AUTO_INCREMENT,
  `nombrePl` VARCHAR(60) NOT NULL,
  `productoresPl` VARCHAR(500) NOT NULL,
  `detallePl` VARCHAR(500) NOT NULL,
  `directorPl` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idPl`))
ENGINE = InnoDB;
-- ALTER TABLE `startwars`.`peliculas` ADD `detallePl` VARCHAR(500) NOT NULL;
-- ALTER TABLE `startwars`.`peliculas` 
-- CHANGE COLUMN `productoresPl` `productoresPl` VARCHAR(500) NOT NULL ;
-- ALTER TABLE `startwars`.`peliculas` 
-- CHANGE COLUMN `nombrePl` `nombrePl` VARCHAR(60) NOT NULL ;
-- ALTER TABLE `startwars`.`peliculas` 
-- CHANGE COLUMN `planetasPl` `planetasPl` VARCHAR(60) NOT NULL ;
-- ALTER TABLE `startwars`.`peliculas` drop COLUMN `peliculas`.`planetasPl`;

-- -----------------------------------------------------
-- Table `mydb`.`personajes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `startwars`.`personajes` (
  `idPj` INT NOT NULL AUTO_INCREMENT,
  `nombrePj` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idPj`)
)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `startwars`.`planetas` (
  `idPla` INT NOT NULL AUTO_INCREMENT,
  `nombrePla` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idPla`)
)
ENGINE = InnoDB;

Create table if not exists `startwars`.`persopelis` (
  `idpeli` INT NOT NULL,
  `idper` INT NOT NULL,
  PRIMARY KEY (`idpeli`,`idper`),
  CONSTRAINT `peliculas_personajes_fk`
    FOREIGN KEY (`idpeli`)
    REFERENCES `startwars`.`peliculas` (`idPl`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
	CONSTRAINT `peliculas_personajes2_fk`
    FOREIGN KEY (`idper`)
    REFERENCES `startwars`.`personajes` (`idPj`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION    
)ENGINE = InnoDB;

Create table if not exists `startwars`.`planetaspelis` (
  `idpeli` INT NOT NULL,
  `idplaneta` INT NOT NULL,
  PRIMARY KEY (`idpeli`,`idplaneta`),
  CONSTRAINT `peliculas_planetas_fk`
    FOREIGN KEY (`idpeli`)
    REFERENCES `startwars`.`peliculas` (`idPl`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
	CONSTRAINT `peliculas_planetas2_fk`
    FOREIGN KEY (`idplaneta`)
    REFERENCES `startwars`.`planetas` (`idPla`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION    
)ENGINE = InnoDB;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
