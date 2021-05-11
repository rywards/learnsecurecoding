#include <stdio.h>
#include <stdbool.h> 
#include <time.h>
#include <stdlib.h>
#include <string.h>

/*
    Tutorial Challenge
    Simple "Hello, World" challenge for the user
    to familiarize themself with submitting code
    through the in-site IDE.
*/

/* BEGIN USER-SUBMITTED */

/* END USER-SUBMITTED */

/*
 // Method that is trying to allocate 3 int items.
    char *hello() {
        static char str[13] = // Make a 'Hello, World' string here.
        return str;
}


*/
// Checker
int main() {

    char *userValues = hello();
	
    // Check if returned array has the NULL pointer in the correct location
    bool hasHello;
    if(strcmp("Hello, World", userValues) == 0){
            hasHello = true;
    } else{
        hasHello = false;
    }
	
    printf("Did the function return the string 'Hello, World'?: %s\n", hasHello ? "PASS" : "FAIL");
	
	//free(userValues);
	
    return 0;
}