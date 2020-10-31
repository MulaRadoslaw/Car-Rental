import mysql.connector
from datetime import date

mydb = mysql.connector.connect(
  user="root",
  database="samochody"
)

def signup():
    try:
        mycursor = mydb.cursor()

        mycursor.execute("SELECT * FROM klienci")

        myresult = mycursor.fetchall()

        zlicz = 0
        for x in myresult:
            print(x)
            zlicz = x[0]
        zlicz += 1

        login = input("Login: ")
        password = input("Password: ")
        f_name = input("First name: ")
        l_name = input("Last name: ")
        dl_year = int(input("Driving licence, year:  ")); dl_month = int(input("month: ")); dl_day = int(input("day: "))
        d_licence = date(dl_year, dl_month, dl_day)
        city = input("City: ")
        gender = input("Gender: M/F: ")

        sql = "INSERT INTO klienci (idklienta, login, haslo, imie, nazwisko, data_wydania, miasto, plec)" \
              " VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        val = (zlicz, login, password, f_name, l_name, d_licence, city, gender)
        mycursor.execute(sql, val)

        mydb.commit()

        print("1 record inserted, ID:", mycursor.lastrowid)
    except ValueError:
        print("Bye.")

signup()
