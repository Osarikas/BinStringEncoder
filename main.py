def binaryEncoder(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, str):
            return ' '.join(format(ord(c), '08b') for c in result)
        return result
    return wrapper

def binaryDecoder(func):
    def wrapper(*args, **kwargs):
        binary_string = func(*args, **kwargs)
        return ''.join(chr(int(b, 2)) for b in binary_string.split())
    return wrapper

@binaryEncoder
def getMessage(binaryString):
    return binaryString

@binaryDecoder
def getBinaryMessage(string):
    return string

encodeType = input("Enter encode or decode: ")
if encodeType == "encode":
    print(getMessage(input("Enter a string: ")))
elif encodeType == "decode":
    print(getBinaryMessage(input("Enter a binary string: ")))
else:
    print("Invalid input")
