import modules.db_manager as mgr

# mgr.drop_rates_from_database()
# mgr.drop_countries_from_database()
# mgr.drop_conversions_from_database()

# mgr.create_table_rates()
# mgr.create_table_conversions()
# mgr.create_table_countries()

# mgr.import_rates_from_json()
# mgr.import_countries_from_json()

mgr.get_rates_online()

# Print table
# hdrs = ["code", "rate_to_euro", "date"] 
# tbl = [
#     ["AED", 	"4.034276",	 "2022-03-27"],
#     ["AFN", 	"4.034276",	 "2022-03-27"],
#     ["ALL", 	"4.034276",	 "2022-03-27"]
# ]

# print(mgr.print_report(hdrs, tbl))

# print(mgr.get_currency_code())

print (mgr.convert())