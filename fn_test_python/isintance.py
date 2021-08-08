a = 5
print(isinstance(a,int)) #true
print(isinstance(a,str)) #false

class A:
    pass
class B(A):
    pass

print(type(A))  #<class 'type'>
print(type(B))  #<class 'type'>
print(type(A)==type(B))  #True
print(isinstance(A,B))  #False
print(type(A()))  #<class '__main__.A'>
print(type(B()))  #<class '__main__.B'>
print(type(A())==A)  #true
print(isinstance(A(),A))  #true
print(type(B())==A)  #false
print(isinstance(B(),A))  #true
# isinstance considers subclasses to be a parent type,considering inheritance