# ciat_importer

## Setup
Install pipenv
For more informantion and installation info -> https://pipenv.readthedocs.io/en/latest/

### Creating virtualenv
```
    pipenv --python 3.7
```

### Activating the virtualenv
```
    pipenv shell
```
### Installing all packages
```
    pipenv install
```

or 

```
    pip install -r requirements.txt
```

## Setup mysql version 8
Download link
https://dev.mysql.com/downloads/

### .env File
Add `.env` file and add the following content
```
    DATABASE=mariadb
    USERNAME=root
    PASSWORD=test
    DB_NAME=test
    ONA_API_KEY=<Your ona api key>
```

### Running
The script will create the table using the form id_string as the table name.
`python data_importer.py --form <XformID from ona>`

Pulling `Feedgap_datacollection_forms_Tanzania_2n_4th_sampling_v2`
`python data_importer.py --form 438737`


### Querying the database
The main data from ona is stored in data column.
For detailed instruction check mysql documentation

Example:
`select data->"$._id" from <Table name>`

Working example
```
    SELECT  data->>'$."sect0/main/hh_id"',
            data->>'$."sect0/hh_consent"',
            data->>'$."sect0/main/country"',
            data->>'$."sect0/main/village_tz"',
            data->>'$."sect0/main/district_tz"',
            data->>'$."sect0/main/farmer_name"',
            data->>'$."sect0/sect2/cattle_count"',
            data->>'$."sect0/main/interview_date"',
            data->>'$."sect0/sect1a/num_hh_people"',
            data->>'$."sect0/main/farmer_tel_number"',
            data->>'$."sect0/sect4/cattle_kept_fed_seperately_4"'
    FROM Feedgap_datacollection_forms_Tanzania_2n_4th_sampling_v2;
```


Example querying repeat field
`select data->'$."sect0/sect2/cattle"' from <Table name>`

Working example

```
    SELECT cattles.* 
    FROM Feedgap_datacollection_forms_Tanzania_2n_4th_sampling_v2, 
        JSON_TABLE(data, '$."sect0/sect2/cattle"[*]' COLUMNS (
                    cattle_age VARCHAR(32)  PATH '$."sect0/sect2/cattle/cattle_age"',
                    cattle_pos VARCHAR(32) PATH '$."sect0/sect2/cattle/cattle_pos"',
                    cattle_sex VARCHAR(32) PATH '$."sect0/sect2/cattle/cattle_sex"',
                    cattleID_lbl VARCHAR(32) PATH '$."sect0/sect2/cattle/cattleID_lbl"',
                    cattle_breed VARCHAR(32) PATH '$."sect0/sect2/cattle/cattle_breed"',
                    cattle_age_lbl VARCHAR(32) PATH '$."sect0/sect2/cattle/cattle_age_lbl"',
                    cattle_breed_lbl VARCHAR(32)  PATH '$."sect0/sect2/cattle/cattle_breed_lbl"',
                    cattle_lactating VARCHAR(32) PATH '$."sect0/sect2/cattle/cattle_lactating"',
                    cattle_ownership VARCHAR(32) PATH '$."sect0/sect2/cattle/cattle_ownership"',
                    cattle_num_births VARCHAR(32) PATH '$."sect0/sect2/cattle/cattle_num_births"',
                    cattle_breast_diameter VARCHAR(32) PATH '$."sect0/sect2/cattle/cattle_breast_diameter"',
                    cattle_curr_birth_date VARCHAR(32) PATH '$."sect0/sect2/cattle/cattle_curr_birth_date"',
                    cattle_decision_maker_vet VARCHAR(32)  PATH '$."sect0/sect2/cattle/cattle_decision_maker_vet"',
                    cattle_decision_maker_sale VARCHAR(32) PATH '$."sect0/sect2/cattle/cattle_decision_maker_sale"',
                    cattle_decision_maker_other VARCHAR(32) PATH '$."sect0/sect2/cattle/cattle_decision_maker_other"',
                    cattle_decision_maker_vet_hh VARCHAR(32) PATH '$."sect0/sect2/cattle/cattle_decision_maker_vet_hh"',
                    cattle_decision_maker_feeding VARCHAR(32) PATH '$."sect0/sect2/cattle/cattle_decision_maker_feeding"',
                    cattle_decision_maker_sale_hh VARCHAR(32) PATH '$."sect0/sect2/cattle/cattle_decision_maker_sale_hh"',
                    cattle_decision_maker_feeding_hh VARCHAR(32)  PATH '$."sect0/sect2/cattle/cattle_decision_maker_feeding_hh"'
                    )
        ) cattles
    WHERE data->'$."sect0/main/hh_id"' = "TZ38";`
```

Working example for a nested repeat field

```
    SELECT data->>'$."sect0/main/hh_id"', milking_cows.* 
    FROM Feedgap_datacollection_forms_Tanzania_2n_4th_sampling_v2, 
        JSON_TABLE(data, '$."sect0/sect5/milking_cows"[*]' COLUMNS (
                    milking_cow_id FOR ORDINALITY,
                    milking_count VARCHAR(32)  PATH '$."sect0/sect5/milking_cows/milking_count"',
                    milking_times VARCHAR(32) PATH '$."sect0/sect5/milking_cows/milking_times"',
                    NESTED PATH '$."sect0/sect5/milking_cows/milking"[*]' COLUMNS (
                        child_id FOR ORDINALITY,
                        milk_qaunt VARCHAR(30) PATH '$."sect0/sect5/milking_cows/milking/milk_qaunt"',
                        milking_dm VARCHAR(30) PATH '$."sect0/sect5/milking_cows/milking/milking_dm"',
                        milking_time VARCHAR(30) PATH '$."sect0/sect5/milking_cows/milking/milking_time"',
                        first_suckling VARCHAR(30) PATH '$."sect0/sect5/milking_cows/milking/first_suckling"',
                        second_suckling VARCHAR(30) PATH '$."sect0/sect5/milking_cows/milking/second_suckling"',
                        daily_milking_ids VARCHAR(30) PATH '$."sect0/sect5/milking_cows/milking/daily_milking_ids"',
                        daily_milking_pos VARCHAR(30) PATH '$."sect0/sect5/milking_cows/milking/daily_milking_pos"',
                        milking_hh_member VARCHAR(30) PATH '$."sect0/sect5/milking_cows/milking/milking_hh_member"',
                        sale_milk VARCHAR(30) PATH '$."sect0/sect5/milking_cows/milking/milk_use/sale_milk"',
                        milking_start_time VARCHAR(30) PATH '$."sect0/sect5/milking_cows/milking/milking_start_time"',
                        home_consumption VARCHAR(30) PATH '$."sect0/sect5/milking_cows/milking/milk_use/home_consumption"',
                        animal_consumption VARCHAR(30) PATH '$."sect0/sect5/milking_cows/milking/milk_use/animal_consumption"'
                        )
        ) )milking_cows
    WHERE data->'$."sect0/main/hh_id"' = "TZ38";
```

