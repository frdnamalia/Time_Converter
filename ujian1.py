print("="*50)
print("=========Soal 1 - Time Converter=========== \n")
print("by Fardhina Amalia\n\n")



def converter():
    
    try:
        print("======INPUT======")
        x=(input("Masukkan detik:"))
        x=int(x) 
        if (x>=0 and x<359999):
            HH=0
            MM=0
            SS=0
            Jam=3600
            Menit=60
            HH+=(x//Jam) 
            x=x%Jam 
            MM+=(x//Menit) 
            x=x%Menit 
            SS+=x
            if(HH<10):
                HH="0"+str(HH)
            else:
                HH=HH
            if(MM<10):
                MM="0"+str(MM)
            else:
                MM=MM                
            if(SS<10):
                SS="0"+str(SS)
            else:
                SS=SS
            return HH,MM,SS
        elif x< 0:
            return "tidak menerima nilai negatif"
        else:
            return "Maaf angka diluar jangkauan"
    except:
        return "Input Invalid"

con=converter()
if type(con)==str:
    print("======INPUT======")
    print(con)
else:
    HH,MM,SS=con
    print("======INPUT======")
    print("konversi:",HH,":",MM,":",SS)
