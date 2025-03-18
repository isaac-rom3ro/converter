class Binary:
    #created a init function just to pass it haha
    def __init__(self):
        pass

    #method that transforms number -> binary
    def convertNumberToBinary(self, number) -> list:
        #i have used the formule ->
        # 1. divide the number by 2 -> (dividend)4 / (fix divisor)2
        # 2. takes the rest and add to the list where we will build the binary form -> 4 % 2 = 0 | binary.append(0)
        # 3. the new dividend will be the quocient(result) of last operation -> 4 / 2 = newDividend(2)
        # 4. repeat while the dividend be greater than 1
        # 5. on the last allowed division we need to take the quocient as part of binary -> 2/2 = 2 * (this one we got 1 | stops here)
        # 6. now we have [0, 0, 1], so we need just to reverse it binary.reverse() this function will do the work for us
        # 7. return the result [1, 0 ,0] = 4

        dividend = number
        divisor = 2
        quocient = 0
        binaryNumber = []

        while(dividend > 1):
            rest = int(dividend % divisor)
            binaryNumber.append(rest)

            quocient = int(dividend / divisor)
            dividend = quocient
            
        binaryNumber.append(quocient)

        binaryNumber.reverse()

        return binaryNumber
    
    def convertBinaryToNumber(self, number) -> int:
        #for this convertion i used this follow formule ->
        # 1. receive the number as string "100" 
        # 2. make a sequence of base 2 starting by the last element -> (1 = [2²]) (0 = [2¹]) (0 = [2⁰])
        # 3. where letter is equal to 1 we take it as part o sum (1 = [2²]) = 4
        # 4. do it until the first element
        # 4. return the sum
        
        base = 2
        expoent = 0
        numberTransformed = 0

        for letter in reversed(str(number)):
            if(letter == "1"):
                numberTransformed = base ** expoent
            
            expoent+= 1

        return numberTransformed
