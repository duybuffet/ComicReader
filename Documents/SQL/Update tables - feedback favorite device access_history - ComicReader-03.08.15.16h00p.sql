USE comicreader;

DROP TABLE `comicreader`.`favorite`;

DROP TABLE `comicreader`.`feedback`;

DROP TABLE `comicreader`.`access_history`;

DROP TABLE `comicreader`.`device`;
-- -----------------------------------------------------
-- Table `comicreader`.`device`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `comicreader`.`device` ;

CREATE TABLE IF NOT EXISTS `comicreader`.`device` (
  `id` VARCHAR(255) NOT NULL,
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
  `device_id` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `fk_favorite_2`
    FOREIGN KEY (`ebook_id`)
    REFERENCES `comicreader`.`ebook` (`id`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_favorite_device1`
    FOREIGN KEY (`device_id`)
    REFERENCES `comicreader`.`device` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `fk_favorite_2_idx` ON `comicreader`.`favorite` (`ebook_id` ASC);

CREATE INDEX `fk_favorite_device1_idx` ON `comicreader`.`favorite` (`device_id` ASC);


-- -----------------------------------------------------
-- Table `comicreader`.`access_history`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `comicreader`.`access_history` ;

CREATE TABLE IF NOT EXISTS `comicreader`.`access_history` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `date_request` DATETIME NULL,
  `num_request` INT NULL,
  `device_id` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `fk_access_history_device1`
    FOREIGN KEY (`device_id`)
    REFERENCES `comicreader`.`device` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `fk_access_history_device1_idx` ON `comicreader`.`access_history` (`device_id` ASC);


-- -----------------------------------------------------
-- Table `comicreader`.`feedback`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `comicreader`.`feedback` ;

CREATE TABLE IF NOT EXISTS `comicreader`.`feedback` (
  `id` INT NOT NULL AUTO_INCREMENT COMMENT '	',
  `title` TEXT NULL,
  `send_date` DATE NULL,
  `status` TINYINT(1) NULL,
  `description` TEXT NULL,
  `chapter_id` INT NULL,
  `ebook_id` INT NULL,
  `device_id` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `fk_feedback_chapter1`
    FOREIGN KEY (`chapter_id`)
    REFERENCES `comicreader`.`chapter` (`id`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_feedback_ebook1`
    FOREIGN KEY (`ebook_id`)
    REFERENCES `comicreader`.`ebook` (`id`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_feedback_device1`
    FOREIGN KEY (`device_id`)
    REFERENCES `comicreader`.`device` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `fk_feedback_chapter1_idx` ON `comicreader`.`feedback` (`chapter_id` ASC);

CREATE INDEX `fk_feedback_ebook1_idx` ON `comicreader`.`feedback` (`ebook_id` ASC);

CREATE INDEX `fk_feedback_device1_idx` ON `comicreader`.`feedback` (`device_id` ASC);