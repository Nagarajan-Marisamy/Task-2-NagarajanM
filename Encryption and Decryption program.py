print("welcome to Encryption and Decryption program ")
print("Type 0 to Perform Encryption and 1 to Perform Decryption and 2 to do both ")
decision=int(input("Enter your Choice of Operation: "))
if decision==0:
    text=input("Enter the text you need to encrypt:  ")
    while True:
        try:
            shift=int(input("Enter how many shifts needed : "))
            break
        except ValueError:
            print("please enter number only:")
    encrypted=""
    for char in text:
        if char.isupper():
            encrypted+=chr((ord(char)-65 + shift )% 26 + 65)
        elif char.islower():
            encrypted+=chr((ord(char)-97 + shift )% 26 + 97)
        elif char.isdigit():
            encrypted+=str((int(char)+ shift) % 10)
        else:
            encrypted+=char
    print(f"the text is encrypted successfully : {encrypted}")


elif decision==1:
    text=input("Enter the text you want to decrypt: ")
    while True:
        try:
            shift=int(input("Enter how many shifts used while encryption : "))
            break
        except ValueError:
            print("please enter number only:")

   
    decrypted=""
    for char in text:
        if char.isupper():
            decrypted+=chr((ord(char)-65 - shift) % 26 + 65)
        elif char.islower():
            decrypted+=chr((ord(char)-97 - shift) % 26 + 97)
        elif char.isdigit():
            decrypted+=str((int(char)- shift) % 10)
        else:
            decrypted+=char
    print(f"the text is decrypted succesfully: {decrypted}")


elif decision==2:
    text=input("Enter the text you want to Encrypt: ")
    while True:
        try:
            shift=int(input("Enter how many shifts needed : "))
            break
        except ValueError:
            print("please enter number only:")

    encrypted=""
    for char in text:
        if char.isupper():
            encrypted+=chr((ord(char)-65 + shift) % 26 + 65)
        elif char.islower():
            encrypted+=chr((ord(char)-97 + shift) % 26 + 97)
        elif char.isdigit():
            encrypted+=str((int(char)+ shift) % 10)
        else:
            encrypted+=char
    print(f"the text is succesfully encrypted :{encrypted} ")

    decrypted=""
    for char in encrypted:
        if char.isupper():
            decrypted+=chr((ord(char)-65 - shift) % 26 + 65) 
        elif char.islower():
            decrypted+=chr((ord(char)-97 - shift) % 26 + 97)
        elif char.isdigit():
            decrypted+=str((int(char)- shift )% 10)
        else:
            decrypted+=char
    print(f"the decrypted text is : {decrypted}")
else:
    print("invalid choice , choose the correct choice")
input("press enter to exit the program ")
