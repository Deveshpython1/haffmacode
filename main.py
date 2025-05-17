
class Node:
    def __init__(self,char=None,data=None,):
        self.char=char
        self.data=data
        self.right=None
        self.left=None
        self.head=None
class Pointer:
    def __init__(self,current=""):
        self.current=current
class Huffmancodeing:
    def __init__(self,string):
        dic={}
        for i in string:
           if i not in  dic:
              dic[i]=0
              for x in string:
                  if i==x:
                     dic[i]+=1 
        self.l=[]
        self.array=[]
        for i in dic:
            self.array.append(Node(char=i,data=dic[i]))
    def mergesort(self,array):
      if len(array)==0:
         return []
      mid=len(array)//2
      data=array[mid]
      right=[]
      left=[]
      equal=[]
      for i in array:
         if i.data>data.data:
             right.append(i)
         elif i.data<data.data:
             left.append(i)
         elif i.data==data.data:
             equal.append(i)
         else:
             pass
      return self.mergesort(left)+equal+self.mergesort(right)
    def constructtree(self):
        self.array=self.mergesort(self.array)
        while len(self.array)!=1:
            first=self.array[0]
            second=self.array[1]
            n=Node()
            n.left=first
            n.right=second
            n.data=first.data+second.data
            self.array.pop(0)
            self.array.pop(0)
            self.array.append(n)
            self.array=self.mergesort(self.array)
        self.head=self.array[0]
        self.start(self.head,Pointer())
        for i in self.l:
            print(f"{i[0]} : {i[1]}")

    
    def start(self,head,pointer):
        if head==None:
            return None
        if head.char!=None:

           self.l.append((head.char,pointer.current))
        self.start(head.left,Pointer(pointer.current+"0"))
        self.start(head.right,Pointer(pointer.current+"1"))


s=input("Enter a string for which you want the huffman code\n")        
Huffmancodeing(s).constructtree()
