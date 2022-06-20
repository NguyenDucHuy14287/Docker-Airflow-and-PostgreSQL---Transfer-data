import psycopg2
import function_db_y
import function_db_x


def transfer_data_by_last_id():
    db_y_last_id = function_db_y.get_last_id()
    print("database Y last id: ", db_y_last_id)

    print("database X: ")
    list_transaction = function_db_x.get_transactions("WHERE id > " + str(db_y_last_id))
    print(list_transaction)
    function_db_y.insert_list_transaction(list_transaction)


def insert_x_to_y():
    list_transaction = function_db_x.get_transactions("WHERE id > 0")
    function_db_y.insert_list_transaction(list_transaction)


# function_db_x.insert_transaction("2022-06-14", 4000)
# function_db_x.get_transactions()

# START TRANSFER DATA BY LAST ID
# tao database Y
function_db_y.create_tables_transactions()
transfer_data_by_last_id()
# END TRANSFER DATA BY LAST ID

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
