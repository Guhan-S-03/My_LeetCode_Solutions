
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* removeNodes(ListNode* head) {
        ListNode *dummy,*temp;
        dummy=new ListNode();
        temp=dummy;

        while(head){
            int val=head->val;
            ListNode *nextt=head->next;
            int flag=0;
            while(nextt){
                if(nextt->val>val){
                    flag=1;
                    break;
                }
                nextt=nextt->next;
            }
            if(flag==0){
                temp->next=head;
                temp=temp->next;
            }
            head=head->next;
        }
        temp->next=head;
        return dummy->next;
    }
   
    
};