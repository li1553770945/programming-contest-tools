from fabric import Connection
from typing import List
from threading import Thread,Lock
from datetime import datetime
import time
import os
PRIVATE_KEY = "id_rsa"
ADMIN_USER = "liyaning"
NORMAL_USER = "jscpc"
SUDO_PASSWORD = "123"
UNLOCK_COMMAND = {'command':"export DISPLAY=:0; gnome-screensaver; gnome-screensaver-command -d;",'user':NORMAL_USER}
LOCK_COMMAND = {'command':"export DISPLAY=:0; gnome-screensaver; gnome-screensaver-command -l;",'user':ADMIN_USER}
LOGOUT_COMMAND = {'command':"gnome-session-quit --force",'user':NORMAL_USER}
CLEAR_COMMAND = {'command':["rm -rf /tmp/*", "rm -rf /var/tmp/*", "rsync -av --delete /opt/backup/jscpc-backup/jscpc /home"],'user':ADMIN_USER}
SHUTDOWN_COMMAND = {'command':["shutdown -h now"],'user':ADMIN_USER}

COMMAND = SHUTDOWN_COMMAND


class Result:
    def __init__(self,server,success,msg):
        self.server = server
        self.success = success
        self.msg = msg


def generage_servers()->List[Connection]:
    return [f'192.168.{x}.{y}' for x in range(1,2) for y in range(103,104)]


def fun(server:str):
    conn = Connection(server,user = COMMAND['user'])
    try:
        if COMMAND['user'] == ADMIN_USER:
            for comm in COMMAND['command']:
                msg:str = str(conn.sudo(comm,hide="both",password=SUDO_PASSWORD))
        else:
            msg:str = str(conn.run(COMMAND['command'],hide="both"))
        msg = msg.replace("\n","").replace("\r","")
        result = Result(server,True,msg)
        success_lock.acquire()
        successes.append(result)
        success_lock.release()
    except Exception as err:
        msg = str(err)
        msg = msg.replace("\n","").replace("\r","")
        result = Result(server,False,msg)
        fail_lock.acquire()
        fails.append(result)
        fail_lock.release()

success_lock = Lock()
fail_lock = Lock()

successes:List[Result] = list()
fails:List[Result] = list()



if __name__ == "__main__":

    start_time = time.time()
    threads:List[Thread] = list()
    servers = generage_servers()
    for server in servers:
        t = Thread(target=fun,args=(server,))
        t.start()
        threads.append(t)
    
    for  t in threads:
        t.join()

    print(f"总数量:{len(servers)},成功数量:{len(successes)},失败数量:{len(fails)}")


    end_time = time.time()
    print(f"程序运行时间为：{end_time - start_time}秒")

    fmt_time = datetime.now().strftime("%Y-%m-%d-%H-%M-%S.txt")

    successes.sort(key=lambda x: x.server)
    fails.sort(key=lambda x: x.server)

    if not os.path.exists("log"):
        os.mkdir("log")
    with open(f"log/success-{fmt_time}","w",encoding="utf8") as f:
        f.write(f"command:{COMMAND}\n")
        for suc in successes:
            content = f"{suc.server}\n"
            f.write(content)
    
    with open(f"log/fail-{fmt_time}","w",encoding="utf8") as f:
        f.write(f"command:{COMMAND}\n")
        for fail in fails:
            content = f"{fail.server}:{fail.msg}\n"
            f.write(content)
    

