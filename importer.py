import xlrd

from connection import Connection
from loader.baseloader import BaseLoader
from db import columns

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

            cursor.execute("SET GLOBAL sql_mode = '';")
            connection.commit()

            cursor.execute("SET SESSION sql_mode = '';")
            connection.commit()

    def read_xls(self, loc):
        wb = xlrd.open_workbook(loc)
        main_sheet = wb.sheet_by_index(0)
        demographic_sheet = wb.sheet_by_index(1)
        seasons_sheet = wb.sheet_by_index(2)
        hh_menber_sheet = wb.sheet_by_index(3)
        subplots_details_sheet =  wb.sheet_by_index(4)
        long_rains_cropped_a_sheet =  wb.sheet_by_index(5)
        long_rains_cropped_b_sheet =  wb.sheet_by_index(6)
        short_rains_cropped_a_sheet =  wb.sheet_by_index(7)
        short_rains_cropped_b_sheet =  wb.sheet_by_index(8)
        dry_season_cropped_a_sheet =  wb.sheet_by_index(9)
        dry_season_cropped_b_sheet =  wb.sheet_by_index(10)
        long_rain_season_sheet =  wb.sheet_by_index(11)
        long_rain_act_sheet =  wb.sheet_by_index(12)
        long_rain_inputs_sheet =  wb.sheet_by_index(13)
        long_rain_crop_products_sheet =  wb.sheet_by_index(14)
        long_rains_crops_products_sheet =  wb.sheet_by_index(15)
        long_rains_intercrop_comp_sheet =  wb.sheet_by_index(16)
        long_rains_intercrop_residue_sheet =  wb.sheet_by_index(17)
        short_rain_season_sheet =  wb.sheet_by_index(18)
        short_rain_act_sheet =  wb.sheet_by_index(19)
        short_rain_inputs_sheet =  wb.sheet_by_index(20)
        short_rain_crop_products_sheet =  wb.sheet_by_index(21)
        short_rains_crops_products_sheet =  wb.sheet_by_index(22)
        short_rains_intercrop_comp_sheet =  wb.sheet_by_index(23)
        short_rains_intercrop_residue_sheet =  wb.sheet_by_index(24)
        dry_season_sheet =  wb.sheet_by_index(25)
        dry_season_act_sheet =  wb.sheet_by_index(26)
        dry_season_inputs_sheet =  wb.sheet_by_index(27)
        dry_season_crop_products_sheet =  wb.sheet_by_index(28)
        dry_season_crops_products_sheet =  wb.sheet_by_index(29)
        dry_season_intercrop_comp_sheet =  wb.sheet_by_index(30)
        dry_rains_inter_products_sheet =  wb.sheet_by_index(31)
    
        forage_act_sheet =  wb.sheet_by_index(32)
        forage_inputs_sheet =  wb.sheet_by_index(33)
        non_ruminants_sheet =  wb.sheet_by_index(34)
        ruminants_sheet =  wb.sheet_by_index(35)
        dairy_animals_sheet =  wb.sheet_by_index(36)
        
        feedbasket_sheet =  wb.sheet_by_index(37)
        feedbasket_months_sheet =  wb.sheet_by_index(38)
        feedbasket_adequacy_sheet =  wb.sheet_by_index(39)
        feedbasket_item_types_sheet =  wb.sheet_by_index(40)
        feedbasket_item_source_sheet =  wb.sheet_by_index(41)

        additional_supplements_sheet =  wb.sheet_by_index(42)
        livestock_prod_utilization_sheet =  wb.sheet_by_index(43)
        livestock_act_inputs_sheet = wb.sheet_by_index(44)
        livestock_inputs_sheet =  wb.sheet_by_index(45)
        management_practices_a_sheet =  wb.sheet_by_index(46)
        management_practices_b_sheet =  wb.sheet_by_index(47)

        manure_product_details_a_sheet =  wb.sheet_by_index(48)
        manure_product_details_b_sheet =  wb.sheet_by_index(49)
        credit_access_sheet =  wb.sheet_by_index(50)
        food_insecurity_sheet =  wb.sheet_by_index(51)
        hdds_sheet =  wb.sheet_by_index(52)


        BaseLoader(connection, 'db/scripts/main.sql', 'main', columns.MAIN).handle(main_sheet)
        BaseLoader(connection, 'db/scripts/demographics.sql', 'demographics', columns.DEMOGRAPHIC).handle(demographic_sheet)
        BaseLoader(connection, 'db/scripts/season.sql', 'season', columns.SEASONS).handle(seasons_sheet)
        BaseLoader(connection, 'db/scripts/hh_members.sql', 'hh_members', columns.HH_MEMBERS).handle(hh_menber_sheet)
        BaseLoader(connection, 'db/scripts/subplots_details.sql', 'subplots_details', columns.SUBPLOT_DETAILS).handle(subplots_details_sheet)
        
        BaseLoader(connection, 'db/scripts/long_rains_cropped_a.sql', 'long_rains_cropped_a', columns.LONG_RAINS_CROPPEDA).handle(long_rains_cropped_a_sheet)
        #-- BaseLoader(connection, 'db/scripts/long_rains_cropped_b.sql', 'long_rains_cropped_b', columns.LONG_RAINS_CROPPEDB).handle(long_rains_cropped_b_sheet)
        
        BaseLoader(connection, 'db/scripts/short_rains_cropped_a.sql', 'short_rains_cropped_a', columns.SHORT_RAINS_CROPPEDA).handle(short_rains_cropped_a_sheet)
        BaseLoader(connection, 'db/scripts/short_rains_cropped_b.sql', 'short_rains_cropped_b', columns.SHORT_RAINS_CROPPEDB).handle(short_rains_cropped_b_sheet)
        
        BaseLoader(connection, 'db/scripts/dry_season_cropped_a.sql', 'dry_season_cropped_a', columns.DRY_SEASON_CROPPEDA).handle(dry_season_cropped_a_sheet)
        BaseLoader(connection, 'db/scripts/dry_season_cropped_b.sql', 'dry_season_cropped_b', columns.DRY_SEASON_CROPPEDB).handle(dry_season_cropped_b_sheet)
        
        BaseLoader(connection, 'db/scripts/long_rain_season.sql', 'long_rain_season', columns.LONG_RAIN_SEASON).handle(long_rain_season_sheet)
        BaseLoader(connection, 'db/scripts/long_rain_act.sql', 'long_rain_act', columns.LONG_RAIN_ACT).handle(long_rain_act_sheet)
        BaseLoader(connection, 'db/scripts/long_rain_inputs.sql', 'long_rain_inputs', columns.LONG_RAIN_INPUT).handle(long_rain_inputs_sheet)
        BaseLoader(connection, 'db/scripts/long_rain_crop_products.sql', 'long_rain_crop_products', columns.LONG_RAIN_CROP_PRODUCT).handle(long_rain_crop_products_sheet)
        BaseLoader(connection, 'db/scripts/long_rains_crops_products.sql', 'long_rains_crops_products', columns.LONG_RAINS_CROPS_PRODUCT).handle(long_rains_crops_products_sheet)
        BaseLoader(connection, 'db/scripts/long_rains_intercrop_comp.sql', 'long_rains_intercrop_comp', columns.LONG_RAINS_INTERCROP_COMP).handle(long_rains_intercrop_comp_sheet)
        BaseLoader(connection, 'db/scripts/long_rains_intercrop_residue.sql', 'long_rains_intercrop_residue', columns.LONG_RAINS_INTERCROP_RESIDUE).handle(long_rains_intercrop_residue_sheet)
        
        BaseLoader(connection, 'db/scripts/short_rain_season.sql', 'short_rain_season', columns.SHORT_RAIN_SEASON).handle(short_rain_season_sheet)
        BaseLoader(connection, 'db/scripts/short_rain_act.sql', 'short_rain_act', columns.SHORT_RAIN_ACT).handle(short_rain_act_sheet)
        BaseLoader(connection, 'db/scripts/short_rain_inputs.sql', 'short_rain_inputs', columns.SHORT_RAIN_INPUT).handle(short_rain_inputs_sheet)
        BaseLoader(connection, 'db/scripts/short_rain_crop_products.sql', 'short_rain_crop_products', columns.SHORT_RAIN_CROP_PRODUCTS).handle(short_rain_crop_products_sheet)
        BaseLoader(connection, 'db/scripts/short_rains_crops_products.sql', 'short_rains_crops_products', columns.SHORT_RAINS_CROPS_PRODUCTS).handle(short_rains_crops_products_sheet)
        BaseLoader(connection, 'db/scripts/short_rains_intercrop_comp.sql', 'short_rains_intercrop_comp', columns.SHORT_RAINS_INTERCROP_COMP).handle(short_rains_intercrop_comp_sheet)
        BaseLoader(connection, 'db/scripts/short_rains_intercrop_residue.sql', 'short_rains_intercrop_residue', columns.SHORT_RAINS_INTERCROP_RESIDUE).handle(short_rains_intercrop_residue_sheet)
        
        BaseLoader(connection, 'db/scripts/dry_season.sql', 'dry_season', columns.DRY_SEASON).handle(dry_season_sheet)
        BaseLoader(connection, 'db/scripts/dry_season_act.sql', 'dry_season_act', columns.DRY_SEASON_ACT).handle(dry_season_act_sheet)
        BaseLoader(connection, 'db/scripts/dry_season_inputs.sql', 'dry_season_inputs', columns.DRY_SEASON_INPUTS).handle(dry_season_inputs_sheet)
        BaseLoader(connection, 'db/scripts/dry_season_crop_products.sql', 'dry_season_crop_products', columns.DRY_SEASON_CROP_PRODUCTS).handle(dry_season_crop_products_sheet)
        BaseLoader(connection, 'db/scripts/dry_season_crops_products.sql', 'dry_season_crops_products', columns.DRY_SEASON_CROPS_PRODUCT).handle(dry_season_crops_products_sheet)
        BaseLoader(connection, 'db/scripts/dry_season_intercrop_comp.sql', 'dry_season_intercrop_comp', columns.DRY_SEASON_INTERCROP_COMP).handle(dry_season_intercrop_comp_sheet)
        
        BaseLoader(connection, 'db/scripts/forage_act.sql', 'forage_act', columns.FORAGE_ACT).handle(forage_act_sheet)
        BaseLoader(connection, 'db/scripts/forage_inputs.sql', 'forage_inputs', columns.FORAGE_INPUT).handle(forage_inputs_sheet)
        BaseLoader(connection, 'db/scripts/non_ruminants.sql', 'non_ruminants', columns.NON_RUMINANT).handle(non_ruminants_sheet)
        BaseLoader(connection, 'db/scripts/ruminants.sql', 'ruminants', columns.RUMINANT).handle(ruminants_sheet)
        BaseLoader(connection, 'db/scripts/dairy_animals.sql', 'dairy_animals', columns.DAIRY_ANIMALS).handle(dairy_animals_sheet)
        BaseLoader(connection, 'db/scripts/feedbasket.sql', 'feedbasket', columns.FEEDBASKET).handle(feedbasket_sheet)

        BaseLoader(connection, 'db/scripts/feedbasket_months.sql', 'feedbasket_months', columns.FEEDBASKET_MONTHS).handle(feedbasket_months_sheet)
        BaseLoader(connection, 'db/scripts/feedbasket_adequacy.sql', 'feedbasket_adequacy', columns.FEEDBASKET_ADEQUECY).handle(feedbasket_adequacy_sheet)
        BaseLoader(connection, 'db/scripts/feedbasket_item_types.sql', 'feedbasket_item_types', columns.FEEDBASKET_ITEM_TYPES).handle(feedbasket_item_types_sheet)
        BaseLoader(connection, 'db/scripts/feedbasket_item_source.sql', 'feedbasket_item_source', columns.FEEDBASKET_ITEM_SOURCE).handle(feedbasket_item_source_sheet)
        BaseLoader(connection, 'db/scripts/additional_supplements.sql', 'additional_supplements', columns.ADDITIONAL_SUPPLEMENTS).handle(additional_supplements_sheet)
        BaseLoader(connection, 'db/scripts/livestock_prod_utilization.sql', 'livestock_prod_utilization', columns.LIVESTOCK_PROD_UTILIZATION).handle(livestock_prod_utilization_sheet)
        
        BaseLoader(connection, 'db/scripts/livestock_act_inputs.sql', 'livestock_act_inputs', columns.LIVESTOCK_ACT_INPUTS).handle(livestock_act_inputs_sheet)
        BaseLoader(connection, 'db/scripts/livestock_inputs.sql', 'livestock_inputs', columns.LIVESTOCK_INPUTS).handle(livestock_inputs_sheet)
        BaseLoader(connection, 'db/scripts/management_practices_a.sql', 'management_practices_a', columns.MANAGEMENT_PRACTICES_A).handle(management_practices_a_sheet)
        BaseLoader(connection, 'db/scripts/management_practices_b.sql', 'management_practices_b', columns.MANAGEMENT_PRACTICES_B).handle(management_practices_b_sheet)
        BaseLoader(connection, 'db/scripts/manure_product_details_a.sql', 'manure_product_details_a', columns.MANURE_PRODUCT_DETAILS_A).handle(manure_product_details_a_sheet)
        BaseLoader(connection, 'db/scripts/manure_product_details_b.sql', 'manure_product_details_b', columns.MANURE_PRODUCT_DETAILS_B).handle(manure_product_details_b_sheet)
        
        BaseLoader(connection, 'db/scripts/credit_access.sql', 'credit_access', columns.CREDIT_ACCESS).handle(credit_access_sheet)
        BaseLoader(connection, 'db/scripts/food_insecurity.sql', 'food_insecurity', columns.FOOD_SECURITY).handle(food_insecurity_sheet)
        BaseLoader(connection, 'db/scripts/hdds.sql', 'hdds', columns.HDDS).handle(hdds_sheet)
        


if __name__ == "__main__":
    connection = Connection.get_instance()
    try:
        importer = CIATDataImporter(connection)
        importer.read_xls("data/test.xlsx") 
    finally:
        connection.close()