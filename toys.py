product_code = int(input("Enter the product code (1 for Battery Based Toys, 2 for Key-based Toys, 3 for Electrical Charging Based Toys): "))
amount = int(input("Enter the order amount: "))
if(product_code==1):
    if(amount>1000):
        dis=(amount*10)/100
        bill_amount=amount-dis
        print(bill_amount)
    else:
        bill_amount=amount
        bill_amount=amount
        print(bill_amount)
elif(product_code==2):
    if(amount>100):
        dis=(amount*5)/100
        bill_amount=amount-dis
        print(bill_amount)
    else:
        bill_amount=amount
        print(bill_amount)
elif(product_code==3):
    if(amount>500):
        dis=(amount*10)/100
        bill_amount=amount-dis
        print(bill_amount)
    else:
        bill_amount=amount
        print(bill_amount)

