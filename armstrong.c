#include <stdio.h>
#include <conio.h>
  
int main ()
{
int num, var, rem, sum = 0, a = 0 ;
  
printf ( “ Please enter an integer: “ );  // Taking the user input
scanf ( “%d”, &num );
  
var = num;
  
while (var != 0)    // Finding the numbers of digits in a given number
{
var = var / 10;
++a;
}
  
var = num;
  
while (var > 0 )     // Calculate the number to check  it is Armstrong or not
{
rem = var % 10;
sum = sum +  pow( rem, a );
var = var / 10;
}
  
if ( sum == num )   // Check whether the sum is equal to the given number of not
{
printf ( “ %d is an Armstrong number \n ”, num );
}
else
{
printf ( “ %d is not an Armstrong number \n ”, num );
}
return 0;
}