solver = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"

cipher_sent = input("Enter the cipher text:  ")
cipher_list = cipher_sent.split()

shift = input("Enter the shift if known:  ")

# I separated the small and capital letters to keep the index matching with the solver
indexer = "abcdefghijklmnopqrstuvwxyz..........................ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def engine():
    decoded = ""
    for word in cipher_list:
        decoded_word = ""
        for letter in word:
            index = indexer.index(letter)
            # print(index)
            decoded_letter = solver[index + ishift]
            decoded_word += decoded_letter
            # print(decoded)
        decoded = decoded + " " + decoded_word
    print("For", ishift, "shift the result is: ", decoded)


if len(shift) > 0:
    ishift = int(shift)
    engine()
else:
    for i in range(1, 27):
        ishift = i
        engine()
