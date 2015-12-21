# -*- coding:utf-8 -*-

import codecs, re, random
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def common():
    return render_template('common.html')

@app.route('/verbs')

def index():   
    nouns = []
    taxon = []
    actual = []
    colloc = []
        
    reg_class = re.compile(';([^;]+?)\r\n')
    reg_word = re.compile('^(.+?);')
    reg_col = re.compile('^.+?;(.+?);')

    f = codecs.open('Nouns.csv', 'r', 'cp1251')
    for line in f:
        classif = reg_class.findall(line)
        if classif != []:
            classif = ''.join(classif)
            if ''.join(classif) not in nouns:
                nouns.append(''.join(classif))

    f = codecs.open('Taxonomic.csv', 'r', 'cp1251')
    for line in f:
        classif = reg_class.findall(line)
        if classif != []:
            classif = ''.join(classif)
            if ''.join(classif) not in taxon:
                taxon.append(''.join(classif))

    f = codecs.open('Actional.csv', 'r', 'cp1251')
    for line in f:
        classif = reg_class.findall(line)
        if classif != []:
            classif = ''.join(classif)
            if ''.join(classif) not in actual:
                actual.append(''.join(classif))

    f = codecs.open('Collocations.csv', 'r', 'cp1251')
    for line in f:
        classif = reg_col.findall(line)
        if classif != []:
            classif = ''.join(classif)
            if ''.join(classif) not in colloc:
                colloc.append(''.join(classif))

    whole_nouns = []
    whole_taxon = []
    whole_actual = []

    for classif in nouns:
        string = '<li class="main-class"><p>' + classif + '</p><ul class="sub-menu">'
        f = codecs.open('Nouns.csv', 'r', 'cp1251')
        for line in f:
            if ''.join(reg_class.findall(line)) == classif:
                string += '<li><p>' + ''.join(reg_word.findall(line)) + '</p></li>'
        string += '</ul></li>'
        whole_nouns.append(string)

    for classif in taxon:
        string = '<li class="main-class"><p>' + classif + '</p><ul class="sub-menu">'
        f = codecs.open('Taxonomic.csv', 'r', 'cp1251')
        for line in f:
            if ''.join(reg_class.findall(line)) == classif:
                string += '<li><p>' + ''.join(reg_word.findall(line)) + '</p></li>'
        string += '</ul></li>'
        whole_taxon.append(string)

    for classif in actual:
        string = '<li class="main-class"><p>' + classif + '</p><ul class="sub-menu">'
        f = codecs.open('Actional.csv', 'r', 'cp1251')
        for line in f:
            if ''.join(reg_class.findall(line)) == classif:
                string += '<li><p>' + ''.join(reg_word.findall(line)) + '</p></li>'
        string += '</ul></li>'
        whole_actual.append(string)
            
    try:
        word_v = request.args['verbs']
        word_n = request.args['nouns']
        word_c = request.args['colls']


        if word_v != '':
            collocations_file = codecs.open(u'Collocations.csv', 'r', encoding="cp1251")
            actual_file = codecs.open(u'Actional.csv', 'r', encoding="cp1251")
            taxonomic_file = codecs.open(u'Taxonomic.csv', 'r', encoding="cp1251")

            r=re.compile(u'(.*);' + word_v + u'(.*);([1|2]?);(.*);\??([А-Яа-яё\"»\[\]― ]+.*?);;([0-9]+)\r\n', flags=re.U)
            r1=re.compile('^' + word_v + u';(([а-яё :]+./?)([а-яё :]+)?)', flags=re.U)
            r2=re.compile('^' + word_v + u';([а-яё :]+.)*', flags=re.U)

            
            b = []
            for line in taxonomic_file:               
                m=r1.match(line)
                if m!=None:
                    b.append(m.group(1))
            words = u'<div class="cl"><p>Таксономический класс: <b>' + ', '.join(b) + '</b></p>'

            c = []
            for line in actual_file:               
                m=r2.match(line)
                if m!=None:
                    c.append(m.group(1))
            words = words + u'<p>Акциональный класс: <b>' + ', '.join(c) + '</b></p></div><hr>'
            

            for line in collocations_file:               
                m=r.match(line)
                if m!=None:
                    a = u'<p>Коллокация: <i><b>' + word_v + u" как " + m.group(1) + u'</i></b></p><p>Частота: ' + m.group(6) + u'</p><p>Пример употребления: <i>' + m.group(5) + '</i></p>'
                    words = words + a + '<hr>'
                    
            l = ''.join(words)
            s = '<p style="font-size:20px; margin-left:20px;"><b><i>' + word_v + '</i></b></p>' + l

        if word_n != '':
            collocations_file = codecs.open(u'Collocations.csv', 'r', encoding="cp1251")
            nouns_file = codecs.open(u'Nouns.csv', 'r', encoding="cp1251")
            
            r = re.compile('^' + word_n + u'([;\?12]{1,4})(.*?)([;\?12]{2,4}).*?;([А-Яа-яё\?«\"»\[\]― ]+.*?);;([0-9]+)\r\n', flags=re.U)
            r1=re.compile('^' + word_n + u';([а-яё :]+.)', flags=re.U)

            n = []
            for line in collocations_file:               
                m=r.search(line)
                if m!=None:
                    ex = u'<p><i><b>' + m.group(2) + u'</b></i></p><p>Частота: ' + m.group(5) + u'</p><p>Пример употребления: <i>' + m.group(4) + '</i></p>'
                    n.append(ex)
            third = '<hr>'.join(n)


            d = []
            for line in nouns_file:               
                m=r1.search(line)
                if m!=None:
                    ex = m.group(1) 
                    d.append(ex)
            second = u'<div class="cl"><p>Класс: <b>' + ', '.join(d) + '</b></p></div><hr>'

            s = u'<p style="font-size:20px; margin-left:20px;"><b><i>' + word_n + '</i></b></p>' + second + third

        if word_c != '':
            f=codecs.open(u'Collocations.csv', 'r', encoding="cp1251")
            f1=codecs.open(u'Nouns.csv', 'r', encoding="cp1251")
            f2=codecs.open(u'Taxonomic.csv', 'r', encoding="cp1251")
            f3=codecs.open(u'Actional.csv', 'r', encoding="cp1251")
            
            splt = word_c.split(u' как ')
            x = splt[0]
            y = splt[1]
          
            r = re.compile(';' + word_c + u';[^;]*?;([^;]*?);([^;]+?);;([0-9]*)\r\n', flags=re.U)
            r1 = re.compile('^' + x + u';(.+?)\r\n', flags=re.U)
            r2 = re.compile('^' + y + u';(.+?)\r\n', flags=re.U)

            for line in f:               
                m = r.search(line)
                if m != None:
                    a1 = u'<p>Частота: ' + m.group(3) + u'</i></p>'
                    a3 = u'<p>Пример употребления: <i>' + m.group(2) + '</i></p>'
                    a2 = u'<p>Субъекты (кроме человека): <b>' + m.group (1) + u'</b></p>'
                        
            b = []           
            for line in f2:               
                if r1.search(line) == None:
                    pass
                else:
                    b.append(''.join(r1.findall(line)))
                    
            if b == []:
                b = u'<div class="cl"><p>Таксономический класс: <b>нет класса</b></p>'
            else:
                b = u'<div class="cl"><p>Таксономический класс: <b>' + ', '.join(b) + '</b></p>'

            c = []
            for line in f3:               
                if r1.search(line) == None:
                    pass
                else: 
                    c.append(''.join(r1.findall(line)))
            if c == []:
                c = u'<p>Акциональный класс: <b>нет класса</b></p>'
            else:
                c = u'<p>Акциональный класс: <b>' + ', '.join(c) + '</b></p>'


            for line in f1:               
                m = r2.search(line)
                if m != None:
                    d =  u'<p>Класс существительного: <b>' + m.group(1) + '</b></p></div><hr>'


            s =  u'<p style="font-size:20px; margin-left:20px;"><i><b>' + word_c + '</i></b></p>' + b + c + d + a1 + a2 + a3 


        return render_template('res.html', s = s, whole_nouns = whole_nouns, whole_taxon = whole_taxon, whole_actual = whole_actual, colloc = colloc)    

    except:             
        return render_template('index_verbs.html', whole_nouns = whole_nouns, whole_taxon = whole_taxon, whole_actual = whole_actual, colloc = colloc)


