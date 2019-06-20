CREATE TABLE dry_season_inputs (
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  district_31 VARCHAR(255),
  ward_31 VARCHAR(255),
  village_31 VARCHAR(255),
  hhid_31 VARCHAR(255),
  dry_rain_input_pos VARCHAR(255),
  dry_rain_input_type VARCHAR(255),
  dry_rain_input_other_fertilizer VARCHAR(255),
  dry_rain_input_other_type VARCHAR(255),
  dry_rain_input_quantity VARCHAR(255),
  dry_rain_input_units VARCHAR(255),
  dry_rain_input_total_costs VARCHAR(255)
);