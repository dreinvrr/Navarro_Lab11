words = []
for i in range(10):
    word = input(f"Enter a word {i + 1}: ")
    words.append(word)
    
while True:
    length = input("Enter a length/number: ")
    if length.isdigit():
        length = int(length)
        break
    else:
        print("Invalid input. Please enter a number.")
        
matching_words = [word for word in words if len(word) >= length]
print("\nSuccess!")
if matching_words:
    print("\nWords with the required length:", ', '.join(matching_words))
else:
    print("\nNo words are found with the required length.\n")