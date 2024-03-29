def unique_word_composition(strings):
	# Create a set to hold the unique words
	unique_words = set()
	
    # Iterate through the words in the list and initialize the set to hold the letters
	for word in strings:
		word_letters = set()
        
        # Add each letter to the set which will then only hold duplicates
		for letter in word:
			word_letters.add(letter)
            
        # Compare the new set with the original string. If there are the same number
        # of letters in each then we know that the string is made of only unique elements
		if len(word_letters) == len(word):
			unique_words.add(word)
            
	return unique_words

strings = ["apple", "banana", "orange", "grape", "kiwi", "watermelon", "peach", "pear", "plum", "strawberry", "pineapple"]
#strings = ["Life is beautiful.", "Coding is fun!", "Stay positive.", "Dream big.", "Never give up."]
#strings = ["banana", "hello", "coffee", "success", "butter", "pizza", "apples"]

# Run the function and store the results
unique_strings = unique_word_composition(strings)

# Print the original list of strings
print(strings)

# If there were no strings with a unique composition, then print a message to the user
if len(unique_strings) > 0:
	print(f"{unique_strings} is/are composed of unique elements.")
    
else:
	print("None of the strings are composed of unique elements.")
	
