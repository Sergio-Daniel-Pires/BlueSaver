from pymongo import MongoClient
from abc import abstractmethod, ABC
import os
import pandas
import json

class Data(ABC):
    name: str
    
    def __init__(self):
        self.name = None    

    @abstractmethod
    def get_graph_as_csv(self, graph: str) -> list:
        """
        Get an graph name and return respective value

        :param str graph: Graph that want
        :return: Values extract lines-like, first line is labels
        :rtype: list
        """
        ...

    @abstractmethod
    def get_all_hints(self) -> dict:
        """
        Get all hints for water

        :return: Return all hints as dict
        :rtype: dict
        """

class DataMongoDB(Data):
    def __init__(self):
        super().__init__()
        self.name = "MongoDB"
        self.client = MongoClient('mongodb://localhost:27017')
        self.db = self.client['BlueSaver']
        self.collection = self.db['Graphs']

    def get_graph_as_csv(self, graph: str) -> list:
        data_document = self.collection.find_one({'name', graph})
        if data_document:
            return data_document['data']
        else:
            return None
        
    def get_all_hints(self) -> dict:
        raise Exception("Not implemented")

class DataLocal(Data):
    def __init__(self):
        super().__init__()
        self.name = "Local"

    def get_graph_as_csv(self, graph: str) -> list:
        path_df = f"static/{graph}.csv"
        if os.path.exists(path_df):
            raw_values = pandas.read_csv(path_df, sep=',')
            return [raw_values.columns.tolist()] + raw_values.values.tolist()
        else:
            return None
        
    def get_all_hints(self) -> dict:
        all_hints = json.load(open('static/dicas.json', 'r'))
        return all_hints

class DataFactory:
    @staticmethod
    def create_data(opcao):
        if opcao == 'mongodb':
            return DataMongoDB()
        elif opcao == 'local':
            return DataLocal()
        else:
            raise ValueError("Opção inválida. Escolha 'banco' ou 'local'.")
        
data = DataFactory.create_data('local')