import demo01

if __name__ == '__main__':
    url = input("请输入要扫描的url:")
    # 调用 get_url 方法
    mulu = demo01.Dict(url=url, dict_list="dict.txt")
    mulu.get_url()

