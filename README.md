# SerializeVulTest
在一次灰盒测试时发现burp发POST请求时不能正确的传输序列化过后的ysoserial的payload
参考并修改了weblogic.py，通过http post方式发送ysoserial的payload
旨在方便测试存在反序列化路由点
![image](https://user-images.githubusercontent.com/63454826/129454278-9e4f67c0-3b62-46d9-bb68-86b65e872200.png)
