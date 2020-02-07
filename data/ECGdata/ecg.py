from matplotlib import pyplot as plt
import numpy as np
import csv

rec1a=[]
rec1b=[]
rec1c=[]
rec2a=[]
rec2b=[]
rec2c=[]
rec3a=[]
rec3b=[]
rec3c=[]
rec4a=[]
rec4b=[]
rec4c=[]
rec5a=[]
rec5b=[]
rec5c=[]
rec6a=[]
rec6b=[]
rec6c=[]
rec7a=[]
rec7b=[]
rec7c=[]
rec8a=[]
rec8b=[]
rec8c=[]
rec9a=[]
rec9b=[]
rec9c=[]
rec10a=[]
rec10b=[]
rec10c=[]
rec11a=[]
rec11b=[]
rec11c=[]
rec12a=[]
rec12b=[]
rec12c=[]
rec13a=[]
rec13b=[]
rec13c=[]
rec14a=[]
rec14b=[]
rec14c=[]
rec15a=[]
rec15b=[]
rec15c=[]
rec16a=[]
rec16b=[]
rec16c=[]
rec17a=[]
rec17b=[]
rec17c=[]
rec18a=[]
rec18b=[]
rec18c=[]
rec19a=[]
rec19b=[]
rec19c=[]
rec20a=[]
rec20b=[]
rec20c=[]

inp=int(input("Enter the person's number: "))

recno=int(input('Enter the record number:'))

inp1=str(inp)
recno1=str(recno)
if inp<10:
    j=str(i)
    with open('/Users/chaitanya/Downloads/ecg-id-database-1.0.0/Person_0'+inp1+'/rec'+recno1+'.txt','r') as csvfile:
        reader=csv.reader(csvfile,delimiter="\t")
        for row in reader:
            if recno==1:
                rec1a.append(float(row[0]))
                rec1b.append(float(row[1]))
                rec1c.append(float(row[2]))
            elif recno==2:
                rec2a.append(float(row[0]))
                rec2b.append(float(row[1]))
                rec2c.append(float(row[2]))
            elif recno==3:
                rec3a.append(float(row[0]))
                rec3b.append(float(row[1]))
                rec3c.append(float(row[2]))
            elif recno==4:
                rec4a.append(float(row[0]))
                rec4b.append(float(row[1]))
                rec4c.append(float(row[2]))
            elif recno==5:
                rec5a.append(float(row[0]))
                rec5b.append(float(row[1]))
                rec5c.append(float(row[2]))
            elif recno==6:
                rec6a.append(float(row[0]))
                rec6b.append(float(row[1]))
                rec6c.append(float(row[2]))
            elif recno==7:
                rec7a.append(float(row[0]))
                rec7b.append(float(row[1]))
                rec7c.append(float(row[2]))
            elif recno==8:
                rec8a.append(float(row[0]))
                rec8b.append(float(row[1]))
                rec8c.append(float(row[2]))
            elif recno==9:
                rec9a.append(float(row[0]))
                rec9b.append(float(row[1]))
                rec9c.append(float(row[2]))
            elif recno==10:
                rec10a.append(float(row[0]))
                rec10b.append(float(row[1]))
                rec10c.append(float(row[2]))
            elif recno==11:
                rec11a.append(float(row[0]))
                rec11b.append(float(row[1]))
                rec11c.append(float(row[2]))
            elif recno==12:
                rec12a.append(float(row[0]))
                rec12b.append(float(row[1]))
                rec12c.append(float(row[2]))
            elif recno==13:
                rec13a.append(float(row[0]))
                rec13b.append(float(row[1]))
                rec13c.append(float(row[2]))
            elif recno==14:
                rec14a.append(float(row[0]))
                rec14b.append(float(row[1]))
                rec14c.append(float(row[2]))
            elif recno==15:
                rec15a.append(float(row[0]))
                rec15b.append(float(row[1]))
                rec15c.append(float(row[2]))
            elif recno==16:
                rec16a.append(float(row[0]))
                rec16b.append(float(row[1]))
                rec16c.append(float(row[2]))
            elif recno==17:
                rec17a.append(float(row[0]))
                rec17b.append(float(row[1]))
                rec17c.append(float(row[2]))
            elif recno==18:
                rec18a.append(float(row[0]))
                rec18b.append(float(row[1]))
                rec18c.append(float(row[2]))
            elif recno==19:
                rec19a.append(float(row[0]))
                rec19b.append(float(row[1]))
                rec19c.append(float(row[2]))
            elif recno==20:
                rec20a.append(float(row[0]))
                rec20b.append(float(row[1]))
                rec20c.append(float(row[2]))
