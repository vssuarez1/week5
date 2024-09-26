# Problem Set 1: Indexing and Slicing Strings
# Basic Indexing:
# Given the string magic = 'abracadabra',
# a. Retrieve the 5th character. 
magic = "abracadabra" 
print(magic [0:5])
# b. Retrieve the second to last character.
print(magic [-2])
# c. Find the first occurrence of the letter 'c'.
print(magic.find("c"))

# Advanced Slicing:
# Given the string alphabet = 'abcdefghijklmnopqrstuvwxyz',
alphabet = "abcdefghijklmnopqrstuvwxyz"
print(alphabet[8:10])
# a. Extract the letters 'hij'.
print(alphabet[7:10])
# b. Extract every second letter starting from 'a' to 'm'.
print(alphabet[0:13:2])
# c. Reverse the entire string using slicing.
print(alphabet[::-1])

# Problem Set 2: Extracting Information
# From Descriptions:
# Extract the name of the famous personality from the quote "Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy"
print("kennedy")
# Manipulating Words:
# Given the string info = "Python is fun. Fun is good. Good is subjective.",
# a. Extract the word 'subjective' without knowing its exact position.
info="python is fun.Fun is good.Good is subjective"
subject=info.find("subjective")
# b. Extract every third word.
print(info[36:-1])
# c. Reverse the positions of the words, but keep the characters in each word in the same order.
print(info[-1])

# Problem Set 3: String Methods
# Upper & Lower:
# Convert the following text to lowercase: "MAY THE FORCE BE WITH YOU."
text1 = "MAY THE FORCE BE WITH YOU."
print(text1.lower)

# String Joining and Splitting:
# Given the list motto = ["Make", "haste", "slowly."],
# a. Convert the list into a single string.
# b. Now, split the string at every occurrence of the letter 'a'.
word_list = ["Make", "haste", "slowly."]
joined_list = " ".join(word_list)
print(joined_list)
split_sentence = joined_list.split("a")


# Replacing Words:
# Modify the sentence: "Life is what happens when you are busy making other plans."
# a. Replace "busy" with "distracted".
# b. Replace "plans" with "mistakes".
sentence1 = "Life is what happens when you are busy making other plans." 
new_sentence1 = sentence1.replace("busy","distracted").replace("plans","mistakes")
print(new_sentence1)

# Problem Set 4: String Properties and Advanced Operations
# Repetition:
# Concatenate the word "Iteration" 7 times.
word1 = "Iteration" * 7
print(word1)

# Word Search:
# Check if the word "moonlight" appears in the quote: "With freedom, books, flowers, and the moon, who could not be happy? - Oscar Wilde"
quote = "With freedom, books, flowers, and the moon, who could not be happy? - Oscar Wilde"
print(quote.find("moonlight"))

# Length and Count:
# a. Calculate the number of characters (including spaces and punctuation) in the word/phrase: "Supercalifragilisticexpialidocious".
# b. Count the number of times the letter 'i' appears in the same word/phrase.
phrase = "Supercalifragilisticexpialidocious" 
print(len(phrase))
print(phrase.find("i"))

#Name: Vanessa Suarez, Malik Hreish 

