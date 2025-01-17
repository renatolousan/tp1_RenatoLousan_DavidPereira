from Parser import Parser
from ManagerDB import Manager
from Query import Query
import sys
import time

host = sys.argv[1]
user = sys.argv[2]
db_name = sys.argv[3]
password = sys.argv[4]
path = sys.argv[5]

if __name__ == '__main__':
    if len(sys.argv) < 6:
        print("Para rodar o programa, é necessário passar 5 argumentos para a execução: host user nome_db password path")
        exit()

    print(host, user, db_name, password, path)
    manager = Manager(host, user, db_name, password)
    manager.connect()

    # criando e carregando a base
    if manager.isConnected():
        print("criando o banco de dados...")
        manager.executeArbitraryStatement(Query.CREATE_DATABASE_SCHEMA)
        begin = time.time()
        print('Carregando os dados...')
        parser = Parser(manager)
        parser.parse(path)
        print("costumers quantity: ", len(parser.getCostumerSet()))
        print("548552 produtos inseridos..\n\nInserindo groups, categories and costumers... ")
        manager.bulkInsertGroupList(parser.groupList)
        manager.bulkInsertCustomerList(parser.customerSet)
        manager.bulkInsertMap(parser.mapCategorioes)
        print("Adicionando as chaves estrangeiras...")
        manager.executeArbitraryStatement(Query.ADD_PROD_GROUP_FK)
        manager.executeArbitraryStatement(Query.REMOVE_SIMILAR_INCONSISTENCES)
        manager.executeArbitraryStatement(Query.ADD_SIMILAR_PROD_FKS)
        manager.executeArbitraryStatement(Query.ADD_REVIEW_COSTUMER_FK)
        manager.executeArbitraryStatement(Query.ADD_CATEGORY_BY_PROD_FKS)

        end = time.time()

        print("Eba, terminou! Tempo decorrido: ", (end-begin))




