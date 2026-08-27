class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        neigh=defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                pattern=word[:i]+'*'+word[i+1:]
                neigh[pattern].append(word)
        print(neigh)
        visited=set()
        queue=[]
        queue.append(beginWord)
        visited.add(beginWord)
        res=1
        while queue:
            for i in range(len(queue)):
                word=queue.pop(0)
                if word==endWord:
                    return res
                for i in range(len(word)):
                    pattern=word[:i]+'*'+word[i+1:]
                    for nei in neigh[pattern]:
                        if nei not in visited:
                            visited.add(nei)
                            queue.append(nei)
            res+=1
        return 0

        