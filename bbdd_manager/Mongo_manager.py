import pymongo

from bbdd_manager import ConfigVariablesBbdd

class Mongo_manager:
    """Clase que gestiona el acceso a la BBDD MongoDB

    """

    def __init__(self,bbdd_name):
        """La inicializacion de la clase consiste en establecer la conexion a la BBDD.

        """
        # Creamos la conexion con la BBDD indicando el servidor y el puerto
        self.mongo_client = pymongo.MongoClient(ConfigVariablesBbdd.server, ConfigVariablesBbdd.port)
        # Seleccionamos la BBDD que vamos a usar (podriamos utilizar varias a la vez) (ConfigVariablesBbdd.database)
        self.db = self.mongo_client[bbdd_name]

    def insert_one_doc_col(self, documento, coleccion):
        """Funcion para insertar un documento en una coleccion

        Si insertamos dos documentos con mismo _id, falla por clave duplicada.
        Acepta dos parametros:
           -documento: documento que se desea insertar.
           -coleccion: collecion en la que se desea insertar el documento.
        """
        self.db[coleccion].insert_one(documento)

    def save_one_doc_col(self, documento, coleccion):
        """Funcion para insertar un documento en una coleccion

        Inserta si el documento no existe y actuliza si existe (NO falla por clave duplicada, sobreescribe):
           -documento: documento que se desea insertar.
           -coleccion: collecion en la que se desea insertar el documento.
        """
        self.db[coleccion].save(documento)

    def insert_many_docs_col(self, docs_iter, coleccion):
        """Funcion para insertar varios documentos en una coleccion

        Si insertamos dos documentos con mismo _id, falla por clave duplicada.
        Acepta dos parametros:
           -docs_iter: iterador con documentos.
           -coleccion: collecion en la que se desea insertar el documento.
        """
        self.db[coleccion].insert_many(docs_iter)

    def recover_docs(self, coleccion, condicion):
        """Funcion para recuperar varios documentos de una coleccion.

        Acepta dos parametros:
            <coleccion>: Coleccion donde se buscara el documento.
            <condicion>: Dicionario que conforma la condicion de busqueda ej: {"claveBusqueda":"valorBuscado"}
        Devuelve un cursor de documentos que coincidan con la condicion de busqueda. Los documentos se puede extraer
        con cursor.next() o iterando en un for.
        """
        documento = self.db[coleccion].find(condicion)
        return documento

    def recover_one_doc(self, coleccion, condicion):
        """Funcion para recuperar un unico documento de una coleccion.

        Acepta dos parametros:
           <coleccion>: Coleccion donde se buscara el documento.
           <condicion>: Dicionario que conforma la condicion de busqueda ej: {"claveBusqueda":"valorBuscado"}
        Y devuelve un unico documento.
        """
        documento = self.db[coleccion].find_one(condicion)
        return documento

    def recover_all_doc(self, coleccion):
        """Funcion para recuperar todos documentos de una coleccion.

        Acepta un parametro:
           <coleccion>: Coleccion de la que se extraeran todos sus documentos
        Y devuelve un cursor, el documento se puede extraer con cursor.next(), o un for.
        """
        documento = self.db[coleccion].find()
        return documento

    def recover_values(self, coleccion, condicion, campos):
        """Funcion para recuperar campos concretos de un documento de una coleccion.

        Acepta tres parametros:
           <coleccion>: Coleccion donde se buscara el documento
           <condicion>: Dicionario que conforma la condicion de busqueda ej: {"claveBusqueda":"valorBuscado"}
           <campos>: Diccionario con las claves de los campos que se quieren consultar igualados al valor 1.
                     Ej: {"claveDeseada": 1 , "claveDeseada2": 1 , ...}
        Y devuelve un cursor, el documento se puede extraer con cursor.next() o iterando en un for.
        """
        documento = self.db[coleccion].find(condicion, campos)
        return documento

    def update_keyValue_docs(self, coleccion, condicion, clave, valor):
        """
        Funcion que permite actualizar/incluir campos de uno o varios documentos
        :param coleccion: Coleccion donde se va a buscar el/los documento/s
        :param condicion: Condicion para seleccionar el/los documento/s
        :param clave_valor: Diccionario con el par clave/valor a cambiar/insertar
        :return: Se devuelve una lista de 3 elementos con el resultado del update.
                 lista[0]--> (Si OK) True                    (Si KO) False
                 lista[1]--> (Si OK) Elementos encontrados   (Si KO) None
                 lista[2]--> (Si OK) Elementos modificados   (Si KO) None
        """
        resultado = self.db[coleccion].update_many(condicion, {"$set": {clave: valor}})
        if (resultado.acknowledged):
            lista_res = [resultado.acknowledged, resultado.matched_count, resultado.modified_count]
        else:
            lista_res = [resultado.acknowledged, None, None]
        return lista_res

    def collection_count(self,coleccion):
        """Function to retrieve the numbers of documents in a collections

        Accepts two parameters:
           <colection>: Collection from which is going to count the documents
        And returns the number of documents
        """
        number_of_docs = self.db[coleccion].count()
        return number_of_docs

    def pick_random_docs(self,coleccion, total_number):
        """Function to retrieve a random number of documents from a collection.

        Accepts two parameters:
           <colection>: Collection from which the documents are going to be extracted
           <total_number>: Number of documents to be obtained randomly
        And returns a cursor, the document can be extracted with cursor.next(), or a for.
        """
        requested_number = total_number
        doc_cursor = self.db[coleccion].aggregate([{ "$sample": { "size": requested_number } }])
        return doc_cursor

# Creamos una conexion a la BBDD
#bbdd_connec = Mongo_manager(ConfigVariablesBbdd.env_database)
#cur = bbdd_connec.pick_random_docs('data_person_names_sample',1)
#for doc in cur:
#    print(doc)
#print(type(cur))
#num = bbdd_connec.collection_count('data_person_names_sample')
#print(num)