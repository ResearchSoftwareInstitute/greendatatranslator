import json, pprint, requests, textwrap, time

host = 'http://localhost:8998'
data = {'kind': 'spark'}
headers = {'Content-Type': 'application/json'}
r = requests.post(host + '/sessions', data=json.dumps(data), headers=headers)
print (r.json())

session_url = host + r.headers['location']
statements_url = session_url + '/statements'

while True:
    r = requests.get(session_url, headers=headers)
    print (r.json ())
    if r.json()['state'] == 'idle':
        break
    else:
        time.sleep (5)
        print ("waiting...")
'''
{u'id': 0,
  u'output': {u'data': {u'text/plain': u'res0: Int = 2'},
              u'execution_count': 0,
              u'status': u'ok'},
  u'state': u'available'}
'''

data = {
  'code': textwrap.dedent("""
    import random
    NUM_SAMPLES = 100000
    def sample(p):
      x, y = random.random(), random.random()
      return 1 if x*x + y*y < 1 else 0

    count = sc.parallelize(xrange(0, NUM_SAMPLES)).map(sample).reduce(lambda a, b: a + b)
    print "Pi is roughly %f" % (4.0 * count / NUM_SAMPLES)
    """)
}

r = requests.post(statements_url, data=json.dumps(data), headers=headers)
pprint.pprint(r.json())
