import re
import datetime
import tkinter as tk


def button_click():
    print("բարև Ռուբիկ!")
    

root = tk.Tk()
button = tk.Button(root, text="start", command=button_click)
button.pack()
root.mainloop()


def greet_user():
    greeting_ = button_click()
    print("Ռուբիկ: Ողջույն, ես Ռուբիկն եմ:")
    print("Ցանկանու՞մ եք Ձեզ օգնեմ հաշվել առողջության ապահովագրության սակագինը։ Գրեք այո կամ ոչ")
    yes_no = input("User: ").lower()
    if yes_no == "այո" or yes_no=="հա" or yes_no=="ha" or yes_no=="ayo":
        print("Ռուբիկ: Շատ բարի։ Այդ դեպքում նշեք Ձեր սեռը Ի-իգական, Ա-արական")
        gender = ask_gender()
        print("Ձեր սեռը գրանցված է: ", gender)
        birth_year = ask_birth_date()
        current_year = datetime.datetime.now().year
        if current_year - birth_year > 63:
            print("Ռուբիկ: Ցավում եմ, Դուք չեք կարող օգտվել առողջության ապահովագրությունից:")
        else:
            print("Ռուբիկ: Դուք կարող եք օգտվել առողջության ապահովագրությունից:")
    elif yes_no=="ոչ" or yes_no=="չէ" or yes_no=="voch" or yes_no=="che":
        print("Ռուբիկ: Լավ, հաջողություն:")
    else:
        print("Ես Ձեզ չեմ հասկանում, գրե՛ք ևս մեկ անգամ այո կամ ոչ")

def ask_gender():
    gender = input("User: ")
    while not re.match(r'^[իաԻԱiaIA]$', gender):
        gender = input("User: Նշե՛ք համապատասխան ձևով։ի կամ ա ")
    return gender.upper()

def ask_birth_date():
    print("Ռուբիկ: Շատ բարի, նշե՛ք Ձեր ծննդյան ամիս ամսաթիվը հետևյալ ֆորմապոտվ՝ (Օր-ամիս-տարի)")
    birth_date_str = input("User: ")
    while not re.match(r'^\d{2}-\d{2}-\d{4}$', birth_date_str):
        print("Ռուբիկ: Խնդրում եմ գրեք տրված ֆորմատով (DD-MM-YYYY):")
        birth_date_str = input("User: ")

    birth_date_parts = birth_date_str.split('-')
    birth_year = int(birth_date_parts[2])

    birth_date = datetime.datetime.strptime(birth_date_str, '%d-%m-%Y').date()
    print("Ռուբիկ: Ծննդյան ամսաթիվը գրանցված է: ", birth_date)

    return birth_year

def has_chronic_disease():
    print("Ռուբիկ: Դուք խրոնիկ հիվանդություններ ունե՞ք: Գրեք այո կամ ոչ")
    chronic_yes_no = input("User: ")
    if chronic_yes_no.lower() in ["այո", "հա", "ayo", "ha"]:
        print("Ռուբիկ: Ցավոք, առողջության ապահովագրությունը չի փոխհատուցում խրոնիկ հիվանդությունները ")
    elif chronic_yes_no.lower() in ["ոչ", "չէ", "voch", "che"]:
        print("Ռուբիկ։ Շատ բարի")
    else:
        print("Ռուբիկ։ Խնդրում եմ գրե՛ք այո կամ ոչ։")
    return has_chronic_disease



        


def main():
    greet_user()

if __name__ == "__main__":
    main()
