#coding:utf-8

from sys import argv
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import os

jsFolder = 'js'
pageFolder = 'page'
slash = '/'

boardgame_home = os.getenv('BG_HOME')
pageGenerator_home = os.getenv('PG_HOME')

hotlist_variables_filename = 'hotlist.variables.js'

js_page_folder = boardgame_home + slash + jsFolder + slash + pageFolder + slash
js_hotlist_path = js_page_folder + hotlist_variables_filename

top_list=[]
top1 = ('拼布艺术','Patchwork')
top2 = ('约德尔战斗学院','Mechs-vs.-Minions')
top3 = ('火星开发计划','Terraforming-Mars')
top4 = ('加拿大棋','Crokinole')
gamelist = ('说明书列表','rulebook-list')

top_list.append(top1)
top_list.append(top2)
top_list.append(top3)
top_list.append(top4)
#top_list.append(top5)

game = ('拉密','Rummikub')
#game = ('伊斯坦布尔','Istanbul')
#game = ('国王的早餐','kings-breakfast')
#game = ('我知道','iknow')
#game = ('两室一弹','two-rooms-and-boom')
#game=('无穷大里的奥秘','lex-lemniscate')
#game=('翠屿秘境','inis')
#game=('冷战热斗','twilight-struggle')
#game=('权力的游戏(第二版)','game-thrones-board-game-second-edition')
#game=('大护法','dahufa')
#game = ('波多黎各','Puerto-Rico')
#game = ('冰酷企鹅','Ice-Cool')
#game = ('多米诺王国','Kingdomino')
#game = ('庞氏骗局','Ponzi-Scheme')
#game = ('七大奇迹','7-Wonders')
#game = ('圣托里尼','Santorini')
#game = ('东海道','Tokaido')
#game = ('火星开发计划','Terraforming-Mars')
#game = ('拼布艺术','Patchwork')
#game = ('卡卡颂','Carcassonne')
#game = ('约德尔战斗学院','Mechs-vs.-Minions')
#game = ('香料之路','Century-Spice-Road')
top_list.insert(0,game)
#print top_list
with open(js_hotlist_path,'w') as f:
    f.write("var hot_arrayEN = [];\n")
    f.write("var hot_arrayCN = [];\n")
    f.write("hot_arrayCN[0] = \'"+top_list[0][0]+"\';\n")
    f.write("hot_arrayCN[1] = \'"+top_list[1][0]+"\';\n")
    f.write("hot_arrayCN[2] = \'"+top_list[2][0]+"\';\n")
    f.write("hot_arrayCN[3] = \'"+top_list[3][0]+"\';\n")
    f.write("hot_arrayCN[4] = \'"+top_list[4][0]+"\';\n")
    f.write("hot_arrayCN[5] = \'"+gamelist[0]+"\';\n")

    f.write("hot_arrayEN[0] = \'"+top_list[0][1]+"\';\n")
    f.write("hot_arrayEN[1] = \'"+top_list[1][1]+"\';\n")
    f.write("hot_arrayEN[2] = \'"+top_list[2][1]+"\';\n")
    f.write("hot_arrayEN[3] = \'"+top_list[3][1]+"\';\n")
    f.write("hot_arrayEN[4] = \'"+top_list[4][1]+"\';\n")
    f.write("hot_arrayEN[5] = \'"+gamelist[1]+"\';\n")

print "SUCCESS!"


