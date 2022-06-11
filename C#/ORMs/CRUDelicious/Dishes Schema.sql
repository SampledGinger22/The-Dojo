-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema dishes_schema
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `dishes_schema` ;

-- -----------------------------------------------------
-- Schema dishes_schema
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `dishes_schema` DEFAULT CHARACTER SET utf8 ;
USE `dishes_schema` ;

-- -----------------------------------------------------
-- Table `dishes_schema`.`dishes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dishes_schema`.`dishes` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `Name` VARCHAR(255) NULL,
  `Chef` VARCHAR(255) NULL,
  `Tastiness` INT(11) NULL,
  `Calories` INT(11) NULL,
  `Description` TEXT NULL,
  `CreatedAt` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `UpdatedAt` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
