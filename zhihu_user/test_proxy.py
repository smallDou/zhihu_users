from os import path
import requests

file_in = path.join(path.abspath('.'),'list1.txt')
file_out = path.join(path.abspath('.'),'list.txt')

headers = {
    'Accept':
    'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language':
    'en',
    'USER-AGENT':
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
    'authorization':
    'Bearer 2|1:0|10:1523697248|4:z_c0|92:Mi4xdTlPWkFnQUFBQUFBQU1MQXhYLVREQ1lBQUFCZ0FsVk5ZQlNfV3dBbm1LVDdwS1YxR3NyaTRCMUZXaWU1Y2RsVUdB|bd3d6476b94563144e77cb7ce841f33f00ad074d940e717824b17a692f60d5c2',
}

def parse_proxy():
    for time in range(3): #跑三遍确认代理可用
        with open(file_in, 'r') as f:
            list = []
            lines = f.readlines()
            for line in lines:
                print(line.strip())
                try:
                    proxies = {'https': line.strip() }
                    response = requests.get('https://www.zhihu.com/api/v4/members/yan-jia-cheng-75?include=allow_message,is_followed,is_following,is_org,is_blocking,employments,answer_count,follower_count,articles_count,gender,badge[?(type=best_answerer)].topics',headers=headers, proxies=proxies,timeout=6)
                    if response.status_code == 200:
                        list.append(line)
                    print(list)
                except:
                    print('error')
        with open(file_in, 'w+') as f:
            for i in list:
                if 'https://' in i:
                    f.write(i)
                else:
                    f.write('https://' + i)
        time+=1

def write_file1_to_file2(file1,file2):
    with open(file1,'r+') as f1:
        with open(file2,'w+') as f2:
            for line in f1.readlines():
                f2.write(line)

def main():
    parse_proxy()
    write_file1_to_file2(file_in,file_out)

if __name__ == '__main__':
    main()