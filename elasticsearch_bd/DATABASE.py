# -*- coding:utf-8 -*-

import codecs, re, random, json
from flask import Flask, render_template, request
from elasticsearch import Elasticsearch

es = Elasticsearch()

app = Flask(__name__)

@app.route('/')

def index():
    try:
        word = request.args['words']
        col = request.args['colls']
        res_n = es.search(index="verbs", body={"query": {"match": {'noun': word}}})
        res_v = es.search(index="verbs", body={"query": {"match": {'verb': word}}})
        res_c = es.search(index="verbs", body={"query": {"match": {'collocation': col}}})
        try:
            if res_c:
                hit = res_c['hits']['hits'][0]
                colloc = hit['_source']['collocation']
                subject = hit['_source']['subject']
                freq = hit['_source']['freq']
                example = hit['_source']['example']
                return render_template('res_c.html', colloc=colloc, subject=subject, freq=freq, example=example)
        except:
            try:
                if res_v:
                    arr_for_v = []
                    for hit in res_v['hits']['hits']:
                        verb = hit['_source']['verb']
                        tax_v = hit['_source']['tax_verb']
                        act_v = hit['_source']['act_verb']
                        c_f_e = u'<p>Коллокация: <i><b>' + hit['_source']['collocation'] + u'</b></i></p>' \
                                u'<p>Частота в НКРЯ: ' + str(hit['_source']['freq']) + '</p>' \
                                u'<p>Пример употребления: <i>' + hit['_source']['example'] + '</i></p><hr>'
                        arr_for_v.append(c_f_e)
                    return render_template('res_v.html', verb=verb, tax_v=tax_v, act_v=act_v, arr_for_v=arr_for_v)
            except:
                if res_n:
                    arr_for_n = []
                    for hit in res_n['hits']['hits']:
                        noun = hit['_source']['noun']
                        class_n = hit['_source']['class_noun']
                        c_f_e = u'<p>Коллокация: <i><b>' + hit['_source']['collocation'] + u'</b></i></p>' \
                                u'<p>Частота в НКРЯ: ' + str(hit['_source']['freq']) + '</p>' \
                                u'<p>Пример употребления: <i>' + hit['_source']['example'] + '</i></p><hr>'
                        arr_for_n.append(c_f_e)
                    return render_template('res_n.html', noun=noun, clas=class_n, arr_for_n=arr_for_n)
    except:
        return render_template('index_verbs.html')

@app.route('/classes_verbs')
def class_v():
    try:
        try:
            req_act = request.args['act']
            res_act = es.search(index="verbs", body={"query": {"match": {'act_verb': req_act}}})
            arr = []
            if res_act:
                for hit in res_act['hits']['hits']:
                    arr.append(hit['_source']['verb'])
                arr = set(arr)
                note = u'<p style="margin-left: 20px">Глаголы класса "<b>' + req_act + '</b>":</p>'
                return render_template('res_cl.html', note=note, arr=arr)
        except:
            req_tax = request.args['tax']
            res_tax = es.search(index="verbs", body={"query": {"match": {'tax_verb': req_tax}}})
            arr = []
            if res_tax:
                for hit in res_tax['hits']['hits']:
                    if hit['_score'] >= 2.0:
                        arr.append(hit['_source']['verb'])
                arr = set(arr)
                note = u'<p style="margin-left: 20px">Глаголы класса "<b>' + req_tax + '</b>":</p>'
                return render_template('res_cl.html', note=note, arr=arr)
    except:
        return render_template('cl_verbs.html')

@app.route('/classes_nouns')

def class_n():
    try:
        req = request.args['noun']
        res = es.search(index="verbs", body={"query": {"match": {'class_noun': req}}})
        arr = []
        if res:
            for hit in res['hits']['hits']:
                arr.append(hit['_source']['noun'])
            arr = set(arr)
            note = u'<p style="margin-left: 20px">Существительные класса "<b>' + req + '</b>":</p>'
            return render_template('res_cl.html', note=note, arr=arr)
    except:
        return render_template('cl_nouns.html')

@app.route('/classes')

def classes():
    try:
        req = request.args['cl']
        res = es.search(index="verbs", body={"query": {"match": {'tax_verb': req}}})
        arr = []
        if res:
            for hit in res['hits']['hits']:
                arr.append(hit['_source']['class_noun'])
            arr = set(arr)
            note = u'<p style="margin-left: 20px">Выявлены следующие закономерности у класса глаголов "<b>' + req + '</b>":</p>'
            return render_template('res_cl.html', note=note, arr=arr)
    except:
        return render_template('cl_cl.html')

@app.route('/collocations')

def collocs():
    try:
        res = es.search(index="verbs", body={"from": 0, "size": 500, "query": {"match_all": {}}})
        arr = []
        if res:
            for hit in res['hits']['hits']:
                arr.append(hit['_source']['collocation'])
            arr = sorted(set(arr))
            note = u'<p style="margin-left: 20px"><b>Коллокации:</b></p>'
            return render_template('res_cl.html', note=note, arr=arr)
    except:
        return render_template('index_verbs.html')

@app.route('/game')

def game():
    global choice
    try:
        input = request.args['inputtext']
        res_answer = es.search(index="verbs", body={"from": 0, "size": 500, "query": {"match": {'verb': choice}}})
        arr = []
        colls = []
        if res_answer:
            for hit in res_answer['hits']['hits']:
                arr.append(hit['_source']['noun'])
                colls.append(hit['_source']['collocation'])
            if input in arr:
                return render_template('game_luck.html')
            else:
                return render_template('game_lost.html', colls=colls)
        else:
            return render_template('game_lost.html', colls=colls)
    except:
        res = es.search(index="verbs", body={"from": 0, "size": 500, "query": {"match_all": {}}})
        arr = []
        if res:
            for hit in res['hits']['hits']:
                if not hit['_source']['special construction']:
                    arr.append(hit['_source']['verb'])
            choice = random.choice(arr)
            return render_template('game.html', choice=choice)

app.run(debug=True)
