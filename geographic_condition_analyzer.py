places = [
    {'name':'Delhi', 'population':19000000, 'rainfall':80},
    {'name':'Mumbai', 'population':20000000, 'rainfall':220},
    {'name':'Jaipur', 'population':4000000, 'rainfall':60},
    {'name':'Shillong', 'population':500000, 'rainfall':250},
    {'name':'Chennai', 'population':11000000, 'rainfall':140}
]


print('Geographic Condition Analyzer')
print('---------------------------------')


population_count = 0
rainfall_count = 0
both_condition_count = 0
count=0

for place in places:
  if place['population'] > 10000000:
    population_count += 1
  if place['rainfall'] > 100:
    rainfall_count +=1 
  if place['population'] > 10000000 and place['rainfall'] > 100:
   both_condition_count += 1
  if place['population'] > 10000000 or place['rainfall'] > 100:
    count += 1

print('cities with population > 10 million:',population_count) 
print('cities with rainfall> 100:', rainfall_count)
print('cities satisfies both conditions:',both_condition_count) 
print('Cities satisfying AT LEAST ONE condition:',count)
