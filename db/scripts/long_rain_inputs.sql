CREATE TABLE long_rain_inputs (
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  district_23 VARCHAR(255),
  ward_23 VARCHAR(255),
  village_23 VARCHAR(255),
  hhid_23 VARCHAR(255),
  long_rain_input_pos INT,
  long_rain_input_type VARCHAR(255),
  long_rain_input_other_fertilizer VARCHAR(255),
  long_rain_input_other_type VARCHAR(255),
  long_rain_input_quantity VARCHAR(255),
  long_rain_input_units VARCHAR(255),
  long_rain_input_total_costs VARCHAR(255)
);