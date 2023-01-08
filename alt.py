from tabulate import tabulate
j1= 4
j2=-2
n = abs(j1+j2)
j3=0
j4=0
#j5=0
#j6=0
x=-10
count = 0
data = []

for j3 in range(x,-x):
    for j4 in range(x,-x):
        #for j5 in range(x, -x):
            #for j6 in range(x, -x):
                if abs(j3)+abs(j4)==n  and j1+j2+j3+j4==0:
                    temp_dat = []
                    temp_dat.append(j1)
                    temp_dat.append(j2)
                    temp_dat.append(j3)
                    temp_dat.append(j4)
                    #temp_dat.append(j5)
                    #temp_dat.append(j6)
                    data.append(temp_dat)
                    #print("j1= "+str(j1)+" j2= "+str(j2)+" j3= "+str(j3)+" j4= "+str(j4)+" j5= "+str(j5)+" j6= "+str(j6))
                    #count+=1

col_names = ["j1", "j2", "j3","j4"]
print(tabulate(data, headers=col_names, tablefmt="fancy_grid", showindex="always"))
