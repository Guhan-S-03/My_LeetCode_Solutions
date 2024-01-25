/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int digit[11];
    int result=0;
    int pseudoPalindromicPaths (TreeNode* root) {
        dfs(root);
        return result;
    }
    void dfs(TreeNode *root){
        if(root==NULL){
            return;
        }
        digit[root->val]+=1;
        if(root->left==NULL && root->right==NULL){
            if(palindrome()){
                result++;
            }
        }
        else{
            dfs(root->left);
            dfs(root->right);
        }
        digit[root->val]-=1;
    }
    bool palindrome(){
        int odd=0;
        for(int i=1;i<11;i++){
            if(digit[i]%2!=0){
                odd+=1;
            }
        }
        if(odd>1){
            return false;
        }
        else{
            return true;
        }
    }
};