# xbox download host

寻找xbox下载速度最快的hosts

## 所需环境

- Windows/Linux/MacOS
- [python3](https://www.python.org/)

## 使用方式

- Windows: 运行命令`py -3 run.py` 或直接运行 `run.bat`

- Linux/MacOS: 运行命令`python3 run.py` 或 `./run.sh`

运行之后，最佳hosts保存在`log/hosts.txt`中，速度日志保存在`log/speed.log`中

## 更新ip列表

如果`ip.list`中的ip大范围过期，可手动更新ip列表

- Windows: `py -3 update_ip_list.py`
- Linux/MacOS: `python3 update_ip_list.py`
