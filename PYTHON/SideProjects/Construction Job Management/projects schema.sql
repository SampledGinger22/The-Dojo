-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema projects
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `projects` ;

-- -----------------------------------------------------
-- Schema projects
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `projects` DEFAULT CHARACTER SET utf8 ;
USE `projects` ;

-- -----------------------------------------------------
-- Table `projects`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `projects`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(255) NULL,
  `last_name` VARCHAR(255) NULL,
  `email` CHAR(60) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `projects`.`customers`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `projects`.`customers` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `display_name` VARCHAR(255) NULL,
  `notes` VARCHAR(255) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_customers_users_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_customers_users`
    FOREIGN KEY (`user_id`)
    REFERENCES `projects`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `projects`.`projects`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `projects`.`projects` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NULL,
  `start_date` DATE NULL,
  `start_time` TIME NULL,
  `projectscol` VARCHAR(45) NULL,
  `customer_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_projects_customers1_idx` (`customer_id` ASC) VISIBLE,
  CONSTRAINT `fk_projects_customers1`
    FOREIGN KEY (`customer_id`)
    REFERENCES `projects`.`customers` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `projects`.`addresses`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `projects`.`addresses` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `address` VARCHAR(255) NULL,
  `city` VARCHAR(255) NULL,
  `state` CHAR(2) NULL,
  `zip_code` CHAR(10) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `project_id` INT NOT NULL,
  `customer_id` INT NOT NULL,
  PRIMARY KEY (`id`, `customer_id`),
  INDEX `fk_addresses_projects1_idx` (`project_id` ASC) VISIBLE,
  INDEX `fk_addresses_customers1_idx` (`customer_id` ASC) VISIBLE,
  CONSTRAINT `fk_addresses_projects1`
    FOREIGN KEY (`project_id`)
    REFERENCES `projects`.`projects` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_addresses_customers1`
    FOREIGN KEY (`customer_id`)
    REFERENCES `projects`.`customers` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `projects`.`tasks`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `projects`.`tasks` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `checkbox` TINYINT NULL,
  `description` VARCHAR(255) NULL,
  `date` DATE NULL,
  `hours` INT NULL,
  `minutes` INT NULL,
  `taskscol` VARCHAR(45) NULL,
  `project_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_tasks_projects1_idx` (`project_id` ASC) VISIBLE,
  CONSTRAINT `fk_tasks_projects1`
    FOREIGN KEY (`project_id`)
    REFERENCES `projects`.`projects` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `projects`.`contacts`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `projects`.`contacts` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(255) NULL,
  `last_name` VARCHAR(255) NULL,
  `phone` VARCHAR(255) NULL,
  `email` VARCHAR(255) NULL,
  `notes` VARCHAR(255) NULL,
  `customer_id` INT NOT NULL,
  `project_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_contacts_customers1_idx` (`customer_id` ASC) VISIBLE,
  INDEX `fk_contacts_projects1_idx` (`project_id` ASC) VISIBLE,
  CONSTRAINT `fk_contacts_customers1`
    FOREIGN KEY (`customer_id`)
    REFERENCES `projects`.`customers` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_contacts_projects1`
    FOREIGN KEY (`project_id`)
    REFERENCES `projects`.`projects` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
