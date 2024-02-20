#include <stdio.h>
#include <stdlib.h>


/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* productExceptSelf(int* nums, int numsSize, int* returnSize) {
    int i;
    int *response = (int*) malloc(sizeof(int)*numsSize);
    
    int prefix = 1;
    for (i=0; i<numsSize; i++){
        response[i] = prefix;
        prefix *= nums[i];
    }

    int posfix = 1;
    for (i = numsSize-1; i>=0; i--){
        response[i] *= posfix;
        posfix *= nums[i];
    }
    
    *returnSize = numsSize;
    return response;
}


void main(){
    int nums[] = {1, 2, 3, 4};
    int numsSize = sizeof(nums) / sizeof(nums[0]);
    int returnSize;
    int* response = productExceptSelf(nums, numsSize, &returnSize);

    printf("Output: [");
    for (int i = 0; i < returnSize; i++) {
        printf("%d", response[i]);
        if (i < returnSize - 1) {
            printf(",");
        }
    }
    printf("]\n");

    free(response); // Free allocated memory
}