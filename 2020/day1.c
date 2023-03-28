#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void part1(int numbers[], int length){
   for (int i = 0; i < length-1; i++) {
      for (int j = i+1; j<length; j++){
         if(numbers[j]+numbers[i]==2020){
            int result = numbers[j]*numbers[i];
            printf("Part 1: %d\n", result);
         }
      }
   }
}

void part2(int numbers[], int length){
   for (int i = 0; i < length-2; i++) {
      for (int j = i+1; j<length-1; j++){
         for(int k=j+1; k<length; k++){
            if(numbers[j]+numbers[i]+numbers[k]==2020){
               int result = numbers[j]*numbers[i]*numbers[k];
               printf("Part 2: %d\n", result);
            }
         }
      }
   }
}

int* read(int *length){
   FILE* ptr;
   char str[50];
   ptr = fopen("day1.txt", "r");

   if (NULL == ptr) {
      printf("file can't be opened \n");
   }

   int static num[500];
   int index = 0;

   while (fgets(str, 50, ptr) != NULL) {
      num[index] = atoi(str);
      index++;
   }

   fclose(ptr);
   *length = index;
   return num;
}

int main()
{
   int length = 0;
   int *num = read(&length);
   part1(num, length);
   part2(num, length);

   return 0;
}
