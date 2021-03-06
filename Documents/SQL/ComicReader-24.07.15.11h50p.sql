SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

DROP SCHEMA IF EXISTS `comicreader` ;
CREATE SCHEMA IF NOT EXISTS `comicreader` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci ;
USE `comicreader` ;

-- -----------------------------------------------------
-- Table `comicreader`.`ebook`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `comicreader`.`ebook` ;

CREATE TABLE IF NOT EXISTS `comicreader`.`ebook` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NULL,
  `url` TEXT NULL,
  `cover` TEXT NULL,
  `author` VARCHAR(225) NULL,
  `update` DATETIME NULL,
  `description` TEXT NULL,
  `complete` TINYINT(1) NULL,
  `check` TINYINT(1) NULL,
  `totalchap` INT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `comicreader`.`view_count`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `comicreader`.`view_count` ;

CREATE TABLE IF NOT EXISTS `comicreader`.`view_count` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `num_view` INT NOT NULL,
  `ebook_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `fk_view_1`
    FOREIGN KEY (`ebook_id`)
    REFERENCES `comicreader`.`ebook` (`id`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `fk_view_1_idx` ON `comicreader`.`view_count` (`ebook_id` ASC);


-- -----------------------------------------------------
-- Table `comicreader`.`chapter`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `comicreader`.`chapter` ;

CREATE TABLE IF NOT EXISTS `comicreader`.`chapter` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `ebook_id` INT NOT NULL,
  `name` TEXT NOT NULL,
  `url` TEXT NOT NULL,
  `description` TEXT NULL,
  `status` VARCHAR(45) NULL,
  `update` DATETIME NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `fk_chapter_1`
    FOREIGN KEY (`ebook_id`)
    REFERENCES `comicreader`.`ebook` (`id`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `fk_chapter_1_idx` ON `comicreader`.`chapter` (`ebook_id` ASC);


-- -----------------------------------------------------
-- Table `comicreader`.`image`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `comicreader`.`image` ;

CREATE TABLE IF NOT EXISTS `comicreader`.`image` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `chapter_id` INT NOT NULL,
  `url` TEXT NOT NULL,
  `status` TINYINT(1) NULL,
  `name` VARCHAR(255) NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `fk_image_1`
    FOREIGN KEY (`chapter_id`)
    REFERENCES `comicreader`.`chapter` (`id`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `fk_image_1_idx` ON `comicreader`.`image` (`chapter_id` ASC);


-- -----------------------------------------------------
-- Table `comicreader`.`category`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `comicreader`.`category` ;

CREATE TABLE IF NOT EXISTS `comicreader`.`category` (
  `id` INT NOT NULL,
  `name` VARCHAR(225) NOT NULL,
  `description` TEXT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `comicreader`.`bookcat`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `comicreader`.`bookcat` ;

CREATE TABLE IF NOT EXISTS `comicreader`.`bookcat` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `ebook_id` INT NOT NULL,
  `category_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `fk_bookcat_1`
    FOREIGN KEY (`category_id`)
    REFERENCES `comicreader`.`category` (`id`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_bookcat_2`
    FOREIGN KEY (`ebook_id`)
    REFERENCES `comicreader`.`ebook` (`id`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `fk_bookcat_1_idx` ON `comicreader`.`bookcat` (`category_id` ASC);

CREATE INDEX `fk_bookcat_2_idx` ON `comicreader`.`bookcat` (`ebook_id` ASC);


-- -----------------------------------------------------
-- Table `comicreader`.`device`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `comicreader`.`device` ;

CREATE TABLE IF NOT EXISTS `comicreader`.`device` (
  `id` INT NOT NULL,
  `last_date` DATETIME NOT NULL,
  `block` TINYINT(1) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `comicreader`.`favorite`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `comicreader`.`favorite` ;

CREATE TABLE IF NOT EXISTS `comicreader`.`favorite` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `ebook_id` INT NOT NULL,
  `device_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `fk_favorite_1`
    FOREIGN KEY (`device_id`)
    REFERENCES `comicreader`.`device` (`id`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_favorite_2`
    FOREIGN KEY (`ebook_id`)
    REFERENCES `comicreader`.`ebook` (`id`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `fk_favorite_1_idx` ON `comicreader`.`favorite` (`device_id` ASC);

CREATE INDEX `fk_favorite_2_idx` ON `comicreader`.`favorite` (`ebook_id` ASC);


-- -----------------------------------------------------
-- Table `comicreader`.`access_history`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `comicreader`.`access_history` ;

CREATE TABLE IF NOT EXISTS `comicreader`.`access_history` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `device_id` INT NOT NULL,
  `date_request` DATETIME NULL,
  `num_request` INT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `fk_accesshistory_1`
    FOREIGN KEY (`device_id`)
    REFERENCES `comicreader`.`device` (`id`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `fk_accesshistory_1_idx` ON `comicreader`.`access_history` (`device_id` ASC);


-- -----------------------------------------------------
-- Table `comicreader`.`feedback`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `comicreader`.`feedback` ;

CREATE TABLE IF NOT EXISTS `comicreader`.`feedback` (
  `id` INT NOT NULL COMMENT '	',
  `device_id` INT NULL,
  `title` TEXT NULL,
  `send_date` DATE NULL,
  `status` TINYINT(1) NULL,
  `description` TEXT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `fk_feedback_1`
    FOREIGN KEY (`device_id`)
    REFERENCES `comicreader`.`device` (`id`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `fk_feedback_1_idx` ON `comicreader`.`feedback` (`device_id` ASC);


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
