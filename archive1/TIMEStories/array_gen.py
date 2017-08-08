#coding:utf-8

from sys import argv

filename = argv[1]
output_filename = filename.rstrip('.txt') + '.py'

x_line_no = 0
part_no = 0
with open(filename,'r') as f:
	lines = f.readlines()
	for line_no in range(len(lines)):
		line = lines[line_no].strip('\n')
		if line == 'A':
			lines[line_no] = 'part['+str(part_no)+']=generate(array);\nlist_line = \'\';\n'
			x_line_no = line_no + 1
			part_no = part_no + 1
		else:
			line_no_mod = line_no - x_line_no
			lines[line_no] = ("array[" + str(line_no_mod) + "]='" + line + "';\n")

		

		
with open(output_filename,'w') as f:
	f.writelines(lines);