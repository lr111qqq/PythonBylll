#1.
# C = float(input('请输入一个摄氏温度：'))
# F = float(C * 1.8 +32)
# print('%.2f' %F)


#2.
# import math
# radius = float(input('请输入圆柱的半径：'))
# height= float(input('请输入圆柱的高：'))
# area = radius * radius * math.pi
# volume = area * height
# print('%.2f,%.2f' %(area , volume))


#3.
# feet = float(input('请输入英尺：'))
# meters = feet * 0.305
# print('%.1f feet is %.4f meters'%(feet,meters))


#4.
# M = float(input('请输入按千克计算的水量：'))
# initialTemperature = float(input('请输入水的初始温度：'))
# finalTemperature = float(input('请输入水的最终温度：'))
# Q = M * (finalTemperature - initialTemperature) * 4184
# print('所需能量:%.1f' %Q)


#5.
# balance = float(input('请输入差额：'))
# interest_rate = float(input('请输入年利率：'))
# insterest = balance * (interest_rate / 1200)
# print('下月需付利息:%.5f' %insterest)


#6.
# v0 = float(input('请输入初速度：'))
# v1 = float(input('请输入末速度：'))
# t = float(input('请输入时间：'))
# a = (v1 - v0) / t
# print('平均加速度是:%.4f'%a)


#7.
# num = float(input('请输入每月存款数：'))
# rate = 0.05 / 12
# interest = 1 + rate
# count =[0]
# for i in range(6):
#     month = (100 + count[i]) * interest
#     count.append(month)
# print('六个月后的账户总额：%.2f' % count[6])


#8.
# num = int(input('请输入1-1000的一个整数：'))
# b = int(num//100)
# s = int(num/10%10)
# g = int(num%10%10)
# sum = b + s + g
# print ('各位数字之和：',sum)


#9.
# import math
# r = float(input('请输入顶点到中心的距离：'))
# s = 2 * r *math.sin(math.pi/5)
# area = 5 * s * s /(4*math.tan(math.pi/5))
# print('五边形的面积: %.2f'%area)


#10.
# import math
# s = float(input('请输入边长：'))
# area = 5 * s * s /(4*math.tan(math.pi/5))
# print('五角形的面积:%f' %area)


#11.
# year = int(input('请输入一个年份：'))
# if (year % 4==0 and year % 100 != 0) or (year % 400 == 0):
#     print('%d 是闰年'%year)
# else:
#     print('%d 不是闰年'%year)


#12.
# a = 'huahua ia a cat'
# print('hu' in a)
# print('huisa' in a)


#13.
# email = '111@qq.com'
# for m in email:
#     o = ord(m) -10
#     print(chr(o),end=(""))


#14.
# num1 = int(input('请输入：'))
# num2 = int(input('请输入'))
# print(num1 - num2)


#15.
# import math
# x1,y1 = eval(input('Please input point1(latitude and longitude) in degrees:'))
# x2,y2 = eval(input('Please input point2(latitude and longitude) in degrees:'))
# radius = 6371.01
# x11 = math.radians(x1)    #math.radians()函数将度数转换成弧度数
# y11 = math.radians(y1)
# x22 = math.radians(x2)
# y22 = math.radians(y2)
# d = radius * math.acos(math.sin(x11) * math.sin(x22) + math.cos(x11) * math.cos(x22) * math.cos(y11-y22))
# print('The distance between the two points is %5.2f km'%d)


#16.
# a = eval(input('请输入一个ASCII码值'))
# b = chr(a)
# print('The character is:',b)


#17.
# 将输入的邮箱进行加密使用ASCII.
#1. for i in a:
#print(i)
#2. ord()
#3. chr()
#进阶:python使用md5.
# import hashlib
# email = ‘34567@123.com’
# m = hashlib.md5()
# b = email.encode(encoding=‘utf-8’)
# m.update(b)
# email_md5 = m.hexdigest()
# print(‘md5加密前为：’ + email)
# print(‘md5加密后为：’ + email_md5)


#18.
# num = input('请输入一个四位整数')
# print(num[ : : -1])


#19.
# name = input('Please input employee’s name:')
# hours = eval(input('Please input number of hours worked in a week:'))
# PayRate = eval(input('Please input hourly pay rate:'))
# federalRate = eval(input('Please input federal tax withholding rate:'))
# stateRate = eval(input('Please input state tax withholding rate:'))
# Federal = hours * PayRate * federalRate
# State = hours * PayRate * stateRate
# Gross = hours * PayRate
# NetPay = hours * PayRate - Federal - State
# Total = Federal + State
# print('Employee Name:',name)
# print('Hours Worked:',hours)
# print('Pay Rate:',PayRate)
# print('GrossPay:',Gross)
# print('Deductions:')
# print("\tFederal withholding (20.0%):KaTeX parse error: Expected 'EOF'", got \tState at 
# position 19: …ederal)
# print('\̲t̲S̲t̲a̲t̲e̲ ̲withholding (9.…',State)
# print('\tTotal Deduction:',Total)print('NetPay:',Total)


#20.
# import math
# radius = float(input('请输入圆的半径: '))
# perimeter = 2 * math.pi * radius
# area = math.pi * radius * radius
# print('周长: %.2f' % perimeter)
# print('面积: %.2f' % area)


#21.
# import math
# (x1,y1,x2,y2,x3,y3)= eval(input('Please input three point for a triangle:'))
# side1 = math.sqrt((x1-x2)**2+(y1-y2)**2)
# side2 = math.sqrt((x1-x3)**2+(y1-y3)**2)
# side3 = math.sqrt((x2-x3)**2+(y2-y3)*2)
# s = (side1+side2+side3)/2
# area = math.sqrt(s(s - side1)(s - side2)(s - side3))
# print('The area of the triangle is %.2f'%area)


#22.
# number = input('请输入一个数字：')
# b = int(number[0])
# s = int(number[1])
# g = int(number[2])
# if b **3 + s **3 + g **3 == int(number):
#     print('是水仙花数')
# else:
#     print('不是水仙花数')

#23.
# import math
# s = float(input('请输入边长'))
# n = float(input('请输入边数：'))
# area = n * s * s /(4*math.tan(math.pi/n))
# print('正多边形的面积:%f' %area)


