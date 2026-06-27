import FoodClass as fc

# this dictionary represents transactions. The key of the dictionary is the transaction identifier.
# The Value of the dictionary is a list. The elements in each list are -
# ['Date', 'Name of item', 'Cost', 'customerid' ]

def main():

    # Created a dictionary to represent a customer database at the supermarket.
    customer_dict = {
        570: ['Danni Sellyar', '97 Mitchell Way Hewitt Texas 76712', 'dsellyarft@gmpg.org', '254-555-9362', False],
        569: ['Aubree Himsworth', '1172 Moulton Hill Waco Texas 76710', 'ahimsworthfs@list-manage.com', '254-555-2273', True]
    }

    # Renamed dictionary so it doesn't cause error with the dict funtions in python
    trans_dict = {'trans1':['2/15/2023','The Lone Patty',17,569],
                    'trans2':['2/15/2023','The Octobreakfast',18,569],
                    'trans3':['2/15/2023','The Octoveg',16,570],
                    'trans4':['2/15/2023','The Octoburger',20,570]}

    # Created a loop to search customer by customerid to display transactions.
    again = 'y'

    while again.lower() == 'y':
        print("Please enter the customer information to display transactions:")
        search_customerid = int(input("Customer ID: "))

        # Search for the customerid that was entered to see if it is in
        # the customer_dict dictionary.
        if search_customerid in customer_dict:
            
            # Pull the requested data based on the customerid
            cust_data = customer_dict[search_customerid]
        

            # This will generate the output from the provided screenshot.
            customer = fc.CustomerClass(search_customerid, cust_data[0], cust_data[1], cust_data[2], cust_data[3], cust_data[4])

            print(f"Customer Name: {customer.get_name()}")
            print(f"Phone: {customer.get_phone()}")
    
            order_total = 0

            for trans in trans_dict.values():
                if trans[3] == customer.get_customerid():
                    order = fc.TransactionType(trans[0], trans[1], trans[2], trans[3])
                    
                    # Print the item and add to the total
                    print(f"Order Item: {order.get_item_name()} \tPrice: ${order.get_cost():.2f}")
                    order_total += order.get_cost()

            print(f"Total Cost: \t\t\t\t${order_total:.2f}")

            # Calculate the 20% discount for members only
            if customer.get_member_status() == True:
                discount = order_total * 0.20
                print(f"Member Discount:\t\t\t-${discount:.2f}")
                order_total -= discount 
                print(f"Total cost after discount:\t\t${order_total:.2f}")
            
        else:
            # Added a quick error message if they type a wrong ID
            print("Customer ID not found in the system.")
        
        # Repeat the search for the next customer
        again = input("\nSearch for another customer transaction? (y/n): ")

        
# Call the main function
if __name__ == '__main__':
    main()