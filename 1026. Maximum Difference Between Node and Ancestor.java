
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
    int dist=0; 
    int maxAncestorDiff(TreeNode root) {
        helper(root);
        return dist;   
    }
    int []helper(TreeNode node){
        if(node==null){
            return new int[]{Integer.MAX_VALUE,Integer.MIN_VALUE};

        }
        if(node.left ==null && node.right==null){
            return new int[]{node.val,node.val};

        }
        int [] left=helper(node.left);
        int [] right=helper(node.right);
        diff=Math.max(diff,Math.max(Math.abs(min-node.val),Math.abs(max-node.val)));
        min=Math.min(min,node.val);
        max=Math.max(max,node.val);
        return new int[]{min,max};
    }
};