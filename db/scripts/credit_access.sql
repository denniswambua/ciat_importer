CREATE TABLE credit_access (
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  loan_pos VARCHAR(255),
  district_15 VARCHAR(255),
  ward_15 VARCHAR(255),
  village_15 VARCHAR(255),
  hhid_15 VARCHAR(255),
  loan_type VARCHAR(255),
  loan_when VARCHAR(255),
  loan_amount VARCHAR(255),
  loan_interest VARCHAR(255),
  loan_repayment_duration VARCHAR(255),
  loan_source VARCHAR(255),
  loan_source_other VARCHAR(255),
  loan_purpose VARCHAR(255),
  loan_purpose_other VARCHAR(255),
  loan_satisfied VARCHAR(255)
);