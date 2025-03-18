#importing the required classes that i created to use their functions
from binary import Binary
from words import WordNumbers

myNumber = Binary()
myWordNumber = WordNumbers(400)

print(myNumber.convertNumberToBinary(4)) #number -> binary
print(myNumber.convertBinaryToNumber(100)) #binary -> number
print(myWordNumber.convertNumberIntoWord()) #number -> word