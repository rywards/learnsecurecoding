#include <stdio.h>
#include <stdbool.h> 
#include <stddef.h>
#include <stdint.h>

int getValueFromArray(int *array, int len, int index) {

	int value;
	
	// get the value at the specified index
	value = array[index];
	
	return value;
}


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

int main() {
	
	
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
	
	printf("Regular (Expected) Values: %s\n", checkExpectedValues ? "PASS" : "FAIL");
	printf("Negative Values: %s\n", checkNegativeValues ? "PASS" : "FAIL");
	printf("Greater Values: %s\n", checkGreaterValues ? "PASS" : "FAIL");
	
	return 0;
}