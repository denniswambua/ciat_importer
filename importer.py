import xlrd

from connection import Connection
from loader.baseloader import BaseLoader


MAIN = ["starttime","endtime","today","const","Demographics_count","district_02","ward_02","village_02","hhid_02","hhid_confirmed","Seasons_count","hh_type","hhh_marital","hhh_read_write","hhh_indigenous","hhh_move_here","hh_no","hh_position_dummy","offfarm_desc_dummy","hh_members_count","age_num","bigger_plots","type_of_tenure_dummy","subplots_info_count","other_plots_planning_forages","other_plots_planning_forages_codes","other_plots_planning_forages_year","other_plots_planning_forages_season","non_ruminant_livestock_no","non_ruminant_livestock_count","ruminant_yesno","categories_no","species9_dummy","breed9_dummy","sex9_dummy","ageclass9_dummy","ruminants_count","notes9","livestock1","livestock2","livestock3","livestock4","livestock5","livestock6","livestock7","livestock8","livestock9","livestock10","livestock11","livestock12","livestock13","livestock14","livestock15","livestock16","livestock17","livestock18","livestock19","livestock20","feeding_seasons_no","Typical_Livestock_Feedbasket_count","lactation_supplements","additional_supplements_no","dairy_additional_supplements_count","confirm_no_of_all_livestock","livestock_products_utilization_count","value_addition","value_addition_prdct","value_addition_frqncy","value_addition_ltrs","value_addition_other","vol_produced","vol_consumed","vol_sold","vol_gift","product_sale_price","milk_purchases_count","livestock_activity_ID_dummy","livestock_activity_breed_dummy","Livestock_activity_dummy","management_practicesA_count","management_practicesB_count","feed_conservation_profitable","reducing_area_under_fodder","use_fresh_manure_profitable","use_fresh_manure_plants","natural_env_compared_10_yrs","believe","believe_explanation","manure_production_comments","long_term_dairy_credit","num_dairy_credit","loans_count","access_to_credit_comments","Food_insecurity_count","HDDS_count","gpsloc"]
DEMOGRAPHIC = ["enum","country","region","district","sector","ward","village","hhid","respname","respgender","respphone","Hhposition","other_Hhposition"]
SEASONS = ["district_01","ward_01","village_01","hhid_01","Long_rain_season","Short_rain_season","Long_Dry_season","short_Dry_season"]
HH_MEMBERS = ["hh_member_no","district_1","ward_1","village_1","hhid_1","hh_position","hhposition_name","hh_position_other","hh_age","hh_age_1","hh_gender","Highest_completed_education","labour_availability","work_calendar","activmain","activshort","dry_season","offfarm_desc","offfarmwork_name","offfarmwork_other","experience","hh_notes"]
SUBPLOT_DETAILS = ["sub_plot","district_2","ward_2","village_2","hhid_2","subplot_ID","subplot_acreas","tenant_owner","decision_maker","other_tenant_owner","land_type","long_rain_utilization","long_rain_utilization_crop","long_rains_croppedA_count","long_rains_croppedB_count","short_rain_utilization","short_rain_utilization_crop","short_rains_croppedA_count","short_rains_croppedB_count","dry_season_utilization","dry_season_utilization_crop","dry_season_croppedA_count","dry_season_croppedB_count","long_rain_season_count","long_rains_Number_Intercrop_components","long_rains_Intercrops_components_count","short_rain_season_count","dry_rain_season_count","dry_rains_Number_Intercrop_components","dry_rains_Intercrops_components_count","planted_with_forages","if_not_planted_sub_plotID","if_not_planted_percentage","plot_ID_forage_area","forage__Tractor_ploughing_note_summary_of_farming_activities"]
LONG_RAINS_CROPPEDA = ["district_221","ward_221","village_221","hhid_221","long_rain_utilization_cropsA","long_rain_utilization_otherCropsA"]
LONG_RAINS_CROPPEDB = ["district_222","ward_222","village_222","hhid_222","long_rain_utilization_cropsB","long_rain_utilization_otherCropsB"]
SHORT_RAINS_CROPPEDA = ["district_223","ward_223","village_223","hhid_223","short_rain_utilization_cropsA","short_rain_utilization_otherCropsA"]
SHORT_RAINS_CROPPEDB = ["district_224","ward_224","village_224","hhid_224","short_rain_utilization_cropsB","short_rain_utilization_otherCrops"]
DRY_SEASON_CROPPEDA = ["district_225","ward_225","village_225","hhid_225","dry_season_utilization_cropsA","dry_season_utilization_otherCropsA"]
DRY_SEASON_CROPPEDB = ["district_226","ward_226","village_226","hhid_226","dry_season_utilization_cropsB","dry_season_utilization_otherCropsB"]
LONG_RAIN_SEASON = ["district_21,ward_21,village_21,hhid_21,long_rain_crops,long_rain_types_variety,long_rain_start_month,long_rain_end_month,long_rain_if_intercropped,otherlong_rain_crops,long_rain_crop_products_count"]
LONG_RAIN_ACT = ["district_22","ward_22","village_22","hhid_22","long_rain_act_pos","long_rain_activity_type","long_rain_activity_other","long_rain_activity_date","long_rain_activity_Hh_male_no","long_rain_activity_Hh_male_days","long_rain_activity_Hh_male_hrs_days","long_rain_activity_Hh_female_no","long_rain_activity_Hh_female_days","long_rain_activity_Hh_female_hrs_day","long_rain_activity_Hh_child_no","long_rain_activity_Hh_child_days","long_rain_activity_Hh_child_hrs_day","long_rain_activity_Permantly_employed_worker_no","long_rain_activity_Permntly_employed_days","long_rain_activity_Permntly_employed_hrs_day","long_rain_activity_Unpaid_labour_no","long_rain_activity_Unpaid_labour_days","long_rain_activity_Unpaid_labour_hrs_day","long_rain_activity_hired_no","long_rain_activity_hired_hours","long_rain_activity_hired_hours_day","long_rain_activity_other_Total_costs"]
LONG_RAIN_INPUT = ["district_23,ward_23,village_23,hhid_23,long_rain_input_pos,long_rain_input_type,long_rain_input_other_fertilizer,long_rain_input_other_type,long_rain_input_quantity,long_rain_input_units,long_rain_input_total_costs"]
LONG_RAIN_CROP_PRODUCT = ["district_24,ward_24,village_24,hhid_24,Long_rains_Crop_products_count,long_rains_residue_type,long_rains_residue_other,long_rains_left_in_share,long_rains_grazing_share,long_rains_burnt_share,long_rains_residue_sales_share,long_rains_residue_sales_total_value,long_rains_residue_sales_income_control,long_rains_residue_sales_main_buyer,long_rains_residue_feed_stall,long_rains_residue_feed_own_graze,long_rains_residue_livestock_bedding,long_rains_residue_fuel,long_rains_residue_other,long_rains_crop_residues_notes"]
LONG_RAINS_CROPS_PRODUCT = ["district_241,ward_241,village_241,hhid_241,long_rains_crops_products,long_rains_production_Quantity,long_rains_production_Quantity_units,long_rains_Hhfood_consumption_Qty,long_rains_Hhfood_consumption_Qty_units,long_rains_Payment_in_kind_quantity,long_rains_Payment_in_kind_quantity_units,long_rains_other_Qty,long_rains_other_Qty_units,long_rains_Livestock_feeding_Qty,long_rains_Livestock_feeding_Qty_units,long_rains_kept_as_seed_Qty,long_rains_kept_as_seed_Qty_units,long_rains_sales_Qnty,long_rains_Sales_quantity,long_rains_Sales_units,long_rains_Sales_total_value,long_rains_Sales_income_control,long_rains_main_buyer,long_rains_crop_products_notes,long_rains_stored_for_Dry_Season"]
LONG)_RAINS_INTERCROP_COMP = ["long_rains_Intercrop_components","district_5","ward_5","village_5","hhid_5","long_rains_types_of_intercrop","long_rains_interCrop_products","long_rains_interCrop_production_Quantity","long_rains_interCrop_production_Quantity_units","long_rains_interCrop_Hhfood_consumption_Qty","long_rains_interCrop_Hhfood_consumption_Qty_units","long_rains_interCrop_Payment_in_kind_quantity","long_rains_interCrop_Payment_in_kind_quantity_units","long_rains_interCrop_other_Qty","long_rains_interCrop_other_Qty_units","long_rains_interCrop_Livestock_feeding_Qty","long_rains_interCrop_Livestock_feeding_Qty_units","long_rains_interCrop_kept_as_seed_Qty","long_rains_interCrop_kept_as_seed_Qty_units","long_rains_interCrop_sales_Qnty","long_rains_interCrop_Sales_quantity","long_rains_interCrop_Sales_units","long_rains_interCrop_Sales_total_value","long_rains_interCrop_Sales_income_control","long_rains_interCrop_main_buyer","long_rains_intercrop_products_notes","Long_rains_interCrop_Residue_utilisation_count"]
LONG_RAINS_INTERCROP_RESIDUE = ["district_51,ward_51,village_51,hhid_51,long_rains_interCrop_residue_type,long_rains_interCrop_residue_other,long_rains_interCrop_left_in_share,long_rains_interCrop_grazing_share,long_rains_interCrop_burnt_share,long_rains_interCrop_residue_sales_share,long_rains_interCrop_residue_sales_total_value,long_rains_interCrop_residue_sales_income_control,long_rains_interCrop_residue_sales_main_buyer,long_rains_interCrop_residue_feed_stall,long_rains_interCrop_residue_feed_own_graze,long_rains_interCrop_residue_livestock_bedding,long_rains_interCrop_residue_fuel,long_rains_interCrop_residue_other,long_rains_interCrop_residues_notes"]
SHORT_RAIN_SEASON = ["district_25","ward_25","village_25","hhid_25","short_rain_crops","short_rain_types_variety","short_rain_start_month","short_rain_end_month","short_rain_if_intercropped","othershort_rain_crops","short_rain_season_activity_notes","short_rain_crop_products_count","short_rains_Number_Intercrop_components","short_rains_Intercrops_components_count"]
SHORT_RAIN_ACT = ["district_26","ward_26","village_26","hhid_26","short_rain_act_pos","short_rain_activity_type","short_rain_activity_other","short_rain_activity_date","short_rain_activity_Hh_male_no","short_rain_activity_Hh_male_days","short_rain_activity_Hh_male_hrs_days","short_rain_activity_Hh_female_no","short_rain_activity_Hh_female_days","short_rain_activity_Hh_female_hrs_day","short_rain_activity_Hh_child_no","short_rain_activity_Hh_child_days","short_rain_activity_Hh_child_hrs_day","short_rain_activity_Permantly_employed_worker_no","short_rain_activity_Permntly_employed_days","short_rain_activity_Permntly_employed_hrs_day","short_rain_activity_Unpaid_labour_no","short_rain_activity_Unpaid_labour_days","short_rain_activity_Unpaid_labour_hrs_day","short_rain_activity_hired_no","short_rain_activity_hired_hours","short_rain_activity_hired_hours_day","short_rain_activity_other_Total_costs","short_rain_activity_notes"]
SHORT_RAIN_INPUT = ["district_27","ward_27","village_27","hhid_27","short_rain_input_pos","short_rain_input_type","short_rain_input_other_fertilizer","short_rain_input_other_type","short_rain_input_quantity","short_rain_input_units","short_rain_input_total_costs","short_rain_input_notes"]
class CIATDataImporter:
    def __init__(self, connection):
        self.connection = connection

        # confirm connection
        self.version()

    def version(self):
        # prepare a cursor object using cursor() method
        with self.connection.cursor() as cursor:

            # execute SQL query using execute() method.
            cursor.execute("SELECT VERSION()")
            connection.commit()

            # Fetch a single row using fetchone() method.
            data = cursor.fetchone()
            print("Database version : {} ".format(data))

    def read_xls(self, loc):
        wb = xlrd.open_workbook(loc)
        main_sheet = wb.sheet_by_index(0)
        demographic_sheet = wb.sheet_by_index(1)
        seasons_sheet = wb.sheet_by_index(2)

        BaseLoader(connection, 'db/scripts/main.sql', 'main', MAIN).handle(main_sheet)
        BaseLoader(connection, 'db/scripts/demographics.sql', 'demographics', DEMOGRAPHIC).handle(demographic_sheet)
        BaseLoader(connection, 'db/scripts/season.sql', 'season', SEASONS).handle(seasons_sheet)


if __name__ == "__main__":
    connection = Connection.get_instance()
    try:
        importer = CIATDataImporter(connection)
        importer.read_xls("db/data.xls") 
    finally:
        connection.close()