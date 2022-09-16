import math

class Heap(object):
    """docstring for Heap"""
    def __init__(self):
        self.array = [1, 2, 3, 4, 5, 6, 7]


    def insert(self, val):
        self.array.append(val)
        self.rebalance(len(self.array)-1)

    def remove(self, index):
        self.swap(index, len(self.array)-1)
        del self.array[len(self.array)-1]
        self.rebalance(index)


    def peek(self):
        return self.array[0]


    def rebalance(self, index):
        if self.array[self.getChild(index)] < self.array[index]:
            #print("down")
            self.rebalanceDown(index)
        elif self.array[self.getParent(index)] > self.array[index]:
            #print("up")
            self.rebalanceUp(index)
        print(self.array)


    def rebalanceUp(self, index):
        parent = self.getParent(index)
        if self.array[parent] > self.array[index]:
            self.swap(index, parent)
            self.rebalanceUp(parent)


    def rebalanceDown(self, index):
        child = self.getChild(index)
        if self.array[child] < self.array[index]:
            self.swap(index, child)
            self.rebalanceDown(child)

    def getChild(self, index):

        if 2*index+2 < len(self.array) and self.array[2*index+1] < self.array[2*index+2]:
            if 2*index+1 < len(self.array):
                return 2*index+1
            else:
                return index
        if 2*index+2 < len(self.array):
            return 2*index+2
        else:
            return index


    def getParent(self, index):
        #print((index-1)/2)
        if math.floor((index-1)/2) > -1:
            return math.floor((index-1)/2)
        else:
            return index

    def swap(self, i1, i2):
        placehold = self.array[i1]
        self.array[i1] = self.array[i2]
        self.array[i2] = placehold



if __name__ == '__main__':
    h = Heap()
    
