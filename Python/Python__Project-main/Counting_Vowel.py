'''
Creator Details
Name : Bishal jaiswal
Class : VIII(8)
Nationality : Nepali
'''

Word = input("Enter the word or sentence you want to know number of vowel\n> ").lower().strip()

vowel = ["a","e","i","o","u"]

count_vowel = 0 #Initializing the count form 0

for word in Word:
    if word in vowel:  # Checking if the vowels are present in the input word
        count_vowel+=1 # Counting how many vowels are there in the giver input
        
print(f"The number of vowel is {count_vowel}")
