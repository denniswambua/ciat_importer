CREATE TABLE long_rain_season (
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  district_21 VARCHAR(255),
  ward_21 VARCHAR(255),
  village_21 VARCHAR(255),
  hhid_21 VARCHAR(255),
  long_rain_crops VARCHAR(255),
  long_rain_types_variety INT,
  long_rain_start_month VARCHAR(255),
  long_rain_end_month VARCHAR(255),
  long_rain_if_intercropped VARCHAR(255),
  otherlong_rain_crops VARCHAR(255),
  long_rain_crop_products_count INT
);