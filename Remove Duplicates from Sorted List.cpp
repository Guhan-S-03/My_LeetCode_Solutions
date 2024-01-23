

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
        ListNode *sortedlist,*dummy;
        sortedlist=new ListNode();
        dummy=sortedlist;
        int prev=9999;

        while(head){
            if(head->val!=prev){
                prev=head->val;
                dummy->next=head;
                dummy=dummy->next;
            }
            head=head->next;
        }
        dummy->next=head;
        return sortedlist->next;
    }
};