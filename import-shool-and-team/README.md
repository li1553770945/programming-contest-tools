# domjudge 导入队伍

由于用文件导入队伍和用户一直失败，队伍和账号匹配不上，另外导入队伍无法添加座位号，所以写了个简单的脚本模拟浏览器行为添加。需要将teams.xlsx放置在data目录下。请确保xlsx中的内容均为值而不是公式。



### 修改config.py中的内容

+ DOMJUDGE_URL = "http://192.168.1.197/domjudge"  # domjudge的地址，不需要最后的“/”
+ COOKIE = "XXX"  # 使用admin账号登陆的cookie
+ SCHOOL_NAME_COL = 2  # 学校名字所在列

## add-team-and-user

添加队伍和用户。 

## add-schools

添加学校。

## delete

批量删除。具体用法直接看代码，很简单。

## print-account

打印密码条。需要在domjudge中选择“Generate passwords“，生成"accounts.tsv"放到data目录下。


