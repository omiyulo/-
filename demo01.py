import exrex
import requests


class Dict:
    def __init__(self, url, dict_list="dict.txt"):
        self.url = url
        self.dict_list = dict_list

    def get_txt_contents(self):
        with open(f"{self.dict_list}", "r") as f:
            # 去除\n换行方法
            new_dict_list = f.read().splitlines()
            return new_dict_list

    def add_url(self):
        new_dict_list = self.get_txt_contents()
        new_url_list = [f"{self.url}/{value}" for value in new_dict_list]
        return new_url_list

    def get_new_url(self):
        # 这里返回的是一个 URL 列表，不是单个 URL
        return self.add_url()

    def get_url(self):
        new_url_list = self.get_new_url()
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
        }
        for new_url in new_url_list:
            r = requests.get(url=new_url, headers=headers)
            # 判断状态码
            if r.status_code == 200:
                with open("successful_url.txt", "a") as f:
                    f.write(new_url + "\n")
                print("{} 请求成功".format(new_url))
            else:
                with open("default_url.txt", "a") as f:
                    f.write(new_url + "\n")
                print("{} 请求失败".format(new_url))


# 创建 Dict 类的实例并传入 URL
# my_dict = Dict("http://www.EyouCMS.com")
# 调用 get_url 方法
# my_dict.get_url()

