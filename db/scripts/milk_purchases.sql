CREATE TABLE milk_purchases (
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  district_011 VARCHAR(255),
  ward_011 VARCHAR(255),
  village_011 VARCHAR(255),
  hhid_011 VARCHAR(255),
  hh_buy_milk_buyers VARCHAR(255),
  hh_buy_packaged_milk VARCHAR(255),
  hh_buy_processed_other_milk_products VARCHAR(255)
);