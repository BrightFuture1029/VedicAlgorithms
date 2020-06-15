#This solves this problem with arithmatic 
#We will hop to 3 position excluding current position
#if array limit breaches then we should start again
 
import os
p= ['Shani (Saturn)','Guru (Jupiter)','Mangal (Mars)','Ravi (Sun)','Shukra (Venus)','Budh (Mercury)','Chandra (Moon)']
dayNames = ['Shaniwar','Guruwar','Mangalwar','Raviwar','Shukrawar','Budhwar','Somwar']
lastStart = 0
for i in range(0,30):
    lastStart = lastStart+3 if lastStart+3 < 7 else (lastStart+3) -7 
    print( i, '->', lastStart,'->', p[lastStart],'->',dayNames[lastStart])




