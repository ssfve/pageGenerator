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
index_dict['CC']=['Splendor',u'璀璨宝石']
index_dict['CP']=['Ticket-to-Ride',u'车票之旅']
index_dict['CY']=['Inis',u'翠屿秘境']
index_dict['D']=['D']
index_dict['DFQ']=['Coda',u'达芬奇密码']
index_dict['DFW']=['Monopoly',u'大富翁']
index_dict['DHF']=['dahufa',u'大护法']
index_dict['DHD']=['Tokaido',u'东海道']
index_dict['DM']=['Kingdomino',u'多米诺王国']
index_dict['E']=['E']
index_dict['F']=['F']
index_dict['G']=['G']
index_dict['GW']=['kings-breakfast',u'国王的早餐']
index_dict['H']=['H']
index_dict['HH']=['Hanabi',u'花火']
index_dict['HS']=['cottage-garden',u'花舍物语']
index_dict['HX']=['Terraforming-Mars',u'火星开发计划']
index_dict['I']=['I']
index_dict['J']=['J']
index_dict['JBD']=['Forbidden-Island',u'禁闭岛']
index_dict['JBSM']=['Forbidden-Desert',u'禁闭沙漠']
index_dict['JD']=['Blokus',u'角斗士']
index_dict['JN']=['Crokinole',u'加拿大棋']
index_dict['JZ']=['Famiglia',u'家族']
index_dict['K']=['K']
index_dict['KK']=['Carcassonne',u'卡卡颂']
index_dict['KT']=['Catan',u'卡坦岛']
index_dict['L']=['L']
index_dict['LH']=['Tigris-&-Euphrates',u'两河流域']
index_dict['LM']=['Rummikub',u'拉密']
index_dict['LS']=['two-rooms-and-boom',u'两室一弹']
index_dict['LSB']=['lisboa',u'里斯本']
index_dict['LZ']=['twilight-struggle',u'冷战热斗']
index_dict['M']=['M']
index_dict['MN']=['Manila',u'马尼拉']
index_dict['N']=['N']
index_dict['O']=['O']
index_dict['P']=['P']
index_dict['PB']=['Patchwork',u'拼布艺术']
index_dict['PS']=['Ponzi-Scheme',u'庞氏骗局']
index_dict['Q']=['Q']
index_dict['QD']=['7-Wonders',u'七大奇迹']
index_dict['QL']=['A-Game-of-Thrones-The-Board-Game-Second-Edition',u'权力的游戏(第二版)']
index_dict['QS']=['Love-Letter',u'情书']
index_dict['R']=['R']
index_dict['S']=['S']
index_dict['SJSW']=['time-stories',u'时间守望']
index_dict['SJX']=['Timeline-Inventions',u'时间线：发明']
index_dict['SN']=['kanagawa',u'神奈川学苑']
index_dict['SQSDE']=['my-first-stone-age',u'石器时代(儿童版)']
index_dict['ST']=['Santorini',u'圣托里尼']
index_dict['T']=['T']
index_dict['TT']=['Jungle-Speed',u'图腾快手']
index_dict['U']=['U']
index_dict['V']=['V']
index_dict['W']=['W']
index_dict['WQ']=['lex-lemniscate',u'无穷大里的奥秘']
index_dict['WQSSR']=['13Days:TheCubanMissileCrisis',u'危情13日:古巴导弹危机',]
index_dict['WZ']=['iknow',u'我知道']
index_dict['X']=['X']
index_dict['XBW']=['Crabs!',u'蟹霸王',]
index_dict['XD']=['modern-art',u'现代艺术']
index_dict['XL']=['Century-Spice-Road',u'香料之路']
index_dict['XT']=['Stop-Thief!',u'小偷别跑']
index_dict['Y']=['Y']
index_dict['YD']=['Mechs-vs.-Minions',u'约德尔战斗学院']
index_dict['YS']=['Istanbul',u'伊斯坦布尔']
index_dict['YY']=['One-Night-Ultimate-Werewolf',u'一夜终极狼人']
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


