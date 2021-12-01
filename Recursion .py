# i=0
# def fun(a):
#     global i
#     print("deepu",i)
#     i+=1
#     fun()
# fun(20)    


# import sys
# print(sys.getrecursionlimit())
# sys.setrecursionlimit(4000)
# print(sys.getrecursionlimit())



def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)