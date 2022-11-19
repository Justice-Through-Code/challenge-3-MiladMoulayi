
def stock_purchases():

    stocks = {
        'Amazon': 3000,
        'Apple': 100,
        'Facebook': 250,
        'Google': 1400,
        'Microsoft': 200
    }

    # Given the prices above and a client's investment budget, how much stock can they buy?
    # 1.1 TODO: Ask the client's name (use the string: "What is your name? ") and save it into a variable
    client_name = input("What is your name? ")

    # 1.2 TODO: Ask the client how many dollars they would like to invest (use the string: "How much would you like to invest? $")
    # and save it into a variable
    # NOTE: When you use the `input` function to get user input, what do numbers get saved as?
    investment = int(input("How much would you like to invest? $"))

    # 1.3 TODO: Uncomment the line below to ask the client which stock they're interested in.
    # NOTE: Take a look at how this input string prints out
    stock_name = input(
        "\nWhich stock are you interested in? Enter the full name:\nAmazon\nApple\nFacebook\nGoogle\nMicrosoft\nStock Name: ")

    # Now that you have all of the client info, you can check how much they can purchase of the stock
    # they're interested in.

    # 1.4 TODO: Use `if/elif/else` conditional logic to determine how much stock the client can buy,
    # and save it in a variable

    # if (stock_name == "Amazon"):
    #   price = amazon
    # elif (stock_name == "Apple"):
    #   price = apple
    # elif (stock_name == "Facebook"):
    #   price = fb
    # elif (stock_name == "Google"):
    #   price = investment / google
    # elif (stock_name == "Microsoft"):
    #   price = msft

    price = stocks[stock_name]

    max_stock = int(investment / price)

    # 1.5 TODO: Once you've calculated the number of stocks that can be purchased,
    # Use an f-string to print the result for the client, ala:
    # Alex has $5000 to invest and can buy 50 shares of Apple at the current price of $100.
    print(f'{client_name} has ${investment} to invest and can buy {max_stock} shares of {stock_name} at the current price of ${price}.')


stock_purchases()
