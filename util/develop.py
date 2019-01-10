from spider.HtmlPraser import Html_Parser
from spider.HtmlDownloader import Html_Downloader


def developParser():
    '''
    规则开发例子
    '''

    test_parser = {
        'webname':'佛山市人民政府门户网站',
        'urls': ['http://www.foshan.gov.cn/'],
        'type': 'regular',
        'pattern': r"<li class=[\s\S]*?href='([\s\S]*?)' title='([\s\S]*?)'[\s\S]*?([0-9]{4}-[0-9]{2}-[0-9]{2})",
        'position': {'title':1,'href':0,'time':2}
        }
    html_parser = Html_Parser()
    r = Html_Downloader.download(test_parser['urls'][0])
    print(r)
    info_list,info_node = html_parser.parse(r,test_parser)
    for infoList in info_list:
        print(infoList)
    print('=============')
    for infoNode in info_node:
        print(infoNode)


if __name__ == '__test__':
    import sys
    sys.path.append(r'C:\Users\dalaomai\Source\Accurate_recommendation\ProjectSourceCode\InFoPool')
    from util import develop
    from imp import reload
    reload(develop)
    from util.develop import developParser
    developParser()