@app.route('/classes_verbs')

def comparison():

    reg_class = re.compile(';([^;]+?)\r\n')
    reg_word = re.compile('^(.+?);')
    reg_col = re.compile(u'^(.+?);(.+?) как')

    taxon = []
    f = codecs.open('Taxonomic.csv', 'r', 'cp1251')
    for line in f:
        classif = reg_class.findall(line)
        if classif != []:
            classif = ''.join(classif)
            if ''.join(classif) not in taxon:
                taxon.append(''.join(classif))
    
    whole = []
    for classif in taxon:
        example = []
        string = '<ul><li class = "nuu" style="font-size: 20px;"><b>' + classif + u"</b> может употребляться с: "
        f = codecs.open('Taxonomic.csv', 'r', 'cp1251')
        for line in f:
            if ''.join(reg_class.findall(line)) == classif:
                example.append(''.join(reg_word.findall(line)))
        ex_nouns = []
        for el in example:
            f1 = codecs.open('Collocations.csv', 'r', 'cp1251')
            for line in f1:
                m = re.search(u'^(.+?);' + el + u' как',line)
                if m != None:
                    ex_nouns.append(m.group(1))
            cl_nouns = []
            for el in ex_nouns:
                f2 = codecs.open('Nouns.csv', 'r', 'cp1251')
                for line in f2:
                    n = re.search('^' + el + ';(.+?)\r\n', line)
                    if n != None:
                        cl_nouns.append(n.group(1))
        cl_nouns = set(cl_nouns)
        string += '<ul class="content">'
        for i in cl_nouns:
            string += '<li>'
            string += i
            string += '</li>'
        string += '</ul></li></ul>'
        whole.append(string)

    return render_template('comp.html', whole = whole)

