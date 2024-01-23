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
    int amountOfTime(TreeNode* root, int start) {
        map<TreeNode *,TreeNode *> mapp;
        TreeNode *target=bfs(root,start,mapp);
        int time=findtime(mapp,target);
        return time;
        
    }
    TreeNode *bfs(TreeNode *root,int start, map<TreeNode *,TreeNode *> &mapp){
        queue<TreeNode *> q;
        q.push(root);
        TreeNode *result;
        while(!q.empty()){
            TreeNode *node=q.front();
            if(node->val==start){
                result=node;
            }
            q.pop();
            if(node->left){
                mapp[node->left]=node;
                q.push(node->left);
            }
            if(node->right){
                mapp[node->right]=node;
                q.push(node->right);
            }


        }
        return result;
    }

    int findtime(map<TreeNode *,TreeNode *> &mapp, TreeNode *target){
        queue<TreeNode *> q;
        q.push(target);
        map<TreeNode *,int>burnt;
        burnt[target]=1;
        int timer=0;
        while(!q.empty()){
            int size=q.size();
            int flag=0;
            for(int i=0;i<size;i++){
                TreeNode *node=q.front();
                q.pop();
                if(node->left && !burnt[node->left]){
                    flag=1;
                    burnt[node->left]=1;
                    q.push(node->left);
                }
                if(node->right && !burnt[node->right]){
                    flag=1;
                    burnt[node->right]=1;
                    q.push(node->right);
                }
                if(mapp[node]&& !burnt[mapp[node]]){
                    flag=1;
                    burnt[mapp[node]]=1;
                    q.push(mapp[node]);
                }

                }
             if(flag){
                timer++;
             }   

            }
        return timer;
    }
        
};

