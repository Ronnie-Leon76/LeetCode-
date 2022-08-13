class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> twoSumIndex;
        bool elementOkay;
        bool targetOkay;
        for(int j=0; j<nums.size();j++){
            if((nums[j]>= -1000000000) && (nums[j]<= 1000000000)){
                elementOkay = true;
            }else{
                elementOkay = false;
            }
        }
        if((target>= -1000000000) && (target<= 1000000000)){
            targetOkay = true;
        }else{
            targetOkay = false;
        }
        if((nums.size()>=2) && (nums.size()<=10000) && (elementOkay) && (targetOkay)){
            int i;
            for(i=0; i<nums.size(); i++){
                int value = nums[i] + nums[i+1];
                if(value == target){
                    twoSumIndex.push_back(i);
                    twoSumIndex.push_back(i+1);
                    break;
                }else{
                    for(int j = i+2; j<nums.size();j++){
                        int val = nums[i] + nums[j];
                        if(val == target){
                            twoSumIndex.push_back(i);
                            twoSumIndex.push_back(j);
                            break;
                        }
                    }
                    continue;
                }
            }
        }
        
        return twoSumIndex;
    }
};