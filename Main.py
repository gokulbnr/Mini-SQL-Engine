#!/usr/bin/env python

import copy
import csv
import sqlparse
import sys

dat = {}
tab = {}

def loadData(file):
	op = 0
	name = "a"
	for line in file:
		if line == "<begin_table>":
			op = 1;
		elif op == 1:
			dat[line] = [];
			op = 0;
			name = line;
		elif line == "<end_table>":
			continue
		else:
			dat[name].append(line)

def loadTable(name):
	rel = []
	file = 'files/' + name + '.csv'
	f = open(file,'r')
	d = csv,reader(f)
	for line in d:
		r = {}
		for i in xrange(len(line)):
			col = dat[name][i]
			val = int(row[i])
			r[col] = val
		rel.append(r)
	return rel

def queryHandler(query):
	dist = 0;
	query = sqlparse.parse(query)[0]
	print(query)
	word = query.tokens[0]
	word = str(word).lower()
	if word != "select":
		raise NotImplementedError('Query not supported')
	word = query.tokens[1]
	word = str(word).lower()
	tname = query.tokens[3]
	if word == "*":
		col = [];
		for vals in meta[tname]:
			col.append(tname.col)

def main():
	file = open('files/metadata.txt','r')
	loadData(file)
	for name in dat:
		tab[name] = loadTable(name)
	try:
		queryHandler(sys.argv[1])
	except Exception, err:
		print Exception, error

main()