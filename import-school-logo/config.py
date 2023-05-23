ADMIN_USERANME = "admin"  # admin 用户名
ADMIN_PASSWORD = "admin123456"  # admin 密码
DOMJUDGE_URL = "http://192.168.1.197/domjudge"  # domjudge的地址，不需要最后的“/”
CONTEST_ID = "2"  # 比赛的id，实测随便一场比赛的ID都行，DOMJUDGE为了获取所有学校信息必须有一个比赛ID
COOKIE = "domjudge_refresh=1; domjudge_submissionsfilter=%7B%7D; domjudge_submissionview=0; domjudge_refresh=1; domjudge_cid=2; domjudge_scorefilter=%5B%5D; PHPSESSID=nmksoprhcmcgn0fldu9fqth6fv"  # 使用admin账号登陆的cookie

SCHOOL_NAME_COL = 2  # 学校名字所在列
TEAM_CHINESE_NAME_COL = 3  # 队伍中文名列
TEAM_ENGLISH_NAME_COL = 4  # 队伍英文名列
TEAM_TYPE_COL = 5  # 如果是打星队，必须有“打星”两个汉字
LOCATION_COL = 8  # 位置信息所在列

PARTICIPANTS_ID = 3
OBSERVERS_ID = 4
GIRLS_ID = 7  # 女队的category id
