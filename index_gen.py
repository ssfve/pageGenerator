#coding:utf-8

from sys import argv
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import codecs


import os

jsFolder = 'js'
pageFolder = 'page'
slash = '/'

index_dict={
    'A':['A'],
    'B':['B'],
    'C':['C'],
    'CC':['splendor',u'璀璨宝石'],
    'D':['D'],
    'DF':['monopoly',u'大富翁'],
    'E':['E'],
    'F':['F'],
    'G':['G'],
    'GW':['kings-breakfast',u'国王的早餐'],
    'H':['H'],
    'HH':['hanabi',u'花火'],
    'HS':['cottage-garden',u'花舍物语'],
    'I':['I'],
    'J':['J'],
    'K':['K'],
    'L':['L'],
    'LS':['lisboa',u'里斯本'],
    'M':['M'],
    'N':['N'],
    'O':['O'],
    'P':['P'],
    'Q':['Q'],
    'QL':['game-thrones-board-game-second-edition',u'权力的游戏(第二版)'],
    'R':['R'],
    'S':['S'],
    'SJ':['time-stories',u'时间守望'],
    'SN':['kanagawa',u'神奈川学苑'],
    'T':['T'],
    'U':['U'],
    'V':['V'],
    'W':['W'],
    'X':['X'],
    'XD':['modern-art',u'现代艺术'],
    'Y':['Y'],
    'Z':['Z'],
    'ZY':['dixit',u'只言片语']
}

boardgame_home = os.getenv('BG_HOME')
pageGenerator_home = os.getenv('PG_HOME')

index_variables_filename = 'index.variables.js'

js_page_folder = boardgame_home + slash + jsFolder + slash + pageFolder + slash
js_index_path = js_page_folder + index_variables_filename

#default open file only accept ascii
f = codecs.open(js_index_path,'w','utf-8')
f.write("var index_letters = [];\n")
f.write("var index_games = [];\n")
for i, letter in enumerate([chr(x) for x in range(65,91)]):
    f.write('index_letters['+str(i)+']=\''+letter+'\';\n')

for i, key in enumerate(sorted(index_dict.keys())):
    gameinfo = index_dict[key]
    gameinfo.append(key)
    if len(gameinfo) == 2:
        f.write(('index_games['+str(i)+']=[\''+gameinfo[0]+'\',\''+gameinfo[1]+'\'];\n'))
    elif len(gameinfo) == 3:
        f.write(('index_games['+str(i)+']=[\''+gameinfo[0]+'\',\''+gameinfo[1]+'\',\''+gameinfo[2]+'\'];\n'))
f.close()

print "SUCCESS!"


