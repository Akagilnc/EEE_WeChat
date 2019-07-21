import werobot
from werobot.replies import ArticlesReply, Article, ImageReply
from werobot.client import Client
import requests, json

robot = werobot.WeRoBot(token='eeewomenbusinessacademy')
client = Client(config={
    'APP_ID': 'wx3ff24c6f361db7c0',
    'APP_SECRET': '42d3c288053541acb9a1b73da8a7b175'
})


def get_media():
    res = client.get_media_list('image', 0, 20)
    print(res)


def send_reminder():
    token = client.grant_token().get('access_token', None)
    groups = client.get_groups()
    tag_id = -1
    for group in groups['groups']:
        if group.get('name', None) == '3E_Inner':
            tag_id = group['id']
            print(tag_id)
            break
    if token:
        URL = 'https://api.weixin.qq.com/cgi-bin/user/tag/get?access_token={token}'.format(token=token)
        params = {'tagid': tag_id}
        response = requests.post(url=URL, json=params)
        if response.json()['count'] > 0:
            user_infos = client.get_users_info(response.json()['data']['openid'])['user_info_list']
            for user_info in user_infos:
                message = "亲爱的{}，这是来自ak老师的定向发送消息\n".format(user_info.get('nickname', '没有昵称的人'))
                message += '你的手机系统语言为{}, 填写的国家信息为{}, Have fun'.format(user_info['language'], user_info['country'])
                client.send_text_message(user_info['openid'], message)


@robot.subscribe
def hello(message, session):
    user_info = client.get_user_info(message.source, lang='zh_CN')
    session[message.source] = user_info
    print('subscribe', user_info)
    return '''感谢关注【3E女子商学院】3E即3要素（Three Elements）人、财、务3要素。
    【3E女子商学院】目前主要通过线下为期2个月的初创女性训练营与后期陪伴式的创业咨询、指导，以提升女性初创业者的综合能力，解决初创公司人、财、务3方面的问题。
    欢迎有志成为女老板的小伙伴加入我们，详情可私信【3E女子商学院】教务处微信服务号：17308077367。
    【3E女子商学院】2019年度初创女性训练营第05、06、07期报名即日开始，报名链接 : http://na6pe3xlrb1jajy5.mikecrm.com/q19wZQs'''


@robot.unsubscribe
def goodbye(message, session):
    print('unsubscribe', session.get(message.source, 'subscribed before 2019.3.12'))
    return 'success'


@robot.location
@robot.location_event
def location():
    return 'success'


@robot.text
def hello(message):
    print(message.content)
    if message.content.lower() in ['hello', '你好', '好', 'hi']:
        return "Hello, 欢迎来到【3E女子商学院】的世界"
    if message.content.lower() in ['ak', '猩猩', '李胖娃', '胖娃', '胖娃儿']:
        return "{} loves Winnie".format(message.content)
    if message.content.lower() in ['课表', 'kebiao', '课程表', '日程']:
        reply = ArticlesReply(message=message)
        article = Article(title="课表",
                          description="3E女子商学院课表",
                          img='''https://github.com/Akagilnc/Landing_Page_3EWBS/blob/master/img/3e_logo.jpeg?raw=true''',
                          url='''http://www.3ewbs.com/class_schedule.html''')
        reply.add_article(article)
        return reply
    if message.content.lower() in ['location', '地点', '教室']:
        reply = ImageReply(message=message, media_id='CVHC0-1CfQ0wxmPCoRJIMTg2kUalhmdPYsIfbDwBrfQ')
        return reply
    return "主人正在努力挖土烧砖盖楼 \n内容很快就来 \n不要着急 \n休息 \n休息一下"


@robot.key_click("menu1")
def menu1(message):
    reply = ArticlesReply(message=message)
    article = Article(title="胡说八道",
                      description="找个树洞 打着胡说八道的名义 说那些只能、只敢、只想在梦里说的话",
                      img='''https://mmbiz.qpic.cn/mmbiz_jpg/RnMhjm9oqzBG3
                      PcfuXDcxOdd9BhUBKibIMXDdOicU0sEKa1tYy1JOFsGu3icG73Xh4p0zSgicXP6zKJ5JWPPO5BLKQ/0?wx_fmt=jpeg''',
                      url='''https://mp.weixin.qq.com/advanced/selfmenu?action=index&t=advanced
                      /menu-setting&token=1153211364&lang=zh_CN''')
    reply.add_article(article)
    return reply
