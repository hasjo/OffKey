docker build -t offkeysite .

docker run -it --rm -v `pwd`:/workspace offkeysite /bin/bash
