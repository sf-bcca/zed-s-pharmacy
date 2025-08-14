from dataclasses import dataclass
import csv
@dataclass
class Customer:
    client_name: str
    birthday: int
    ssn: int
vaccinations_type = [
    "Flu", "RSV", "Covid-19", "Pneumonia", "Shingles"
]

vaccinations_to_get = []

def get_patients_name(client_name: Customer) -> str:
    while True:
        client_name = input("Name: ")
       

def get_birthday(birthday: Customer) -> int:
    birthday = input("Birthday(00/00/0000): ")
    return

def get_ssn(ssn: Customer) -> int:
    ssn = input("Social Sercurity Number (last 4 digits): ")
    return

def get_vaccinations_type():
    print(vaccinations_type)
    type_to_remove = input("What type of vaccination are you taken today?: ")
    try:
        vaccinations_to_get.append(type_to_remove)
        vaccinations_type.remove(type_to_remove)
        print(f"💉💉💉 ")
    except ValueError:
        print(f"{type_to_remove} not found in list.")
    return
    
def get_medicine_type():
    pass

def get_vac_price():
    pay = input("")
    insurnance_dictionary = {}
    with open('Insurance - Sheet1.csv', mode = 'r', newline = '') as file:
        reader = csv.DictReader(file)
        for row in reader:
            name = row['Name']
            percent = row['Percent']
            insurnance_dictionary[name] = float(percent)  # or use int() if it's an integer
    print(insurnance_dictionary)

    vaccines_prices_dictionary = {}
    with open('Vaccines & Prices - Sheet1.csv', mode = 'r', newline = '') as file:
        reader = csv.DictReader(file)
        for row in reader:
            name = row['Name']
            price = row['Price']
            vaccines_prices_dictionary[name] = int(price)
    print(vaccines_prices_dictionary)

def main():
    print("Welcome to the Zed's Pharmacy!")
    print("May you sign in for us today?")
    name = get_patients_name(client_name = str)
    birthday = get_birthday(birthday = int)
    ssn = get_ssn(ssn = int)
    print("What can we help you with today?")
    user_input = input("Vaccinations or Medicine?: ")
    while user_input != "All Done":
        if user_input == "Vaccinations":
            get_vaccinations_type()
            print("Alrighty, all finished! Can I help you with anything else today?")
            user_input = input("Vaccinations, Medicine, Or Done? ")
        elif user_input == "Medicine":
            pass
        elif user_input == "Done":
            print("You have received these :")
            for vaccine in vaccinations_to_get:
                print(vaccine)
            print("Hey! I hope your visit was well today!")
            pay_me = input("Will you being using your insurance today? yes or no? ")
            if pay_me == "yes":
                pass
            break



        

if __name__ == "__main__":
    main()





