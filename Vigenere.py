def decrypt(ciphertext, key):
    result = ""
    key = key.lower()
    key_index = 0
    key_length = len(key)

    for char in ciphertext:
        if char.isalpha():
            # convert letter to 0-25 index (case-insensitive)
            c = ord(char.lower()) - ord('a')
            # get shift amount from key
            k = ord(key[key_index % key_length]) - ord('a')
        # Vigenère decryption
            p = (c - k) % 26
        # convert back to lowercase letter
    
            result += chr(p + ord('a'))
            key_index += 1
        else:
            result += char  # preserve spaces, punctuation, etc.

    return result


ciphertext = input("Enter the cipher: ")
key = input("Enter the key: ")
print(decrypt(ciphertext, key))