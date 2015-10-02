docker build -t offkeyauth .

docker run -it --link redis:redis --rm --name auth -p 80:80 -v `pwd`:/workspace offkeyauth /bin/bash
