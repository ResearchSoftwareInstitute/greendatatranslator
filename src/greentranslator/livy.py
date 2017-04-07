import json, pprint, requests, textwrap, time

host = 'http://localhost:8998'
data = {'kind': 'pyspark'}
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
        print ("   waiting for spark context...")

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

statement_url = host + r.headers['location']
print ('statement url: {}'.format (statement_url))
while True:
    r = requests.get(statement_url, headers=headers)
    print (r.json ())
    if r.json()['state'] == 'waiting':
        continue
    break

pprint.pprint(r.json())

requests.delete(session_url, headers=headers)
