from PIL import ImageGrab, Image, ImageFilter
from aip import AipOcr
from matplotlib import pyplot as plt
import webbrowser, time, os, requests, urllib.parse, platform, config, json, sys, cv2, numpy as np

# 获取电脑操作系统
pc_system = platform.system()


# 定义手机系统选择方法
def phone_system():
    system_id = input(u'1:IOS\n2:Android\n请选择手机系统,输入序号并敲回车：')
    return system_id


# 定义app选择方法
def app():
    app_id = input(u'1：冲顶大会\n2：芝士超人\n3：百万英雄\n4：百万赢家\n请选择APP,输入序号并敲回车：')
    return app_id


# 电脑截屏方法
def pcScreenImg():
    pic = ImageGrab.grab()
    pic.save('pic.png')


# Win+Android执行adb命令截屏方法
def winAndroidScreenImg():
    os.system('adb shell /system/bin/screencap -p /sdcard/screenshot.png')
    os.system('adb pull /sdcard/screenshot.png pic.png')


# Mac+ios截屏方法
def macIosScreenImg():
    import wda
    wda.Client().screenshot('pic.png')


# 截取图片问题区域方法
def saveQuestionImg(app_id):
    # 打开本地图片
    open_img = Image.open('pic.png')
    width, height = open_img.size
    # 开始截取问题区域图片
    if int(app_id) == 1:
        question_img = open_img.crop((0, int(height) * 0.2, width, int(height) * 0.38))
    elif int(app_id)==2:
        question_img = open_img.crop((0, int(height) * 0.13, width, int(height) * 0.25))
    elif int(app_id)==3:
        question_img = open_img.crop((0, int(height) * 0.13, width, int(height) * 0.25))
    elif int(app_id)==4:
        question_img = open_img.crop((0, int(height) * 0.18, width, int(height) * 0.38))
    # 保存问题区域图片
    question_img.save('question.png')


def getImgContent(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


# 百度ORC识别文字并提取
def baiduOrc():
    # 百度ORC APPID,AK,SK
    APP_ID = '10665196'
    API_KEY = 'Vzts1FQORkGMydqNyWieFdX6'
    SECRET_KEY = '43k9OGgOcj5RZOQe0KXmdmKeeKTUXonT'
    clicent = AipOcr(APP_ID, API_KEY, SECRET_KEY)

    # 读取图片内容
    question_image = getImgContent('question.png')

    # 调用通用文字识别, 图片参数为本地图片
    qusetion_image_text = clicent.basicGeneral(question_image)

    # 提取问题
    question = ''
    for i in qusetion_image_text['words_result']:
        question += i['words']

    # 过滤字符
    # 查找第一个字符‘.’，返回键值
    dot_num = question.find('.')
    if dot_num > -1:
        question = question[dot_num + 1:]
    else:
        if question[:2].isdigit():
            question = question[2:]
        elif question[:1].isdigit():
            question = question[1:]
    print(u'问题：{}'.format(question))
    return question


# 百度搜索
def baiduSearch(result):
    webbrowser.open('https://www.baidu.com/s?wd={}'.format(result))


# 阿里智能问答机器人
def aliIntelligent(qustion):
    # 定义请求参数
    host = 'http://jisuznwd.market.alicloudapi.com'
    path = '/iqa/query'
    appcode = 'e55eb7b83cfd4c129a8cc5c52ddc8f45'
    querys = 'question={}'.format(qustion)
    # 定义头部
    header = {
        'Authorization': 'APPCODE ' + appcode
    }
    # 组装请求链接
    url = host + path + '?' + querys
    # 开始请求
    result = requests.get(url, headers=header)
    # 获取返回结果
    answer = result.json()['result']['content']
    return answer


# 开始搜索
def start(system_id, app_id):
    # 判断手机操作系统调用不同的截屏方法
    # try:
    #     if int(system_id) == 1:
    #         macIosScreenImg()
    #     elif int(system_id) == 2:
    #         winAndroidScreenImg()
    # except:
    #     print(u'请配置环境并连接手机')
    #     exit()
    # 调用问题区域图片保存方法
    saveQuestionImg(app_id)
    # 调用百度文字识别方法
    question = baiduOrc()
    # 中文转义
    result = urllib.parse.quote(question)
    # 调用百度搜索方法
    baiduSearch(result)
    # 调用阿里只能问答机器人
    # answer = aliIntelligent(question)
    # print(u'阿里小智：{}'.format(answer))


# windows环境下获取键盘事件
def winPressKeybrod():
    import msvcrt
    return ord(msvcrt.getch())


# Unix环境下获取键盘事件
def unixPressKeybord():
    # 获取标准输入的描述符
    fd = sys.stdin.fileno()
    # 从终端读取
    return ord(os.read(fd, 3))


# 开始答题
def nextQuestion():
    # 获取手机操作系统
    while (True):
        system_id = phone_system()
        if int(system_id) == 1 or int(system_id) == 2:
            break
    # 获取APP
    while (True):
        app_id = app()
        if int(app_id) == 1 or int(app_id) == 2 or int(app_id) == 3 or int(app_id) == 4:
            break

    while (True):
        # 判断操作系统，获取键盘事件
        if pc_system == 'Windows':
            print(u"\nENTER 开始答题 ,ESC 结束答题:")
            key = winPressKeybrod()
            os.system('cls')
            # 判断按下的键盘执行方法
            if key == 13:  # Enter
                start(system_id, app_id)
            elif key == 27:  # Esc
                print(u'答题结束')
                break
            else:
                break
        else:
            print(u"\nENTER 开始答题 ,ESC 结束答题:")
            key = unixPressKeybord()
            os.system('clear')
            # 判断按下的键盘执行方法
            if key == 10:  # Enter
                start(system_id, app_id)
            elif key == 27:  # Esc
                print(u'答题结束')
                break
            else:
                break


nextQuestion()
