array[0]='﻿G每回合玩家';
array[1]='O顺时针';
array[2]='GE轮流担任时间队长，初始队长随机。';
array[3]='G时间队长负责带领团队';
array[4]='O奔袭';
array[5]='G，奔袭包括';
array[6]='O3';
array[7]='GE个阶段：';
part[0]=generate(array);
list_line = '';
array[0]='S1 - 打开区域';
array[1]='G如果场景区';
array[2]='O有';
array[3]='GE区域卡 -> 阶段结束。';
array[4]='G如果场景区';
array[5]='O没有';
array[6]='GE区域卡 -> 阶段继续。';
array[7]='G- 找到';
array[8]='O团队指示物';
array[9]='GE所在区域对应的一叠区域卡';
array[10]='GE- 边转述第一张卡片A，边放置其余卡片';
array[11]='G- 开放的卡片';
array[12]='O正面朝上，';
array[13]='G封锁的卡片';
array[14]='OE背面朝上，';
array[15]='GE- 封锁卡片解锁后才翻开，类型详见官方规则';
array[16]='SE';
part[1]=generate(array);
list_line = '';
array[0]='S2 - 探索区域';
array[1]='G移动时间指示物';
array[2]='O1';
array[3]='GE格。';
array[4]='G所有人可以执行';
array[5]='O1';
array[6]='G个行动，分开执行顺序随意，';
array[7]='O3';
array[8]='GE选一:';
array[9]='O1、';
array[10]='GE移动到其他区域，不是1格';
array[11]='O2、';
array[12]='G执行掷骰Die Roll(试炼Test),';
array[13]='O4';
array[14]='GE个步骤:';
array[15]='GE试炼前预先设置盾牌、骷髅盾牌和试验类型标志';
array[16]='OE- 扔骰子';
array[17]='拿取你载体对应的骰子数';
array[18]='OE- 击中';
array[19]='每有1个击中标记从左往右移除1个盾牌';
array[20]='OE- 反击';
array[21]='OE- 惩罚';
array[22]='G如果试炼后玩家死亡，把玩家指示物放在时间条前';
array[23]='O7';
array[24]='GE格';
array[25]='G如果试炼成功，把区域卡';
array[26]='OE移出游戏。';
array[27]='O3、';
array[28]='GE放弃行动';
array[29]='GE所有人行动后，阶段结束，未述细节详见官方规则';
array[30]='SE';
part[2]=generate(array);
list_line = '';
array[0]='S3 - 变换区域';
array[1]='G如果';
array[2]='O不';
array[3]='G变换区域 -> 左传';
array[4]='O时间队长骰子';
array[5]='GE，进入下一回合。';
array[6]='G如果变换区域 -> 执行下面';
array[7]='O5';
array[8]='GE个动作：';
array[9]='O1、';
array[10]='GE玩家从行动区取回玩家指示物。';
array[11]='O2、';
array[12]='G移动';
array[13]='O团队指示物';
array[14]='GE至新区域。';
array[15]='O3、';
array[16]='G按顺序收好原区域卡放回牌堆';
array[17]='OE底部。';
array[18]='O4、';
array[19]='G扔';
array[20]='OE时间队长骰子。';
array[21]='G如果原区域名字为';
array[22]='O红色';
array[23]='GE,支付(骰面数量+2)个时间点';
array[24]='G如果原区域名字为';
array[25]='O白色';
array[26]='GE,支付骰面数量的时间点';
array[27]='O5、';
array[28]='G左传';
array[29]='O时间队长骰子';
array[30]='G，进入下一回合。';
array[31]='SE';
part[3]=generate(array);
list_line = '';
