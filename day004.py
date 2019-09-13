# 1.读取成绩并输出成绩等级
# def score(a,b,c,d):
#     x = [a,b,c,d]
#     y = sorted(x)
#     best = y[3]
#     for i in range(len(x)):
#         if x[i] >= best-10:
#             print('A')
#         elif x[i] >= best-20:
#             print('B')
#         elif x[i] >= best-30:
#             print('C')
#         elif x[i] >= best-40:
#             print('D')
#         else:
#             print('F')
# score(40,55,70,58)


# 2.逆序顺序显示一个整数列表
# def num():
#     a = [1,2,3,4,0,9,8,7]
#     b = a[::-1]
#     print(b)
# num()


# 3.统计数字个数
# def num(str1):
#    str3 = str1
#    str2 = []
#    for i in str1:
#        if i not in str2 :
#            str2.append(i)

#    for i in range(len(str2)):
#        num1 = 0
#        for j in range(len(str3)):
#            if str3[j] == str2[i]:
#                num1 += 1
#            else:
#                num1 = num1
#        print('按照顺序的数字个数%d'%num1)
# num([1,2,3,4,5,4,3,5,3,2,4,2])


# 4.计算有多少是大于平均数有多少是小于平均数的
# def average(list):
#    pinjun = sum(list)/(len(list)*1.0)
#    return pinjun
# num1 = 0
# num2 = 0
# def fenshu(list_):
#    pinjun = average(list_)
#    for i in range(len(list_)):
       
#        global num1
#        global num2
#        if list_[i] > pinjun: 
#            num1 += 1
#        elif list_[i] < pinjun:
#            num2 += 1
#        else:
#            pass
#    print(num1)
#    print(num2)
#    print(pinjun)
# fenshu([2,4,2,4,8])


# #6.输出最小元素的下标
# def IndexOfSmallestElement():
#     list1=list(map(int,input('Please enter a list of numbers:').split(',')))
#     list2=sorted(list1)
#     num=0
#     for i in list1:
#         if i==list2[0]:
#             print('The subscript of the smallest element is：%d'%num)
#         else:
#             num+=1
# if __name__ == '__main__':
#     indexOfSmallestElement()

# #7.打乱一个列表并返回这个列表
# import random
# lst=list(map(int,input('Please enter a list of number:').split(' ')))
# def Shuffle(lst):
#     random.shuffle(lst)
#     for i in lst:
#        print(i,end=' ')
# if __name__ == '__main__':
#     Shuffle(lst)

# #8.消除重复
# lst=list(map(int,input('Please enter a list of number:').split(' ')))
# def eliminateDupLicates(lst):
#     set1=set(lst)
#     for i in set1:
#         print(i,end=' ')   
# if __name__ == '__main__':
#     eliminateDupLicates(lst)

# #9.检测是否排序
# lst=list(map(int,input('Please enter a list of number:').split(' ')))
# def isSorted(lst):
#     if lst != sorted(lst):
#         print('Not sorted !')
#     else:
#         print('Already sorted !')
# if __name__ == '__main__':
#     isSorted(lst)

# #10.冒泡排序
# lst=list(map(int,input('Please enter a list of number:').split(' ')))
# def MaoPaoSort(lst):
#     while lst != sorted(lst):
#         for i in range(0,len(lst)-1):
#             if lst[i] > lst[i+1]:
#                 lst[i],lst[i+1] = lst[i+1],lst[i] #不能分两行写，会刷新列表
#     else:
#         print(lst)
# if __name__ == '__main__':
#     MaoPaoSort(lst)

# #12.判断序列包含具有相同值的连续四个数字
# def isconsecutivefour():
#     num=0
#     list_=list(map(int,input('请输入一个整数序列（用逗号隔开）:').split(',')))
#     for i in range(0,len(list_)-3):
#         if list_[i]==list_[i+1]==list_[i+2]==list_[i+3]:
#             if num==0:
#                 print('这个序列包含具有相同值的连续四个数字！')
#                 num+=1
#     if num==0:
#         print('不包含！')
# if __name__ == '__main__':
#     isconsecutivefour()
