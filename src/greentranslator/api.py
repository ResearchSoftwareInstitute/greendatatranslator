import json
import logging
import os
import traceback
from SPARQLWrapper import SPARQLWrapper2, JSON

class LoggingUtil(object):
    @staticmethod
    def init_logging (name):
        FORMAT = '%(asctime)-15s %(filename)s %(funcName)s %(levelname)s: %(message)s'
        logging.basicConfig(format=FORMAT, level=logging.INFO)
        return logging.getLogger(name)

class TripleStore(object):
    def __init__(self, hostname):
        self.service =  SPARQLWrapper2 (hostname)
    def execute_query (self, query):
        self.service.setQuery (query)
        self.service.setReturnFormat (JSON)
        return self.service.query().convert ()
    def execute_query_file (self, query_file):
        result = None
        with open (query_file, "r") as stream:
            query = stream.read ()
            result = self.execute_query (query)
        return result

logger = LoggingUtil.init_logging (__file__)

class DataLake(object):
    def __init__(self, name):
        self.name = name

class Translator (DataLake):
    def __init__(self, name):
        DataLake.__init__(self, name)

class GreenTranslator (Translator):

    def __init__(self, name, config):
        Translator.__init__(self, name)
        with open (config, 'r') as stream:            
            self.config = json.loads (stream.read ())
            self.blazegraph = TripleStore (self.config ['blazegraph_uri'])
            self.exposures_uri = self.config ['exposures_uri']

    def query_biochem (self, query):
        return self.blazegraph.execute_query (query)


