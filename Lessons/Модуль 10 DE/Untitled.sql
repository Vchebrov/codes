CREATE TABLE `Nobel_Laureates` (
  `full_name` varchar(255),
  `category` varchar(255),
  `year` int,
  `laureate_id` int,
  `birth_city` varchar(255)
);

CREATE TABLE `countries` (
  `country` varchar(255),
  `region` varchar(255),
  `population` int
);

CREATE TABLE `world_cities` (
  `country_code` varchar(255),
  `city_name` varchar(255)
);

CREATE TABLE `country_data` (
  `country_codecode` varchar(255)
);

ALTER TABLE `world_cities` ADD FOREIGN KEY (`city_name`) REFERENCES `Nobel_Laureates` (`birth_city`);

ALTER TABLE `country_data` ADD FOREIGN KEY (`country_codecode`) REFERENCES `world_cities` (`country_code`);

ALTER TABLE `countries` ADD FOREIGN KEY (`country`) REFERENCES `world_cities` (`country_code`);
