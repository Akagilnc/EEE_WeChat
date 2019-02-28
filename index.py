import werobot
from werobot.replies import ArticlesReply, Article

robot = werobot.WeRoBot(token='eeewomenbusinessacademy')


@robot.subscribe
def hello(message):
    return "Hi \n不知道你是怎么发现这个公众号的 \n不过 \n一起玩吧!"


@robot.text
def hello(message):
    if message.content.lower() in ['hello', '你好', '好', 'hi']:
        return "Hello wechat world"
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
    return "https://mp.weixin.qq.com/advanced/selfmenu?action=index&t=advanced/menu-setting&token=1153211364&lang=zh_CN"
