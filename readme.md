# BUCT-JailBreak-Applier

基于 Python3 的适用于北京化工大学的备案制出校（俗称刷脸出校）申请 Demo 脚本  
项目用于学习交流，非必要不出校！！！

## 使用方式

1. 在企业微信进入 `校园通行-通行申请-学生申请` 页面，抓包获得 `cookies`
2. 根据 `cookies` 修改 `report.py` 内的 `PHPSESSID` 字段  
3. 填写 `payload` 字段内容
4. 安装所需依赖：`pip3 install -r requirements.txt` （Windows下请用命令提示符输入，报错请检查PATH；Linux在shell直接打就行）  

>>`若提示'pip' 不是内部或外部命令，也不是可运行的程序或批处理文件，请加入PATH`具体可参考[CSDN博客](https://blog.csdn.net/AlbenXie/article/details/79054409)

5. 执行 `main.py`  
6. 查看返回结果，若备案成功，结果将会于企业微信内的 `平安北化` 应用内返回

## 抓包方法

### 抓包方法视频教程 [BiliBili](https://www.bilibili.com/video/BV1bC4y147Pj) [Youtube](https://www.youtube.com/watch?v=oAiY4iCu9Kk)


因本URL仅使用http协议，故可以直接使用 `Fiddler` + `企业微信` 进行抓包获得 `cookies` 


