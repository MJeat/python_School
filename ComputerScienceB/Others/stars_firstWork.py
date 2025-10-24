

while True:
    # Define the main function for execution
    def main():
        # Infinite loop to continuously prompt user for input. Had to use another loop to create a continuous prompt if the symbol is among [*, -, +]
        while True:
            symbols = input("Enter *, -, + of symbols and click e to exit: ")

            if symbols in ['*', '-', '+']:
                printing_symbols(symbols)

            if symbols == 'e':
                print("Exiting program.")
                exit(0) # Exit the program if user inputs 'e'
                
    # This function prints the symbols in decreasing order from 5 to 1
    def printing_symbols(amount):
        for i in range(5,0,-1):
            print(amount*i)

    # Call the main function to start the program
    main()






