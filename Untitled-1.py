import itertools
import string
import hashlib
import base64
class Count:
    c=0
    def __init__(self):
        
        Count.c+=1
        self.instance_va1 = Count.c
        
class MyClass:
    def __init__(self,var):
        
        MyClass.static_var = var
        self.instance_var = MyClass.static_var
        
try1='password'
text ='aaaaza'

m = hashlib.sha512(text.encode('UTF-8')).digest()
m1 = hashlib.sha512(try1.encode('UTF-8')).digest()
print(base64.b64encode(m1))
s=b'AsC8IYY1WOSfr5UO0UspPCNT5r1D5n+h4E5HMHv6FuG2Em7zX+ysXBDzLsFbC53Ga62eVeBdxkrvY8AerGnUPg=='

print(base64.b64encode(m))
x=False
obj1=MyClass(0)
def generate_passwords(n):
    """    all_chars = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation """
    all_chars = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    obj1=MyClass(6)
    while MyClass.static_var<=n:
      for password in itertools.product(all_chars, repeat=MyClass.static_var):
        
         
         obj2=Count()
         yield ''.join(password)
         if(MyClass.static_var>n): 
                
           break
         
      obj1=MyClass(MyClass.static_var+1)
    
for password in generate_passwords(40):
    
    if base64.b64encode(m)== base64.b64encode(hashlib.sha512(password.encode('UTF-8')).digest()):
       obj1=MyClass(100)
       x=True
       print('founded :'+password+'   after trying '+str(Count.c)+' password')
       break
if x==True:
  print('exist') 
else:
  print('not exist')   
