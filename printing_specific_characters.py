# Accept a string input from the user
print("Here are the only even index char:")
user_input = input("Please enter the word: ")

# Display characters at even index numbers
print("Here are the only even index char:")
for index in range(0, len(user_input), 2):
    result = user_input[index]
    
# Print the result
    print(result)

