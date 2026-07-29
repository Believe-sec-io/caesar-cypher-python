def encrypt(text: str, shift: int) -> str:
    """Chiffre un texte avec un décalage donné."""
    result = []
    for char in text:
        if char.isupper():
            result.append(chr((ord(char) - ord('A') + shift) % 26 + ord('A')))
        elif char.islower():
            result.append(chr((ord(char) - ord('a') + shift) % 26 + ord('a')))
        else:
            result.append(char)  # Préserve les espaces/punctuation
    return ''.join(result)

def decrypt(text: str, shift: int) -> str:
    """Déchiffre un texte avec un décalage donné."""
    return encrypt(text, -shift)  # Le déchiffrement est l'inverse
