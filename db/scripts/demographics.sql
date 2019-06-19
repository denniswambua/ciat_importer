CREATE TABLE demographics (
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  enum VARCHAR(255),
  country VARCHAR(255),
  region VARCHAR(255),
  district VARCHAR(255),
  sector VARCHAR(255),
  ward VARCHAR(255),
  village VARCHAR(255),
  hhid VARCHAR(255),
  respname VARCHAR(255),
  respgender INT,
  respphone VARCHAR(255),
  Hhposition VARCHAR(255),
  other_Hhposition VARCHAR(255)
);