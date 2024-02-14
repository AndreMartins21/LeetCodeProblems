#include <stdio.h>
#include <stdlib.h>


/**
 * Note: The returned array must be malloced, assume caller calls free().
 * Example:
    Input: nums = [3,1,-2,-5,2,-4]
    Output: [3,-2,1,-5,2,-4]
 */

void get_positive_and_negative_numbers(int *nums, int numsSize, int **all_pos, int **all_neg){
    int i, count_p = 0, count_n = 0;

    for(i=0; i<numsSize; i++){
        if(nums[i] < 0){
            (*all_neg)[count_n] = nums[i];
            count_n ++;            
        } else {
            (*all_pos)[count_p] = nums[i];
            count_p ++;
        }
    }
}

int* rearrangeArray(int* nums, int numsSize, int* returnSize) {
    int i, aux = 0;

    int* x_return = (int *) malloc(sizeof(int) * numsSize);

    get_positive_and_negative_numbers(nums, numsSize, &all_pos, &all_neg);
    
    
    for (i=0; i<(numsSize/2);i++){
        x_return[aux] = all_pos[i];
        x_return[aux+1] = all_neg[i];
        aux += 2;
    }

    *returnSize = numsSize;
    return x_return;
}


void main(){
    int nums[] = {3, 1, -2, -5, 2, -4};
    int numsSize = sizeof(nums) / sizeof(nums[0]);
    int returnSize;
    int* rearrangedArray = rearrangeArray(nums, numsSize, &returnSize);

    printf("Output: [");
    for (int i = 0; i < returnSize; i++) {
        printf("%d", rearrangedArray[i]);
        if (i < returnSize - 1) {
            printf(",");
        }
    }
    printf("]\n");

    free(rearrangedArray); // Free allocated memory
}