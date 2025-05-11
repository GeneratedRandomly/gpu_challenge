## glibc 版本过低无法使用 popcorn-cli 的解法：
新建一个文件夹，暂存 glibc  
**如要让新版 glibc 覆盖旧版，务必保存系统快照**
~~~bash
# 下载 glibc 源码
wget http://ftp.gnu.org/gnu/libc/glibc-2.39.tar.gz
# 解压
tar -xvzf glibc-2.39.tar.gz
cd glibc-2.39
# 创建构建目录
mkdir build
cd build
# 新开一个 opt 处的 glibc
# 以免覆盖原有 glibc 导致系统崩溃
# 可能会缺少 bison，下好再重新执行
../configure --prefix=/opt/glibc-2.39
make -j$(nproc)
sudo make install
~~~
运行 popcorn-cli时的命令：
~~~bash
/opt/glibc-2.39/lib/ld-linux-x86-64.so.2 --library-path /opt/glibc-2.39/lib:/usr/lib/x86_64-linux-gnu ./popcorn-cli
~~~
这时会显示
~~~
POPCORN_API_URL is not set. Please set it to the URL of the Popcorn API.
~~~
然后照着[popcorn-cli](https://github.com/gpu-mode/popcorn-cli)所说的做即可。凡是 `popcorn-cli` 命令，都要写成
~~~bash
/opt/glibc-2.39/lib/ld-linux-x86-64.so.2 --library-path /opt/glibc-2.39/lib:/usr/lib/x86_64-linux-gnu ./popcorn-cli
~~~
## 提交
如果是按照上述流程，python3 commit.py -t moe或fp8或id即可。