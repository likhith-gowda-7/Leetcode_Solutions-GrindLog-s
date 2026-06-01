class Solution:
    def build(self,baskets):
        #Segament Tree
        size=1
        self.n=len(baskets)
        while size<self.n:
            size*=2
        self.size=size
        self.tree=[0]*(2*size)
        #for leaves
        for i in range(self.n):
            self.tree[size+i]=baskets[i]
        #for parent 
        for i in range(size-1,0,-1):
            self.tree[i]=max(self.tree[2*i],self.tree[(2*i)+1])

    def update(self,idx):
        self.tree[idx]=0
        idx//=2 # going to its parent node
        while idx>0:
            self.tree[idx]=max(self.tree[2*idx],self.tree[(2*idx)+1])
            idx//=2
        
    def query(self,idx,target):
        if((2*idx)>=(2*self.size)):
            if(self.tree[idx]>=target):
                return idx
            return None
        if(self.tree[idx]<target):
            return None
        left=self.query(2*idx,target)
        if(left):
            return left
        return self.query(2*idx+1,target)

    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        self.build(baskets)
        unplaced=0
        for f in fruits:
            found=self.query(1,f)
            if(found):
                self.update(found)
            else:
                unplaced+=1
        return unplaced
        