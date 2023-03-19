#BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
def blackjack(a,b,c):
    totalsum = a+b+c
    if totalsum <=21:
        return totalsum
    elif totalsum >21 and (a ==11 or b ==11 or c==11):
        return (totalsum -10)
    else: 
        pass
    return "Bust"
# Check
print(blackjack(5,6,7))
# Check
print(blackjack(9,9,9))
# Check
print(blackjack(9,9,11))

#SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.

def summer_69(arr):
    total = 0
    add = True
    for num in arr:
        while add:
            if num != 6:
                total += num
                break
            else:
                add = False
        while not add:
            if num != 9:
                break
            else:
                add = True
                break
    return total
# Check
print(summer_69([1, 3, 5]))
# Check
print(summer_69([4, 5, 6, 7, 8, 9]))
# Check
print(summer_69([2, 1, 6, 9, 11]))
#Just for fun:
#PRINT BIG: Write a function that takes in a single letter, and returns a 5x5 representation of that letter
def print_big(letter):
    patterns = {1:'  *  ',2:' * * ',3:'*   *',4:'*****',5:'**** ',6:'   * ',7:' *   ',8:'*   * ',9:'*    '}
    alphabet = {'A':[1,2,4,3,3],'B':[5,3,5,3,5],'C':[4,9,9,9,4],'D':[5,3,3,3,5],'E':[4,9,4,9,4]}
    for pattern in alphabet[letter.upper()]:
        print(patterns[pattern])
print_big('b')