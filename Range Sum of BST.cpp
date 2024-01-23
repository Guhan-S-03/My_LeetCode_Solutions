
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
    int tot=0;
    int inorder(TreeNode* root,int a,int b){
        if(root){
            inorder(root->left,a,b);
            if(root->val>=a && root->val<=b){
                tot+=root->val;
            }
            inorder(root->right,a,b);
        }
        return tot;
    }
    int rangeSumBST(TreeNode* root, int low, int high) {
        if(!root){
            return 0;
        }
        return inorder(root,low,high);
    }
};