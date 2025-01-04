import json

with open('birthday_data.json', 'r+') as f:
    info = json.load(f)

    print("""Welcome to the birthday dictionary. We know the birthdays of:
        """) # How to load only the keys

    for key,value in info.items():
        print(key)
 
    data = input("Who's birthday do you want to look up? \n")
    print(info[data])


with open('birthday_data.json', 'r+') as f:
    while(True):
        decision = input("""If you want to update the file Type 'Y' else 'N'""")
        if decision == 'Y':
            update_data_name = input("Enter the new name :")
            update_data_date = input("Enter the date :")
            info[update_data_name] = update_data_date # query regarding updating json
            json.dump(info,f)
        else:
            break;            


    