from numpy import product
import pandas as pd
import csv

product = pd.read_csv("input.csv")
stax = pd.read_csv("output.csv")

with open("FinalResult.csv", "w", newline="") as f:
    thewritter = csv.writer(f)

    thewritter.writerow(["ProductName", "Product-CostPrice", "Product-SalesTax", "Product-SalesTaxAmount", "Product-FinalPrice", "Country"])

    i = 0
    print(type(float(stax['Product-SalesTax'][i])))


    while i < len(stax):
        j = 0
        while j < len(product):
            taxprice = (float(stax['Product-SalesTax'][i])* float(product['Product-CostPrice'][j]))/100
            salesprice = float(product['Product-CostPrice'][j])+taxprice
            #print(f"{stax['Country'][i]}         {stax['SalseTaxInPercent'][i]}%           {product['ProductName'][j]}           {product['ProductCost'][j]} {salesprice} cost AT")
            thewritter.writerow([product['ProductName'][j], product['Product-CostPrice'][j], stax['Product-SalesTax'][i], taxprice, salesprice, product['Country'][i]])
            j+=1
        i+=1
