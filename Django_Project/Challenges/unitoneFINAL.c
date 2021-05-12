#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <stdint.h>

#define ARR_SIZE 5
#define MIN_VAL 0
#define MAX_VAL 32766
#define SEED_VAL 32766

/*
    Unit One Final Challenge
    First Iteration by Ryan Edwards

    This challenge will encompass a range of the
    CWE's encountered throughout the unit. The challenge will
    be to solve all of them. This final will be based off of the
    CWE challenges that I (Ryan) worked on: CWE-20, CWE-190, and CWE-680.

    Uses format Jordan Lees established.

    The user must write a function that satisfies all the requirements.

*/

/* BEGIN USER-SUBMITTED */

/* END USER-SUBMITTED */

int finalChallengeCOMPARE(int *numArr) {

    // MIN_VAL and MAX_VAL are 0,32766 respectively 
    // fix the overflow without removing the equation
    // function MUST return value
    int *buffer;
    int memToAllocate = 0;
    
    // loop through 
    for (int i = 0; i < sizeof(numArr)+1; i++) {

        // should not add when number is too big
        if ((numArr[i] > MAX_VAL) || (numArr[i] < MIN_VAL)) {
            memToAllocate += 0;
        }
        else {
            memToAllocate += numArr[i];
        }
    } 

    buffer = (int*) malloc(memToAllocate);
    free(buffer);
    return memToAllocate;
    
}

/*
int finalChallenge(int *numArr) {

    
       // Ensure the code does not overflow
      //  and allocate the wrong amount of memory.
       // MIN_VAL is 0; MAX_VAL is 32766.
    

    int *buffer;
    short int memToAllocate = 0;

    for (int i = 0; i < sizeof(numArr)+1; i++) {

        memToAllocate += numArr[i]; 
    } 

    buffer = (int*) malloc(memToAllocate);
    free(buffer);
    return memToAllocate;

} 
*/




// Seed value used to simulate input
// user seed will be used and nums 
// need to be the same to pass
// MAX and SEED values are named
// differently for clarity's sake

// Note: short int overflows past 32767

int main() {

    // user should end up allocating 7953 in their function
    bool didPass = true;
    int inputCheck, compareCheck;
    int seedArr[ARR_SIZE] = {9, 45, 50000, 123456, 7899};

    inputCheck = finalChallenge(seedArr);
    compareCheck = finalChallengeCOMPARE(seedArr);

    if (inputCheck != compareCheck) {
        didPass = false;
    }

    printf("Did you check if there was an integer overflow or whether the input value was within the correct range?: %s\n", didPass ? "PASS" : "FAIL");

}