from rent_a_car.sign_up import signup
import rent_a_car.sign_in
from rent_a_car.store_menu import storemenu


def mainmenu():

    print("""
1. SIGN IN
2. SIGN UP
3. EXIT
    """)
    try:
        selection=int(input("Enter choice: "))
        if selection==1:
            rent_a_car.sign_in.signin()
            while rent_a_car.sign_in.zalogowano == True:
                storemenu()
            mainmenu()

        elif selection==2:
            signup()

        elif selection==3:
            rent_a_car.sign_in.zalogowano = False
            return rent_a_car.sign_in.zalogowano
            print("Bye.")
            rent_a_car.sign_in.login = ""
            rent_a_car.sign_in.password = ""
            exit()

        else:
            print("Invalid choice.")
            mainmenu()
    except ValueError:
        print("Invalid choice.")
        mainmenu()
