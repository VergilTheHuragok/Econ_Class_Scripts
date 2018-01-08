initial = int(input())
rr = float(input())

bank = 1
banks = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lend = initial
totlend = 0

banksym = -1
save = -1
while lend >= .01:
    save = lend*rr
    lend = lend - save
    totlend += lend
    if bank > len(banks) - 1:
        banksym = banks[(bank-1)%26].lower()
    else:
        banksym = banks[bank -1]
    #print("Bank " + str(bank) + ":" + banksym + " saved: " + str(round(save, 2)) + " loaned: " + str(round(lend, 2)))
    bank += 1
print("Bank " + str(bank) + ":" + banksym + " saved: " + str(round(save, 2)) + " loaned: " + str(round(lend, 2)))
print(str(totlend) + " Lent")
print(str((initial * (1/rr)) - initial) + " Created")