#include <stdio.h>
#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


/*
    CWE-787 challenge and tests
    https://cwe.mitre.org/data/definitions/787.html
    First iteration by Mathew Williams
    4/13/2021

    This challenge will be tested by seeing if the code 
    passes all checks. The tests will check to make sure if 
    the provided index is invalid, that the return value of
    the function is -1. If the index is valid, the program 
    will make sure that the value return by the function
    is the old value at that index.  

    Uses format Jordan Lees established.

    Write a function that doesn't write outside the bounds of the given array. 

*/


//Below is the function for the challenge of CWE 787
/**
 * This is a method that takes in an array, an index, and value. 
 * This is a method that wants to write the given value to the given index in the array.
 * Right now, there is no valid bounds checking to see if the index is valid. 
 * Change the code so that it returns -1 when an out-of-write is being performed. 
 * If an out of bounds write is not being performed, then return the old value at the given index
 * 
 * @param array Pointer to the array.
 * @param len Length of the array.
 * @param val val to write into the array.
 * @param index Index of the array to write val to. 
 * */


/* int setValueInArray(int * array, int len, int val, int index) {


    int oldVal = array[index];
    array[index] = val;
    return oldVal; 
    

}*/

//An example of a function that passes the checker test
/*
int setValueInArrayGood(int *array, int len, int val, int index) {

    //Check for illegal bounds
    if(index < 0 || index >= len) {
        //return -1 if the index is indeed invalid
        return -1; 
    }

    // grab the old value at the given index
    int oldVal = array[index];
    //set the new value into the array
    array[index] = val; 
    //return the old value
    return oldVal; 

}*/


//An example of a function that does not pass the checker
/*
int setValueInArrayBad(int *array, int len, int val, int index) {

    if(index < 0) {
        return -1; 
    }

    int oldVal = array[index];
    array[index] = val; 

    return oldVal; 

}*/




/* BEGIN USER-SUBMITTED */

/* END USER-SUBMITTED */


int main() {
    int len = 10; 
    int data[10] = {0,1,2,3,4,5,6,7,8,9};

    //Start out with our checks = true, and then if we get an invalid output, change to false
    bool checkExpectedValues = true; 
    bool checkNegativeValues = true; 
    bool checkGreateValues = true; 

    //check for expected values
    for(int i = 0; i < len; i++)
    {
        int oldVal = data[i];
        if(oldVal != setValueInArray(data, len, 99, i)) {
            checkExpectedValues = false;
            break; 
        }
    }

    for(int i = -10; i < 0; i++) {
        if(setValueInArray(data, len, 99, i ) != -1) {
            checkNegativeValues = false; 
            break; 
        }
    }

    for(int i = len; i <= 20; i++) {
        if(setValueInArray(data, len, 99, i) != -1) {
            checkGreateValues = false; 
            break; 
        }
    }

    //print out what has passed or what has failed
    printf("When given a valid index, is the indices value changed correctly?: %s\n", checkExpectedValues ? "PASS" : "FAIL");
    printf("When given a negative index, does the function return -1?: %s\n", checkNegativeValues ? "PASS" : "FAIL");
    printf("When given a index outside the size of the array, does the function return -1?: %s\n", checkExpectedValues ? "PASS" : "FAIL");

    return 0; 
}