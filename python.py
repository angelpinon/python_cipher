def cipher():
    shiftAmt= int((input)("By how much would you like the string to be shifted by?"))
    myString= input("What string would you like me to encrypt?")
    cipherString= " "

    for c in myString:
        if c.isalpha():
            asciiValue= ord(c)
            asciiValue+= shiftAmt

            if asciiValue< ord("a"):
                asciiValue+= 26
            if asciiValue> ord("z"):
                asciiValue-= 26
            
            x= chr(asciiValue)
            cipherString+= x
        
        
    print(cipherString)

if __name__== "__main__":
    cipher()
