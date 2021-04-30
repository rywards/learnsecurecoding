#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdbool.h>

#define SEED_VALUE 32766
#define ARR_SIZE 5

/*
    CWE-680 
    https://cwe.mitre.org/data/definitions/680.html
    By Ryan Edwards

    This test will use parts of the CWE190 test/challenge that I created.
    The same topics apply; if an integer overflow occurs, we will allocate less
    memory than we intended to when using that overflowed value. Function will 
    return one integer value used as a seed to compare to the static seed
    value.

    Uses format Jordan Lees established.

    Write a function that mitigates the integer overflow 
    causing a buffer overflow.

*/

/* BEGIN USER-SUBMITTED */

/* END USER-SUBMITTED */

// Keep the short int values
// I'm trying to avoid actually allocating too much memory
// short int max 32767, min -32768

/*
int buffOverflow(int entryNum){
    entryNum = SEED_VALUE;
    return entryNum;
}
*/

/*int buffOverflow(){
    int *buffer;
    short int memToAllocate = 32766;
    memToAllocate += 5;
    buffer = (int*) malloc(memToAllocate);
    free(buffer);

    return memToAllocate;
}
*/


int main() {

    srand(SEED_VALUE);
    int seedArr[ARR_SIZE], compArr[ARR_SIZE];
    int checkSeed = buffOverflow();
    bool didPass;

    for (int i = 0; i < 5; i++){
        seedArr[i] = rand();
    }

    srand(checkSeed);

    for (int i = 0; i < ARR_SIZE; i++){
        compArr[i] = rand();
    }

    buffOverflow();
    for (int i = 0; i < ARR_SIZE; i++){
        if (seedArr[i] == compArr[i]) {
            //printf("Result set %d ------\nYour result: %d\nCorrect result: %d\n", i, compArr[i], seedArr[i]);
            didPass = true;
        }
        else {
            didPass = false;
            break;
        }
    }

    printf("Did you fix the memory allocation issue: %s\n",  didPass ? "PASS" : "FAIL");

    return 0;
    
}