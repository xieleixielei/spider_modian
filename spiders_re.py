import re  # 正则表达式，进行文字匹配`
# author info
find_authorimage = re.compile(r'src="(.*?)"')
find_catagory = re.compile(r'项目类别：(.*?)<')
find_authorname =  re.compile(r'data-nickname="(.*?)"')
find_authoruid =re.compile(r'data-username="(.*?)"')
# preheat--
findsubscribe = re.compile(r'<span subscribe_count="(\d+)">(.*)</span>')
find_preheatgoal = re.compile(r'<span>(.*?)</span></h3>')
# main right
find_backheadmoney = re.compile(r'<span>(.*?)</span>')
find_backheadsponsor=re.compile(r'<em(.*?)>(.*?)</em>',re.S)
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!换行符
find_backheadsignlogo = re.compile(r'<span>(.*?)</span>')
find_backlisttilte=re.compile(r'<div class="back-sub-title">(.*?)</div>')
#
find_trueauthorid=re.compile(r'https://me.modian.com/u/detail\?uid=(\d+)')
find_fannum=re.compile(r'<i>(\d+)</i>')
find_noticenum=re.compile(r'<span>(\d+)</i>')

# add
#<span upadte_count="125632">3</span>
find_update_time_item=re.compile(r'<span upadte_count="(\d+)">(.*)</span>')
#<span comment_count="125632">187</span>
find_comment_item=re.compile(r'<span comment_count="(\d+)">(.*)</span>')
#<span backer_count="125632">676</span>
find_userlist_item=re.compile(r'<span backer_count="(\d+)">(.*)</span>')
# <span bull_count="125410">0</span>
find_idea_userlist_item=re.compile(r'<span bull_count="(\d+)">(.*)</span>')
find_collect_item=re.compile(r'<span>(.*?)</span>')