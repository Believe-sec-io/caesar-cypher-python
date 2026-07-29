from cipher import encrypt, decrypt

def main():
  print("====Chiffre cesar===")
  choice= input("Need to (c)rypt or (d)crypt ? ")
  text=input("Entrer you text: ")
  shift= int(input("Entrer the offset (integer)"))

if choice== "c":
  result=encrypt(text,shift)
elif choice== "d":
  result=decrypt(text,shift)
else:
  ptint("invalide choice")
  return

 print=(f"result: {result}")

if __name__=="__main__":
    main()
