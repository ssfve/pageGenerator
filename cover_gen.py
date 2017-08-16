#coding:utf-8

from sys import argv
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import mysql.connector
import os
import shutil

button1 = '游戏背景'
button2 = '游戏名称'
button3 = '游戏概念'
button4 = '其它规则'
button5 = '中文规则'
button6 = '关注我们'

schema_name = 'boardgames'
table_name = 'bggdata'
table_name_cn = 'bggdatacn'

boardgame_home = os.getenv('BG_HOME')
pageGenerator_home = os.getenv('PG_HOME')
img_home = os.getenv('IMG_HOME')
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
gamepic = 'gamepic'
variables = 'variables'
explain = 'gameexplain'
play = 'gameplay'
none_str = 'N/A'

color_dict = dict()
color_dict['blue']=('#283593','#E8EAF6')
color_dict['lime']=('#827717','#F9FBE7')
color_dict['yellow']=('#FFEB3B','#FFFDE7')
color_dict['orange']=('#FF6600','#FFF3E0')
color_dict['purple']=('#6A1B9A','#F3E5F5')
color_dict['grey']=('#616161','#F5F5F5')
color_dict['pink']=('#AD1457','#FCE4EC')
color_dict['green']=('#2E7D32','#E8F5E9')
color_dict['bluegrey']=('#37474F','#CFD8DC')
color_dict['scarlet']=('#C62828','#FFEBEE')
color_dict['lightblue']=('#1976D2','#E3F2FD')
color_dict['deeporange']=('#BF360C','#FBE9E7')
color_dict['brown']=('#4E342E','#EFEBE9')
color_dict['lightbrown']=('#795548','#EFEBE9')

try:
    color = argv[2]
except Exception,e:
    #print e
    print color_dict.keys()

theme_color = color_dict[color][0]
subcontent_color = color_dict[color][1]

#column_str = "(self.gameid,year,age,average,usersrated,rank,averageweight,minplayers,time,designers,categorys,mechanisms,publishers,maxplayers,suggested_numplayers,self.name)"
#value_str = str(self.gameid)+','+str(year)+','+str(age)+','+str(average)+','+str(usersrated)+','+str(rank)+','+str(averageweight)+','+str(minplayers)+','+str(time)+','+  \
#'"'+str(designer_str)+'","'+str(category_str)+'","'+str(mechanism_str)+'","'+str(publisher_str)+'",'+str(maxplayers)+','+str(suggested_numplayers)+',"'+str(self.name)+'"'
#sql = 'SELECT * FROM '+schema_name+'.'+table_name+' where nameEN = \''+nameEN+'\''

cur = con.cursor()

#gameid = argv[1]
if argv[1].isdigit():
    gameid = argv[1]
    sql = 'SELECT NAME FROM '+schema_name+'.'+table_name+' where gameid = '+gameid
    cur.execute(sql)
    records = cur.fetchall()
    data = list(records[0])
    nameEN = data[0].replace(' ','-').replace('"','').replace(':','').replace('(','').replace(')','')
    print nameEN
    sql = 'SELECT * FROM '+schema_name+'.'+table_name_cn+' where gameid = '+gameid
else:
    gameid = ''
    nameEN = argv[1]
    sql = 'SELECT * FROM '+schema_name+'.'+table_name+' where nameEN = \''+nameEN+'\''

print sql

try:
    cur.execute(sql)
    records = cur.fetchall()
    data = list(records[0])
    print data
    yearpublished = str(data[1])
    age = str(data[2])
    suggested_playerage = str(data[3])
    usersrated = str(data[4])
    rank_subtype = str(data[5])
    rank_type = str(data[6])
    numweights = str(data[7])
    minplayers = str(data[8])
    maxplayers = str(data[9])
    minplaytime = str(data[10])
    maxplaytime = str(data[11])
    language_dependence = str(data[12])

    average = data[13]
    bayesaverage_subtype = data[14]
    bayesaverage_type = data[15]
    averageweight = data[16]

    suggested_numplayers = str(data[17])
    nameCN = str(data[18])
    expansionsCN = str(data[19])
    game_typeCN = str(data[20])
    categorysCN = str(data[21])
    mechanicsCN = str(data[22])
    familysCN = str(data[23])
    subdomainCN = str(data[24])
    designersCN = str(data[25])
    artistsCN = str(data[26])
    publishersCN = str(data[27])

except Exception,e:
    print 'error when executing sql'
    yearpublished = str(0)
    age = str(0)
    suggested_playerage = str(0)
    usersrated = str(0)
    rank_subtype = str(0)
    rank_type = str(0)
    numweights = str(0)
    minplayers = str(0)
    maxplayers = str(0)
    minplaytime = str(0)
    maxplaytime = str(0)
    language_dependence = str(0)

    average = 0
    bayesaverage_subtype = 0
    bayesaverage_type = 0
    averageweight = 0

    suggested_numplayers = str(0)
    nameCN = str(0)
    expansionsCN = str(0)
    game_typeCN = str(0)
    categorysCN = str(0)
    mechanicsCN = str(0)
    familysCN = str(0)
    subdomainCN = str(0)
    designersCN = str(0)
    artistsCN = str(0)
    publishersCN = str(0)
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
picfolder = gamefolder + gamepic + slash
variablesfolder = gamefolder + variables + slash
explainfolder = gamefolder + explain + slash
playfolder = gamefolder + play + slash
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
if not os.path.exists(picfolder):
    os.mkdir(picfolder)
