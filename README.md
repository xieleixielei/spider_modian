注：本仓库爬取信息仅用以研究用途，作者为爬虫初学者，代码不良之处可依需修改
## spider_modian


这是一个用于爬取摩点众筹网站数据的爬虫，采用Python语言编写。求star:dizzy::dizzy::dizzy:
### 安装
1.下载代码：git clone https://github.com/xieleixielei/spider_modian.git

2.进入项目目录：cd spider_modian


### 使用
1.安装依赖所需要的包：
如：
- urllib3
- requests
- bs4
- re
- xlwt

2.运行main.py文件：
python main.py
爬取的数据将会保存在excel中。

3.数据内容
| 列名 | 描述 |
| --- | --- |
| 序号 | 数据行的序号 |
| 项目link | 项目的链接 |
| 项目6位id | 项目的6位id |
| 项目名称 | 项目的名称 |
| 项目图 | 项目的图片 |
| 开始时间 | 项目的开始时间 |
| 结束时间 | 项目的结束时间 |
| 项目结果 | 项目的结果 |
| 用户主页 | 用户的主页链接 |
| 用户头像 | 用户的头像图片 |
| 分类 | 项目的分类 |
| 用户名 | 用户的用户名 |
| 项目id | 项目的id |
| 已筹金额 | 项目已筹集的金额 |
| 百分比 | 项目已筹集金额与目标金额的百分比 |
| 目标金额 | 项目的目标金额 |
| 支持者 | 项目的支持者数量 |
| uid | 用户的uid |
| 粉丝数 | 用户的粉丝数量 |
| 关注数 | 用户的关注数量 |
| 赞数 | 用户的赞数量 |
| 发起人信息列表 | 项目发起人的信息列表 |
| 发起人发起项目信息 | 项目发起人的发起项目信息 |
| 发起人详细主页 | 项目发起人的详细主页链接 |
| 回报列表信息-标题-限量-金额-标签-数量-内容 | 项目回报列表的信息，包括标题、限量、金额、标签、数量和内容 |
| 回报列表项目数 | 项目回报列表的项目数 |
| 项目更新数 | 项目的更新数 |
| 评论数 | 项目的评论数 |
| 项目支持者列表人数 | 项目支持者列表的人数 |
| 收藏数 | 项目的收藏数 |
| 项目详情-图片数量 | 项目详情中的图片数量 |
| 项目详情-图片 | 项目详情中的图片 |
| 项目详情-视频数量 | 项目详情中的视频数量 |
| 项目详情-视频 | 项目详情中的视频 |

### 注意事项
- 请勿滥用该爬虫，遵守相关法律法规。
- 请勿将该爬虫用于商业用途。
- 该爬虫仅供学习和研究使用。
- 请注意网站的robots.txt文件，遵守网站的爬虫协议。
- 如有需要，您可以修改代码中的请求头信息和请求延迟时间，以避免被网站屏蔽。
### 贡献
欢迎大家一起来完善这个爬虫，如果您发现了任何问题或者有任何建议，请提交issue或者pull request。

###  许可证
该项目采用MIT许可证。
