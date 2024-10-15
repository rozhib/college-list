import csv

def get_university(file_name, column, word):
    with open(file_name, mode='r') as file:
        reader = csv.DictReader(file)
        return [row[column] for row in reader if word.lower() in row[column].lower()]

file_name = 'data.csv'
final = []
column_name = 'INSTNM'

name = input("University Search \n\nEnter the name of the university that you want to add to your list. Enter 'done' to finish. ")

print("")

while name != "Done":
    universities = get_university(file_name, column_name, name)

    if len(universities) == 0:
        name = input("No results. \n\nEnter the name of the university that you want to add to your list. Enter 'Done' to finish. ")

    elif len(universities) == 1:
        final.append(universities[0])
        name = input(f"Added university: {universities[0]}\n\nEnter the name of the university that you want to add to your list. Enter 'Done' to finish. ")

    
    elif len(universities) < 20:
        print("\nMultiple universities found:")
        for i, university in enumerate(universities):
            print(f"{i+1}. {university}")

        valid_choice = False
        while not valid_choice:
            choice = input("\nEnter the number of the university you want to add (or 'skip' to skip): ")

            if choice.isdigit() and 1 <= int(choice) <= len(universities):
                final.append(universities[int(choice) - 1])
                name = input(f"Added university: {universities[int(choice) - 1]}\n\nEnter the name of the university that you want to add to your list. Enter 'Done' to finish. ")
                valid_choice = True 
            elif choice.lower() == 'skip':
                name = input("\nNo university added. Enter the name of the university that you want to add to your list. Enter 'Done' to finish. ")
                valid_choice = True  
            else:
                print("\nInvalid input. Please enter a valid number or 'skip' to skip.")

    else:
        name = input("Try something more specific. \n\nEnter the name of the university that you want to add to your list. Enter 'Done' to finish. ")

print("\nFinal list of universities:\n")
for uni in final:
    print(uni)
print("\n")