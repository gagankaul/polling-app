# A program that conducts a poll on a yes or no issue. At the start of the program, the program asks the user
# to input the polling issue, the number of voters and a password to view the results. 

print("Welcome to the Yes or No Issue Polling App")

#Get user input
issue = input("\nWhat is the yes or no issue you will be voting on today: ")
num_voters = int(input("What is the number of voters you will allow on the issue: "))
passwd = input("Enter a password for viewing the results of the poll: ")

#Create a dictionary to save polled users and their response
results = {}

#The main program loop
for voter in range(num_voters):
    name = input("\nEnter your full name: ").title()
    if name not in results:
        print(f"Here is our issue: {issue}")
        response = input("What do you think ... yes or no: ").lower().strip()
        if (response != "yes") and (response != "no"):
            print("That's not a valid response")
        else:
            if response == "yes":
                results[name] = "yes"
            else:
                results[name] = "no"
            print(f"Thank you, {name}! Your vote of yes has been recorded.")
    else:
        print("Sorry, someone with this name has already voted.")

#Display names of people who voted
print(f"\nThe following {len(results)} people voted: ")
for key in results.keys():
    print(key)

#Display the results of the poll
yes = 0
no = 0
for value in results.values():
    if value == "yes":
        yes += 1
    else:
        no += 1
print(f"\nOn the following issue: {issue}")
if yes > no:
    print(f"Yes wins! {yes} votes to {no}.")
elif no > yes:
    print(f"No wins! {no} votes to {yes}.")
else:
    print("It's a tie!")

#Display full voting results by entering admin password

user_passwd = input("\nPlease enter the password to view polling results: ")
if user_passwd == passwd:
    for key,value in results.items():
        print(f"Voter: {key} \t\t Vote: {value}")

print("\nThank you for using the Yes or No Issue Polling App.")
