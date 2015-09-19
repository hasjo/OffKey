docker build -t offkeysite .

docker run -it --rm -p 80:80 -v `pwd`:/workspace offkeysite /bin/bash
