# Caesar Cipher - Encryption and Decryption

# Alphabet list for reference
alphabets = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

# Get user inputs
direction = input("Type 'encode' to encrypt and 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(original_text, shift_amount):
    """
    Encrypts text using Caesar Cipher by shifting letters forward.
    
    Parameters:
    - original_text: The message to encrypt
    - shift_amount: Number of positions to shift each letter
    """
    cipher_text = ""
    for letter in original_text:
        # Find current position and shift forward
        shifted_position = alphabets.index(letter) + shift_amount
        # Use modulo to wrap around if needed (z → a)
        shifted_position %= len(alphabets)
        cipher_text += alphabets[shifted_position]
    print(f"Here is the encoded result: {cipher_text}")


def decrypt(original_text, shift_amount):
    """
    Decrypts Caesar Cipher text by shifting letters backward.
    
    Parameters:
    - original_text: The encrypted message
    - shift_amount: Number of positions letters were shifted
    """
    plain_text = ""
    for letter in original_text:
        # Find current position and shift backward
        shifted_position = alphabets.index(letter) - shift_amount
        # Use modulo to wrap around if needed (a → z)
        shifted_position %= len(alphabets)
        plain_text += alphabets[shifted_position]
    print(f"Here is the decoded result: {plain_text}")


# Call appropriate function based on user choice
if direction == "encode":
    # Using keyword arguments for clarity
    encrypt(original_text=text, shift_amount=shift)
elif direction == "decode":
    # Using keyword arguments
    decrypt(original_text=text, shift_amount=shift)
else:
    print("Invalid direction. Please type 'encode' or 'decode'.")
