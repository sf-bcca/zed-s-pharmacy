from dataclasses import dataclass
import csv

insurnace_dictionary = {}

with open('Insurance - Sheet1.csv', mode='r', newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        name = row['Name']
        percent = row['Percent']
        insurnace_dictionary[name] = float(percent)  # or use int() if it's an integer

print(insurnace_dictionary)

#todo - read csv files for insurance, medication, and vacines

@dataclass
class Customer:
    client_name: str
    birthday: int
    ssn: int
vaccinations_type = [
    "Flu", "RSV", "Covid-19", "Pneumonia", "Shingles"
]

#todo - def calculate_total => in: float, float. out: float -> total
#todo - def get_insurance_perc => in: insurance_dictionary, str (user input insurance). out -> float
#todo - def get_med_price => in: medication_dictionary, str (user input choice). out -> float
#todo - def get_vac_price => in: vac_dictionary, str (user input choice). out -> float


def get_patients_name(client_name: Customer) -> str:
    client_name = input("Name: ")
    return 

def get_birthday(birthday: Customer) -> int:
    birthday = input("Birthday: ")
    return

def get_ssn(ssn: Customer) -> int:
    ssn = input("Social Sercurity Number (last 4 digits): ")
    return

def get_vaccinations_type():
    print(vaccinations_type)
    type_to_remove = input("What type of vaccination are you taken today?: ")
    try:
        vaccinations_type.remove(type_to_remove)
        print(f"💉💉💉 ")
    except ValueError:
        print(f"{type_to_remove} not found in list.")
    return
    
def get_medicine_type():
    pass
#todo
def main():
    print("Welcome to the Zed's Pharmacy!")
    print("May you sign in for us today?")
    name = get_patients_name(client_name = str)
    birthday = get_birthday(birthday = int)
    ssn = get_ssn(ssn = int)
    print("What can we help you with today?")
    choices = input("Vaccinations or Medicine?: ")
    while True:
        if choices == "Vaccinations":
            vaccinations = get_vaccinations_type()
            print("Already, your done! Can I help you with anything else today?")
            print("Vaccination, Medicine, Or All Done?")
        elif choices == "Medicine":
            pass
        else:
            break

        

if __name__ == "__main__":
    main()





