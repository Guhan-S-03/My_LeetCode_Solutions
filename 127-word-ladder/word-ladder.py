class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        ##here we want to find the words with one char diff at a time
        #so intially we can find the adjacency list of pattern(*ot) that tells us the
        #single char diff words that follows this pattern and we will do the bfs in the 
        #adjacency(graph) to find the shortest path
        if endWord not in wordList:
            return 0

        patterns=defaultdict(list)
        wordList.append(beginWord)
        for w in wordList:
            for j in range(len(w)):
                pat=w[:j]+"*"+w[j+1:]
                patterns[pat].append(w)
        ##bfs
        visit=set([beginWord])
        q=deque([beginWord])

        res=1
        while q:
            for i in range(len(q)):
                word=q.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pat=word[:j]+"*"+word[j+1:]
                    for neighbor in patterns[pat]:
                        if neighbor not in visit:
                            visit.add(neighbor)
                            q.append(neighbor)
            res+=1
        return 0

                


        