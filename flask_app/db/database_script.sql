-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema whatsdown
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema whatsdown
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `whatsdown` DEFAULT CHARACTER SET utf8 ;
USE `whatsdown` ;

-- -----------------------------------------------------
-- Table `whatsdown`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `whatsdown`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `fname` VARCHAR(45) NULL,
  `lname` VARCHAR(45) NULL,
  `nick` VARCHAR(45) NULL,
  `email` VARCHAR(45) NULL,
  `created_at` VARCHAR(45) NULL,
  `picture` VARCHAR(150) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `whatsdown`.`logins`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `whatsdown`.`logins` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `pwd` VARCHAR(45) NULL,
  `users_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_logins_users_idx` (`users_id` ASC) VISIBLE,
  CONSTRAINT `fk_logins_users`
    FOREIGN KEY (`users_id`)
    REFERENCES `whatsdown`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `whatsdown`.`chats`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `whatsdown`.`chats` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `user1_id` INT NOT NULL,
  `user2_id` INT NOT NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_chats_users1_idx` (`user1_id` ASC) VISIBLE,
  INDEX `fk_chats_users2_idx` (`user2_id` ASC) VISIBLE,
  CONSTRAINT `fk_chats_users1`
    FOREIGN KEY (`user1_id`)
    REFERENCES `whatsdown`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_chats_users2`
    FOREIGN KEY (`user2_id`)
    REFERENCES `whatsdown`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `whatsdown`.`messages`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `whatsdown`.`messages` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `content` VARCHAR(100) NULL,
  `timestamp` DATETIME NULL,
  `chat_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_messages_chats1_idx` (`chat_id` ASC) VISIBLE,
  CONSTRAINT `fk_messages_chats1`
    FOREIGN KEY (`chat_id`)
    REFERENCES `whatsdown`.`chats` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `whatsdown`.`reactions`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `whatsdown`.`reactions` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `character` INT NULL,
  `messages_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_reactions_messages1_idx` (`messages_id` ASC) VISIBLE,
  CONSTRAINT `fk_reactions_messages1`
    FOREIGN KEY (`messages_id`)
    REFERENCES `whatsdown`.`messages` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
