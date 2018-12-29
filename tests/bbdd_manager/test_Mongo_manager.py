from unittest import TestCase
from bbdd_manager.Mongo_manager import Mongo_manager

class TestUnidadGestionable(TestCase):
    # Atributes
    bbdd_name = 'test'
    col_name = 'my_tests'
    # We create the object BBDD that we are going to test
    mongoDDBB = Mongo_manager(bbdd_name)
    # Then we delete de colection created in the previous test
    mongoDDBB.db.drop_collection(col_name)

    # Methods
    def test_insert_one_recover_one(self):
        in_doc = {"_id":1,"NAME":"Fernando","SURNAME":"Fuentes","DNI":"55820953R"}
        # We insert the doc that we just created
        self.mongoDDBB.insert_one_doc_col(in_doc,self.col_name)
        # We extract the previous insert
        cond = {"_id":1}
        out_doc = self.mongoDDBB.recover_one_doc(self.col_name,cond)
        # Test validation
        self.assertEqual(in_doc,out_doc, msg="Empleando metodos insert_one_doc_col() and recover_one_doc()"
                                                + "recuperamos " + str(out_doc) + " cuando espera "
                                                + str(in_doc))
        print("Test of the methods insert_one_doc_col() and recover_one_doc()  --> OK")

    def test_insert_update_one_recover_one(self):
        in_doc = {"_id":2,"NAME":"Jorge","SURNAME":"Gomez","DNI":"55820953R"}
        # We insert the doc that we just created
        self.mongoDDBB.save_one_doc_col(in_doc,self.col_name)
        # Prepare modification
        mod_doc = {"_id": 2, "NAME": "Jorge", "SURNAME": "Gomez", "DNI": "66824953R"}
        # We extract the previous insert
        self.mongoDDBB.save_one_doc_col(mod_doc,self.col_name)
        # We extract the previous insert
        cond = {"_id": 2}
        out_doc = self.mongoDDBB.recover_one_doc(self.col_name, cond)
        # Test validation 1
        self.assertEqual(mod_doc,out_doc, msg="Empleando metodos save_one_doc_col() and recover_one_doc()"
                                                + "recuperamos " + str(out_doc) + " cuando espera "
                                                + str(in_doc))
        print("Test of the methods save_one_doc_col() and recover_one_doc()  --> OK")

    def test_insert_many_recover_many(self):
        in_doc_1 = {"_id":3,"NAME":"Pablo","SURNAME":"Martinez","DNI":"59470951R"}
        in_doc_2 = {"_id": 4, "NAME": "Raquel", "SURNAME": "Martinez", "DNI": "59470951R"}
        in_doc_list = [in_doc_1,in_doc_2]
        # We insert the doc that we just created
        self.mongoDDBB.insert_many_docs_col(in_doc_list,self.col_name)
        # We extract the previous insert
        cond = {"SURNAME":"Martinez"}
        out_cursor = self.mongoDDBB.recover_docs(self.col_name,cond)
        for doc in out_cursor:
            if doc["_id"] == 3:
                # Test validation 1
                self.assertEqual(in_doc_1,doc, msg="Empleando metodos insert_many_docs_col() and recover_docs()"
                                                        + "recuperamos " + str(in_doc_1) + " cuando espera "
                                                        + str(doc))
            elif doc["_id"] == 4:
                # Test validation 2
                self.assertEqual(in_doc_2, doc, msg="Empleando metodos insert_many_docs_col() and recover_docs()"
                                                    + "recuperamos " + str(in_doc_2) + " cuando espera "
                                                    + str(doc))
        print("Test of the methods insert_many_docs_col() and recover_docs()  --> OK")

    def test_recover_all(self):
        # We extract the previous insert
        out_cursor = self.mongoDDBB.recover_all_doc(self.col_name)
        num_count = out_cursor.count()
        num_all = 4
        # Test validation
        self.assertEqual(num_count,num_all, msg="Empleando metodo recover_all_doc()"
                                                + "recuperamos " + str(num_count) + " cuando espera "
                                                + str(num_all))
        print("Test of the method recover_all_doc() --> OK")

    def test_recover_values(self):
        # We extract the previous insert
        cond = {"_id": 1}
        fields = {"NAME":1}
        doc_expected = {'_id': 1, 'NAME': 'Fernando'}
        out_cursor = self.mongoDDBB.recover_values(self.col_name, cond, fields)
        out_doc = out_cursor.next()
        # Test validation
        self.assertEqual(out_doc,doc_expected, msg="Empleando metodo recover_values()"
                                                + "recuperamos " + str(out_doc) + " cuando espera "
                                                + str(doc_expected))
        print("Test of the method recover_values() --> OK")

    def test_update_keyValue(self):
        # We extract the previous insert
        cond = {"SURNAME": "Martinez"}
        clave = "TELF"
        valor = 911
        out_result = self.mongoDDBB.update_keyValue_docs(self.col_name, cond, clave, valor)
        # Test validation
        self.assertTrue(out_result, msg="Fails of the method update_keyValue_docs()")
        print("Test of the method update_keyValue_docs() --> OK")