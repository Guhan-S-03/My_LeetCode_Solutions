
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* removeElements(ListNode* head, int val) {
        ListNode *dummy,*temp;
        dummy=new ListNode();
        temp=dummy;

        while(head){
            if(head->val!=val){
                temp->next=head;
                temp=temp->next;
            }
            head=head->next;
        }
        temp->next=head;
        return dummy->next;

        
    }
};