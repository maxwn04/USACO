def dumbway():
    for filename in range(1,11):
        with open('test/' + str(filename)+'.in') as file:
            cows = ["Beatrice", "Belinda", "Bella", "Betsy", "Bessie", "Blue", "Buttercup", "Sue"]
            pair = {"Beatrice":[], "Belinda":[], "Bella":[], "Betsy":[], "Bessie":[], "Blue":[], "Buttercup":[],   
            "Sue":[]}
            order = []
            lines = file.read().splitlines()
            n = int(lines[0])
            for i in range(1, n+1):
                s = lines[i].split()
                pair[s[0]].append(s[5])
                pair[s[5]].append(s[0])

            for i in range(8):
                if cows[i] not in order:
                    pair[cows[i]].sort()
                    if len(pair[cows[i]]) > 1:
                        order.append(pair[cows[i]][0])
                        order.append(cows[i])
                        order.append(pair[cows[i]][1])
                        i += 2
                    elif len(pair[cows[i]]) > 0:
                        if cows[i] < pair[cows[i]][0]:
                            order.append(cows[i])
                            order.append(pair[cows[i]][0])
                        else:
                            order.append(pair[cows[i]][0])
                            order.append(cows[i])
                        i += 1 
                    else:
                        for spot in range(len(order)):
                            if cows[i] < order[spot]:
                                begin = order[0:spot]
                                end = order[spot+1:len(order)]
                                order = begin+[cows[i]]+end
                        if cows[i] not in order:
                            order.append(cows[i])

            print(filename, order)
        with open('test/' + str(filename)+'.out') as file:
            s = file.read().split()
        
            print(filename, s)

def smartway():
    for filename in range(1,11):
        with open('test/' + str(filename)+'.in') as file:
            cows = ["Beatrice", "Belinda", "Bella", "Bessie", "Betsy", "Blue", "Buttercup", "Sue"]
            cowTree = {}
            for cow in cows:
                cowTree[cow] = TreeNode(cow)
            lines = file.read().splitlines()
            n = int(lines[0])
            for i in range(1, n+1):
                s = lines[i].split()
                cow1 = s[0]
                cow2 = s[5]
                cowTree[cow1].neigh.append(cowTree[cow2])
                cowTree[cow2].neigh.append(cowTree[cow1])

            for cow int cows:
                assert len(cowTree[cow].neigh) < 3

            order = []
            for cow in cows:
                if cow not in order:
                    startdfs(order, cowTree[cow])
            #print(filename, order)
        with open('test/' + str(filename)+'.out') as file:
            s = file.read().split()
        
            assert order == s

def startdfs(order, TreeNode):
    if len(TreeNode.neigh) == 0:
        order.append(TreeNode.name)
    if len(TreeNode.neigh) == 1:
        order.append(TreeNode.name)
        dfs(order, TreeNode.neigh[0], TreeNode)

def dfs(order, TreeNode, passed):
    order.append(TreeNode.name)
    if len(TreeNode.neigh) == 2:
        if not TreeNode.neigh[0] == passed:
            dfs(order, TreeNode.neigh[0], TreeNode)
        else:
            dfs(order, TreeNode.neigh[1], TreeNode)


    


class TreeNode(object):
    def __init__(self, name = None, neigh=None):
        self.name = name
        self.neigh = []

if __name__ == '__main__':
    smartway()