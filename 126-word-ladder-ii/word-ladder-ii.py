class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        h=defaultdict(list)
        wordList=set(wordList)
        wordList.add(beginWord)
        for word in wordList:
            for i in range(len(word)):
                pattern=word[:i]+"*"+word[i+1:]
                h[pattern].append(word)
        visited=set()
        queue=[]
        visited.add(beginWord)
        queue.append(beginWord)
        hmap={}
        hmap[beginWord]=0
        count=1
        while queue:
            for i in range(len(queue)):
                word=queue.pop(0)
                

                for i in range(len(word)):
                    pattern=word[:i]+"*"+word[i+1:] 
                    for nei in h[pattern]:
                        if nei not in visited:
                            visited.add(nei)
                            queue.append(nei)
                            hmap[nei]=count
            count+=1
        if endWord not in hmap:
            return []
        # print(hmap)
        res=[]
        def dfs(word,arr):
            if word==beginWord:
                res.append(arr.copy())
                return
            for i in range(len(word)):
                pattern=word[:i]+"*"+word[i+1:] 
                for nei in h[pattern]:
                    if hmap[nei]<hmap[word]:
                        arr.insert(0,nei)
                        dfs(nei,arr)
                        arr.pop(0)
        dfs(endWord,[endWord])
        # print(res)
        return res
        
