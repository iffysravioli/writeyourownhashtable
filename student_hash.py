class Student_Hashtable:
  def __init__(self,buckets=10):
    self.buckets=buckets
    self.data=[[] for _ in range(buckets)]
  
  def my_hash(self,key):
    return key % self.buckets
  
  def insert(self, key, value):
    tola = self.my_hash(key)
    for i in range(len(self.data[tola])):
      if self.data[tola][i][0] == key:
        self.data[tola][i] = (key,value)
        return
   
    
  def get(self,key):
    tola = self.my_hash(key)
    for i in range(len(self.data[tola])):
      if self.data[tola][i][0] == key: 
        return self.data[tola][i][1]
    return f"Hashkey does not exist"

 
  
def remove(self,key) :
  tola = self.my_hash (key)
  for i in range(len(self.data[tola])):
    if self.data[tola][1][0] == key:
      self.data[tola].pop(i)
      return
  return f"Hashkey does not exist!"

