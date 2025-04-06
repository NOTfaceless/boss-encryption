import string
alphabet = string.ascii_lowercase

print(alphabet)





print("BOSS ENCRYPTION (V1.0) ")
print("------------------")
print("Q = quit\n---------\n" "Encr = Encrypts msg\n---------\n" "Decr = Decrypts msg\n---------\n")

TERMINATE = False
LettersAhead = 3
ALPHABET_SIZE = 26
letter_positions = {letter: i for i, letter in enumerate(alphabet)}

def HandleMsg(msg,Encrypt):
    newMsg = []
    strInd = 0
    for char in msg:
        newChar = " "

        if char == newChar:
            newMsg.append(newChar)
            continue

        letterPos = letter_positions[char.lower()]


        if Encrypt:
            newChar = alphabet[(letterPos + LettersAhead) % len(alphabet)]
        else:
            newChar = alphabet[(letterPos - LettersAhead) % len(alphabet)]
                            
        if char.isupper():
            newChar = newChar.upper()
        
        newMsg.append(newChar)


    return "".join(newMsg)   

def numberCheck(msg):

    if  msg.isdigit():
        print("NUMBERS NOT SUPPORTED YET OK BOSS?")
        return True
    else:
        return False
    

while not TERMINATE:

    command = input("Input your command :  ")
    if command.lower() == "q":
        TERMINATE = True
        print("-------------------")
        print("SBoss encryption is closing...")
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




