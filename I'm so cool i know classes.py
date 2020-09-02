class Node:
    def __init__(self,initval=None):
        self.value=initval
        self.next=None

    def isempty(self):
        if self.value==None:
            return True
        else:
            return False

    def appendr(self,v):  #append at the end of the list
        if self.isempty():
            self.value=v
        elif self.next==None:
            newnode=Node(v)#make a new node
            self.next=newnode
        else:
            self.next.appendr(v) #recursive call
        return()

    def insert(self,v): #insert at the beginning
        if self.isempty():
            self.value=v
            return()
        newnode=Node(v)

        (newnode.value,self.value)=(self.value,newnode.value)
        (self.next,newnode.next)=(newnode,self.next)
        return()

    def delete(self,v):
        if self.isempty():
            return()
        if self.value==v:
            if self.next==None:
                self.value=None
            else:
                self.value=self.next.value
                self.next=self.next.next #bypass
        else:
            if self.next!=None:
                self.next.delete(v)
                if self.next.value==None:
                    self.next==None
        return()


    def __str__(self):
        selflist=[]
        if self.value==None:
            return(str(selflist))
        temp=self
        selflist.append(temp.value)
        while(temp.next!=None):
            temp=temp.next
            selflist.append(temp.value)
        return(str(selflist))
    
    
        
        
            
    
