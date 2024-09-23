print("Welcome to Elite 101 Chatbot")
user_name = input("Please enter your name: ")

if input == "":
  print("Please enter your name")
else:
  user_age = input(f'Nice to meet you {user_name}! How old are you? ')

print(
    f'Welcome {user_name}! Oh to be {user_age} years old! How can I help you today? '
)
print("Please choose from the following options:")
print("1. Placeholder Option 1")
print("2. Placeholder Option 2")
print("3. Placeholder Option 3")
print("4. Exit the conversation")
user_choice = input("Enter the number of your choice: ")
if user_choice == "4":
  print(f'Goodbye {user_name}! Have a great day!')
