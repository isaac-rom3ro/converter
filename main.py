from binary import Binary
from words import WordNumbers

myNumber = Binary()
print(myNumber.convertNumberToBinary(4))
print(myNumber.convertBinaryToNumber(100))

myWordNumber = WordNumbers(400)

print(myWordNumber.convertNumberIntoWord())