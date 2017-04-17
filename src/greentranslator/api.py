import json
import logging
import os
import traceback
import swagger_client
from string import Template
from swagger_client.rest import ApiException
from SPARQLWrapper import SPARQLWrapper2, JSON

class LoggingUtil(object):
    """ Logging utility controlling format and setting initial logging level """
    @staticmethod
    def init_logging (name):
        FORMAT = '%(asctime)-15s %(filename)s %(funcName)s %(levelname)s: %(message)s'
        logging.basicConfig(format=FORMAT, level=logging.INFO)
        return logging.getLogger(name)
logger = LoggingUtil.init_logging (__file__)

class TripleStore(object):
    """ Connect to a SPARQL endpoint and provide services for loading and executing queries."""
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

class DataLake(object):
    def __init__(self, name):
        self.name = name

class Translator (DataLake):
    def __init__(self, name):
        DataLake.__init__(self, name)

class Exposures (object):
    """ Services relating to environmental exposures. """
    def __init__(self, exposures):
        self.exposures = exposures
    def get_exposure_by_area (self, exposure_type, latitude, longitude, radius):
        """ get_exposure_score:
            array of location/date parameters
        """
        result = None
        try:
            result = self.exposures. \
                     exposures_exposure_type_coordinates_get(exposure_type,
                                                             latitude=latitude,
                                                             longitude=longitude,
                                                             radius=radius)
        except ApiException as e:
            print("Exception when calling DefaultApi->exposures_exposure_type_coordinates_get: %s\n" % e)
        return result

class MedicalBioChem(object):
    def __init__(self, triplestore):
        self.triplestore = triplestore
    def load_query (self, query_name):
        query = None
        fn = os.path.join(os.path.dirname(__file__), 'query', '{0}.sparql'.format (query_name))
        with open (fn, 'r') as stream:
            query = Template (stream.read ()).substitute (diseaseMeshIDList=diseaseMeshIDList)
            logger.debug ('query template: {0}', query)
        return query
    def query_biochem (self, query):
        return self.triplestore.execute_query (query)
    def get_drugs_by_disease (self, disease):
        text = Template (self.load_query_template ("get_drugs_by_disease")).substitute (disease="asthma")
        return self.triplestore.execute_query (text)
    def get_genes_pathways_by_disease (self, diseases):
        result = None
        # ?diseaseID ?drugGenericName ?swissProtID ?uniprotGeneID ?geneBankID ?pathwayName ?keggPath
        diseaseMeshIDList = ' '.join (list(map (lambda d : "( mesh:{0} )".format (d), diseases)))
        text = Template (self.load_query_template ("get_drugs_by_disease")).substitute (diseaseMeshIDList=diseaseMeshIDList)
        return self.triplestore.execute_query (text)

class GreenTranslator (Translator):

    def __init__(self, name="greentranslator", config={}):
        Translator.__init__(self, name)
        self.config = config
        blaze_uri = None
        if 'blaze_uri' in config:
            blaze_uri = self.config ['blaze_uri']
        if not blaze_uri:
            blaze_uri = 'http://stars-blazegraph.renci.org/bigdata/sparql'
        self.blazegraph = TripleStore (blaze_uri)
        #self.exposures_uri = self.config ['exposures_uri']
        self.exposures = Exposures (swagger_client.DefaultApi ())
        self.medbiochem = MedicalBioChemical (self.blazegraph)

    def get_medbiochem (self):
        return self.medbiochem

    def get_exposures (self):
        return self.exposures

    def test (self):
        translator = GreenTranslator ()
        exposure = translator.get_exposure_by_area (exposure_type = 'pm25',
                                                    latitude      = '',
                                                    longitude     = '',
                                                    radius        = '0')
        print ("Exposure: {}".format (exposure))
        
        results = translator.get_drugs_by_disease ("asthma")
        print ("Asthma drugs: {}".format (list(map (lambda b : b['generic_name'].value, results.bindings))))
        
        
        results = translator.get_genes_pathways_by_disease (diseases = [ 'd001249', 'd003371', 'd001249' ])
        
        genes_paths = list(map (lambda b : "{0}->{1} ({2})".format (b['uniprotGeneID'].value,
                                                                    b['keggPath'].value,
                                                                    b['pathwayName'].value),
                                results.bindings))
        print ("Asthma genes/pathways:")
        for g in genes_paths:
            print (g)

if __name__ == '__main__':
    from greentranslator.api import GreenTranslator
    translator = GreenTranslator ()
    translator.test ()
