CREATE TABLE subplots_details (
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  sub_plot INT,
  district_2 VARCHAR(255),
  ward_2 VARCHAR(255),
  village_2 VARCHAR(255),
  hhid_2 VARCHAR(255),
  subplot_ID VARCHAR(255),
  subplot_acreas INT,
  tenant_owner VARCHAR(255),
  decision_maker VARCHAR(255),
  other_tenant_owner VARCHAR(255),
  land_type VARCHAR(255),
  long_rain_utilization VARCHAR(255),
  long_rain_utilization_crop VARCHAR(255),
  long_rains_croppedA_count INT,
  long_rains_croppedB_count INT,
  short_rain_utilization VARCHAR(255),
  short_rain_utilization_crop VARCHAR(255),
  short_rains_croppedA_count INT,
  short_rains_croppedB_count INT,
  dry_season_utilization VARCHAR(255),
  dry_season_utilization_crop VARCHAR(255),
  dry_season_croppedA_count INT,
  dry_season_croppedB_count INT,
  long_rain_season_count INT,
  long_rains_Number_Intercrop_components VARCHAR(255),
  long_rains_Intercrops_components_count VARCHAR(255),
  short_rain_season_count INT,
  dry_rain_season_count INT,
  dry_rains_Number_Intercrop_components VARCHAR(255),
  dry_rains_Intercrops_components_count VARCHAR(255),
  planted_with_forages VARCHAR(255),
  if_not_planted_sub_plotID VARCHAR(255),
  if_not_planted_percentage INT,
  plot_ID_forage_area INT,
  forage__Tractor_ploughing_note_summary_of_farming_activities VARCHAR(255)
);