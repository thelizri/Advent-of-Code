#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    FILE* ptr;
    char str[50];
    ptr = fopen("day1.txt", "r");
 
    if (NULL == ptr) {
        printf("file can't be opened \n");
    }

    int sum = 0;
 
    printf("content of this file are \n");
 
    while (fgets(str, 50, ptr) != NULL) {
        int x = atoi(str);
        printf("Converting %s: %d\n", str, x);
        sum += x;
    }

    printf("Sum is: %d\n", sum);
 
    fclose(ptr);
    return 0;
}