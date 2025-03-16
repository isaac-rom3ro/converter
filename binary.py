class Binary:
    def convertNumberToBinary(self, number) -> list:
        dividend = number
        divisor = 2
        quocient = 0
        binaryNumber = []

        while(dividend > 1):
            rest = int(dividend % divisor)
            quocient = int(dividend / divisor)
            dividend = quocient

            binaryNumber.append(rest)
            
        binaryNumber.append(quocient)

        binaryNumber.reverse()

        return binaryNumber
    
    def convertBinaryToNumber(self, number) -> int: 
        base = 2
        expoent = 0
        numberTransformed = 0

        for letter in reversed(str(number)):
            if(letter == "1"):
                numberTransformed = base ** expoent
            
            expoent+= 1

        return numberTransformed
