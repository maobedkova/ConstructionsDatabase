# coding: utf-8
from elasticsearch import Elasticsearch

import codecs, json
es = Elasticsearch()

'''
f = codecs.open('vn.json', 'r', 'utf-8')
f_js = json.load(f)
for line in f_js:
    res = es.index(index="verbs", doc_type="vn", body=line)
    print res['created']

#res = es.get(index="verbs", doc_type='vn', id=45)
#print(res['_'])
'''


res = es.search(index="verbs", body={"from": 0, "size": 500, "query": {"match": {'tax_verb': u'эмоции проявление'}}})
#print("Got %d Hits:" % res['hits']['total'])
for hit in res['hits']['hits']:
    if hit['_score'] >= 2.0:
        print hit['_source']['collocation'], hit['_source']['class_noun'], hit['_score']

#hit = res['hits']['hits'][0]
#print hit['_source']['collocation']
    #print ("%(noun)s %(verb)s: %(collocation)s" % hit["_source"])