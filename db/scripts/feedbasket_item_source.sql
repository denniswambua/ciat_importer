CREATE TABLE feedbasket_item_source (
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  district_912 VARCHAR(255),
  ward_912 VARCHAR(255),
  village_912 VARCHAR(255),
  hhid_912 VARCHAR(255),
  Source_Natural_grasses_fresh VARCHAR(255),
  Source_Crop_residue_dry VARCHAR(255),
  Source_Planted_Fodder VARCHAR(255),
  Source_Green_crop_by_products VARCHAR(255),
  Source_Supplements_Concentrates VARCHAR(255)
);