#coding:utf-8

from sys import argv
import mysql.connector
import os

gameid = argv[1]
boardgame_home = os.environ('BG_HOME')

output_filename = filename.rstrip('.txt') + '.py'
cover_vars_filename = 'cover.variables.js'
slash = '/'
quote = '\''
con = mysql.connector.connect(host='localhost',port=3306,user='root',password='b0@rdg@merule5')

schema_name = 'boardgames'
table_name = 'bggdata'
#column_str = "(self.gameid,year,minAge,rateScore,rateNum,rank,weight,minplayer,time,designers,categorys,mechanisms,publishers,maxplayer,bestplayer,self.name)" 
#value_str = str(self.gameid)+','+str(year)+','+str(minAge)+','+str(rateScore)+','+str(rateNum)+','+str(rank)+','+str(weight)+','+str(minplayer)+','+str(time)+','+  \
#'"'+str(designer_str)+'","'+str(category_str)+'","'+str(mechanism_str)+'","'+str(publisher_str)+'",'+str(maxplayer)+','+str(bestplayer)+',"'+str(self.name)+'"'
sql = 'SELECT * FROM '+schema_name+'.'+table_name+'where gameid = '+gameid
print sql
cur = con.cursor()

try:
    cur.execute(sql)
    data = cur.fetchall()
    print type(data)
    
except Exception,e:
    print 'error when executing sql'
    print e
cur.close()
con.commit()
con.close()

cover_vars_filepath = boardgame_home + slash + nameEN + slash + cover_vars_filename

with open(cover_vars_filepath,'r') as f:
    lines = f.readlines()
    for line_no in range(len(lines)):
        line = lines[line_no].strip('\n').split(' ')
        if line[1] == 'nameCN':
            line[3] = quote + nameCN + quote
        if line[1] == 'nameEN':
            line[3] = quote + nameEN + quote
        if line[1] == 'nameRates':
            line[3] = quote + nameRates + quote
        if line[1] == 'valueRates':
            line[3] = quote + valueRates + quote
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
            designer_lsit = designers.split('|')
            designer_str = ','.join(designer_lsit)
            line[3] = quote + designer_str + quote
        if line[1] == 'categorys':
            category_lsit = categorys.split('|')
            category_str = ','.join(category_lsit)
            line[3] = quote + categorys + quote
        lines[line_no] = ' '.join(line) + "\n"


with open(cover_vars_filepath,'w') as f:
    f.writelines(lines);
    f.write("var button1 = \'主题概念\'")
    button2_str = 'var button2 = \'>>进入'+nameCN+nameEN+'<<\''
    f.write(button2_str)
    f.write("var numRatesMea = \'点评\'")
    f.write("var valueRatesMea = \'/10\'")
    f.write("var yearPubMea = \'年\'")
    f.write("var weightLimit = \'/5\'")
    f.write("var weightExp = \'复杂度\'")
    f.write("var ageMea = \'岁\'")
    f.write("var ageMeaPlus = \'+\'")
    f.write("var playersMea = \'人\'")
    f.write("var playersBest = bestplayer + \'人最佳\'")
    f.write("var playtimeMea = \'分钟\'")
    f.write("var designerTitle = \'设计师:\'")
    f.write("var langTitleHigh = \'语言\'")
    f.write("var langTitleLow = \'依赖:\'")
    f.write("var langLvl0 = \'0\'")
    f.write("var langLvl1 = \'1\'")
    f.write("var langLvl2 = \'2\'")
    f.write("var langLvl3 = \'3\'")
    f.write("var langLvl4 = \'4\'")
    f.write("var categoryTitle = \'分类机制:\'")
    f.write("var cover_img_scale_factor = 0.5")
    f.write("var pixels = \'px\'")












