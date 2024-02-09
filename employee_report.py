import csv

infile = open('employee_data.csv', 'r')

csv_file = csv.reader(infile)

next(csv_file)

#pre initializing lists
high_efficiency = []
low_efficiency = []
employee_40 = []
employee_30 = []
employee_20 = []
count_40 = 0
count_30 = 0
count_20 = 0


for rec in csv_file:
    name = rec[1]
    hours_worked = float(rec[4])
    productivity = float(rec[5])
    age = int(rec[2])
        
    #calculate efficiency = productivity/hrs worked
    efficiency = float(productivity / hours_worked)

    if efficiency > 2:
        high_efficiency.append(name)
    elif efficiency < 1:
        low_efficiency.append(name)

    if age >= 40:
        employee_40.append(name)
        count_40 += 1
    elif age >= 30:
        employee_30.append(name)
        count_30 += 1
    else:
        employee_20.append(name)
        count_20 += 1
    

#print the results
    
print('Highly Efficient Individuals:')
for name in high_efficiency:
    print(name)
print('\n\n')


print('Low Efficient Individuals:')
for name in low_efficiency:
    print(name)
print('\n\n')


print('Employees in their 40s')
for name in employee_40:
    print(name)
print()
print(f"Total number of employees in their 40s: {count_40}")
print('\n\n')


print('Employees in their 30s')
for name in employee_30:
    print(name)
print()
print(f"Total number of employees in their 30s: {count_30}")
print('\n\n')



print('Employees in their 20s')
for name in employee_20:
    print(name)
print()
print(f"Total number of employees in their 20s: {count_20}")
print('\n\n')




