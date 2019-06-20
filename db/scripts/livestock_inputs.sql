REATE TABLE livestock_inputs (
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  district_13 VARCHAR(255),
  ward_13 VARCHAR(255),
  village_13 VARCHAR(255),
  hhid_13 VARCHAR(255),
  livestock_activity_ID_1 VARCHAR(255),
  livestock_activity_breed_name_1 VARCHAR(255),
  Livestock_activity_name_1 VARCHAR(255),
  livestock_input_type VARCHAR(255),
  livestock_input_type_quantity VARCHAR(255),
  livestock_input_type_units VARCHAR(255),
  livestock_input_type_total_costs VARCHAR(255),
  notes_livestock_inputs_details VARCHAR(255)
);