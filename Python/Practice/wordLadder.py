import ipdb
class Solution(object): 
    def ladderLength(self, beginWord, endWord, wordList):
        # letter = {}
        # for i in range(len(beginWord)):
        #     letter[i] = {}
        #     for j in range(len(wordList)):
        #         if wordList[j][i] not in letter[i]:
        #             letter[i][wordList[j][i]] = 0
        queue = [(beginWord,1)]
        been = {}
        queue2 = [(endWord, 1)]
        been2 = {}
        if endWord not in wordList:
            return 0
        while(True):
            #if either side is cut off break
            if len(queue) == 0 or len(queue2) == 0:
                print(queue, queue2)
                return 0


            
            #forward bfs
            word, layer = queue.pop(0)
            swapScore = self.wordSwaps(word, layer, been, been2, queue)
            if not swapScore == -1:
                return swapScore
            
            #backwards bfs
            word, layer = queue2.pop(0)
            swapScore = self.wordSwaps(word, layer, been2, been, queue2)
            if not swapScore == -1:
                return swapScore
                
    def swap(self, word, swapee, place):
        newWord = word[0:place] + swapee + word[place+1:len(word)+1]
        return newWord

    def wordSwaps(self, word, layer, been, been2, queue):
    	for place, char in enumerate(word):
                for i in range(97, 97+26):
                    if not chr(i) == char:
                        #swap index place for each letter
                        newWord = self.swap(word, chr(i), place)
                        #make sure its not a repeat and its in wordList
                        if newWord not in been and newWord in wordList:
                            #if its the end Word then break  doesn't happen\
                            if newWord == endWord:
                                return layer + 1
                            if newWord in been2: 
                                return layer + been2[newWord]
                            queue.append((newWord, layer+1))
                            been[newWord] = layer +1
        return -1


if __name__ == '__main__':
    with open("test.txt") as file:
        b, e, w = tuple( file.read().replace("\"", "").splitlines())
        w = w.replace("[", "").replace("]", "").split(",")
        # print(b,e,w)

    s = Solution()
    print(s.ladderLength(b, e, w))
