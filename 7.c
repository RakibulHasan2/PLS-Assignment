#include <stdio.h>
#include <stdlib.h>

int main() {
    int var = 10;
    int *ptr = &var;  // Pointer ptr holds the address of var

    // Dereferencing the pointer
    printf("Value of var: %d\n", *ptr);  // Output: 10

    // Changing the value using the pointer
    *ptr = 20;
    printf("Updated value of var: %d\n", var);  // Output: 20

    // Dynamic memory allocation
    int *dyn_ptr = (int *)malloc(sizeof(int));  // Allocate memory for an integer
    if (dyn_ptr != NULL) {
        *dyn_ptr = 30;
        printf("Dynamically allocated value: %d\n", *dyn_ptr);  // Output: 30

        // Freeing the dynamically allocated memory
        free(dyn_ptr);
    }

    return 0;
}