if not os.path.exists(variablesfolder):
    os.mkdir(variablesfolder)
if not os.path.exists(explainfolder):
    os.mkdir(explainfolder)
if not os.path.exists(playfolder):
    os.mkdir(playfolder)

cover_vars_filepath = gamefolder + gamecover + slash + cover_vars_filename
rule_vars_filepath =gamefolder + rule_vars_filename
intro_vars_filepath = gamefolder + gameintro + slash + intro_vars_filename
title_vars_filepath = gamefolder + variables + slash + title_vars_filename

templatefolder = boardgame_home + slash + template + slash
template_cover_folder = templatefolder + gamecover + slash
template_intro_folder = templatefolder + gameintro + slash
template_rule_folder = templatefolder + gamerule + slash
template_pic_folder = templatefolder + gamepic + slash
template_variables_folder = templatefolder + variables + slash
template_explain_folder = templatefolder + explain + slash
template_play_folder = templatefolder + play + slash

template_translate_folder = pageGenerator_home + slash + template + slash

cover_template_filename = templatefolder + gamecover + slash + cover_vars_filename
title_template_filename = templatefolder + variables + slash + title_vars_filename

#print cover_template_filename

with open(cover_template_filename,'r') as f:
    lines = f.readlines()
    for line_no in range(len(lines)):
        line = lines[line_no].strip('\n').split(' ')
        #print line
        if line[1] == 'nameCN':
            line[3] = quote + nameCN + quote
        if line[1] == 'nameEN':
            line[3] = quote + nameEN + quote
        if line[1] == 'average':
            #print average
            if average == 'None':
                line[3] = quote + none_str + quote
            else:
                line[3] = quote + str(round(average,1)) + quote
        if line[1] == 'usersrated':
            line[3] = quote + usersrated + quote
        if line[1] == 'yearpublished':
            line[3] = quote + yearpublished + quote
        if line[1] == 'averageweight':
            line[3] = quote + str(round(averageweight,2)) + quote
        if line[1] == 'age':
            line[3] = quote + age + quote
        if line[1] == 'minplayers':
            line[3] = quote + minplayers + quote
        if line[1] == 'maxplayers':
            line[3] = quote + maxplayers + quote
        if line[1] == 'suggested_numplayers':
            line[3] = quote + suggested_numplayers + quote
        if line[1] == 'minplaytime':
            line[3] = quote + minplaytime + quote
        if line[1] == 'maxplaytime':
            line[3] = quote + maxplaytime + quote
        if line[1] == 'language_dependence':
            line[3] = quote + language_dependence + quote
        if line[1] == 'designers':
            if designersCN == None:
                line[3] = quote + none_str + quote
                line = line[0:4]
            else:
                designer_lsit = designersCN.split('|')[:-1]
                designer_str = ','.join(designer_lsit)
                line[3] = quote + designer_str + quote
                line = line[0:4]
        if line[1] == 'artists':
            if artistsCN == None:
                line[3] = quote + none_str + quote
                line = line[0:4]
            else:
                artist_lsit = artistsCN.split('|')[:-1]
                #print designer_lsit
                artist_str = ','.join(artist_lsit)
                #print designer_str
                line[3] = quote + artist_str + quote
                line = line[0:4]
        if line[1] == 'categorys':
            try:
                category_lsit = categorysCN.split('|')[:-1]
            except:
                category_lsit = ['无']
            #print category_lsit
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

#pic
for filename in os.listdir(template_pic_folder):
    if not os.path.exists(picfolder+filename):
        shutil.copy(template_pic_folder+filename,picfolder+filename)

#variables
for filename in os.listdir(template_variables_folder):
    if not os.path.exists(variablesfolder+filename):
        shutil.copy(template_variables_folder+filename,variablesfolder+filename)


#explain
for filename in os.listdir(template_explain_folder):
    if not os.path.exists(explainfolder+filename):
        shutil.copy(template_explain_folder+filename,explainfolder+filename)

#play
for filename in os.listdir(template_play_folder):
    if not os.path.exists(playfolder+filename):
        shutil.copy(template_play_folder+filename,playfolder+filename)



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

#print img_home
shutil.copy(img_home+slash+'interface/logo.jpg',img_home+slash+nameEN+slash+'logo.jpg')

with open(title_vars_filepath,'w') as f:
    f.write("var nameCN = \'" + nameCN + "\';\n")
    f.write("var nameEN = \'"+ nameEN + "\';\n")
    f.write("var theme_color = \'"+ theme_color + "\';\n")
    f.write("var subcontent_color = \'"+ subcontent_color + "\';\n")
    f.write("var button1 = \'"+ button1 + "\';\n")
    f.write("var button2 = \'"+ button2 + "\';\n")
    f.write("var button3 = \'"+ button3 + "\';\n")
    f.write("var button4 = \'"+ button4 + "\';\n")
    f.write("var button5 = \'"+ button5 + "\';\n")
    f.write("var button6 = \'"+ button6 + "\';\n")


print "SUCCESS!"













