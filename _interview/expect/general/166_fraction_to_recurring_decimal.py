"""
166. Fraction to Recurring Decimal
Medium

692

1519

Add to List

Share
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

Example 1:

Input: numerator = 1, denominator = 2
Output: "0.5"
Example 2:

Input: numerator = 2, denominator = 1
Output: "2"
Example 3:

Input: numerator = 2, denominator = 3
Output: "0.(6)"
"""
def fractionToDecimal(numerator, denominator):
    num, den = numerator, denominator
    if not den:  # denominator is 0
        return
    if not num:  # numerator is 0
        return "0"

    res = []

    # meaning only one is smaller than 0
    if (num < 0) ^ (den < 0):
        res.append("-")  # add the sign

    num, den = abs(num), abs(den)
    res.append(str(num//den))
    rmd = num % den
    if not rmd:
        return "".join(res)  # only has integral part

    res.append(".")  # has frational part
    dic = {}

    while rmd:
        # print(1, dic, rmd)
        if rmd in dic:   # the remainder recurs => *** anyway rmd is one length int because rmd is always length one you know => that means we can terminate it first repeat point.
            res.insert(dic[rmd], "(")
            res.append(")")
            break
        # for having the index as a value
        dic[rmd] = len(res)
        # one position by one position
        div, rmd = divmod(rmd*10, den)
        # when we insert "(" into the index of dic[rmd] => this will be automatically go to next index
        # we do that if that is recur, otherwise it just remain that point
        res.append(str(div))
    return "".join(res)


test = fractionToDecimal(7, -12)
print(test)