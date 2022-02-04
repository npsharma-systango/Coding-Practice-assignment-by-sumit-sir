import pandas as pd
import csv
import os
# Global variables

product = ""
sales = ""

ProductPath = os.path.join(".","input.csv")
salesPath = os.path.join(".","output.csv")

def uniqueName( heading):
    return len(heading) == len(set(heading))

def CalculateTax():
    # Checking Country Name
    
    if uniqueName(sales["Country"]):
        print("inside csv")
        with open("FinalResult.csv", "w", newline="") as fobj:
            thewritter = csv.writer(fobj)

            thewritter.writerow(["Product-Name", "Product-CostPrice", "Product-SalesTax", "Product-SalesTaxAmount", "Product-FinalPrice", "Country"])

            salesIndex = 0

            while salesIndex < len(sales):
                productIndex = 0
                while productIndex < len(product):
                    
                    try:
                        if( float(sales['SalseTaxInPercent'][salesIndex]) >= 0.0 and float(product['ProductCost'][productIndex])> 0.0):
                            taxprice = (float(sales['SalseTaxInPercent'][salesIndex])* float(product['ProductCost'][productIndex]))/100

                            salesprice = float(product['ProductCost'][productIndex])+taxprice
                
                            thewritter.writerow([product['ProductName'][productIndex], product['ProductCost'][productIndex], sales['SalseTaxInPercent'][salesIndex], taxprice, salesprice, sales['Country'][salesIndex]])
                            
                        else:
                            print("input file contain invalid values")
                  
                            
                    except ValueError:
                        print("input file contain characters instead of values")
                        break;
                    except:
                        print("invalid inputs")
                        break

                    finally:
                        productIndex+=1

                salesIndex+=1
    else:
        print("Country name is repeating")
            

        
#  file validations(  does file exist )
 
if os.path.exists(ProductPath) and os.path.exists(   salesPath):
    print("file exist")
    product = pd.read_csv("input.csv")
    sales= pd.read_csv("output.csv")
    CalculateTax();

        
    
