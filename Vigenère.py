def header(alphabet):
    alpha_len = len(alphabet)
    print("|   ",end="")
    for i in range(alpha_len):
        print(f"| {alphabet[i]}",end=" ")
    print("|")
    print(f"{'|---' * (alpha_len + 1)}|")

def vigenere_square(alphabet:str):
    shift = 0
    alpha_len = len(alphabet)
    header(alphabet)
    for shift in range(alpha_len):
        for i, _ in enumerate(alphabet):
            if i == 0:
                c = alphabet[(i + shift) % alpha_len]
                print(f"| {c}",end=" ")
                print(f"| {c}", end=" ")
            else: print(f"| {alphabet[(i + shift) % alpha_len]}",end=" ")
        print("|")

def letter_to_index(letter,alphabet:str):
    al_lower = alphabet.lower()
    le_lower = letter.lower()
    return al_lower.index(le_lower)

def index_to_letter(index,alphabet:str):
    alpha_len = len(alphabet)
    if 0 < index < alpha_len:
        return alphabet[index]
    else:
        raise ValueError(f"number must be between 0 and {alpha_len - 1}")

def vigenere_index(key_letter, plaintext_letter, alphabet):
    return (letter_to_index(key_letter, alphabet) + letter_to_index(plaintext_letter, alphabet)) % len(alphabet)
key = "cybertruck"
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
message = "Hello World"

# vigenere_square(alphabet)
print(letter_to_index("a", alphabet))
print(index_to_letter(20, alphabet))
print(vigenere_index(key[0], message[0], alphabet))