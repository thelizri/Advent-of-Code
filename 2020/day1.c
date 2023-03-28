#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    FILE* ptr;
    char str[50];
    ptr = fopen("day1.txt", "a+");
 
    if (NULL == ptr) {
        printf("file can't be opened \n");
    }
 
    printf("content of this file are \n");
 
    while (fgets(str, 50, ptr) != NULL) {
        printf("%s", str);
    }
 
    fclose(ptr);
    return 0;
}