'''
There was a set of cards with numbers from 1 to N. One of the card is now lost. Determine the number on that lost card given the numbers for the remaining cards.
Given a number N, followed by N - 1 integers - representing the numbers on the remaining cards (distinct integers in the range from 1 to N). Find and print the number on the lost card.

'''
N = int(input("Enter the limit: "))
remaining_sum = 0
for i in range(N - 1):
    remaining_sum += int(input("Enter the numbers between 1 and N: "))
total_sum = N * (N + 1) // 2
missing_card = total_sum - remaining_sum
print(missing_card)
