neo4j Dockerfile
====

neo4jを起動するためのDockerfileです。  
公式のimageに加えて、以下を行っています。  

公式 : https://hub.docker.com/_/neo4j/

* neo4j-shell-toolsのインストール ( https://github.com/jexp/neo4j-shell-tools )

# 手順

1. `./image-build.sh` によりDockerイメージをビルドしてください。  
1. `./container-start.sh` によりneo4jコンテナを起動してください。
1. 以下にアクセスすれば、GUIで確認することができます。  
http://localhost:7474/browser/  
1. `neo4j-shell`を利用する場合は、以下を実行します。

```
$ docker exec neo4j_custom bin/neo4j-shell -c "<command>"
```

docker build -t neo4j_test_python .
docker run -itd --publish=7474:7474 --publish=7687:7687 \
 -v ${HOME}/Desktop/mv/matsui_lab_git/neo4j-docker/data/testdata:/var/lib/neo4j/import\
 -v ${HOME}/neo4j/data:/data neo4j_test_python

username neo4j
password neo4j(neo4jpw)

# 実際のコマンド

docker-compose 作成
docker-compose up

python のコンテナに入る
docker exec -it neo4j-docker-python_python_1 bash

python のコンテナで
pip install neo4j

memo
curl http://localhost:7474
が
curl http://neo4j:7474（こっちだと同じ compose 内の外部コンテナからアクセス可）
と一緒になる
