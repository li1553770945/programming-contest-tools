import os
import requests
from requests.auth import HTTPBasicAuth
from config.config import *

schools = list()
school_max_id = 1000


def get_exists_schools():
    url = f"{DOMJUDGE_URL}/api/contests/{CONTEST_ID}/organizations"
    res = requests.get(url, auth=HTTPBasicAuth(ADMIN_USERANME, ADMIN_PASSWORD))
    for school in res.json():
        schools.append({"id": school['id'], "name": school['name']})
    print(schools)


def find_school(name):
    for school in schools:
        if school["name"] == name:
            return school
    return None


def upload_logo(school_id, file_name):
    url = f"{DOMJUDGE_URL}/api/contests/{CONTEST_ID}/organizations/{school_id}/logo"
    with open(file_name, "rb") as file:
        files = {"logo": file}  # 构建文件字典，键名可以根据需求自定义
        response = requests.post(url, auth=HTTPBasicAuth(ADMIN_USERANME, ADMIN_PASSWORD), files=files)
        if response.status_code != 204:
            print(f"上传失败：{response.status_code},{response.text}")
        else:
            print(f"上传成功{file_name}")


def read_files(dir_name):
    files = os.listdir(dir_name)
    for filename in files:
        basename, extension = os.path.splitext(filename)
        basename = basename.replace(" ","")
        school = find_school(basename)
        if school is None:
            print(f"warning:domjudge无法找到学校:{basename}")
            continue
        print(f"正准备上传{basename}")
        upload_logo(school['id'], os.path.join(dir_name, filename))


if __name__ == "__main__":
    get_exists_schools()

    read_files("../data/logos")
