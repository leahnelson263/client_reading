import csv

infile = open('employee_data.csv', 'r')

csv_file = csv.reader(infile)

next(csv_file)


efficiency_level = ''
age_range = ''

def main():
    display_high_efficiency()
    print()
    display_low_efficiency()
    print()
    display_40s()
    print()
    display_30s()
    print()
    display_20s()
    print()

#FUNCTION 1: EFFICIENCY - HIGH
def display_high_efficiency():
    print('Highly Efficient Individuals:')

    for rec in csv_file:
        name = rec[1]
        hours_worked = float(rec[4])
        productivity = float(rec[5])

        #calculate efficiency = productivity/hrs worked
        efficiency = float(productivity / hours_worked)

        if efficiency > 2:
            print(name)


#FUNCTION 2: EFFICIENCY - LOW
def display_low_efficiency():
    print('Low Efficient Individuals:')

    for rec in csv_file:
        name = rec[1]
        hours_worked = float(rec[4])
        productivity = float(rec[5])

        #calculate efficiency = productivity/hrs worked
        efficiency = float(productivity / hours_worked)

        if efficiency < 1:
            print(name)


#FUNCTION 3: AGE - 40s 
def display_40s():
    print('Employees in their 40s')
    count = 0
    for rec in csv_file:
        name = rec[1]
        hours_worked = float(rec[4])
        productivity = float(rec[5])
        age = rec[2]

        if age == range(40,50,1):
            print(name)


    print('Total number of employees in their 40s: ')


#FUNCTION 4: AGE - 30s 
def display_30s():
    print('Employees in their 30s')

    for rec in csv_file:
        name = rec[1]
        hours_worked = float(rec[4])
        productivity = float(rec[5])
        age = rec[2]

        if age == range(30,40,1):
            print(name)

    print('Total number of employees in their 30s: ')


#FUNCTION 5: AGE - 20s 
def display_20s():
    print('Employees in their 20s')

    for rec in csv_file:
        name = rec[1]
        hours_worked = float(rec[4])
        productivity = float(rec[5])
        age = rec[2]

        if age == range(20,30,1):
            print(name)

    print('Total number of employees in their 20s: ')



main()