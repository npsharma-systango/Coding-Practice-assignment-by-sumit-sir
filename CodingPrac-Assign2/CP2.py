import csv
import pandas as pd

product = pd.read_csv("input.csv")
sales = pd.read_csv("output.csv")

with open("FinalResult.csv", "w", newline="") as csvObj:
    thewritter = csv.writer(csvObj)

    thewritter.writerow(["Product-Name", "Product-CostPrice", "Product-SalesTax", "Product-SalesTaxAmount", "Product-FinalPrice", "Country"])

    salesIndex = 0

    while salesIndex< len(sales):
        productIndex = 0
        while  productIndex  < len(product):
            #print( type(salesTaxDf['SalseTaxInPercent'][salseTaxDfIndex]), " ", type(productCatalogDf['ProductCost'][productCatalogDfIndex]) )
            try:
                if( float(sales['SalseTaxInPercent'][salesIndex]) >= 0.0 and float(product['ProductCost'][ productIndex ])> 0.0):
                    taxprice = (float(sales['SalseTaxInPercent'][salesIndex])* float(product['ProductCost'][ productIndex ]))/100

                    salesprice = float(product['ProductCost'][ productIndex ])+taxprice
        
                    thewritter.writerow([product['ProductName'][ productIndex ], product['ProductCost'][ productIndex ], sales['SalseTaxInPercent'][salesIndex], taxprice, salesprice, sales['Country'][salesIndex]])
                    productIndex +=1
                else:
                    print("input file contain invalid values")
                    break;
            except ValueError:
                print("input file contain characters instead of values")
                break;
            except:
                print("invalid inputs")

        salesIndex+=1