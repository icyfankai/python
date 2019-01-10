#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Thu 03 Aug 2017 07:44:05 PM CST

# File Name: login-test.py
# Description: 模拟使用MD5加密密码，用户登陆

"""

import hashlib
import json
#输入用户名密码
def input_info():
    username = raw_input("please input your username: ")
    password = raw_input("please input your password: ")
    return username, password
#注册后保存数据到json文件
def save_data(db):
    try:
        l = read_data()
        with open('login-and-register.json', 'w') as f:
            l.append(db)
            json.dump(l, f)
    except IOError:
        print "save data failed..."
    finally:
        f.close()
#从json文件中读取数据
def read_data():
    try:
        with open('login-and-register.json', 'r') as f:
            content = json.load(f)
        f.close()
        return content
    except:
        content = []
        return content
#获取用户名列表
def get_user_list():
    datalist = read_data()
    had_usernamelist = []
    for data in datalist:
        had_username = data.keys()
        had_usernamelist.append(had_username)
    return had_usernamelist

#注册过程
def register(username, password):
    check_password = raw_input("please input your password again to ensure it. Your password: ")
    while True:
        if password != check_password:
            print "password do not accordance, please input again!"
            check_password = raw_input("please input your password again to ensure it. Your password: ")
        else:
            break
    db = {}
    db[username] = calc_md5(username + password + 'kellan-salt')
    save_data(db)
#md5编码    
def calc_md5(string):
    md5 = hashlib.md5()
    md5.update(string)
    return md5.hexdigest()
#登陆过程
def login(username, password):
    had_username = get_user_list()
    data = read_data()
    users_dict = {}
    for users_dic in data:
        users_dict = dict(users_dict, **users_dic)
    userNameList = []
    for user in had_username:
        userNameList.append(user[0])
    if username in userNameList:
        md5_pass = calc_md5(username + password + 'kellan-salt')
        if users_dict[username] == md5_pass:
            return 0
        else:
            return 1
    else:
        return 2

#主程序

if __name__ == '__main__':
    print "="*30
    print "  用户登录与注册V0.1"
    print "="*30
    print "welcome to my system!"
    choose = raw_input("Please choose login[0] or register[1]: ")
    if choose == 'login' or choose == '0':
        (username, password) = input_info()
        i = 0
        flag = login(username, password)
        if flag == 0:
            print "login successful! have fun!!!"
        elif flag == 1:
#BUG:正常来说这应该有个循环，比如连续输错3次后再退出
            print "Password is ERROR!!! Please try again!"
        elif flag == 2:
            print "NOT has the user, please register!!!"
    elif choose == 'register' or choose == '1':
        (username, password) = input_info()
        register(username, password)
