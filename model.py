debug = False

class model:
    def __init__(self,size):
        self.edge_length = size
        self.last = size**2+1
        self.total_count = self.edge_length**2
        
        self.array = [] #parent index of each index
        for i in range(0,self.last+1):
            self.array.append(i)

        self.graph_size = [1]*(size**2+2)
        self.unblock_status = [0]*(size**2+2)
        self.unblock_count = 0
        self.initial_connection()

    '''
    #debugging tools

    def display_all(self):
        print(self.array)
        print(self.graph_size)

    def display_parent(self):
        for i in range(1,self.last):
            print(self.array[i],end = '\t')
            if(i%self.edge_length==0):
                print("\n")
        print("\n")

    def display_unblock_status(self):
        for i in range(1,self.last):
            print(self.unblock_status[i],end = '\t')
            if(i%self.edge_length==0):
                print("\n")
        print("\n")
    '''

    def root(self,ind):
        if(debug):print("called root of",ind,end=" ")
        
        root=ind
        while(self.array[root] != root):
            root = self.array[root]
        
        #Path compression
        old_root = self.array[ind]
        while(old_root!=root):
            self.graph_size[old_root]-=1
            old_root=self.array[old_root]
        self.array[ind]=root
        
        if(debug):print("returned",root)
        return root

    def connected(self,ind1,ind2):
        return self.root(ind1)==self.root(ind2)

    def union(self,ind1,ind2):
        if(debug):print("union",ind1,ind2)
        root1 = self.root(ind1)
        root2 = self.root(ind2)
     
        if(root1!=root2):
            #weight balancing
            if(self.graph_size[root1]>self.graph_size[root2]):
                self.array[root2]=root1
                self.graph_size[root1]+=self.graph_size[root2]
                if(debug):print(root1,"is the new parent of",root2)
            else :
                self.array[root1]=root2
                self.graph_size[root2]+=self.graph_size[root1]
                if(debug):print(root2,"is the new parent of",root1)

    def initial_connection(self):
        for x in range(1,self.edge_length+1):
            self.union(0,x)
            self.union(self.last-1-self.edge_length+x,self.last)

    def unblock(self,x):
        if(debug):print("unblock",x)

        if(self.unblock_status[x]==0):
            if((x-1)%self.edge_length and self.unblock_status[x-1]):
                self.union(x-1,x)
            if(x%self.edge_length and self.unblock_status[x+1]):
                self.union(x,x+1)
            if(x>self.edge_length and self.unblock_status[x-self.edge_length]):
                self.union(x,x-self.edge_length)
            if(x<self.last-self.edge_length and self.unblock_status[x+self.edge_length]):
                self.union(x,x+self.edge_length)
            self.unblock_status[x]=1
            self.unblock_count += 1

def simulate(size,unblock_input):
    x = model(size)

    for i in unblock_input:
        x.unblock(i)
        if(x.connected(0,x.last)):
            break

    return x.unblock_count
