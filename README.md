# SerializeVulTest


在一次灰盒测试时发现burp发POST请求时不能正确的传输序列化过后的ysoserial的payload

参考并修改了weblogic.py，通过http post方式发送ysoserial的payload

旨在方便测试存在反序列化的点

![image](https://user-images.githubusercontent.com/63454826/129454278-9e4f67c0-3b62-46d9-bb68-86b65e872200.png)

2021-08-26-14:54更新
1、添加：可指定ser文件，以读取序列化文件数据通过POST请求发送（需指定-m参数值为ser，-f参数值为ser文件路径）
2、添加提示信息
3、添加header头"Content-Type":"application/x-java-serialized-object"，发送POST数据时以该header发送
![image](https://user-images.githubusercontent.com/63454826/130916984-5ac0908d-f39d-4ea6-a380-1bf0ac7ba8d8.png)
