#  Trabalho BD1

### Execução

Obs: Você precisa ter o postgres instalado e configurado em sua máquina. 

- Precisa baixar o arquivo amazon-meta no site: https://snap.stanford.edu/data/amazon-meta.html
I
- Colocar o arquivo dentro da pasta data

- Mudar o path no arquivo Parser.py na linha 7 para: path = "/home/user_do_seu_computador/Documentos/trab_bd/data/amazon-meta.txt"

Após isso, rodar:

- python3 Builder.py **host** **user** **database** **password** **path** 

- python3 DashboardServer.py **host** **user** **database** **password** 

