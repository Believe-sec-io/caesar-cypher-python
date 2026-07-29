
from cipher import encrypt, decrypt

def main():                    
    print("==== Caesar Cipher ====")      
    choice = input(...).lower()            
    text = input(...)                       
    shift = int(input(...))                 

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
