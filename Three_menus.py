#!/usr/bin/env python
#coding:utf-8
"""
  Author:   --hong
  Purpose: 三级菜单
  Created: 2018/5/16
"""
data = {
    "北京":{
        "东城区":{
            "安定门":["国子监大街","孔庙","钟楼"],
            "建国门":["Jinbaojie","长安街","西街"],
            "朝阳门":["东四南大街","朝阳门内大街","孚王府"]
            },
        "朝阳区":{
            "和平街":["胜古庄社区","樱花社区","和平东街社区"],
            "八里庄":["慈寿寺塔","定慧寺"],
            "三里屯":["798艺术区","北京工人体育馆"]
        },
        "海淀":{}
    },
    '山东':{
        "德州":{},
        "青岛":{},
        "济南":{}
    },
    '广东':{
        "东莞":{},
        "常熟":{},
        "佛山":{}
    }
}

exit_flag = False   #循环标记
while not exit_flag:
    for i in data:  #打印第一层
        print(i)

    choice = input("选择进入-->:")  #第一层输入
    if choice in data:
        while not exit_flag:
            for i2 in data[choice]: #打印第二层
                print("\t",i2)
            choice2 = input("选择进入2-->:")    #第二层输入
            if choice2 in data[choice]:
                while not exit_flag:
                    for i3 in data[choice][choice2]:    #打印第三层
                        print("\t\t",i3)
                    choice3 = input("选择进入3-->:")    #第三层输入
                    if choice3 in data[choice][choice2]:
                        while not exit_flag:
                            for i4 in data[choice][choice2][choice3]:   #打印第四层
                                print("\t\t\t",i4)
                            choice4 = input("最后一层，按b返回,q退出-->:")    #第四层输入按b返回,q退出
                            if choice4 == "b":
                                break
                            elif choice4 == "q":
                                exit_flag = True
                    if choice3 == "b":
                        break
                    elif choice3 == "q":
                        exit_flag = True
            if choice2 == "b":
                break
            elif choice2 == "q":
                exit_flag = True
    if choice == 'b':
        break
    elif choice == 'q':
        exit_flag = True
