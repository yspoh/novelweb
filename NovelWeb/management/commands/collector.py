from django.core.management.base import BaseCommand, CommandError
from NovelWeb.models import title, list, rank
import requests
import datetime


class Command(BaseCommand):
    help = 'The spider for collecting info from shuapi.jiaston.com'

    def add_arguments(self, parser):
        # Named (optional) arguments
        parser.add_argument(
            '--title',
            action='store_true',
            help='Collect books info from url into title table',
        )
        parser.add_argument(
            '--list',
            action='store_true',
            help='Collect chapters from url into list table',
        )
        parser.add_argument(
            '--rank',
            action='store_true',
            help='Collect books ranking from url into rank table',
        )

    def handle(self, *args, **options):
        print('Collect Title Table')
        if options['title']:
            url = 'http://shuapi.jiaston.com/info/'
            # 小说搜索范围 601800 missing 62123 end at 162123
            for j in range(162124, 192124):
                print('Load ' + str(j) + '.html')
                i = str(j) + '.html'
                r = requests.get(url + i)
                # GET请求成功
                if (r.status_code == 200):
                    print('The connection is good')
                    r.encoding = 'UTF-8-SIG'
                    if '映射出错' in r.text:
                        print('映射出错')
                        continue
                    # data = json.loads(r.json())
                    data = r.json()
                    # 修正日期格式
                    # datestr = str()
                    # string = data['data']['LastTime']
                    # datestr = datetime.datetime.strptime(string, '%Y-%')
                    # for k in range(len(string)):
                    #     if string[k] == '/':
                    #         datestr = datestr + '-'
                    #     else:
                    #         datestr = datestr + string[k]
                    # print(datestr)
                    # 数据库数据save
                    # 检查数据中有没有图片文件名
                    if 'Img' in data['data']:
                        imagedata = data['data']['Img']
                    else:
                        imagedata = 'null.jpg'
                    if 'LastChapterId' not in data['data']:
                        continue
                    cache = title(book_id=data['data']['Id'], book_name=data['data']['Name'],
                                  status=data['data']['BookStatus'], author=data['data']['Author'],
                                  type=data['data']['CName'], info=data['data']['Desc'],
                                  last_update=data['data']['LastTime'], last_list_id=data['data']['LastChapterId'],
                                  image=imagedata)
                    cache.save()
                else:
                    print('The connection failed')
        if options['list']:
            pass
        if options['rank']:
            pass
            # with open('first.json', 'w', encoding='utf-8') as f:
            #     json.dump(r.json(), f, ensure_ascii=False)
        print(datetime.datetime.now())
        self.stdout.write(self.style.SUCCESS('Collect End'))
