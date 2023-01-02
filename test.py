# data = [10,20,30,40,50]
# data.pop()
# print(data)
# data.pop(2)
# print(data)

# array=["welcome", 'to', 'turing']
# print("-".join(array))

# f = None
# for i in range(5):
#     with open("app.log", "w") as f:
#         if i>2:
#             break
# print(f.closed)

# class Developer:

#     def __init__(self):
#         self.__seniority = "Junior"
#         self.skills = ''

#     def display(self):
#         print('Welcome to Turing with {seniority} developer with skill {skills}'.format(seniority=self.__seniority, skills=self.skills))

# class NodeJS(Developer):

#     def __init__(self):
#         super().__init__()
#         self.__seniority = 'Senior'
#         self.skills = 'NodeJS'

# c = NodeJS()
# c.display()

# l = [1,2,3,4,5]
# m = map(lambda x: 2**x, l)
# print(list(m))

# inputs = ['nodejs', 'reactjs','vuejs']
# print(inputs)

# for i in inputs:
#     inputs.append(i.upper())

# print(inputs)
# z = set('abc')
# z.add('san')
# z.update(set(['p','q']))
# print(z)

# x = "abcdef"
# i = "a"
# while i in x[:-1]:
#     print(i, end="")

# data = [1,2,3,4,5]
# newdata= data.copy()
# print(newdata)

# list1 =[1,2,3,4]
# list2 =[sum(list1[0:x+1]) for x in range(0, len(list1))]
# print(list2)
# import re
# result = re.findall('Welcome to Turing','Welcome', 1)
# print(result)

# print(2**(3**2),(2**3)**2,(2**3)**3)
# print("Welcome to TURING".capitalize())
# \
# print([i.lower() for i in "TURING"])
# \
# array1=[1,2,3,4,5]
# array2=array1
# array2[0]= 0
# print(array1)
# \
# def add(c, k):
#     c.test = c.test + 1
#     k = k + 1

# class Plus:
#     def __init__(self):
#         self.test=0

# def main():
#     p = Plus()
#     index = 0

#     for i in range(0,25):
#         add(p, index)
    
#     print("p.test", p.test)
#     print("index=", index)

# main()

# data = [1,2,3]

# def incr(x):
#     return x + 1

# print(list(map(incr, data)))

class Hello:

    def __init__(self, a='Welcome to '):
        self.a = a
    
    def welcome(self, x):
        print(self.a + x)

h = Hello()
h.welcome('Turing')