@app.route('/adjs')
def adj():
    nouns = []
    taxon = []
    colloc = []
    
    reg_class = re.compile(';([^;]+?)\r\n')
    reg_word = re.compile('^(.+?);')
    reg_col = re.compile('^.+?;(.+?);')

    f = codecs.open('Adj_nouns.csv', 'r', 'cp1251')
    for line in f:
        classif = reg_class.findall(line)
        if classif != []:
            classif = ''.join(classif)
            if ''.join(classif) not in nouns:
                nouns.append(''.join(classif))

    f = codecs.open('Adj_taxonomic.csv', 'r', 'cp1251')
    for line in f:
        classif = reg_class.findall(line)
        if classif != []:
            classif = ''.join(classif)
            if ''.join(classif) not in taxon:
                taxon.append(''.join(classif))

    f = codecs.open('Adj_colloc.csv', 'r', 'cp1251')
    for line in f:
        classif = reg_col.findall(line)
        if classif != []:
            classif = ''.join(classif)
            if ''.join(classif) not in colloc:
                colloc.append(''.join(classif))

    whole_nouns = []
    whole_taxon = []
    whole_actual = []

    for classif in nouns:
        string = '<li class="main-class"><p>' + classif + '</p><ul class="sub-menu">'
        f = codecs.open('Adj_nouns.csv', 'r', 'cp1251')
        for line in f:
            if ''.join(reg_class.findall(line)) == classif:
                string += '<li><p>' + ''.join(reg_word.findall(line)) + '</p></li>'
        string += '</ul></li>'
        whole_nouns.append(string)

    for classif in taxon:
        string = '<li class="main-class"><p>' + classif + '</p><ul class="sub-menu">'
        f = codecs.open('Adj_taxonomic.csv', 'r', 'cp1251')
        for line in f:
            if ''.join(reg_class.findall(line)) == classif:
                string += '<li><p>' + ''.join(reg_word.findall(line)) + '</p></li>'
        string += '</ul></li>'
        whole_taxon.append(string)

    try:
        word_v = request.args['verbs']
        word_n = request.args['nouns']
        word_c = request.args['colls']


        if word_v != '':
            collocations_file = codecs.open(u'Adj_colloc.csv', 'r', encoding="cp1251")
            taxonomic_file = codecs.open(u'Adj_taxonomic.csv', 'r', encoding="cp1251")

            r=re.compile(u'(.*);' + word_v + u'(.*);([1|2]?);(.*);\??([А-Яа-яё\"»\[\]― ]+.*?);;([0-9]+)\r\n', flags=re.U)
            r1=re.compile('^' + word_v + u';(([а-яё :]+./?)([а-яё :]+)?)', flags=re.U)
            r2=re.compile('^' + word_v + u';([а-яё :]+.)*', flags=re.U)

            
            b = []
            for line in taxonomic_file:               
                m=r1.match(line)
                if m!=None:
                    b.append(m.group(1))
            words = u'<div class="cl"><p>Класс: <b>' + ', '.join(b) + '</b></p></div><hr>'            

            for line in collocations_file:               
                m=r.match(line)
                if m!=None:
                    a = u'<p>Коллокация: <i><b>' + word_v + u" как " + m.group(1) + u'</i></b></p><p>Частота: ' + m.group(6) + u'</p><p>Пример употребления: <i>' + m.group(5) + '</i></p>'
                    words = words + a + '<hr>'
                    
            l = ''.join(words)
            s = '<p style="font-size:20px; margin-left:20px;"><b><i>' + word_v + '</i></b></p>' + l

        if word_n != '':
            collocations_file = codecs.open(u'Adj_colloc.csv', 'r', encoding="cp1251")
            nouns_file = codecs.open(u'Adj_nouns.csv', 'r', encoding="cp1251")
            
            r = re.compile('^' + word_n + u'([;\?12]{1,4})(.*?)([;\?12]{2,4}).*?;([А-Яа-яё\?«\"»\[\]― ]+.*?);;([0-9]+)\r\n', flags=re.U)
            r1=re.compile('^' + word_n + u';([а-яё :]+.)', flags=re.U)

            n = []
            for line in collocations_file:               
                m=r.search(line)
                if m!=None:
                    ex = u'<p><i><b>' + m.group(2) + u'</b></i></p><p>Частота: ' + m.group(5) + u'</p><p>Пример употребления: <i>' + m.group(4) + '</i></p>'
                    n.append(ex)
            third = '<hr>'.join(n)


            d = []
            for line in nouns_file:               
                m=r1.search(line)
                if m!=None:
                    ex = m.group(1) 
                    d.append(ex)
            second = u'<div class="cl"><p>Класс: <b>' + ', '.join(d) + '</b></p></div><hr>'

            s = u'<p style="font-size:20px; margin-left:20px;"><b><i>' + word_n + '</i></b></p>' + second + third

        if word_c != '':
            f=codecs.open(u'Adj_colloc.csv', 'r', encoding="cp1251")
            f1=codecs.open(u'Adj_nouns.csv', 'r', encoding="cp1251")
            f2=codecs.open(u'Adj_taxonomic.csv', 'r', encoding="cp1251")
            
            splt = word_c.split(u' как ')
            x = splt[0]
            y = splt[1]
          
            r = re.compile(';' + word_c + u';[^;]*?;([^;]*?);([^;]+?);;([0-9]*)\r\n', flags=re.U)
            r1 = re.compile('^' + x + u';(.+?)\r\n', flags=re.U)
            r2 = re.compile('^' + y + u';(.+?)\r\n', flags=re.U)

            for line in f:               
                m = r.search(line)
                if m != None:
                    a1 = u'<p>Частота: ' + m.group(3) + u'</i></p>'
                    a3 = u'<p>Пример употребления: <i>' + m.group(2) + '</i></p>'
                    a2 = u'<p>Субъекты: <b>' + m.group (1) + u'</b></p>'
                        
            b = []           
            for line in f2:               
                if r1.search(line) == None:
                    pass
                else:
                    b.append(''.join(r1.findall(line)))
                    
            if b == []:
                b = u'<div class="cl"><p>Класс глагола: <b>нет класса</b></p>'
            else:
                b = u'<div class="cl"><p>Класс глагола: <b>' + ', '.join(b) + '</b></p>'


            for line in f1:               
                m = r2.search(line)
                if m != None:
                    d =  u'<p>Класс существительного: <b>' + m.group(1) + '</b></p></div><hr>'


            s =  u'<p style="font-size:20px; margin-left:20px;"><i><b>' + word_c + '</i></b></p>' + b + d + a1 + a2 + a3 


        return render_template('res.html', s = s, whole_nouns = whole_nouns, whole_taxon = whole_taxon, whole_actual = whole_actual, colloc = colloc)    

    except:             
        return render_template('index_adjs.html', whole_nouns = whole_nouns, whole_taxon = whole_taxon, whole_actual = whole_actual, colloc = colloc)

