docker build -t offkeyauth .

docker run -it --rm --name auth -p 6311:6311 -v `pwd`:/workspace offkeyauth /bin/bash
