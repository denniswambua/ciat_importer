CREATE TABLE additional_supplements (
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  dairy_additional_supplements_no VARCHAR(255),
  district_10 VARCHAR(255),
  ward_10 VARCHAR(255),
  village_10 VARCHAR(255),
  hhid_10 VARCHAR(255),
  dairy_additional_supplements_type_of_feed VARCHAR(255),
  Same_quantity_throughout VARCHAR(255),
  Qty_begining VARCHAR(255),
  Qty_begining_units VARCHAR(255),
  Qty_middle VARCHAR(255),
  Qty_middle_units VARCHAR(255),
  Qty_End VARCHAR(255),
  Qty_End_units VARCHAR(255),
  Qty_throughout_lactation VARCHAR(255),
  Qty_throughout_lactation_units VARCHAR(255)
);