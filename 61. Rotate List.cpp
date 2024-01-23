struct ListNode {
int val;
ListNode *next;
ListNode() : val(0), next(nullptr) {}
ListNode(int x) : val(x), next(nullptr) {}
ListNode(int x, ListNode *next) : val(x), next(next) {}
 };

class Solution {
public:
    ListNode* rotateRight(ListNode* head, int k) {
        int cnt=0;
        ListNode *neww=head;
        while(neww){
            cnt+=1;
            neww=neww->next;
        }
        
        if(cnt>1){
        k=k%cnt;
        for(int i=0;i<k;i++){
            ListNode *prevhead=head;
            while(head && head->next && head->next->next){
                head=head->next;
            }
            ListNode *lastnode=head->next;
            head->next=nullptr;
            lastnode->next=prevhead;
            head=lastnode;
        }
        }
        return head;

        
    }
};