import csv

infile = open('employee_data.csv', 'r')

csv_file = csv.reader(infile)

next(csv_file)

for rec in csv_file:
    name = rec[1]
    salary = float(rec[3])
    bonus_percentage = float(rec[7])
    bonus = salary * bonus_percentage
    pay = float(bonus + salary)
    
    #print(rec)
    # print(f"Name: {rec[1]}")
    # print(f"Salary: ${rec[3]}")
    # print(f"Bonus:  $ {rec[7]}")
    # print(f"Pay:   $ {rec[]}")
    
    print(f"Name: {name}")
    print(f"Salary:  $  {salary:,.2f}")
    print(f"Bonus:   $   {bonus:,.2f}")
    print(f"Pay:     $  {pay:,.2f}")
    print()
    input()
