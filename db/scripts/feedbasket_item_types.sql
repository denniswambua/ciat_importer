CREATE TABLE feedbasket_item_types (
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  district_911 VARCHAR(255),
  ward_911 VARCHAR(255),
  village_911 VARCHAR(255),
  hhid_911 VARCHAR(255),
  Natural_grasses_fresh VARCHAR(255),
  Crop_residue_dry VARCHAR(255),
  Planted_Fodder VARCHAR(255),
  Green_crop_by_products VARCHAR(255),
  Supplements_Concentrates VARCHAR(255)
);