elif inp>=10:
    with open('/Users/chaitanya/Downloads/ecg-id-database-1.0.0/Person_'+inp1+'/rec'+recno1+'.txt','r') as csvfile:
        reader=csv.reader(csvfile,delimiter="\t")
        for row in reader:
            if recno==1:
                rec1a.append(float(row[0]))
                rec1b.append(float(row[1]))
                rec1c.append(float(row[2]))
                
            elif recno==2:
                rec2a.append(float(row[0]))
                rec2b.append(float(row[1]))
                rec2c.append(float(row[2]))
                
            elif recno==3:
                rec3a.append(float(row[0]))
                rec3b.append(float(row[1]))
                rec3c.append(float(row[2]))
                
            elif recno==4:
                rec4a.append(float(row[0]))
                rec4b.append(float(row[1]))
                rec4c.append(float(row[2]))
                
            elif recno==5:
                rec5a.append(float(row[0]))
                rec5b.append(float(row[1]))
                rec5c.append(float(row[2]))
              
            elif recno==6:
                rec6a.append(float(row[0]))
                rec6b.append(float(row[1]))
                rec6c.append(float(row[2]))
                
            elif recno==7:
                rec7a.append(float(row[0]))
                rec7b.append(float(row[1]))
                rec7c.append(float(row[2]))
                
            elif recno==8:
                rec8a.append(float(row[0]))
                rec8b.append(float(row[1]))
                rec8c.append(float(row[2]))
            elif recno==9:
                rec9a.append(float(row[0]))
                rec9b.append(float(row[1]))
                rec9c.append(float(row[2]))
            elif recno==10:
                rec10a.append(float(row[0]))
                rec10b.append(float(row[1]))
                rec10c.append(float(row[2]))
            elif recno==11:
                rec11a.append(float(row[0]))
                rec11b.append(float(row[1]))
                rec11c.append(float(row[2]))
            elif recno==12:
                rec12a.append(float(row[0]))
                rec12b.append(float(row[1]))
                rec12c.append(float(row[2]))
            elif recno==13:
                rec13a.append(float(row[0]))
                rec13b.append(float(row[1]))
                rec13c.append(float(row[2]))
            elif recno==14:
                rec14a.append(float(row[0]))
                rec14b.append(float(row[1]))
                rec14c.append(float(row[2]))
            elif recno==15:
                rec15a.append(float(row[0]))
                rec15b.append(float(row[1]))
                rec15c.append(float(row[2]))
            elif recno==16:
                rec16a.append(float(row[0]))
                rec16b.append(float(row[1]))
                rec16c.append(float(row[2]))
            elif recno==17:
                rec17a.append(float(row[0]))
                rec17b.append(float(row[1]))
                rec17c.append(float(row[2]))
            elif recno==18:
                rec18a.append(float(row[0]))
                rec18b.append(float(row[1]))
                rec18c.append(float(row[2]))
            elif recno==19:
                rec19a.append(float(row[0]))
                rec19b.append(float(row[1]))
                rec19c.append(float(row[2]))
            elif recno==20:
                rec20a.append(float(row[0]))
                rec20b.append(float(row[1]))
                rec20c.append(float(row[2]))
    
                        

plt.title('ECG RECORD')
plt.xlabel('')
plt.ylabel('')

if recno==1:
    plt.plot(rec1a,rec1b)
elif recno==2:
    plt.plot(rec2a,rec2b)
elif recno==3:
    plt.plot(rec3a,rec3b)
elif recno==4:
    plt.plot(rec4a,rec4b)
elif recno==5:
    plt.plot(rec5a,rec5b)
elif recno==6:
    plt.plot(rec6a,rec6b)
elif recno==7:
    plt.plot(rec7a,rec7b)
elif recno==8:
    plt.plot(rec8a,rec8b)
elif recno==9:
    plt.plot(rec9a,rec9b)
elif recno==10:
    plt.plot(rec10a,rec10b)
elif recno==11:
    plt.plot(rec11a,rec11b)
elif recno==12:
    plt.plot(rec12a,rec12b)
elif recno==13:
    plt.plot(rec13a,rec13b)
elif recno==14:
    plt.plot(rec14a,rec14b)
elif recno==15:
    plt.plot(rec15a,rec15b)
elif recno==16:
    plt.plot(rec16a,rec16b)
elif recno==17:
    plt.plot(rec17a,rec17b)
elif recno==18:
    plt.plot(rec18a,rec18b)
elif recno==19:
    plt.plot(rec19a,rec19b)
elif recno==20:
    plt.plot(rec20a,rec20b)