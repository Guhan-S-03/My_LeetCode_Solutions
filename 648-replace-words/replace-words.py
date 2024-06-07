class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        #just find the smallest prefx for every word and replace 
        #if not p then leave it as it is
        words=sentence.split(" ")
        res=""

        for w in words:
            cur_res=w
            prefix_len=999999
            for p in dictionary:
                if w.startswith(p) and len(p)<prefix_len:
                    cur_res=p
                    prefix_len=len(p)
            res+=" "+cur_res
        return res[1:]


        