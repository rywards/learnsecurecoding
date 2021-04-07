#include <stdio.h>
#include <stdbool.h> 
#include <time.h>
#include <stdlib.h>
#define MAX_VAL 1000
#define MIN_VAL 0
#define ARR_SIZE 10
#define HIGH_RANGE 2500

/*
    CWE-20 
    https://cwe.mitre.org/data/definitions/20.html
    Built off of Example 2 from this page
    First iteration by Ryan Edwards

    This challenge will be tested by seeing if the code 
    passes all checks. It will check whether certain 
    parameters can be passed through or not. Random inputs
    will be made to simulate a user.

    Uses format Jordan Lees established.

    Write a function that checks values input into the array.
*/

/********************WORKING FUNCTION********************/
/*
bool checkInput(int *inputToCheck, int index) {
    // Checks array input
    // if function returns false in any case
    // should be fixed to completely stop on invalid input, or go back around.
    bool isChecked;

    if ((inputToCheck[index] <= MAX_VAL) & (inputToCheck[index] >= MIN_VAL)) {
        isChecked = true;
    }
    else {
        isChecked = false;
    }

    return isChecked;
}

bool checkInputBAD(int *inputToCheck, int index) {
    // Checks array input
    // if function returns false in any case
    // should be fixed to completely stop on invalid input, or go back around.
    bool isChecked;

    if ((inputToCheck[index] <= MAX_VAL)) {
        isChecked = true;
    }
    else {
        isChecked = false;
    }

    return isChecked;
}

*/

/* BEGIN USER-SUBMITTED */

/* END USER-SUBMITTED */

int main() {

    
    int i, inputparams[ARR_SIZE], randInput;
    bool passBounds;
    srand(time(NULL));

    for (int i = 0; i < ARR_SIZE; i++) {
        
        randInput = (rand() % HIGH_RANGE - MAX_VAL);
        printf("Input param %d: %d\n", (i+1), inputparams[i] = randInput);
        passBounds = checkInput(inputparams, i);
        printf("Result %d: %s\n", i+1, passBounds ? "PASS" : "FAIL");

    }

    return 0;
    
}