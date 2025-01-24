/*Extemporaneous exam: Create a system based on C, to indicate accounts, and applies discounts.
Chong Santiago Hungman Emmanuel
13/08/2024*/

#include <stdio.h>

// Function declarations
void applyDiscount(char product, double discount, double *price);
double getDiscount(char product);
void displayPrices(double prices[], int size);
void inputPrices(double prices[], char products[], int size);

// Main function
int main() {
    int numAccounts; // Number of accounts
    int i;

    // Prompt user for the number of accounts
    printf("Enter the number of accounts: ");
    scanf("%d", &numAccounts);

    char products[numAccounts];                // Product categories
    double discounts[numAccounts];             // Store discount rates for each product
    double prices[numAccounts];                // Store original prices for each account
    double finalPrices[numAccounts];           // Store final prices after discount

    // Input product types and prices from the user
    inputPrices(prices, products, numAccounts);

    // Apply discounts using a for loop
    for (i = 0; i < numAccounts; i++) {
        discounts[i] = getDiscount(products[i]);
        finalPrices[i] = prices[i];
        applyDiscount(products[i], discounts[i], &finalPrices[i]);
    }

    // Display the final prices using a do-while loop
    i = 0;
    do {
        printf("Product %c: Original Price: $%.2f, Discounted Price: $%.2f\n", 
               products[i], prices[i], finalPrices[i]);
        i++;
    } while (i < numAccounts);

    return 0;
}

// Function to apply discount
void applyDiscount(char product, double discount, double *price) {
    *price = *price - (*price * discount / 100);  // Apply discount
}

// Function to get discount based on product using switch-case
double getDiscount(char product) {
    double discount;

    switch (product) {
        case 'A':
            discount = 10.0; // 10% discount for product A
            break;
        case 'B':
            discount = 15.0; // 15% discount for product B
            break;
        case 'C':
            discount = 20.0; // 20% discount for product C
            break;
        case 'D':
            discount = 5.0;  // 5% discount for product D
            break;
        case 'E':
            discount = 0.0;  // No discount for product E
            break;
        default:
            discount = 0.0;  // Default case: no discount
            break;
    }
    
    return discount;
}

// Function to input prices and products
void inputPrices(double prices[], char products[], int size) {
    int i;
    for (i = 0; i < size; i++) {
        printf("Enter the product type for account %d (A/B/C/D/E): ", i + 1);
        scanf(" %c", &products[i]);  // Input product type

        printf("Enter the price for product %c: ", products[i]);
        scanf("%lf", &prices[i]);    // Input price for the product
    }
}