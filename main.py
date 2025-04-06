alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']







print("BOSS ENCRYPTION (V1.0) ")
print("------------------")
print("Q = quit\n---------\n" "Encr = Encrypts msg\n---------\n" "Decr = Decrypts msg\n---------\n")

TERMINATE = False
LettersAhead = 3

def HandleMsg(msg,Encrypt):
    newMsg = ""
    strInd = 0
    for char in msg:
        newChar = " "
        for i in range(0,26):
            if alphabet[i] == char.lower():
                if Encrypt:
                    if i + LettersAhead - 1 >= 25:
                        diff = 25 - i
                        newChar = alphabet[(LettersAhead-diff) - 1]
                    else:    
                        newChar = alphabet[i + LettersAhead]
                else:
                    if i - LettersAhead < 0:
                        newChar = alphabet[25 - abs(i - LettersAhead) + 1]
                    else:
                        newChar = alphabet[i - LettersAhead]
                            
                            

        strInd += 1
        newMsg = newMsg[:strInd] + newChar
    return newMsg    

def numberCheck(msg):

    if msg.isdigit():
        print("NUMBERS NOT SUPPORTED YET OK BOSS?")
        return True
    else:
        return False
    

while not TERMINATE:
    command = input("Input your command :  ")
    if command.lower() == "q":
        TERMINATE = True
        print("-------------------")
        print("Super duper encryption is closing...")
    elif command.lower() == "encr":

        msg = input("Insert your messeg: ")

        if numberCheck(msg):
            continue

        encryptedMsg = HandleMsg(msg,True)
        print("Your encrypted msg is : ", encryptedMsg)

    elif command.lower() == "decr":
     

        msg = input("Insert your messeg: ")

        if numberCheck(msg):
            continue

        decryptedMsg = HandleMsg(msg,False)
        print("Your decrypted msg is : ", decryptedMsg)
    else:
        print("Unknown command")           




