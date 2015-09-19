docker build -t offkeyauth .

docker run -it --rm -v `pwd`:/workspace offkeyauth /bin/bash
