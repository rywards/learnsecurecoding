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

/* BEGIN USER-SUBMITTED */

/* END USER-SUBMITTED */

/********************WORKING FUNCTION********************/

bool checkInputCOMPARE(int *inputToCheck, int index) {
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


int main() {

    
    int i, inputparams[ARR_SIZE], randInput;
    bool didPass, passBounds[ARR_SIZE], matchResult[ARR_SIZE];
    srand(time(NULL));

    for (int i = 0; i < ARR_SIZE; i++) {
        
        randInput = (rand() % HIGH_RANGE - MAX_VAL);
        printf("Input param %d: %d\n", (i+1), inputparams[i] = randInput);

        matchResult[i] = checkInputCOMPARE(inputparams, i);
        passBounds[i] = checkInput(inputparams, i);
        printf("Correct Result: %d\n", matchResult[i]);
        printf("User Result: %d\n", passBounds[i]);
        
    }

    for (int i = 0; i < ARR_SIZE; i++) {
        if (passBounds[i] == matchResult[i]) {
            didPass = true;
        }
        else {
            didPass = false;
            break;
        }
    }
    printf("Was every element's value checked to make sure it is within the bounds of MIN_VAL and MAX_VAL?: %s\n",  didPass ? "PASS" : "FAIL");
    return 0;
    
}