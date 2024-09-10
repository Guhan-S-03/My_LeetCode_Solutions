#include<bits/stdc++.h>
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* insertGreatestCommonDivisors(ListNode* head) {
        ListNode *newhead=head;

        while(head && head->next){
            ListNode *forward=head->next;
            int a=head->val;
            int b=head->next->val;
            int gcdv=gcd(a,b);
            ListNode *newnode=new ListNode(gcdv);
            newnode->next=forward;
            head->next=newnode;
            head=forward;
        }
        return newhead;
        
    }
    int gcd(int a,int b){
        int result=min(a,b);
        while(result>0){
            if(a%result==0 && b%result==0){
                break;
            }
            result--;
        }
        return result;
    }
};