@app.route('/classes_adjs')

def comp_adj():

    reg_class = re.compile(';([^;]+?)\r\n')
    reg_word = re.compile('^(.+?);')
    reg_col = re.compile(u'^(.+?);(.+?) как')

    taxon = []
    f = codecs.open('Adj_taxonomic.csv', 'r', 'cp1251')
    for line in f:
        classif = reg_class.findall(line)
        if classif != []:
            classif = ''.join(classif)
            if ''.join(classif) not in taxon:
                taxon.append(''.join(classif))
    
    whole = []
    for classif in taxon:
        example = []
        string = '<ul><li class = "nuu" style="font-size: 20px;"><b>' + classif + u"</b> может употребляться с: "
        f = codecs.open('Adj_taxonomic.csv', 'r', 'cp1251')
        for line in f:
            if ''.join(reg_class.findall(line)) == classif:
                example.append(''.join(reg_word.findall(line)))
        ex_nouns = []
        for el in example:
            f1 = codecs.open('Adj_colloc.csv', 'r', 'cp1251')
            for line in f1:
                m = re.search(u'^(.+?);' + el + u' как',line)
                if m != None:
                    ex_nouns.append(m.group(1))
            cl_nouns = []
            for el in ex_nouns:
                f2 = codecs.open('Adj_nouns.csv', 'r', 'cp1251')
                for line in f2:
                    n = re.search('^' + el + ';(.+?)\r\n', line)
                    if n != None:
                        cl_nouns.append(n.group(1))
        cl_nouns = set(cl_nouns)
        string += '<ul class="content">'
        for i in cl_nouns:
            string += '<li>'
            string += i
            string += '</li>'
        string += '</ul></li></ul>'
        whole.append(string)

    return render_template('comp.html', whole = whole)


@app.route('/game')

def game():

    reg = re.compile(u'(.+?как) (.+?)\r\n')

    global perm_n
    global perm_str


    colloc = []
    f = codecs.open('V+A.csv', 'r', 'cp1251')
    for line in f:
        colloc.append(line)
    
    choice = random.choice(colloc)
    found = reg.search(choice)
    string = found.group(1)
    noun = found.group(2)

    try:
        vvod = request.args['inputtext']
        if vvod == perm_n:
            return render_template('game_luck.html')
        else:
            return render_template('game_lost.html', perm_n = perm_n, perm_str = perm_str)
    except:
        perm_str = string
        perm_n = noun
        return render_template('game_h.html', string = string)

app.run(debug=True)
