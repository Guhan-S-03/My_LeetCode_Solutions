
struct ListNode {
int val;
ListNode *next;
ListNode() : val(0), next(nullptr) {}
ListNode(int x) : val(x), next(nullptr) {}
ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* deleteMiddle(ListNode* head) {
        ListNode *head1=new ListNode();
        ListNode *prev=head1;
        ListNode *slow=head;
        ListNode *fast=head;
        
        while(fast && fast->next){
            prev->next=slow;
            prev=prev->next;
            slow=slow->next;
            fast=fast->next->next;

        }
        prev->next=slow->next;
        return head1->next;
    }
};