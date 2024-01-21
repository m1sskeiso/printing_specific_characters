# Accept a string input from the user
user_input = input("Please enter the word: ")

# Display characters at even index numbers
result = ""
for index in range(0, len(user_input), 2):
    result += user_input[index]
    
# Print the result
    print(f"Here are the only even letters:", result)

