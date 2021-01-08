#include "rmt_library.h"
#include <stdio.h>

// int rmt_search(int result_array[], int size)
char *rmt_search(int var)
{   
   char *FAKE_RESULT1 = "1,3,5,7,9";
   char *FAKE_RESULT2 = "2,4,6,8,10";
   char *FAKE_RESULT3 = "none";

   if (var == 1)
      return FAKE_RESULT1;
   else if (var == 2)
      return FAKE_RESULT2;

   return FAKE_RESULT3;
}