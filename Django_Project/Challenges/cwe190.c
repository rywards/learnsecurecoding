#include <stdio.h>
#include <stdbool.h> 
#include <time.h>
#include <stdlib.h>

/*
    CWE-190 
    https://cwe.mitre.org/data/definitions/190.html
    Built off Example 4 on CWE-190 page
    First Iteration by Ryan Edwards

    This test will use the short int limits
    established in C. The goal of the user will be to fix
    the code so that there isn't overflow of the input values.
    Input values will be a fixed number for simplicity's sake.

    Uses format Jordan Lees established.

    Write a function that does not overflow on the given inputs
    without changing the input parameter type.

*/

/* BEGIN USER-SUBMITTED */

/* END USER-SUBMITTED */

// Working function
int checkOverflowCOMPARE(short int *overflowItemsCheck) {
    short int i = 0;
    int total = 0;

    while (i < (sizeof(overflowItemsCheck)-1)) {
        total = total + overflowItemsCheck[i];
        i++;
    }
    return total;
    
}


/*int checkOverflowBAD(short int *overflowItemsCheck) {
    short int i = 0;
    short int total = 0;
    
    while (i < (sizeof(overflowItemsCheck)-1)) {
        printf("Item %d: %d\n", i, overflowItemsCheck[i]);
        total = total + overflowItemsCheck[i];
        i++;
    }
    printf("Total in function: %d\n", total);
    return total;
    
} */


/*
    REF: short int min is -32768, short int max is 32767
    The user will just have to fix the original code to solve
    the overflow issue. It isn't complicated at all. Just something
    to keep in mind when programming so you know the limits or when
    to extend them.

*/
int main() {

    short int overflowItems[3] = {17986, 745, 32000};
    int COMPARE = 0, INPUTTED = 0; 
    bool didPass;

    COMPARE = checkOverflowCOMPARE(overflowItems);
    INPUTTED = checkOverflow(overflowItems);
    printf("Your result: %d\n", INPUTTED);

    if (COMPARE == INPUTTED) {
        didPass = true;
    }

    printf("Was the Integer Overflow that was present in the code fixed?: %s\n",  didPass ? "PASS" : "FAIL");
   
    return 0;
}
