
struct ListNode {
 int val;
 ListNode *next;
 ListNode() : val(0), next(nullptr) {}
 ListNode(int x) : val(x), next(nullptr) {}
 ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    bool isPalindrome(ListNode* head) {
        ListNode *prev=NULL;
        ListNode *prev1=NULL;
        ListNode *cur=head;
        string s;
        string s1;
        while(cur){
            ListNode *forward=cur->next;
            cur->next=prev;
            s+=to_string(cur->val);
            prev=cur;
            cur=forward;
        }
        ListNode *cur1=prev;
        while(cur1){
            ListNode *forward1=cur1->next;
            cur1->next=prev1;
            s1+=to_string(cur1->val);
            prev1=cur1;
            cur1=forward1;
        }
        return s1==s;


    }
};