boy=float(input("Lutfen boyunuzu giriniz: "))
kilo=int(input("Lutffen kilonuzu giriniz: "))
bmi=kilo/(boy*boy)

if(bmi<18.5):
    print("Zayifsiniz")
elif(18.5<=bmi<=25):
    print("Normalsiniz")
elif(25<=bmi<=30):
    print("Kilolusunuz")
elif(bmi>=30):
    print("Obezsiniz")