#coding:utf-8

from sys import argv
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import mysql.connector
import os

gameid = argv[1]
boardgame_home = os.getenv('BG_HOME')
print boardgame_home
#output_filename = filename.rstrip('.txt') + '.py'
cover_vars_filename = 'cover.variables.js'
slash = '/'
quote = '\''
con = mysql.connector.connect(host='localhost',port=3306,user='root',password='b0@rdg@merule5')

schema_name = 'boardgames'
table_name = 'bggdata'
#column_str = "(self.gameid,year,minAge,rateScore,rateNum,rank,weight,minplayer,time,designers,categorys,mechanisms,publishers,maxplayer,bestplayer,self.name)" 
#value_str = str(self.gameid)+','+str(year)+','+str(minAge)+','+str(rateScore)+','+str(rateNum)+','+str(rank)+','+str(weight)+','+str(minplayer)+','+str(time)+','+  \
#'"'+str(designer_str)+'","'+str(category_str)+'","'+str(mechanism_str)+'","'+str(publisher_str)+'",'+str(maxplayer)+','+str(bestplayer)+',"'+str(self.name)+'"'
sql = 'SELECT * FROM '+schema_name+'.'+table_name+' where gameid = '+gameid
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

cover_vars_filepath = boardgame_home + slash + nameEN + slash + cover_vars_filename
print cover_vars_filepath
with open(cover_vars_filepath,'r') as f:
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
            category_str = '，'.join(category_lsit)
            #print category_str
            line[3] = quote + category_str + quote
            line = line[0:4]
            #print line
        lines[line_no] = ' '.join(line) + "\n"


with open(cover_vars_filepath,'w') as f:
    print lines
    f.writelines(lines);
    f.write("var button1 = \'主题概念\'\n")
    button2_str = 'var button2 = \'>>进入'+nameCN+nameEN+'<<\'\n'
    f.write(button2_str)
    f.write("var numRatesMea = \'点评\'\n")
    f.write("var valueRatesMea = \'/10\'\n")
    f.write("var yearPubMea = \'年\'\n")
    f.write("var weightLimit = \'/5\'\n")
    f.write("var weightExp = \'复杂度\'\n")
    f.write("var ageMea = \'岁\'\n")
    f.write("var ageMeaPlus = \'+\'\n")
    f.write("var playersMea = \'人\'\n")
    f.write("var playersBest = bestplayer + \'人最佳\'\n")
    f.write("var playtimeMea = \'分钟\'\n")
    f.write("var designerTitle = \'设计师:\'\n")
    f.write("var langTitleHigh = \'语言\'\n")
    f.write("var langTitleLow = \'依赖:\'\n")
    f.write("var langLvl0 = \'0\'\n")
    f.write("var langLvl1 = \'1\'\n")
    f.write("var langLvl2 = \'2\'\n")
    f.write("var langLvl3 = \'3\'\n")
    f.write("var langLvl4 = \'4\'\n")
    f.write("var categoryTitle = \'分类机制:\'\n")
    f.write("var cover_img_scale_factor = 0.5\n")
    f.write("var pixels = \'px\'\n")












