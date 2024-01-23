#include<bits/stdc++.h>
struct TreeNode {
int val;
TreeNode *left;
TreeNode *right;
TreeNode() : val(0), left(nullptr), right(nullptr) {}
TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    int diff=0;
    int maxAncestorDiff(TreeNode* root) {
        vector<int> temp=helper(root);
        return diff;  
    }
    vector<int> helper(TreeNode *node){
        if(node==nullptr){
            vector<int> temp;
            temp.push_back(INT_MAX);
            temp.push_back(INT_MIN);
            return temp;
        }
        if(node->left ==nullptr && node->right==nullptr){
           vector<int> temp;
            temp.push_back(node->val);
            temp.push_back(node->val);
            return temp;
        }
        vector<int>left=helper(node->left);
        vector<int>right=helper(node->right);

        int minn =min(left[0],right[0]);
        int maxx=max(left[1],right[1]);
        diff=max(diff,max(abs(minn-node->val),abs(maxx-node->val)));
        minn=min(minn,node->val);
        maxx=max(maxx,node->val);
        vector<int> neww;
        neww.push_back(minn);
        neww.push_back(maxx);
        return neww;
    }
};