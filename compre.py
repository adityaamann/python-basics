#List 
#[expression for item in iterable if condition]

menu = [
    "Masala Tea",
    "Green Tea",
    "Iced Tea",
    "Ginger Tea"
    ]

iced_tea = [tea for tea in menu if "Iced" in tea]
print(iced_tea)

nums = [1,2,3,4,5]
squares = [x*x for x in nums]
print(squares)

even_squares = [x*x for x in nums if x%2 == 0 ]
print(even_squares)


#Set
#{expression for item in iterable if condition}

nums2 = [1,2,2,3,4,4,3,1]
unique_squares = {x*x for x in nums2}
print(unique_squares)


#Dict
#{key_expression: value_expression for item in iterable if condition}

tea_prices_inr = {
    "Masala Chai" : 40,
    "Elaichi Chai" : 70,
    "Mumbaikar Chai" : 30,
    "Indori Chai" : 60
}

tea_price_usd = {tea:price /80 for tea, price in tea_prices_inr.items()}
print(tea_price_usd)


#Generators
#(expression for item in iterable if condition)

daily_sales = [5,10,12,30,20]

total_sales = sum(sales for sales in daily_sales if sales > 5)
print(total_sales)