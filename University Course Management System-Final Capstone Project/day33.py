#day33-using zip, filter, map functions to combine 2 lists, classify adults and difference of age from 18
names = ['Alice', 'Bob', 'Charlie', 'Ahad', 'Chloe']
ages = [30, 12, 17, 21, 20]

result = dict(zip(names, ages))
print(result)

adults = dict(filter(lambda item : item[1] > 18, result.items()))
print(adults)

age_from_18 = dict(map(lambda item :  (item[0], item[1] - 18), result.items()))
print(age_from_18)