#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <time.h>
#include <unistd.h>
#define PASS_SIZE 16

int main(void) {
    int i, prompt_response;
    /* password for admin to provide to dump flag */
    char *password;
    /* true if user is admin */
    uint8_t admin;
    int x = 0;
    /* seed random with time so that we can password */
/*    while (x < 5) { */
    	srand(time(0));
    	admin = 0;
    	password = calloc(1, PASS_SIZE+1);
    	for (i = 0; i < PASS_SIZE; i++) {
        	password[i] = rand() % ('z'-' ') + ' ';
    	}
        password[PASS_SIZE] = 0; 
    	printf("Password: %s\n", password);
    	/*password[PASS_SIZE] = 0;*/

    	/*free(password);
    	fflush(stdout); */
	x = x + 1; 
    /*    sleep(1);
    }*/
}

