import csv

infile= open('Employeepay.csv','r')


csvfile= csv.reader(infile,delimiter= ',')
next (csvfile) #skips the first row of file

for record in csvfile:
    Pay= int(record[3])
    Bonus= float(record[4])
    Total_Pay= format(Pay+ (Bonus*Pay),',.2f')

    print('ID:', record[0])
    print('First Name:', record[1])
    print('Last Name', record[2])
    print('Salary: $', record[3])
    print('Bonus: $', record[4])
    print('Total Pay: $', Total_Pay)
    input('Press enter for next customer')
