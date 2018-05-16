#!/usr/bin/env python
# -*- coding:utf-8 -*-
#coding:utf-8
"""
  Author:   --hong
  Purpose:  登录接口
  Created: 2018/5/16
"""
"""
账户文件account_user.txt内容如下：
Tamir　　123
test1　　123
test2　　123
test3　　123
"""
import os,sys,getpass   #导入os,sys,getpass 模块
i = 0   #循环次数
while i < 3:    #用户不超过3次就继续循环
    username = input("请输入你的用户名: ")     #使用input 让用户输入并赋值给username变量
    lock_file = open('account_lock.txt','r')   #打开account_lock文件(初始为空值)，权限是读取更新，并赋值给lock_f变量
    lock_list = lock_file.readlines()   #使用.readlines的方法逐行读取account_lock文件，并赋值给lock_list变量
    for lock_line in lock_list:
        lock_line = lock_line.strip('\n')
        if username == lock_line:
            print('用户 %s 已经锁定，请联系您的系统管理员'%username)
            sys.exit(1) #跳出循环
    user_file = open('account_user.txt','r')    #打开account_user文件，权限是读取更新，并赋值给user_f变量
    user_list = user_file.readlines()   #使用.readlines的方法逐行读取account_user文件，并赋值给user_list变量
    for user_line in user_list:
        (user,password) = user_line.strip('\n').split()    #分别获取账号和密码信息
        if username == user:
            j = 0
            while j < 3 :   #输入不超过三次的密码
                user_password = getpass.getpass("请输入您的密码：")  #输入密码 getpass密码不显示
                if user_password == password:
                    print('欢迎 %s 登录系统' %username)   #密码对，欢迎登录
                    sys.exit(0) #跳出循环
                else:
                    if j != 2 :
                        print('对不起，%s 的密码错误，请重新输入，您还有 %d 次机会'%(username,2 - j)) #输入错误，提示多少次机会
                j += 1  #计数器+1
            else:
                with open("account_lock.txt","w") as lock_file:
                    lock_file.write('%s \n' %username)    #用户名密码输入次数超过3次的用户添加到account_lock文件中
                    sys.exit('对不起 %s 用户已经锁定，请联系管理员'% username)
        else:
            pass    #当用户没匹配时，跳过并继续循环
    else:
        if i != 2:  #i=2时，是最后一次机会，不用在提示还剩余0次机会了
            print('对不起，%s 输入错误，请重新输入，您还有 %d 次机会' %(username, 2 - i))
    i += 1 #循环值增加1
else:
    sys.exit('因为您的错误输入，程序已经退出，请重新运行')   #用户输入三次错误后，异常退出
lock_file.close()          #关闭lock_f文件
