-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema projects_schema
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `projects_schema` ;

-- -----------------------------------------------------
-- Schema projects_schema
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `projects_schema` DEFAULT CHARACTER SET utf8mb3 ;
USE `projects_schema` ;

-- -----------------------------------------------------
-- Table `projects_schema`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `projects_schema`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(255) NULL DEFAULT NULL,
  `last_name` VARCHAR(255) NULL DEFAULT NULL,
  `email` CHAR(60) NULL DEFAULT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `projects_schema`.`customers`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `projects_schema`.`customers` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `display_name` VARCHAR(255) NULL DEFAULT NULL,
  `notes` VARCHAR(255) NULL DEFAULT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_customers_users_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_customers_users`
    FOREIGN KEY (`user_id`)
    REFERENCES `projects_schema`.`users` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `projects_schema`.`projects`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `projects_schema`.`projects` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NULL DEFAULT NULL,
  `start_date` DATE NULL DEFAULT NULL,
  `end_date` DATE NULL DEFAULT NULL,
  `customer_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_projects_customers1_idx` (`customer_id` ASC) VISIBLE,
  CONSTRAINT `fk_projects_customers1`
    FOREIGN KEY (`customer_id`)
    REFERENCES `projects_schema`.`customers` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `projects_schema`.`addresses`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `projects_schema`.`addresses` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `address` VARCHAR(255) NULL DEFAULT NULL,
  `city` VARCHAR(255) NULL DEFAULT NULL,
  `state` CHAR(2) NULL DEFAULT NULL,
  `zip_code` CHAR(10) NULL DEFAULT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `project_id` INT NOT NULL,
  `customer_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_addresses_customers2_idx` (`customer_id` ASC) VISIBLE,
  INDEX `fk_addresses_projects1_idx` (`project_id` ASC) VISIBLE,
  CONSTRAINT `fk_addresses_customers2`
    FOREIGN KEY (`customer_id`)
    REFERENCES `projects_schema`.`customers` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_addresses_projects1`
    FOREIGN KEY (`project_id`)
    REFERENCES `projects_schema`.`projects` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `projects_schema`.`titles`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `projects_schema`.`titles` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(45) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `projects_schema`.`contacts`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `projects_schema`.`contacts` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(255) NULL DEFAULT NULL,
  `last_name` VARCHAR(255) NULL DEFAULT NULL,
  `phone` VARCHAR(255) NULL DEFAULT NULL,
  `email` VARCHAR(255) NULL DEFAULT NULL,
  `notes` VARCHAR(255) NULL DEFAULT NULL,
  `customer_id` INT NOT NULL,
  `project_id` INT NOT NULL,
  `title_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_contacts_customers1_idx` (`customer_id` ASC) VISIBLE,
  INDEX `fk_contacts_projects1_idx` (`project_id` ASC) VISIBLE,
  INDEX `fk_contacts_titles1_idx` (`title_id` ASC) VISIBLE,
  CONSTRAINT `fk_contacts_customers1`
    FOREIGN KEY (`customer_id`)
    REFERENCES `projects_schema`.`customers` (`id`),
  CONSTRAINT `fk_contacts_projects1`
    FOREIGN KEY (`project_id`)
    REFERENCES `projects_schema`.`projects` (`id`),
  CONSTRAINT `fk_contacts_titles1`
    FOREIGN KEY (`title_id`)
    REFERENCES `projects_schema`.`titles` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `projects_schema`.`tasks`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `projects_schema`.`tasks` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `checkbox` TINYINT NULL DEFAULT NULL,
  `description` VARCHAR(255) NULL DEFAULT NULL,
  `date` DATE NULL DEFAULT NULL,
  `hours` INT NULL DEFAULT NULL,
  `minutes` INT NULL DEFAULT NULL,
  `taskscol` VARCHAR(45) NULL DEFAULT NULL,
  `project_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_tasks_projects1_idx` (`project_id` ASC) VISIBLE,
  CONSTRAINT `fk_tasks_projects1`
    FOREIGN KEY (`project_id`)
    REFERENCES `projects_schema`.`projects` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
