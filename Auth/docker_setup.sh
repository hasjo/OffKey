docker build -t offkeyauth .

docker run -it --rm -p 6311:6311 -v `pwd`:/workspace offkeyauth /bin/bash
