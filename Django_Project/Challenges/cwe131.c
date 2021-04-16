#include <stdio.h>
#include <stdbool.h> 
#include <time.h>
#include <stdlib.h>
#define VALUE_1 721998
#define VALUE_2 531999
#define VALUE_3 5251994
#define VALUE_4 12345
#define NUM_ITEMS 23;

/*
    CWE-131 
    https://cwe.mitre.org/data/definitions/131.html
    Challenge based off of example 5 form link above.

    This challenge will be tested by seeing if the code 
    passes all checks. It will check whether certain 
    parameters can be passed through or not. Random inputs
    will be made to simulate a user.

    Uses format Jordan Lees established.

    Write a function that checks values input into the array.
*/

/* BEGIN USER-SUBMITTED */

/* END USER-SUBMITTED */

/*
 // Method that is trying to allocate 3 int items.
int *makeList() {
    int *list;
    list = (int*) malloc(4);

    list[0] = VALUE_1;
    list[1] = VALUE_2;
    list[2] = VALUE_3;
    list[3] = VALUE_4;

    return list;
}
 // Example of a correct answer for the above method
int *makeList() {
    int *list;
    list = (int*) malloc(5*sizeof(int));

    list[0] = VALUE_1;
    list[1] = VALUE_2;
    list[2] = VALUE_3;
    list[3] = VALUE_4;

    return list;
}
*/

/*
int *makeList() {
	int *list;
    list = (int*) malloc(4*sizeof(int));

    list[0] = VALUE_1;
    list[1] = VALUE_2;
    list[2] = VALUE_3;
    list[3] = VALUE_4;
	

    return list;
}

*/
// Checker
int main() {
	
	int i;
	
    int *userValues = makeList();
    int neededValues[4] = {VALUE_1, VALUE_2, VALUE_3, VALUE_4};
	
    // Check if returned array has the NULL pointer in the correct location
    bool hasExpectedNULL = true;
    if(userValues[4] != NULL) {
        hasExpectedNULL = false;
    }

    // Check values that are in user's returned array
    bool hasExpectedValues = true;
    i = 0;
	while(i < 4){
        printf("%d\n", userValues[i]);
		if (userValues[i] != neededValues[i]) {
			hasExpectedValues = false;
		}
        
        i++;
	}
	
    printf("Has expected NULL pointer index: %s\n", hasExpectedNULL ? "PASS" : "FAIL");
    printf("Has expected values: %s\n", hasExpectedValues ? "PASS" : "FAIL");
	
	//free(userValues);
	
    return 0;
}