#### 1. 用途

* find_keyword.py 给定源码目录，文件扩展名，关键词，获取匹配的文件，提供给开发同学定位关键词被引用的文件

* scan_file.py 给定二进制文件，扫描其私有API/Class引用情况，扫描特定文件中的私有API、Class引用情况


#### 2. 使用说明

1. 首先创建 python3.5.2的环境venv
2. `source venv/bin/activate` 激活python环境
3. `pip install -r req.txt` 安装依赖


* find_keyword.py

```
python find_keyword.py /tmp/ios_check/ENTMOBILE-IOS_7.7.0_REVIEW6 .a UI
在以下文件strings中匹配到关键词 UI
...

```


* scan_file.py (耗时与文件大小有关，一般3分钟左右)

```
python scan_file.py /tmp/ios_check/Payload/YYMobile.app/YYMobile
```

