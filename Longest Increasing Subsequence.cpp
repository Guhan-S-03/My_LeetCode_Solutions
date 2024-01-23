class Solution {
public:
    vector<vector<int>> dp;
    int lengthOfLIS(vector<int>& nums) {
        dp.resize(size(nums),vector<int>(1+size(nums),-1));
        return findmaxl(nums,0,-1);
    }
    int findmaxl(vector<int>& nums,int i, int prev){
        if(i>=size(nums)){
            return 0;
        }
        if(dp[i][prev+1]!=-1){
            return dp[i][prev+1];
        }
        int take=0;
        int nottake=findmaxl(nums,i+1,prev);
        if(prev==-1||nums[i]>nums[prev]){
            take=1+findmaxl(nums,i+1,i);
        }
        return dp[i][prev+1]=max(take,nottake);

    }
};