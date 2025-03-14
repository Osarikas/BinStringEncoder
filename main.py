encodeType = input("Enter encode or decode: ")
resultString = ''
if encodeType == 'encode':
    inputString = input("Enter a binary string: ")
    for i in range(0, len(inputString), 8):
        byte = inputString[i:i+8]
        charCode = int(byte, 2)
        resultString += chr(charCode)
    print(resultString)
elif encodeType == 'decode':
    inputString = input("Enter a string: ")

    for char in inputString:
        charCode = ord(char)
        resultString += format(charCode, '08b')

    print(resultString)
else:
    print("Invalid input")