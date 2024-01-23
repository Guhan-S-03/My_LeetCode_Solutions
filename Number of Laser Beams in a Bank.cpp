class Solution {
public:
    int numberOfBeams(vector<string>& bank) {
        int prevc=0;
        int tot=0;

        for(const string row:bank){
           int rowc=calculatetot(row);
           if(rowc==0){
            continue;
           }

           tot+=rowc*prevc;
           prevc=rowc;
        }
        return tot;
    }
private:
    int calculatetot(string row){
        int count=0;
        for(const char c:row){
            count+=c-'0';
        }
        return count;
    }
};