# import and alias the pandas library
import pandas as pd

# Series
fruits = pd.Series(['Apple', 'Banana', 'Cherry', 'Orange'], name = "Fruit")

print(fruits)


# dictionary of Series
qtys = pd.Series([5,7,2,9])
inventory = pd.DataFrame({ 'Fruit' : fruits, 'Qty' : qtys, 'Price': [2.99,1.99,3.99,2.99] })
print(inventory)

# column selection
fruit_col = inventory['Fruit']
print(fruit_col)

# as DataFrame
fruit_df = inventory[ ['Fruit'] ]
print(fruit_df)

#two columns in the list
new_ef = inventory[ ['Fruit','Price'] ]
print(new_ef)
# # Boolean index

filterd_ser = inventory['Qty'] > 5
print(filterd_ser)


# # applying a boolean index to a dataframe
fitered_df = inventory[ inventory['Qty'] > 5 ]
print(fitered_df)

#combining columns and filters
fruit_and_price_over5 = inventory[['Fruit','Price']][inventory['Qty'] >5 ] 
print(fruit_and_price_over5)


# # Confused? Too hot to handle??? Use variables!
large_qty = inventory[ inventory['Qty'] >5 ]
fruit_and_price_over5 = large_qty[ ['Fruit', 'Price' ] ]
print(fruit_and_price_over5)