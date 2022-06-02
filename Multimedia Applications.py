bits = int(input('Enter number of bits\n'))
xMin = float(input('Enter ADC upper voltage\n'))
xMax = float(input('Enter ADC lower voltage\n'))
voltage = int(input('Enter new number of voltage\n'))
quantizationNumber = 2 ** bits
stepSize = xMax - xMin / quantizationNumber
rounds = int(voltage - xMin / stepSize)
voltQuantized = xMin - rounds*stepSize
upperLimit = voltQuantized + stepSize /2
lowerLimit = voltQuantized - stepSize /2
print('Number of rounds are',rounds)
# print('stepSize is', stepSize)
# print('quantization levels are', quantizationNumber)
# print('upper Limit is', upperLimit)
# print('Lower limit is', lowerLimit)
# print('New voltage quantization level is', voltQuantized)
