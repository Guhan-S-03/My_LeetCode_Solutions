struct ListNode {
int val;
ListNode *next;
ListNode() : val(0), next(nullptr) {}
ListNode(int x) : val(x), next(nullptr) {}
ListNode(int x, ListNode *next) : val(x), next(next) {}
 };

class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        if(headA ==nullptr || headB==nullptr){
            return nullptr;
        }
        ListNode *a=headA;
        ListNode *b=headB;
        while(a!=b){
            if(a==nullptr){
                a=headB;
            }
            else{
                a=a->next;
            }
            if(b==nullptr){
                b=headA;
            }
            else{
                b=b->next;
            }
        }
        return a;
        
    }
};