CREATE TABLE short_rain_season (
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  district_25 VARCHAR(255),
  ward_25 VARCHAR(255),
  village_25 VARCHAR(255),
  hhid_25 VARCHAR(255),
  short_rain_crops VARCHAR(255),
  short_rain_types_variety INT,
  short_rain_start_month VARCHAR(255),
  short_rain_end_month VARCHAR(255),
  short_rain_if_intercropped VARCHAR(255),
  othershort_rain_crops VARCHAR(255),
  short_rain_season_activity_notes VARCHAR(255),
  short_rain_crop_products_count INT,
  short_rains_Number_Intercrop_components INT,
  short_rains_Intercrops_components_count INT
);