CREATE TABLE forage_inputs (
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  district_34 VARCHAR(255),
  ward_34 VARCHAR(255),
  village_34 VARCHAR(255),
  hhid_34 VARCHAR(255),
  forage_inputs_pos VARCHAR(255),
  forage__input_type VARCHAR(255),
  forage__input_other_fertilizer VARCHAR(255),
  forage__input_other_type VARCHAR(255),
  forage__input_quantity VARCHAR(255),
  forage__input_units VARCHAR(255),
  forage__input_total_costs VARCHAR(255)
);