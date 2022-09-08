

import csv

infile=open("steps.csv","r")
outfile=open("avg_steps.csv","w")

csvfile=csv.reader(infile, delimiter=',')

next(csvfile)

months= ['NA','January','February', 'March','April','May','June',
'July','August','September','October','November','December']

month=1
Steps_tkn=0
day_cnt=0

for record in csvfile:


    if record[0]== str(month):
        Steps_tkn+= int(record[1])
        day_cnt+=1
        
         
        
    else:
        Avg_Steps= format(Steps_tkn/day_cnt, '.2f')
        outfile.write(months[int(month)] + ', ' + str(Avg_Steps) + '\n')
        month= record[0]
        Steps_tkn= int(record[1])
        day_cnt=1

Avg_Steps= format(Steps_tkn/day_cnt, '.2f')
outfile.write(months[int(month)] + ', ' + str(Avg_Steps) + '\n')
month= record[0]
Steps_tkn= int(record[1])
day_cnt=1


outfile.close()

        


