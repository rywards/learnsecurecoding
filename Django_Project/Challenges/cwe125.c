#include <stdio.h>
#include <stdbool.h> 
#include <stddef.h>
#include <stdint.h>

/**
 * This is a method that gets the value from an array at a particular index.
 * There is no check that makes sure the index is a valid bounds.
 * Change the code so that it returns -1 when an out-of-bounds read is performed.
 * 
 * @param array Pointer to the array.
 * @param len Length of the array.
 * @param index Index of array to return.
 * */
/*
int getValueFromArray(int *array, int len, int index) {

	int value;
	
	// get the value at the specified index
	value = array[index];
	
	return value;
}

// An example of a function that passes the checker test
int getValueFromArrayGood(int *array, int len, int index) {
	
	int value;
	// check that the array index is less than the maximum

	// length of the array
	if (index < len && index >= 0) {
		// get the value at the specified index of the array
		value = array[index];
	}
	// if array index is invalid then output error message
	// and return value indicating error
	else {
		value = -1;
	}

	return value;
}
*/
/* BEGIN USER-SUBMITTED */

/* END USER-SUBMITTED */

// checker function
int main() {
	
	// Test data
   	int data[16] = {'T','h','i','s',' ','i','s',' ','m','y',' ','d','a','t','a','.'};
	
	//start out with our checks = true, and then if we get an invalid output, change to false
	bool checkExpectedValues = true;
	bool checkNegativeValues = true;
	bool checkGreaterValues = true;
	//bool checkInvalidLength = true;
	
	int i, val;
	// check regular (expected) values
	for(i = 0; i < 16; i++) {
		val = getValueFromArray(data, 16, i);
		if (val != data[i]) {
			checkExpectedValues = false;
		}
	}
	// check negative values
	for (i = -100; i < 0; i++) {
		val = getValueFromArray(data, 16, i);
		if (val != -1) {
			checkNegativeValues = false;
		}
	}
	// check values greater than max length
	for (i = 17; i < 100; i++) {
		val = getValueFromArray(data, 16, i);
		if (val != -1) {
			checkGreaterValues = false;
		}
	}
	
	//print out whether pass or fail
	printf("Did indices within the bounds of the array return the correct value?: %s\n", checkExpectedValues ? "PASS" : "FAIL");
	printf("Did the function return -1 when given a negative index?: %s\n", checkNegativeValues ? "PASS" : "FAIL");
	printf("Did the function return -1 when given a index outside the size of the array?: %s\n", checkGreaterValues ? "PASS" : "FAIL");
	
	return 0;
}