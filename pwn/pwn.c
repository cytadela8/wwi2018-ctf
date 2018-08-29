#include <stdio.h>
#include <stdlib.h>

typedef struct {
   char tab[100];
   char casual;
} state;

state s;

int main(void) {
   int ans;

   printf("How many times to loop:\n");
   fflush(stdout);
   scanf("%d", &ans);
   if (0 > ans || ans > 100) {
      printf("Invalid number\n");
      fflush(stdout);
      return 0;
   }

   s.casual = 1;

   for (int i = 1; i <= ans; i++) {
      int res = getchar();
      if (res < 0) {
          printf("Something went wrong.\n");
          fflush(stdout);
          return 0;
      }
      s.tab[i] = res;
   }

   if (s.casual == 2) {
      printf("YOU SHALL NOT CALL ME!\n");
      fflush(stdout);
      system("/bin/sh");
      return 0;
   }

   printf("No shell for you\n");
   fflush(stdout);
   return 0;
}
