docker build -t offkeysite .

docker run -it --rm -p 8080:80 -v `pwd`:/workspace offkeysite /bin/bash
