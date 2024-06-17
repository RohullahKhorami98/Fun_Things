#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>



int main() {
    int n ;
    scanf("%d", &n);
    int next_loop = (n*2)-1;
    for (int i = 0; i < next_loop; i++)
    {
        for (int j = 0; j <next_loop; j++)
        {   
            int min = 0;
            if (i<j)
            {
                min = i;
            }else
            {
                min = j;
            }
            if(min<next_loop-i){
                min = min;
            }else{
                min = next_loop-i-1;
            }
            if(min<next_loop-j){
                min = min;
            }else{
                min = next_loop-j-1;
            }
            printf("%d ", n-min);
        }
        printf("\n");
    }
    printf("\n");
    return 0;
}