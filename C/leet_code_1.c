#include <stdio.h>
#include <stdlib.h>


/**
 * Note: The returned array must be malloced, assume caller calls free().
 * Link: https://leetcode.com/problems/two-sum/
 */
int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    int i, j;
    int* array_idx = (int*) malloc(sizeof(int)*2);
    
    for (i=0; i<numsSize; i++){
        if (nums[i] > target && nums[i] > 0) continue;

        for (j=0; j<numsSize; j++){
            if(j==i) continue;
            
            if (nums[j] + nums[i] == target){
                array_idx[0] = j;
                array_idx[1] = i;
                break;
            }
        }
    }

    *returnSize = 2;
    return array_idx;
}

void print_array(int *array, int len_array){
    int i;

    printf("\n[");
    for(i=0; i<len_array;i++){
        printf("%d ", array[i]);
    }
    printf("]\n");
}


void main(){
    int nums[] = {2,4,11,3};
    int target = 6;
    int numsSize = sizeof(nums) / sizeof(nums[0]);
    int returnSize;
    int* return_idx;

    return_idx = twoSum(nums, numsSize, target, &returnSize);
    print_array(return_idx, returnSize);
}