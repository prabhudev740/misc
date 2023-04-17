def getConcatenation(nums):
    return [ element for copyTimes in range(2) for element in nums]

print(getConcatenation([1,2,1]))
print(getConcatenation([1,3,2,1]))