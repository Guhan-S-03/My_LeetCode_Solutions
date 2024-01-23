struct ListNode {
int val;
ListNode *next;
ListNode() : val(0), next(nullptr) {}
ListNode(int x) : val(x), next(nullptr) {}
ListNode(int x, ListNode *next) : val(x), next(next) {}
 };

class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        if(head==nullptr || head->next==nullptr){
            return head;
        }
        ListNode *dummy=new ListNode();
        dummy->next=head;
        ListNode *prev=dummy;
        ListNode *cur=head;

        while(cur){
            if(cur->next!=nullptr && cur->val==cur->next->val){
                while(cur->next!=nullptr && cur->val==cur->next->val){
                    cur=cur->next;
                }
                prev->next=cur->next;
            }
            else{
                
                prev=cur;
            }
            cur=cur->next;
        }
        return dummy->next;
    }
};