1.
import math
a = float(input('输入a的值'))
b = float(input('输入b的值'))
c = float(input('输入c的值'))
delta = b ** 2 - 4*a*c
if delta>0:
    x1 = -b+math.sqrt(delta)/(2*a)
    x2 = -b-math.sqrt(delta)/(2*a)
    print('x1=',x1,'x2=',x2)
elif delta == 0:
    x1=x2=-b/(2*a)
    print('x1=x2',x1)
else:
    print('The equation has no real roots')


2.
import numpy as np
num1 = np.random.randint(1,100)
num2 = np.random.randint(1,100)
print(num1,num2)
user =int(input('输入和'))
if user == num1+num2:
    print('真')
else:
    print('假')


3.
def week(day):    
    	if day == 0:
        print('星期日')
	elif day == 1:
	    print('星期一')
	elif day == 2:
	     print('星期二')
	elif day == 3:
	    print('星期三')
	elif day == 4:
	     print('星期四')
	elif day == 5:
	    print('星期五')
	elif day == 6:
	    print('星期六')
def today(day,day_1):
	day_2 = day+day_1
	if day_2>=7:
	    day_3 = (day_2)%7
	    week(day_3)
	else:
	    week(day_2)
	    
def sart():
	day = eval(input('请输入今天是哪一天：'))
	day_1 = eval(input('输入到哪天的天数'))
	week(day)
	today(day,day_1)
sart()


4.
a = int(input('输入a的值'))
b = int(input('输入b的值'))
c = int(input('输入c的值'))
num_ = [a,b,c]
num_.sort()
print(num_)


5.
price1,weight1 = map(float,input('请输入第一种重量和价钱').split())
price2,weight2 = map(float,input('请输入第二种重量和价钱').split())
if price1>price2 and weight1>weight2:
    print('第二种价钱更好')
else:
    print('第一种价钱更好')


6.
month,year = eval(input('请输入月和年：'))
if year % 4 ==0 and month==2:
    day =29
elif month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
    day =31
elif month==4 or month==6 or month==9 or month==11:
    day =30
else:
    day = 28
print(year,"年",month,"月","有",day,"天")


7.
import numpy as np
res = np.random.choice(['正面','反面'])
print(res)
user = input('用户输出')
if user == '正面' and res== '正面':
    print('你赢了')
elif user == '正面' and res== '反面':
    print('你输了')
elif user == '反面' and res== '正面':
    print('你输了')
else:
    print('你赢了')


8.
import numpy as np
res = np.random.choice(['0','1','2'])
0=='剪刀'
1=='石头'
2=='布'
print(res)
user = input('用户输出')
if user == '1' and res== '2':
    print('你输了')
elif user == '0' and res== '1':
    print('你输了')
elif user == '2' and res== '0':
    print('你输了')
elif user == res:
    print('平局')   
else:
    print('再来一局')


9.
year = int(input('请输入年：'))
m = int(input('请输入月：'))
d = int(input('请输入天：'))
week = ['周日','周一','周二','周三','周四','周五','周六']
h = int(d+((26*(m+1))//10)+(year%100)+((year%100)/4)+((year//100)/4)+5*year//100)%7
day = week[h]
if m == 1:
    m = 13
    year = year - 1
if m ==2:
    m = 14
    year = year - 1
print('那一天是一周中的:%s' %day)

10.
import numpy as np
color = np.random.choice(['梅花','方片','红桃','黑桃'])
num = np.random.choice(['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King'])
print("这张是{}{}".format(color,num))


11.
a = input('请输入一个正整数: ')
b = a[::-1]
if a==b:
    print('%s是回文数'%b)
else:
    print('%s不是回文数'%b)


12.
s1,s2,s3=map(int,input('请输入三条边长 :').split())
a = float(s1+s2)
b = float(s1+s3)
c = float(s2+s3)
if a>s3 or b>s2 or c>s1:
    C=a+b+c
    print("周长是："%C)



n=[s1,s2,s3]
n.short()
if n[2] <(n[0] + n[1]):
    print(s1+s2+s3)
else:
    print('不合法')
    

13.
x = 1
zheng = 0
fu = 0
i = 0
sum1 = 0
while x!=0:
    x = int(input('输入一个整数，以输入值0来结束：'))
    if(x>0):
        zheng += 1
    elif(x<0):
        fu += 1
    i += 1
    sum1 = sum1 + x
if sum1 != 0:
        xxx = sum1/(i-1)
        print('输入的正数有%d个，输入的负数有%d个，这组数的和为%d，这组数的平均数为%.2f'%(zheng,fu,sum1,xxx))
else:
        print('结束')


14.
money = 10000
sum1 = 0
for i in range(1,14):
    money = money * 0.05 + money
    if i ==10:
        print('十年之后的学费：%.2f'%money)
    if i >= 10: 
        sum1 += money
    print('十年后大学四年的总学费为：%.2f'%sum1)


15.
geshu = 0
for i in range(100,1001):
    if i%5 == 0 and i%6 == 0:
        print(i,end=' ')
        geshu += 1
    if geshu % 10 == 0:
        print('\n')


16.

n = 0
m = 0
while n**2 <= 12000:
        n += 1
print('n的平方大于12000的最小整数n为：%d'%n)
while m**3 < 12000:
        m += 1
print('n的立方大于12000的最大整数n为：%d'%(m-1))

17.
sum1 = 0
sum2 = 0
for i in range(1,50001):
    sum1 += 1/i
    i += 1
print('从左向右计算为：',sum1)
for i in range(50000,0,-1):
    sum2 += 1/i
    i -= 1
print('从右向左计算为：',sum2)


18.
sum1 = 0
for i in range(3,100,2):
    sum1 += (i-2)/i
print('数列的和为：',sum1) 


19.
pi = 0
i = int(input('输入i的值：'))
for j in range(1,i+1):
    pi += 4 * ((-1)**(1+j)/(2*j-1))
print('π的值为：%f'%pi)


20.
for i in range(1,10000):
    x = 0
    for j in range(1,i):
        if i % j == 0:
            x += j
    if x == i:
            print('10000以下的完全数有：%d'%x)

21.
list1 = []
for i in range(1,8):
    for j in range(1,8):
            if i != j and sorted([i,j]) not in list1:
                list1.append([i,j])
print('所有可能的组合为：',list1)
print('组合总个数为：',len(list1))
