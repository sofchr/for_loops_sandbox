target = int(input()) # Enter a number between 0 and 1000

#two options

#first option
even_sum = 0
for number in range(2, target + 1):
    if number % 2 == 0:
      even_sum += number
print(even_sum)


#second option
# even_sum = 0
# for number in range(2, target + 1, 2):
#   even_sum += number
# print(even_sum)