import csv
#read a file
file_obj = open('customers.csv', 'r')
outfile = open('customer_country.csv', 'w')

csv_file = csv.reader(file_obj)

#this will skip the first record which is the header
next(csv_file)
   
    
#print(file_contents)
outfile.write('Full Name,Country\n')
for rec in csv_file:
    outfile.write(f"{rec[1]} {rec[2]}, {rec[4]}\n")

outfile.close()
