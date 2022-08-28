# Derivando da imagem oficial do Mysql
FROM mysql:5.7

# Adicionando os scripts SQL para serem executados na criação do banco
# Docker Image -> motorcycles.db
COPY ./db/ /docker-entrypoint-initdb.d/