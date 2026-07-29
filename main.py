from cipher import encrypt, decrypt

def main():
    print("==== Caesar Cipher ====")
    choice = input("Need to (c)rypt or (d)ecrypt? ")
    text = input("Enter your text: ")
    shift = int(input("Enter the offset (integer): "))

    if choice == "c":
        result = encrypt(text, shift)
    elif choice == "d":
        result = decrypt(text, shift)
    else:
        print("Invalid choice")
        return

    print(f"Result: {result}")

if __name__ == "__main__":
    main()
