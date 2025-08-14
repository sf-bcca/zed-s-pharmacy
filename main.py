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
medicine_type = [
    "Aspirin", "Ibuprofen", "Acetaminophen", "Lisinopril", "Metformin"
]

vaccinations_to_get = []
medicine_to_get = []

def get_patients_name(client_name: Customer) -> str:
    while True:
        try:
            client_name = input("Name: ")
            if client_name.isalpha():
                return
        except ValueError:
            print("Please try again. We need a valid name.")

def get_birthday(birthday: Customer) -> int:
    birthday = input("Birthday(00/00/0000): ")
    return

def get_ssn(ssn: Customer) -> int:
    while True:
        try:
            ssn = int(input("Social Sercurity Number (last 4 digits): "))
            if 1000 <= ssn <= 9999:
                return
        except ValueError:
            print("It has to be your last 4 digits.")

def get_vaccinations_type():
    print(vaccinations_type)
    type_to_remove = input("What type of vaccination are you taken today?: ")
    while True:
        try:
            vaccinations_to_get.append(type_to_remove)
            vaccinations_type.remove(type_to_remove)
            print(f"💉💉💉 ")
            print("Alrighty, all finished! Can I help you with anything else today?")
            return
        except ValueError:
            print(f"{type_to_remove} not found in list.")
    
def get_medicine_type():
    print(medicine_type)
    type_to_remove = input("What type of medicine do you need for your pain today?: ")
    while True:
        try:
            medicine_to_get.append(type_to_remove)
            medicine_type.remove(type_to_remove)
            print(f"💊💊💊")
            print("Alrighty, all finished! Can I help you with anything else today?")
            return
        except ValueError:
            print(f"{type_to_remove} not found in list.")

# def get_vac_pr():
#     vaccines_prices_dictionary = {}
#     with open('Vaccines & Prices - Sheet1.csv', mode = 'r', newline = '') as file:
#         reader = csv.DictReader(file)
#         for row in reader:
#             name = row['Name']
#             price = row['Price']
#             vaccines_prices_dictionary[name] = int(price)
#     print(vaccines_prices_dictionary)

# def get_insurance_pr():
#     insurance = input("What type of insurance will you be using today? ")
#     insurnance_dictionary = {}
#     with open('Insurance - Sheet1.csv', mode = 'r', newline = '') as file:
#         reader = csv.DictReader(file)
#         for row in reader:
#             name = row['Name']
#             percent = row['Percent']
#             insurnance_dictionary[name] = float(percent)  # or use int() if it's an integer
#     print(insurnance_dictionary)
    
def get_insurance_pr(filename, users_input):
    pass

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
            user_input = input("Vaccinations, Medicine, Or Done? ")
        elif user_input == "Medicine":
            get_medicine_type()
            user_input = input("Vaccinations, Medicine, Or Done? ")
        elif user_input == "Done":
            print("Hey! I hope your visit was well today!")
            print("You have received these checkups today for:")
            for vaccine in vaccinations_to_get:
                print(vaccine)
            for medicine in medicine_to_get:
                print(medicine)
            pay_me = input("Will you being using your insurance today? yes or no? ")
            if pay_me == "yes":
                insurance = get_insurance_pr() 
            elif pay_me == "no":
                full_price = get_vac_pr()
            break



        

if __name__ == "__main__":
    main()





