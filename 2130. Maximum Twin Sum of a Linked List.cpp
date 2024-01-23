
struct ListNode {
int val;
ListNode *next;
ListNode() : val(0), next(nullptr) {}
ListNode(int x) : val(x), next(nullptr) {}
ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    int pairSum(ListNode* head) {
        ListNode *slow=head;
        ListNode *fast=head;
        ListNode *rev=nullptr;

        while(fast && fast->next){
            fast=fast->next->next;
            ListNode *forward=slow->next;
            slow->next=rev;
            rev=slow;
            slow=forward;
        }
        int high=0;
        while(slow){
            if(slow->val+rev->val>high){
                high=slow->val+rev->val;
            }
            slow=slow->next;
            rev=rev->next;
        }
        return high;
        
    }
};