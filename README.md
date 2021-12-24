# terminal-translate
# 将终端程序的错误提示信息进行翻译，如编译器错误提示。<br/>
# Translate the error message of the terminal program, such as the compiler error message<br/>
# 计算机的世界不应只有英文<br/>
# The world of computers should not only have English<br/>
Translate the error message of the terminal program, such as the compiler error message.<br/>
在这里修改要翻译为何种语言。<br/>
Modify the language to be translated here.<br/>
![image](https://user-images.githubusercontent.com/96619734/147350001-0a03e3b5-7701-42fe-9f4f-ee14ca62404f.png)<br/>
这样使用<br/>
Use like this<br/>
![image](https://user-images.githubusercontent.com/96619734/147350280-c8e25fbc-9a48-439e-bb1c-c812fb7dfb4b.png)<br/>
在参数 -i 后面添加要翻译的命令<br/>
Add the command to be translated after the parameter -i<br/>
可交互翻译<br/>
Interactive translation<br/>
![image](https://user-images.githubusercontent.com/96619734/147350509-e7b6fc22-431a-44a3-b5ff-418c23c90a58.png)<br/>
![image](https://user-images.githubusercontent.com/96619734/147350638-74651b8a-bc9c-4290-8549-32f913f975c5.png)<br/>
只要是错误提示信息，都可翻译，如需全部翻译，在这里的输出后添加以下代码。<br/>
As long as it is an error message, it can be translated. If you need to translate all of it, add it after the output here.<br/>
print(Fore.RED + bin.fanyi(a) + Style.RESET_ALL)<br/>
![image](https://user-images.githubusercontent.com/96619734/147350754-4eba8e8c-dd9c-4f57-8207-baa7a37a1b44.png)<br/>
![image](https://user-images.githubusercontent.com/96619734/147350808-15cabec6-4db1-46ba-828b-a238147ead9c.png)<br/>
已打包可执行文件。<br/>
The executable file has been packaged.<br/>
