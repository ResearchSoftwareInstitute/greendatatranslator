import json, pprint, requests, textwrap, time, sys, atexit
from string import Template

class LivyContext(object):
    def __init__(self, host='http://localhost:8998', kind='pyspark'):
        self.host = host
        self.data = { 'kind' : kind }
        self.headers = { 'Content-Type': 'application/json' }
        r = requests.post(host + '/sessions', data=json.dumps(self.data), headers=self.headers)
        self.session_url = host + r.headers['location']
        self.statements_url = self.session_url + '/statements'
        print ("Waiting for Spark connection")
        while True:
            r = requests.get (self.session_url, headers=self.headers)
            if r.json()['state'] == 'idle':
                break
            else:
                time.sleep (2)
        print ("Connected to Spark session")

    def execute (self, code):
        data = { 'code': textwrap.dedent (code) }
        r = requests.post(self.statements_url, data=json.dumps(data), headers=self.headers)
        statement_url = self.host + r.headers['location']
        r = None
        while True:
            r = requests.get(statement_url, headers=self.headers).json ()
            if r['state'] == 'available':
                break
        result = None
        output = r['output']
        if output is None:
            print ("Error: result is 'available' but output is None")
            print (r)
        else:
            if not r['output']['status'] == 'ok':
                print ("Encountered error: {}".format (r))
                raise "Error: {}".format (r)
            if 'data' in output:
                output_data = output['data']
                if 'text/plain' in output_data:
                    result = output_data['text/plain']
        return result

    def close (self):
        requests.delete(self.session_url, headers=self.headers)

acsLoaderCode="""
class ACSLoader(object):
    def __init__(self, path, table, sample_size=1.0):
        self.path = path
        self.rdd = self.load (sample_size=sample_size)
        self.rdd.toDF().registerTempTable (table)
    def load (self, sample_size=1.0):
        return sqlContext.read.                                     \
            format('com.databricks.spark.csv').                     \
            options(comment='#').                                   \
            options(delimiter=",").                                 \
            options(header='true').                                 \
            load(self.path).rdd.                                   \
            sample (False, sample_size, 1234)
acs = ACSLoader (
    path = "/projects/stars/translator/var/acs/dataworld/uscensusbureau-acs-2015-5-e-income/data/USA_All_States.csv",
    table = "acs_income")
"""

class ACSIncome(LivyContext):
    def __init__(self):
        LivyContext.__init__(self)
        r = self.execute (acsLoaderCode)
    def get_col (self, col):
        code = Template ("""
        print(sqlContext.sql('select $column from acs_income').rdd.map(lambda r : int(r.$column)).collect ())
        """).substitute (column=col)
        return self.execute (code)

def main0 ():
    code_path = sys.argv[1]
    lc = LivyContext ()
    with open(code_path, 'r') as stream:
        code = stream.read ()
        print (code)
        print(lc.execute (code))
    lc.close ()

acs_income = None
def cleanup ():
    if acs_income:
        acs_income.close ()
atexit.register (cleanup)

def main ():
    acs_income = ACSIncome ()
    for x in range (0, 100):
        print (acs_income.get_col('B19037E_036'))
    acs_income.close ()

#main ()
