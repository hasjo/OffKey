docker build -t offkeyauth .

docker run -it --rm --name auth -p 80:80 -v `pwd`:/workspace offkeyauth /bin/bash
