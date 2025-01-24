# Exercise 8: Calculate the area of a plot of land after n generations
def calculate_land_area():
    initial_area = float(input("Enter the initial area of the plot of land: "))
    generations = int(input("Enter the number of generations (up to 50): "))
    heirs_per_generation = int(input("Enter the number of heirs per generation: "))

    if generations > 50:
        print("The number of generations should not exceed 50.")
        return
    
    final_area = initial_area / (heirs_per_generation ** generations)
    print(f"The area for each heir after {generations} generations is: {final_area:.2f} square units")


# Exercise 9: Drivers and their kilometers for each day of the week
def calculate_total_kms():
    num_drivers = int(input("Enter the number of drivers: "))
    names = []
    kms = []
    
    for i in range(num_drivers):
        name = input(f"Enter the name of driver {i + 1}: ")
        names.append(name)
        weekly_kms = []
        for j in range(7):
            daily_kms = float(input(f"Enter the kilometers driven by {name} on day {j + 1}: "))
            weekly_kms.append(daily_kms)
        kms.append(weekly_kms)
    
    total_kms = [sum(driver_kms) for driver_kms in kms]
    
    print("\nDriver and their total kilometers:")
    for i in range(num_drivers):
        print(f"{names[i]}: {total_kms[i]} km")


# Exercise 10: Calculate quantities and revenue for items sold in branches
def calculate_revenue():
    prices = [float(input(f"Enter the price of item {i + 1}: ")) for i in range(5)]
    quantities = [[int(input(f"Enter the quantity sold of item {i + 1} in branch {j + 1}: ")) for j in range(4)] for i in range(5)]

    total_item_quantities = [sum(quantities[i]) for i in range(5)]
    branch_2_items = sum(quantities[i][1] for i in range(5))
    branch_1_item_3 = quantities[2][0]
    total_revenue_per_branch = [sum(prices[i] * quantities[i][j] for i in range(5)) for j in range(4)]
    total_revenue = sum(total_revenue_per_branch)
    highest_revenue_branch = total_revenue_per_branch.index(max(total_revenue_per_branch)) + 1

    print("\nTotal quantities of each item:")
    for i in range(5):
        print(f"Item {i + 1}: {total_item_quantities[i]} units")

    print(f"\nTotal number of items sold in branch 2: {branch_2_items} units")
    print(f"Amount of item 3 sold in branch 1: {branch_1_item_3} units")
    print("\nTotal revenue of each branch:")
    for i in range(4):
        print(f"Branch {i + 1}: ${total_revenue_per_branch[i]:.2f}")

    print(f"\nTotal revenue of the company: ${total_revenue:.2f}")
    print(f"The highest-grossing branch is Branch {highest_revenue_branch}")


# Exercise 11: Football pool results management
def football_pool_results():
    teams = [[input(f"Enter the name of team {j + 1} for match {i + 1}: ") for j in range(2)] for i in range(15)]
    results = [[int(input(f"Enter the goals of {teams[i][j]} for match {i + 1}: ")) for j in range(2)] for i in range(15)]

    print("\nResults of the football pool:")
    for i in range(15):
        print(f"{teams[i][0]} {results[i][0]} - {results[i][1]} {teams[i][1]}")


# Exercise 12: Sales company management
def sales_management():
    items = 10
    sellers = 50
    sales = [[int(input(f"Enter the quantity sold of item {j + 1} by seller {i + 1}: ")) for j in range(items)] for i in range(sellers)]
    prices = [float(input(f"Enter the price of item {i + 1}: ")) for i in range(items)]

    # Calculate the money collected by each seller
    money_collected = [sum(sales[i][j] * prices[j] for j in range(items)) for i in range(sellers)]
    highest_seller = money_collected.index(max(money_collected)) + 1
    best_selling_item = max(range(items), key=lambda j: sum(sales[i][j] for i in range(sellers))) + 1
    sellers_with_no_item_8 = sum(1 for i in range(sellers) if sales[i][7] == 0)

    print("\nAmount of money collected by each seller:")
    for i in range(sellers):
        print(f"Seller {i + 1}: ${money_collected[i]:.2f}")

    print(f"\nThe seller who collected the most money is seller {highest_seller}")
    print(f"The best-selling item is item {best_selling_item}")
    print(f"The number of sellers who did not sell any item 8: {sellers_with_no_item_8}")


# Menu to run each function
def main():
    while True:
        print("\nChoose an exercise to run:")
        print("1. Calculate land area after generations")
        print("2. Calculate total kilometers per driver")
        print("3. Calculate quantities and revenue for items sold")
        print("4. Football pool results management")
        print("5. Sales company management")
        print("0. Exit")

        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            calculate_land_area()
        elif choice == 2:
            calculate_total_kms()
        elif choice == 3:
            calculate_revenue()
        elif choice == 4:
            football_pool_results()
        elif choice == 5:
            sales_management()
        elif choice == 0:
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()