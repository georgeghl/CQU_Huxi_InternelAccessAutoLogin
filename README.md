# CQU_Huxi_InternetAccessAutoLogin

**A simple python script for Chongqing University Huxi Campus Internet access automatic login.**

## Usage(Pre-compiled exe):

### 1.Download and extract the zip file. 

Put the program to a directory you want.

### 2.Get your username and password using Chrome or Edge

**If you don't want to use Devtools to get the login link, you can also directly modify the username, password, ip address and mac address in the json file. Just skip step 1 and begin at step2.**

**Step1.** Go to the login page `10.254.7.4` and open the devtools by pressing `F12` key. Then enter your username and password and press OK. Find and copy your `Request site` link like this:

<img src=".\pics\1.png" alt="1" style="zoom:90%;" />

**Step2** Open `account.json` and paste your link after `"accountUrl"`. You can also modify the value `"sleepTime"` here to specify the time to check the network status and try to login again each time.

**Notice: Do not forget to save the file after modified.**

```json
{
    "accountName" : "Guest",
    "accountUrl" : "http://10.254.7.4:801/eportal/portal/login?callback=dr1004&login_method=1&user_account=,0,20000000&user_password=20000000&wlan_user_ip=10.0.0.1&wlan_user_ipv6=&wlan_user_mac=ffffffffffff&wlan_ac_ip=&wlan_ac_name=&jsVersion=4.2&terminal_type=1&lang=zh-cn&v=1891&lang=zh",
    "sleepTime" : 5
}
```

### 3.Run

Run `HuxiInternet.exe`.

**(Alternative)** If you want your Windows system run the script after system logged in, press`Win+R` and enter:`shell:startup`. Then copy the Shortcut of `HuxiInternet.exe` to here.



## Usage(python script):

### 1. Install requirements

run `installRequirements.bat`(Windows) or `installRequirements.sh`(Linux) to install the required packages.

### 2.The same step as "Usage(Pre-compiled exe)"-2.

### 3.Start

Run `start.bat`(Windows) or `start.bat`(Linux). It will check and login automatically.

**(Alternative)** If you want your Windows system run the script after system logged in, press`Win+R` and enter:`shell:startup`. Then copy the Shortcut of `start.bat` to here.









# (中文)CQU_Huxi_InternetAccessAutoLogin

**一个简单的重庆大学虎溪校区上网自动登录python脚本**

## 用法（预编译exe）：

### 1. 下载并解压缩 zip 文件。

把程序放到你想要的目录下。

### 2.使用 Chrome 或 Edge 获取用户名和密码

**如果不想使用Devtools获取登录链接，也可以直接修改json文件中的用户名、密码、ip地址和mac地址。 只需跳过第 1 步并从第 2 步开始。**

**第 1 步。** 转到登录页面`10.254.7.4`，然后按`F12`键打开开发工具。 然后输入您的用户名和密码，然后按确定。 查找并复制您的“请求站点”链接，如下所示：

<img src=".\pics\1.png" alt="1" style="缩放:90%;" />

**第 2 步** 打开 `account.json` 并将您的链接粘贴到 `"accountUrl"` 之后。 您也可以在这里修改值`"sleepTime"`来指定每次检查网络状态并尝试重新登录的时间。

**注意：修改后不要忘记保存文件。**

```json
{
    "accountName" : "Guest",
    "accountUrl" : "http://10.254.7.4:801/eportal/portal/login?callback=dr1004&login_method=1&user_account=,0,20000000&user_password=20000000&wlan_user_ip=10.0.0.1&wlan_user_ipv6=&wlan_user_mac=ffffffffffff&wlan_ac_ip=&wlan_ac_name=&jsVersion=4.2&terminal_type=1&lang=zh-cn&v=1891&lang=zh",
    "sleepTime" : 5
}
```

### 3.运行

运行 `HuxiInternet.exe`。

**（可选）** 如果您希望 Windows 系统在系统登录后运行脚本，请按 `Win+R` 并输入：`shell:startup`。 然后将`HuxiInternet.exe`的快捷方式复制到这里。



## 用法（python 脚本）：

### 1. 安装要求

运行 `installRequirements.bat`(Windows) 或 `installRequirements.sh`(Linux) 安装所需的包。

### 2.与“用法（预编译exe）”-2相同的步骤。

### 3.开始

运行 `start.bat` (Windows) 或 `start.bat` (Linux)。 它将自动检查并登录。

**（可选）** 如果您希望 Windows 系统在系统登录后运行脚本，请按 `Win+R` 并输入：`shell:startup`。 然后将`start.bat`的快捷方式复制到这里。