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

   int num[500];
   int index = 0;

   while (fgets(str, 50, ptr) != NULL) {
      num[index] = atoi(str);
      index++;
   }

   fclose(ptr);

   for (int i = 0; i < index-1; i++) {
      for (int j = i+1; j<index; j++){
         if(num[j]+num[i]==2020){
            int result = num[j]*num[i];
            printf("Part 1: %d\n", result);
         }
      }
   }

   for (int i = 0; i < index-2; i++) {
      for (int j = i+1; j<index-1; j++){
         for(int k=j+1; k<index; k++){
            if(num[j]+num[i]+num[k]==2020){
               int result = num[j]*num[i]*num[k];
               printf("Part 2: %d\n", result);
            }
         }
      }
   }

   /*Find the two entries that sum to 2020; what do you get if you multiply them together?*/

   return 0;
}