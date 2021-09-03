melon_cost = 1.00

# customer1_name = "Joe"
# customer1_melons = 5
# customer1_paid = 5.00

# customer2_name = "Frank"
# customer2_melons = 6
# customer2_paid = 6.00

# customer3_name = "Sally"
# customer3_melons = 3
# customer3_paid = 3.00

# customer4_name = "Sean"
# customer4_melons = 9
# customer4_paid = 9.50

# customer5_name = "David"
# customer5_melons = 4
# customer5_paid = 4.00

# customer6_name = "Ashley"
# customer6_melons = 3
# customer6_paid = 2.00

# customer1_expected = customer1_melons * melon_cost
# if customer1_expected != customer1_paid:
#     print(f"{customer1_name} paid ${customer1_paid:.2f},",
#           f"expected ${customer1_expected:.2f}"
#           )

# customer2_expected = customer2_melons * melon_cost
# if customer2_expected != customer2_paid:
#     print(f"{customer2_name} paid ${customer2_paid:.2f},",
#           f"expected ${customer2_expected:.2f}"
#           )

# customer3_expected = customer3_melons * melon_cost
# if customer3_expected != customer3_paid:
#     print(f"{customer3_name} paid ${customer3_paid:.2f},",
#           f"expected ${customer3_expected:.2f}"
#           )

# customer4_expected = customer4_melons * melon_cost
# if customer4_expected != customer4_paid:
#     print(f"{customer4_name} paid ${customer4_paid:.2f},",
#           f"expected ${customer4_expected:.2f}"
#           )

# customer5_expected = customer5_melons * melon_cost
# if customer5_expected != customer5_paid:
#     print(f"{customer5_name} paid ${customer5_paid:.2f},",
#           f"expected ${customer5_expected:.2f}"
#           )

# customer6_expected = customer6_melons * melon_cost
# if customer6_expected != customer6_paid:
#     print(f"{customer6_name} paid ${customer6_paid:.2f},",
#           f"expected ${customer6_expected:.2f}")
          

def new_customers(customer_order_file, cost=1.00):
    """getting orders from file and turning it into list
        setting each element in individual list as a new variable
        if price paid is the same as the owed skip
        if customer underpaid or overpaid print"""

    new_orders = open(customer_order_file)
    for line in new_orders:
        line = line.rstrip()
        word = line.split('|')
    
        customer = word[1].split(" ")
        customer_first_name = customer[0]
        melons_purchased = word[2]
        price_of_melons= float(melons_purchased) * cost
        price_paid = float(word[3])

        if price_of_melons > price_paid:
            print(f"{customer_first_name} underpaid. They paid ${price_paid}, expected ${price_of_melons}")
        elif price_of_melons < price_paid:
            print(f"{customer_first_name} overpaid. They paid ${price_paid}, expected ${price_of_melons}")
        else:
            continue

        
new_customers("customer-orders.txt")

