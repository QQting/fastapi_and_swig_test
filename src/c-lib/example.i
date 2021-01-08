%module rmt_py_wrapper
%{
/* Includes the header in the wrapper code */
#include "./include/rmt_library.h"
%}
 
/* Parse the header file to generate wrappers */
%include "./include/rmt_library.h"
