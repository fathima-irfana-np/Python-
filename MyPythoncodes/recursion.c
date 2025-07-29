#include <stdio.h> 
int sum=0;
int recur(int);

int main(){
    int digit=0  ,n=0 ;
    printf("enter a number ");
    scanf("%d",&digit);
    n=recur(digit);
    printf("%d", n);   
    
    }
int recur(int num){
   
        if( num<=0  ){
          return sum;
          }

          return (num%10)+recur(num/10 )  ;
             }
