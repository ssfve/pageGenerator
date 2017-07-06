#coding:utf-8

import os
from sys import argv
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import mysql.connector

schema_name = 'boardgames'
table_name = 'bggdata'

if argv[1].isdigit():
    gameid = argv[1]
    sql = 'SELECT * FROM '+schema_name+'.'+table_name+' where gameid = '+gameid
else:
    gameid = ''
    nameEN = argv[1]
    sql = 'SELECT * FROM '+schema_name+'.'+table_name+' where nameEN = \''+nameEN+'\''

pagegenerator_home = os.getenv('PG_HOME')
boardgame_home = os.getenv('BG_HOME')
print boardgame_home

cover_vars_filename = 'cover.variables.js'
slash = '/'
quote = '\''
con = mysql.connector.connect(host='localhost',port=3306,user='root',password='b0@rdg@merule5')

folder_variables = 'variables'

#column_str = "(self.gameid,year,minAge,rateScore,rateNum,rank,weight,minplayer,time,designers,categorys,mechanisms,publishers,maxplayer,bestplayer,self.name)" 
#value_str = str(self.gameid)+','+str(year)+','+str(minAge)+','+str(rateScore)+','+str(rateNum)+','+str(rank)+','+str(weight)+','+str(minplayer)+','+str(time)+','+  \
#'"'+str(designer_str)+'","'+str(category_str)+'","'+str(mechanism_str)+'","'+str(publisher_str)+'",'+str(maxplayer)+','+str(bestplayer)+',"'+str(self.name)+'"'

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

gameintro_filename = 'gameIntro.txt'
gamesetup_filename = 'gameSetup.txt'
gameflow_filename = 'gameFlow.txt'
gameend_filename = 'gameEnd.txt'
gameexplain_filename = 'gameExplain.txt'
gameplay_filename = 'gamePlay.txt'
gamepic_filename = 'gamePic.txt'

intro_js_filename = 'gameIntro.variables.js'
flow_js_filename = 'gameFlow.variables.js'
setup_js_filename = 'gameSetup.variables.js'
end_js_filename = 'gameEnd.variables.js'
explain_js_filename = 'gameExplain.variables.js'
play_js_filename = 'gamePlay.variables.js'
pic_js_filename = 'gamePic.variables.js'

gameintro_filepath = pagegenerator_home + slash + nameEN + slash + gameintro_filename
gamesetup_filepath = pagegenerator_home + slash + nameEN + slash + gamesetup_filename
gameflow_filepath = pagegenerator_home + slash + nameEN + slash + gameflow_filename
gameend_filepath = pagegenerator_home + slash + nameEN + slash + gameend_filename
gameexplain_filepath = pagegenerator_home + slash + nameEN + slash + gameexplain_filename
gameplay_filepath = pagegenerator_home + slash + nameEN + slash + gameplay_filename
gamepic_filepath = pagegenerator_home + slash + nameEN + slash + gamepic_filename

filepath_list = list()
filepath_list.append(gameintro_filepath)
filepath_list.append(gamesetup_filepath)
filepath_list.append(gameflow_filepath)
filepath_list.append(gameend_filepath)
filepath_list.append(gameexplain_filepath)
filepath_list.append(gameplay_filepath)
filepath_list.append(gamepic_filepath)

intro_js_filepath = boardgame_home + slash + nameEN + slash + folder_variables + slash + intro_js_filename
flow_js_filepath = boardgame_home + slash + nameEN + slash + folder_variables + slash + flow_js_filename
setup_js_filepath = boardgame_home + slash + nameEN + slash + folder_variables + slash + setup_js_filename
end_js_filepath = boardgame_home + slash + nameEN + slash + folder_variables + slash + end_js_filename
explain_js_filepath =  boardgame_home + slash + nameEN + slash + folder_variables + slash + explain_js_filename
play_js_filepath =  boardgame_home + slash + nameEN + slash + folder_variables + slash + play_js_filename
pic_js_filepath =  boardgame_home + slash + nameEN + slash + folder_variables + slash + pic_js_filename

jspath_list = list()
jspath_list.append(intro_js_filepath)
jspath_list.append(setup_js_filepath)
jspath_list.append(flow_js_filepath)
jspath_list.append(end_js_filepath)
jspath_list.append(explain_js_filepath)
jspath_list.append(play_js_filepath)
jspath_list.append(pic_js_filepath)

#print cover_vars_filepath

part_no = 0
for index in range(len(filepath_list)):
    x_line_no = 0
    try:
        with open(filepath_list[index],'r') as f:
            lines = f.readlines()
            for line_no in range(len(lines)):
                line = lines[line_no].strip('\n')
                #print line
                if line_no == 0:
                    part_no = 0
                    line_no_mod = line_no - x_line_no
                    lines[line_no] = ("part=[];\narray[" + str(line_no_mod) + "]='" + line + "';\n")
                elif line == 'A':
                    lines[line_no] = 'part['+str(part_no)+']=generate(array);\nlist_line = \'\';\narray=[];\n'
                    x_line_no = line_no + 1
                    part_no = part_no + 1
                else:
                    line_no_mod = line_no - x_line_no
                    lines[line_no] = ("array[" + str(line_no_mod) + "]='" + line + "';\n")

        with open(jspath_list[index],'w') as f:
            #f.write('list_line = \'\';\nvar array=[];\n')
            f.writelines(lines)
            #f.writelines(lines);
    except Exception,e:
        print e