n_values = [2, 3, 7, 9]
multiples_dict = {n: [i for i in range(n, 101, n)] for n in n_values}
print(f"Multiples of 9: {multiples_dict[9]}")
print(f"Multiples of 7: {multiples_dict[7]}")
print(f"Multiples of 3: {multiples_dict[3]}")
print(f"Multiples of 2: {multiples_dict[2]}")

#caesar task

def caesar_cipher(text, shift=13):
    result = ""

    for char in text.upper():
        if "A" <= char <= "Z":
            
            shifted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            result += shifted_char
        else:
            result += char 
    return result


message = "YOXLAMA"
encrypted = caesar_cipher(message)
print(f"Original:  {message}")
print(f"Encrypted: {encrypted}") 
