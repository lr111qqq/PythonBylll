#1.五角数
def getPentagonalNumber(n):
    for i in range(1,n+1):
        num = i * (3*i-1)/2
        print('%d'%num,end=' ')
        if i %10 ==0:
            print('\n')

getPentagonalNumber(100)

#2.求一个整数各个数字的和
def sumDigits(n):
    for _ in range(n):
            b = int(n//100)
            s = int(n/10%10)
            g = int(n%10%10)
            sum = b + s + g
    print ('各位数字之和：%d'%sum)
sumDigits(126)

#3.排序
def display(num1,num2,num3):
    list = [num1,num2,num3]
    s = sorted(list)
    print("给三位数字排序得{}".format(s))
a,b,c = map(int,input("请输入三个数字："))
display(a,b,c)


#5.
COUNT = 0
def printChars():
    global COUNT
    for i in range(49,91):
        COUNT += 1
        print(chr(i),end=" ")
        if COUNT% 10 == 0:
            print("\n")
printChars()

#6.
def numberOfDaysInAYear(year):
    for number in range(year,year+11):
        if number % 4==0 and number % 100 != 0 or number % 400 == 0:
            print("%d年有366天"%number)
        else:
            print("%d年有365天"%number)
numberOfDaysInAYear(2010)


#7.
import math
def distance(x1,x2,y1,y2):
    dis = math.sqrt((x2-x1)**2+(y2 - y1)**2)
    print("这两个点的距离是：%f"%dis)
distance(1,3,5,7)


#10.
import random
def shaizi():
    a=random.choice([1,2,3,4,5,6])
    b=random.choice([1,2,3,4,5,6])
    if a+b==2 or  a+b==3 or a+b==12:
        print('%d + %d = %d' %(a,b,a+b))
        print('你输了')
    elif a+b==7 or a+b==11:
        print('%d + %d = %d' %(a,b,a+b))
        print('你赢了')
    else:
        print('%d + %d = %d' %(a,b,a+b))
        c=random.choice([1,2,3,4,5,6])
        d=random.choice([1,2,3,4,5,6])
        if c+d==7:
            print('%d + %d = %d' %(c,d,c+d))
            print('你输了')
        elif c+d==a+b:
            print('%d + %d = %d' %(c,d,c+d))
            print('你赢了')
shaizi()

#正负数
# def main():
    num_z = 0
    num_f = 0
    sum = 0
    data = 1
    while data != 0:
        data = int(input("请输入数字："))
        if data > 0:
            num_z += 1
        elif data < 0:
            num_f +=1
        sum += data
    print("正数个数为:%d"%num_z)
    print("负数个数为:%d"%num_f)
    aver = sum / (num_z + num_f)
    print("平均值为：%2f"%aver)
main()

#未来学费
def main(money,sum1):
    for i in range(1,14):
        money = money * 0.05 + money
        if i ==10:
            print('十年之后的学费：%.2f'%money)
        if i >= 10: 
            sum1 += money
    print('十年后大学四年的总学费为：%.2f'%sum1)

def start():
    money = 10000
    sum1 = 0
    main(money,sum1)
start()

#被5和6整除的数
COUNT = 0
def main():
    global COUNT   
    for i in range(100,1000):
        if i % 5 == 0 and i % 6 == 0:
            print(i,end = ' ')
            COUNT += 1
            if COUNT % 10 ==0:
                print("\n")
           
# main()


#最大和最小的n
def main():
    n2 = 0
    n3 = 0
    while n2 ** 2 < 12000:
        n2 += 1
    print(n2)
    while n3 ** 3 < 12000:
        n3 += 1
    print(n3-1)
main()

#演示消除错误
def main():
    sum = 0
    for i in range(1,50001):
        sum += 1/i
    print(sum)
main()


#数列求和
def main():
    sum_ = 0
    for i in range(1,98,2):
        sum_ += i / (i + 2)
    print(sum_)
main()


#计算Π
def main():
    sum = 0
    for i in range(1,100000):
        sum += 4 * (-1) ** (i + 1) / (2 * i - 1)
    print(sum)
main()

#完全数
def main():
    for i in range(1,10000):
        sum = 0
        for j in range(1,i):
            if i % j ==0:
                sum += j
        if i ==sum:
            print(i)
main()


#组合
def main():
    count = 0
    list1 = []
    for i in range(1,8):
        for j in range(2,8):
            if i != j and sorted([i,j]) not in list1:
                list1.append([i,j])
                print(i,j)
                count += 1
    print(count)
main()