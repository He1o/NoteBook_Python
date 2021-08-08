a = 'aoaobobo'
b = [1,2,3,5,7,8,34,2,5]
for c in reversed(a):  
    print(c,end = '')  #oboboaoa

print('\n',list(reversed(b)))  #[5, 2, 34, 8, 7, 5, 3, 2, 1]