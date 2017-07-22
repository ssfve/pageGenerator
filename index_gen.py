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
index_dict = dict()
index_dict['A']=['A']
index_dict['AW']=['The-Resistance-Avalon',u'阿瓦隆']
index_dict['B']=['B']
index_dict['BD']=['Puerto-Rico',u'波多黎各']
index_dict['BK']=['Ice-Cool',u'冰酷企鹅']
index_dict['C']=['C']
index_dict['CC']=['splendor',u'璀璨宝石']
index_dict['CY']=['inis',u'翠屿秘境']
index_dict['D']=['D']
index_dict['DF']=['monopoly',u'大富翁']
index_dict['DH']=['dahufa',u'大护法']
index_dict['DM']=['Kingdomino',u'多米诺王国']
index_dict['E']=['E']
index_dict['F']=['F']
index_dict['G']=['G']
index_dict['GW']=['kings-breakfast',u'国王的早餐']
index_dict['H']=['H']
index_dict['HH']=['hanabi',u'花火']
index_dict['HS']=['cottage-garden',u'花舍物语']
index_dict['I']=['I']
index_dict['J']=['J']
index_dict['K']=['K']
index_dict['L']=['L']
index_dict['LS']=['two-rooms-and-boom',u'两室一弹']
index_dict['LSB']=['lisboa',u'里斯本']
index_dict['LZ']=['twilight-struggle',u'冷战热斗']
index_dict['M']=['M']
index_dict['N']=['N']
index_dict['O']=['O']
index_dict['P']=['P']
index_dict['PS']=['Ponzi-Scheme',u'庞氏骗局']
index_dict['Q']=['Q']
index_dict['QL']=['game-thrones-board-game-second-edition',u'权力的游戏(第二版)']
index_dict['R']=['R']
index_dict['S']=['S']
index_dict['SJ']=['time-stories',u'时间守望']
index_dict['SN']=['kanagawa',u'神奈川学苑']
index_dict['SQSDE']=['my-first-stone-age',u'石器时代(儿童版)']
index_dict['T']=['T']
index_dict['U']=['U']
index_dict['V']=['V']
index_dict['W']=['W']
index_dict['WQ']=['lex-lemniscate',u'无穷大里的奥秘']
index_dict['WZ']=['iknow',u'我知道']
index_dict['X']=['X']
index_dict['XD']=['modern-art',u'现代艺术']
index_dict['Y']=['Y']
index_dict['YY']=['one-night-ultimate-werewolf',u'一夜终极狼人']
index_dict['Z']=['Z']
index_dict['ZY']=['dixit',u'只言片语']


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


