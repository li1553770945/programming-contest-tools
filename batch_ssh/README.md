## 一些批量管理ubuntu的命令
为了方便偏批量管理选手机器，写了个python脚本

### 准备
1. 修改一些变量：

PRIVATE_KEY = 私钥文件的路径

ADMIN_USER = 具有root权限的用户名，注意只要具有root权限，其命令就会以sudo执行

NORMAL_USER = 普通用户的用户名

SUDO_PASSWORD = sudo用户的密码

2. 保与私钥对应的公钥已被添加进目标主机。

3. 修改generage_servers()函数，生成需要控制的ip地址。

### 使用

修改COMMAND=XX，为你要执行的命令，直接运行，main.py即可。

### 目前支持的功能

1. 锁定所有设备
2. 解锁所有设备
3. 关机
4. 登出
5. 清楚用户的home目录（需要先用sudo rsync -av --delete /home/jscpc /opt/backup/jscpc-backup）备份其中jscpc是用户名。
