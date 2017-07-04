#coding:utf-8

from sys import argv
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import mysql.connector
import os

#gameid = argv[1]
nameEN = argv[1]

boardgame_home = os.getenv('BG_HOME')
pageGenerator_home = os.getenv('PG_HOME')
print boardgame_home
#output_filename = filename.rstrip('.txt') + '.py'
cover_vars_filename = 'cover.variables.js'
variables = 'variables'
slash = '/'
quote = '\''
con = mysql.connector.connect(host='localhost',port=3306,user='root',password='b0@rdg@merule5')
image = 'img'
template = 'template'
gamecover = 'gamecover'
gameintro = 'gameintro'
schema_name = 'boardgames'
table_name = 'bggdata'
#column_str = "(self.gameid,year,minAge,rateScore,rateNum,rank,weight,minplayer,time,designers,categorys,mechanisms,publishers,maxplayer,bestplayer,self.name)" 
#value_str = str(self.gameid)+','+str(year)+','+str(minAge)+','+str(rateScore)+','+str(rateNum)+','+str(rank)+','+str(weight)+','+str(minplayer)+','+str(time)+','+  \
#'"'+str(designer_str)+'","'+str(category_str)+'","'+str(mechanism_str)+'","'+str(publisher_str)+'",'+str(maxplayer)+','+str(bestplayer)+',"'+str(self.name)+'"'
sql = 'SELECT * FROM '+schema_name+'.'+table_name+' where nameEN = \''+nameEN+'\''
print sql
cur = con.cursor()

try:
    cur.execute(sql)
    records = cur.fetchall()
    data = list(records[0])
    print data
    yearPub = str(data[1])
    minAge = str(data[2])
    rateScore = str(data[3])
    rateNum = str(data[4])
    rank = str(data[5])
    weight = str(data[6])
    minplayer = str(data[7])
    maxplayer = str(data[8])
    bestplayer = str(data[9])
    mintime = str(data[10])
    maxtime = str(data[11])
    nameEN = data[12]
    nameCN = data[13]
    designers = data[14]
    categorys = data[15]
    mechanisms = data[16]
    publishers = data[17]
    artists = data[18]
    langDepLvl = str(data[19])
except Exception,e:
    print 'error when executing sql'
    print e
cur.close()
con.commit()
con.close()

intro_vars_filename = 'intro.variables.js'
rule_vars_filename = 'rule.variables.js'
title_vars_filename = 'title.variables.js'

try:
    os.mkdir(boardgame_home + slash + nameEN)
    os.mkdir(boardgame_home + slash + image + slash + nameEN)
    os.mkdir(pageGenerator_home + slash + nameEN)
except Exception,e:
    print e
    pass

cover_vars_filepath = boardgame_home + slash + nameEN + slash + gamecover + slash + cover_vars_filename
rule_vars_filepath = boardgame_home + slash + nameEN + slash + rule_vars_filename
intro_vars_filename = boardgame_home + slash + nameEN + slash + gameintro + slash + intro_vars_filename
title_vars_filename = boardgame_home + slash + nameEN + slash + variables + slash + title_vars_filename
cover_template_filename = boardgame_home + slash + template + slash + gamecover + slash + cover_vars_filename

print cover_template_filename

with open(cover_template_filename,'r') as f:
    lines = f.readlines()
    for line_no in range(len(lines)):
        line = lines[line_no].strip('\n').split(' ')
        print line
        if line[1] == 'nameCN':
            line[3] = quote + nameCN + quote
        if line[1] == 'nameEN':
            line[3] = quote + nameEN + quote
        if line[1] == 'rateScore':
            line[3] = quote + rateScore + quote
        if line[1] == 'rateNum':
            line[3] = quote + rateNum + quote
        if line[1] == 'yearPub':
            line[3] = quote + yearPub + quote
        if line[1] == 'weight':
            line[3] = quote + weight + quote
        if line[1] == 'minAge':
            line[3] = quote + minAge + quote
        if line[1] == 'minplayer':
            line[3] = quote + minplayer + quote
        if line[1] == 'maxplayer':
            line[3] = quote + maxplayer + quote
        if line[1] == 'bestplayer':
            line[3] = quote + bestplayer + quote
        if line[1] == 'mintime':
            line[3] = quote + mintime + quote
        if line[1] == 'maxtime':
            line[3] = quote + maxtime + quote
        if line[1] == 'langDepLvl':
            line[3] = quote + langDepLvl + quote
        if line[1] == 'designers':
            designer_lsit = designers.split('|')[:-1]
            #print designer_lsit
            designer_str = ','.join(designer_lsit)
            #print designer_str
            line[3] = quote + designer_str + quote
            line = line[0:4]
        if line[1] == 'categorys':
            category_lsit = categorys.split('|')[:-1]
            #print category_lsit
            for index in range(len(category_lsit)):
                if category_lsit[index] == u'Economic':
                    category_lsit[index] = u'经营'
                if category_lsit[index] == u'Negotiation':
                    category_lsit[index] = u'谈判'
                if category_lsit[index] == u'Card Game':
                    category_lsit[index] = u'卡牌游戏'
                if category_lsit[index] == u'City Building':
                    category_lsit[index] = u'城市建设'
                if category_lsit[index] == u'Family':
                    category_lsit[index] = u'家庭'
                if category_lsit[index] == u'Puzzle':
                    category_lsit[index] = u'拼图'
                if category_lsit[index] == u'Renaissance':
                    category_lsit[index] = u'文艺复兴'
                if category_lsit[index] == u'Deduction':
                    category_lsit[index] = u'推断'
                if category_lsit[index] == u'Memory':
                    category_lsit[index] = u'记忆'
                if category_lsit[index] == u'Party Game':
                    category_lsit[index] = u'聚会游戏'
                if category_lsit[index] == u'Humor':
                    category_lsit[index] = u'幽默'
                    
            category_str = '，'.join(category_lsit)
            #print category_str
            line[3] = quote + category_str + quote
            line = line[0:4]
            #print line
        lines[line_no] = ' '.join(line) + "\n"



with open(cover_vars_filepath,'w') as f:
    print lines
    f.writelines(lines);

with open(title_vars_filename,'w') as f:
    f.write("var nameCN = \'" + nameCN + "\';\n")
    f.write("var nameEN = \'"+ nameEN + "\';\n")

print "SUCCESS!"
        
        











