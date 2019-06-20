CREATE TABLE short_rain_inputs (
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  district_27 VARCHAR(255),
  ward_27 VARCHAR(255),
  village_27 VARCHAR(255),
  hhid_27 VARCHAR(255),
  short_rain_input_pos INT,
  short_rain_input_type VARCHAR(255),
  short_rain_input_other_fertilizer VARCHAR(255),
  short_rain_input_other_type VARCHAR(255),
  short_rain_input_quantity VARCHAR(255),
  short_rain_input_units VARCHAR(255),
  short_rain_input_total_costs VARCHAR(255),
  short_rain_input_notes VARCHAR(255)
);