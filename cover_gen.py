#coding:utf-8

from sys import argv
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import mysql.connector
import os
import shutil

schema_name = 'boardgames'
table_name = 'bggdata'
#gameid = argv[1]
if argv[1].isdigit():
    gameid = argv[1]
    sql = 'SELECT * FROM '+schema_name+'.'+table_name+' where gameid = '+gameid
else:
    gameid = ''
    nameEN = argv[1]
    sql = 'SELECT * FROM '+schema_name+'.'+table_name+' where nameEN = \''+nameEN+'\''

color = argv[2]

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
gamerule = 'gamerule'
variables = 'variables'
none_str = 'N/A'

color_dict={
    'blue':('#283593','#E8EAF6'),
    'yellow':('#827717','#F9FBE7'),
    'orange':('#FF6600','#FFF3E0'),
    'purple':('#6A1B9A','#F3E5F5'),
    'grey':('#616161','#F5F5F5'),
    'pink':('#AD1457','#FCE4EC'),
    'green':('#2E7D32','#E8F5E9'),
    'bluegrey':('#37474F','#CFD8DC'),
    'scarlet':('#C62828','#FFEBEE')
}
theme_color = color_dict[color][0]
subcontent_color = color_dict[color][1]

category_dict = {
    u'Economic':u'经济运营',
    u'Negotiation':u'嘴炮谈判',
    u'Card Game':u'卡牌',
    u'City Building':u'城市建设',
    u'Family':u'家庭',
    u'Puzzle':u'拼解通关',
    u'Renaissance':u'文艺复兴',
    u'Deduction':u'推理',
    u'Memory':u'记忆',
    u'Party Game':u'聚会',
    u'Humor':u'幽默',
    u'Adventure':u'冒险',
    u'Mature / Adult':u'成人',
    u'Medieval':u'中世纪',
    u'Science Fiction':u'科幻',
    u'Bluffing':u'吹牛',
    u'Horror':u'惊悚',
    u'Political':u'政治',
    u'Fantasy':u'奇幻',
    u'Novel-based':u'小说改编',
    u'Wargame':u'战棋',
    u'Trivia':u'冷知识',
    u'Spies/Secret Agents':u'间谍卧底'
}
#column_str = "(self.gameid,year,minAge,rateScore,rateNum,rank,weight,minplayer,time,designers,categorys,mechanisms,publishers,maxplayer,bestplayer,self.name)" 
#value_str = str(self.gameid)+','+str(year)+','+str(minAge)+','+str(rateScore)+','+str(rateNum)+','+str(rank)+','+str(weight)+','+str(minplayer)+','+str(time)+','+  \
#'"'+str(designer_str)+'","'+str(category_str)+'","'+str(mechanism_str)+'","'+str(publisher_str)+'",'+str(maxplayer)+','+str(bestplayer)+',"'+str(self.name)+'"'
#sql = 'SELECT * FROM '+schema_name+'.'+table_name+' where nameEN = \''+nameEN+'\''
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


gamefolder = boardgame_home + slash + nameEN + slash
imgfolder = boardgame_home + slash + image + slash + nameEN

pgfolder = pageGenerator_home + slash + nameEN + slash
gameTranslatefolder = pageGenerator_home + slash + nameEN + slash

coverfolder = gamefolder + gamecover + slash
introfolder = gamefolder + gameintro + slash
rulefolder = gamefolder + gamerule + slash
variablesfolder = gamefolder + variables + slash

#gameTranslatefolder = pgfolder

if not os.path.exists(gamefolder):
    os.mkdir(gamefolder)
if not os.path.exists(imgfolder):
    os.mkdir(imgfolder)
if not os.path.exists(pgfolder):
    os.mkdir(pgfolder)
if not os.path.exists(coverfolder):
    os.mkdir(coverfolder)
if not os.path.exists(introfolder):
    os.mkdir(introfolder)
if not os.path.exists(rulefolder):
    os.mkdir(rulefolder)
if not os.path.exists(variablesfolder):
    os.mkdir(variablesfolder)


cover_vars_filepath = gamefolder + gamecover + slash + cover_vars_filename
rule_vars_filepath =gamefolder + rule_vars_filename
intro_vars_filepath = gamefolder + gameintro + slash + intro_vars_filename
title_vars_filepath = gamefolder + variables + slash + title_vars_filename

templatefolder = boardgame_home + slash + template + slash
template_cover_folder = templatefolder + gamecover + slash
template_intro_folder = templatefolder + gameintro + slash
template_rule_folder = templatefolder + gamerule + slash
template_variables_folder = templatefolder + variables + slash

template_translate_folder = pageGenerator_home + slash + template + slash

cover_template_filename = templatefolder + gamecover + slash + cover_vars_filename
title_template_filename = templatefolder + variables + slash + title_vars_filename

print cover_template_filename

with open(cover_template_filename,'r') as f:
    lines = f.readlines()
    for line_no in range(len(lines)):
        line = lines[line_no].strip('\n').split(' ')
        #print line
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
            if designers == None:
                line[3] = quote + none_str + quote
                line = line[0:4]
            else:
                designer_lsit = designers.split('|')[:-1]
                designer_str = ','.join(designer_lsit)
                line[3] = quote + designer_str + quote
                line = line[0:4]
        if line[1] == 'artists':
            if artists == None:
                line[3] = quote + none_str + quote
                line = line[0:4]
            else:
                artist_lsit = artists.split('|')[:-1]
                #print designer_lsit
                artist_str = ','.join(artist_lsit)
                #print designer_str
                line[3] = quote + artist_str + quote
                line = line[0:4]
        if line[1] == 'categorys':
            try:
                category_lsit = categorys.split('|')[:-1]
            except:
                category_lsit = ['无']
            #print category_lsit
            for index in range(len(category_lsit)):
                # translate
                category_lsit[index] = category_dict[category_lsit[index]]
                    
            category_str = ','.join(category_lsit)
            #print category_str
            line[3] = quote + category_str + quote
            line = line[0:4]
            #print line
        lines[line_no] = ' '.join(line) + "\n"

#cover
for filename in os.listdir(template_cover_folder):
    if not os.path.exists(coverfolder+filename):
        shutil.copy(template_cover_folder+filename,coverfolder+filename)
#intro
for filename in os.listdir(template_intro_folder):
    if not os.path.exists(introfolder+filename):
        shutil.copy(template_intro_folder+filename,introfolder+filename)
#rule
for filename in os.listdir(template_rule_folder):
    if not os.path.exists(rulefolder+filename):
        shutil.copy(template_rule_folder+filename,rulefolder+filename)

#variables
for filename in os.listdir(template_variables_folder):
    if not os.path.exists(variablesfolder+filename):
        shutil.copy(template_variables_folder+filename,variablesfolder+filename)

# translate
#print template_translate_folder
#print gameTranslatefolder
for filename in os.listdir(template_translate_folder):
    #print filename
    if not os.path.exists(gameTranslatefolder+filename):
        shutil.copy(template_translate_folder+filename,gameTranslatefolder+filename)

with open(cover_vars_filepath,'w') as f:
    #print lines
    f.writelines(lines);

shutil.copy(title_template_filename,title_vars_filepath)

with open(title_vars_filepath,'w') as f:
    f.write("var nameCN = \'" + nameCN + "\';\n")
    f.write("var nameEN = \'"+ nameEN + "\';\n")
    f.write("var theme_color = \'"+ theme_color + "\';\n")
    f.write("var subcontent_color = \'"+ subcontent_color + "\';\n")


print "SUCCESS!"
        
        











