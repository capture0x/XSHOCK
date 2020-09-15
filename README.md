# ⚡ &nbsp;  xShock ShellShock &nbsp;  ⚡

<img src="https://i.imgur.com/PHIwqe7.png" width="60%"></img>


#### Written by Hulya Karabag 
#### Version 1.0.0
 xShock ShellShock (CVE-2014-6271) 

 This tool exploits shellshock.

Instagram: [Capture the Root](https://www.instagram.com/capturetheroot/)

## 🖼️ Screenshots 🖼️

<img src="https://i.imgur.com/lBI2Bnf.png" width="32%"></img>
<img src="https://i.imgur.com/T5AgZjX.png" width="32%"></img>
<img src="https://i.imgur.com/lyfeMxJ.png" width="32%"></img>
<img src="https://i.imgur.com/WREKK5f.png" width="32%"></img>
<img src="https://i.imgur.com/xuQuwaV.png" width="32%"></img>
<img src="https://i.imgur.com/S5RHqGP.png" width="32%"></img>

## 📹 How to use 📹
[![How to use xShock](https://i.imgur.com/MQdjJ5W.png)](https://www.youtube.com/watch?v=VXP6ZYyBPS4)

Click on the image...


## 📒 Read Me 📒

All founded directories will be saved in **vulnurl.txt** file.
The results of the executed commands are saved in response.txt.


## 🧰  Features  🧰
This tool **include:**
+ CGI VULNERABILITY 
+ DIRECTORY SCAN   
+ RUN COMMAND WITH FOUNDED CGI  
+ SHOW VULNERABLE URLS
+ UPDATE PROXY

## 📀 Installation 📀
### Installation with requirements.txt

```bash
git clone https://github.com/capture0x/xShock/
cd xShock
pip3 install -r requirements.txt
```

## Usage

```bash
python3 main.py
```


### CGI VULNERABILITY
Checks cgi-bin directory on the target site

e.g:
```
http://targetsite.com
```

### DIRECTORY SCAN

 This works with wordlists. Scans url on the target site. Important notice: Please enter full path of wordlist after the url.(Not file. It should be directory)
 
e.g: http:// targetsite.com/cgi-bin/**selectedworlist**
 
e.g:
```
http://targetsite.com/cgi-bin
/usr/share/wordlists/dirb  --> This is directory of wordlist. Not file!
```
 
 
### RUN COMMAND WITH FOUNDED CGI

By entering the url in the vuln.txt file, you can try running commands in the found urls.

```bash
http://targetsite.com/cgi-bin/status
```

### SHOW VULNERABLE URLS

Shows founded urls in vuln.txt file.

### UPDATE PROXY

You can update proxies from web manually.




## Known Issues

--

## Bugs and enhancements

For bug reports or enhancements, please open an [issue](https://github.com/capture0x/xShock/issues) here.



**Copyright 2020**
