import psycopg2
import function_db_y
import function_db_x

def insert_x_to_y():
    list_transaction = function_db_x.get_transactions("WHERE id > 0")
    function_db_y.insert_list_transaction(list_transaction)

function_db_y.create_tables_transactions()
function_db_y.truncate_transaction()
insert_x_to_y()

# function_db_x.insert_transaction("2022-06-14", 4000)
# function_db_x.get_transactions()

# START TRANSFER DATA BY RESTORE
# tao database Y
# function_db_y.create_tables_transactions()
#
# function_db_y.truncate_transaction()
#
# insert_x_to_y()
#
# print("database Y - transactions:")
# function_db_y.get_transactions()
# END TRANSFER DATA BY RESTORE
