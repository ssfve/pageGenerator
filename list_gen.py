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
top1 = ('里斯本','lisboa')
top2 = ('神奈川学苑','kanagawa')
top3 = ('时间守望','time-stories')
top4 = ('一夜终极狼人','one-night-ultimate-werewolf')
top5 = ('权力的游戏(第二版)','game-thrones-board-game-second-edition')
gamelist = ('说明书列表','rulebook-list')

top_list.append(top1)
top_list.append(top2)
top_list.append(top3)
top_list.append(top4)
top_list.append(top5)

game = ('国王的早餐','kings-breakfast')
top_list.insert(0,game)
print top_list
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


