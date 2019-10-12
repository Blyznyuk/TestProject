# d, c = 0, 0
# a = int(input("kol "))
# for i in a:
#     a[i] = input("str")
#     if len(a[i]) %2 == 0
#         d += 1
#     else:
#         c +=1
#
# for i in a:
#
# print(d)
# print(c)

# s = ["a;sdfljdhs", "lak;dsflkjs", "podfiousdj", "ALdfsskjgh"]
# l = 0
# for i in s:
#     if len(i)%2 == 1:
#         l += 1
# print(l)


# #Словари!!!!!!!!!!
# d = {"name": "Llaa",  "age": 20, "pos": "QA"}
# for k, z in d.items():
#     print(k, end=' ')
#     print(z)

#
# name = "1Vacya"
# if name[0].isnumeric():
#     raise NameError("asd")

# a = input("chislo")
# assert (len(a) < 10), "vse ploho"
# print(a)


s = input("str ")
z = []
for i in s:
            a = i.strip('!.,@#$%^&*[]-=+()1234567890'' ')
            if a:
                z.append(i)
for i in z:
    assert i.isalpha(), "Chislo"
    print(i)


# def func(*args):
#     a = list(args)
#     a.sort()
#     return a[1]
# c = func(1, 10, 8, 25, 32, 1456, 878)
# print(c)


# def func(**kwargs):
#     return kwargs
#
#
# print(func(a = 12, name = "Vacya", pos = "QA"))
# print(type(func()))

#
# def func(**kwargs):
#     return '{} is {}'.format(kwargs.get('name'), kwargs.get("job"))
#
#
# print(func(job='lasd', name="vas"))
# print(type(func()))
#
# ln = ["lena", "kolya"]
# d = {'end': "!!!\n", "sep": "-"}
# print(*ln, **d)

# from math import sin, cos, pi
# print(sin(120)**2 + cos(60)**2)
# print(pi)
# import sys
# print(sys.path)
