import csv
def create():
    with open("input.csv","a")as obj:
        fobj=csv.writer(obj)
        fobj.writerow(['Product-Name', 'Product-CostPrice', 'Country'])
        while(True):
            ProductName=(input("Enter Product name  "))
            ProductCostPrice=int(input("Enter Product costPrice"))
            country=input("Enter Country name")
            record=[ProductName, ProductCostPrice, country]
            fobj.writerow(record)
            ch= int(input("1-Enter more Records \n 2- Exit  \n  Enter your choice:"))
            if ch==2:
                break;

def display():
    with open("input.csv","r") as obj:
        fobj=csv.reader(obj)
        for i in fobj:
            print (i)

create()
display()

            

