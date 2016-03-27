import re

OPERATOR_REGEX = '(plus|minus|multiplied|divided)'

def calculate(sentence):
    operators = re.findall(OPERATOR_REGEX, sentence)
    if operators == None:
        raise ValueError

    nums = map(int, re.findall(r"\-?\d+", sentence))
    if len(nums) != len(operators) + 1:
        raise ValueError

    i = 1
    j = 0
    while i < len(nums):
        if operators[j] == 'plus':
            nums[i] = nums[i - 1] + nums[i]
        if operators[j] == 'minus':
            nums[i] = nums[i - 1] - nums[i]
        if operators[j] == 'multiplied':
            nums[i] = nums[i - 1] * nums[i]
        if operators[j] == 'divided':
            nums[i] = nums[i - 1] / nums[i]
        i += 1
        j += 1
    return nums[len(nums) - 1]
