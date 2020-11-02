import mysql.connector
from mysql.connector import Error

zalogowano = False
login = ""
password = ""

def signin():
    global zalogowano, login, password
    try:
        connection = mysql.connector.connect(
            user="root",
            database="samochody"
        )

        sql_select_Query = "select * from klienci"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        print("Total number of rows is: ", cursor.rowcount)

        login = input("login:")
        print(records)

        for row in records:

            if login == row[1]:
                print(row[2])
                password = input("password:")
                if password == row[2]:
                    user_name = row[3]
                    print("Logging in...\n")

                    zalogowano = True
                    print("signin zalogowano?")

                    print(zalogowano)


                else:
                    pass

            else:
                pass

        if zalogowano == True:
            print(f"LOGGED IN! Welcome {user_name}")
        else:
            print("Incorrect.")

    except Error as e:
        print("Error reading data from MySQL table", e)
