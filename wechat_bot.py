import itchat
import time
import random

message1 = '''2019年6月14日(本周五)，晚上有个短视频营销的课，感兴趣朋友可以扫描下方图片中的二维码👇👇
​时间:周五晚上19:00-22:00
地点:​九方文轩BOOKS(成都市府城大道中段88号九方购物中心负一楼)'''

message2 = '''亲爱的{name}

您之前填写的报名表我们已经收到，前期也沟通过。【3E女子商学院】第6期创业女性训练营还有2天就截止报名了。第6期的开营时间是6月15日，为期两个月。我们还有一些细节上的问题需要与你线上沟通一下，请问您这边什么时候比较方便呢？
'''


def start():
    itchat.auto_login(hotReload=True)
    friends_list = get_friend_list_by_tag('学员')
    send_messages(friends_list, message1)
    # friends_list = get_friend_list_by_tag('报名')
    # send_messages(friends_list, message2)
    # itchat.run()


def send_messages(input_list, message):
    for friend in input_list:
        name = get_name(friend['RemarkName'])
        print(name)
        if name == -1:
            continue
        itchat.send(message.format(name=name), friend['UserName'])
        time.sleep(0.5 + random.random() * 2)
        itchat.send_image('./images/event1.jpeg', toUserName=friend['UserName'])
        print(message.format(name=name), friend['UserName'],
              str(input_list.index(friend) + 1) + '/' + str(len(input_list)))
        time.sleep(1+random.random()*2)


def get_name(input_name):
    index_en, index_cn = input_name.find('('), input_name.find('（')
    index = index_en if index_en != -1 else index_cn
    if index != -1:
        return input_name[:index].strip()
    return -1


def get_friend_list_by_tag(input_tag):
    friend_list = itchat.get_friends(update=True)[1:]
    tag = '#' + input_tag
    friend_list_with_tag = []
    for friend in friend_list:
        name = friend['RemarkName'] or friend['NickName']
        if tag in name:
            friend_list_with_tag.append(friend)

    return friend_list_with_tag


@itchat.msg_register(itchat.content.TEXT)
def chat_reply(msg):
    text = msg.text.lower().strip()
    return "Hello {}, 你刚说的是'{}', 很高兴见到你".format(msg.user.nickName, text)


@itchat.msg_register(itchat.content.FRIENDS)
def friend_request(request):
    user = request.user
    user.verify()
    user.send("Hello {}, 很高兴认识你".format(user.nickName))


def invite_to_group(room_name, friend):
    itchat.get_chatrooms(update=True)
    chat_room = itchat.search_chatrooms(room_name)[0]
    r = itchat.add_member_into_chatroom(chat_room['UserName'], [friend], useInvitation=True)
    if r['BaseResponse']['ErrMsg'] == '请求成功':
        return '自动邀请加入群聊成功！请等待获取加群链接！'
    else:
        return '请求发生错误，请重试！'


if __name__ == '__main__':
    start()
