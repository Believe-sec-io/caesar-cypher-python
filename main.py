from cipher import encrypt, decrypt

def main():
    print("==== Caesar Cipher ====")
    choice = input("Chiffrer (c) ou déchiffrer (d) ? ").lower()
    text = input("Entrez le texte : ")
    shift = int(input("Entrez le décalage : "))

    if choice == "c":
        result = encrypt(text, shift)
    elif choice == "d":
        result = decrypt(text, shift)
    else:
        print("Choix invalide")
        return

    print(f"Résultat : {result}")

if __name__ == "__main__":
    main()


