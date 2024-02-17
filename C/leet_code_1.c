#include <stdio.h>
#include <stdlib.h>


/**
 * Note: The returned array must be malloced, assume caller calls free().
 * Link: https://leetcode.com/problems/two-sum/
 */


typedef struct HashMapNum {
    int idx;
    int value;
} HashMapNum;


HashMapNum* number_is_in_hash_map(HashMapNum* hash_map, int v, int size) {
    int i;
    for (i = 0; i < size; i++) {
        if (hash_map[i].value == v)
            return &hash_map[i];
    }
    return NULL;
}

int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    int* result = (int*)malloc(sizeof(int) * 2);
    HashMapNum* hash_map = (HashMapNum*) malloc(sizeof(HashMapNum) * numsSize);
    
    if (!result || !hash_map) {
        *returnSize = 0;
        return NULL;
    }

    int i;
    for (i = 0; i < numsSize; i++) {
        int diff = target - nums[i];
        HashMapNum* found = number_is_in_hash_map(hash_map, diff, numsSize);
        
        if (found != NULL && found->idx != i) {
            result[0] = found->idx;
            result[1] = i;

            *returnSize = 2;
            free(hash_map);
            
            return result;
        }
        
        if (number_is_in_hash_map(hash_map, nums[i], numsSize) == NULL) {
            hash_map[i].idx = i;
            hash_map[i].value = nums[i];
        }
    }
    
    *returnSize = 0;
    free(hash_map);
    free(result);
    return NULL;
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
    int nums[] = {2,7,11,15};
    int target = 18;
    int numsSize = sizeof(nums) / sizeof(nums[0]);
    int returnSize;
    int* return_idx;

    return_idx = twoSum(nums, numsSize, target, &returnSize);
    print_array(return_idx, returnSize);
}