#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
/**
 * Write a C program to find the maximum of n numbers taken as input.
 * using bitwise operation  Hacker Rank solution
 * 
 */
void calculate_the_maximum(int n, int k) {
  int *S = (int *)malloc(n * sizeof(int *));
  int size = n*n;
  int *andstaff = (int *)malloc(size * sizeof(int *));
  int *orstaff = (int *)malloc(size * sizeof(int *));
  int *xorstaff = (int *)malloc(size * sizeof(int *));

  for(int i = 0; i <n; i++) {
    S[i] = i+1;
  }
  int index = 0;
  for(int i = 0; i <n; i++) {
    for (int j = i+1; j < n; j++) {
        int ands = S[i] & S[j];
        int ors = S[i] | S[j];
        int xors = S[i] ^ S[j];
        if(ands < k && ands > 0) {
            andstaff[index] = ands;
        }
        if(ors < k && ors > 0) {
            orstaff[index] = ors;
        }
        if(xors < k && xors > 0) {
            xorstaff[index] = xors;
        }
        index++;
    }
  }
  int maxand = andstaff[0];
  int maxor = orstaff[0];
  int maxxor = xorstaff[0];
  for(int i = 0; i <size; i++) {
    if(andstaff[i] > maxand) {
        maxand = andstaff[i];
    }
    if(orstaff[i] > maxor) {
        maxor = orstaff[i];
    }
    if(xorstaff[i] > maxxor) {
        maxxor = xorstaff[i];
    }
  }
  printf("%d \n", maxand);
  printf("%d \n", maxor);
  printf("%d \n", maxxor);
  free(andstaff);
  free(orstaff);
  free(xorstaff);
  free(S);
}

int main() {
    int n , k;
    scanf("%d %d", &n, &k);
    calculate_the_maximum(n, k);
 
    return 0;
}
