# Considering the given list:
theWeek = ['mon', 'tue', 'wed', 'thu', 'fri']

# ex-1. print out in a sentence the most happiest and the sadiest days in the week
print(f'the happiest is {theWeek[4]} and the saiest is {theWeek[0]}')

# ex-2. now let's suppose you are in this sadiest day and you wan't to be with the mood of the happiest one and it would be possible just switching the days position
# how would do that?
theWeek[0], theWeek[4] = theWeek[4], theWeek[0]
print(theWeek)

theWeek = ['mon', 'tue', 'wed', 'thu', 'fri']
# ex-3. if you would work just 3 days in a row, which ones would be? Answer accessing the list elements
print(theWeek[2:])
print(theWeek[2:5])

# ex-4. now add the weekend days in the list
theWeek.append('sat')
theWeek.insert(0, 'sun')
print(theWeek)

# ex-5. considering the answer given in ex-3, how would you represent in a week with 7 days?
theWeek.insert(0, 'sat')
theWeek.insert(0, 'sat')
theWeek.insert(0, 'sat')
theWeek.insert(0, 'sat')

# ex-6. let's suppose you are during your vacation now, how would you represent the days that you work within a week? 
theWeek.clear()
print(theWeek)

# ex-7. considering you are getting about 5000zl/month as salary and the company will ajust it annually in 10% and it is represented in the following list:
wage = [5500, 5000, 6050]
# now print it out in ascending order and descending order
wage.sort()
print(wage)

wage.reverse()
print(wage)

# ex-8. you were trying to have a phone number of a friend of yours from office. This person gave some tips for you to guess and you made a code to grab the numbers in a list
# the numbers:
phoneNumbers = ['5','1','3','0','6','4','8','6','0']
# what would be the last line of your code to show the number not as list of elements but as we have in our mobiles?
phoneNumbers = "".join(phoneNumbers)
print(f'the phone number is: {phoneNumbers}')