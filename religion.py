#!/usr/bin/python3

"""
Fetch rows for MS SQL, form string of names, check for pattern first, then in database
"""
import sys,os,re,multiprocessing,pymssql,pymysql

tlist = sys.argv[1]

sys.stdout = open("{}/ms/logs/{}.log".format(os.environ['HOME'],tlist),'a')

with open('names_m') as f:
	names_m = [f.replace('\n','') for f in f.readlines()]

with open('names_h') as f:
	names_h = [f.replace('\n','') for f in f.readlines()]

names_t = open('names_t').read().splitlines()


def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]

def proc_rel(table):
	try:
		 conn = pymssql.connect(server='124.123.42.71', user='sa', password='R@ylabs11@2019', database='IndiaVotes')
		#conn = pymssql.connect(server='173.249.51.122', user='ra', password='R@ylabs7@9', database='mLeaderNewII_T')
	except pymssql.InterfaceError:
		print("A MSSQLDriverException has been caught.")
		print(pymssql.InterfaceError)

	except pymssql.DatabaseError as e:
		print("A MSSQLDatabaseException has been caught.")
		print(e)

	cursor = conn.cursor()
	cursor.execute("select id,EFULLNAME,EGFULLNAME from %s" % table)

	idlist_m, idlist_h, idlist_t = [],[],[]

	for row in cursor:
		# print(row)
		vid = row[0]

		if isinstance(row[1],str):
			name_eng = re.sub(r'[^a-z ]+', ' ',row[1].lower())
		else:
			name_eng = 'NA'

		if isinstance(row[2],str):
			name_gdn_eng = re.sub(r'[^a-z ]+', ' ',row[2].lower())
		else:
			name_gdn_eng == 'NA'

		names = (name_eng+' '+name_gdn_eng).replace('  ',' ')
		match_h = re.findall(r'reddy|agarwal|purohit|goud|setty|setti|amma\b|anna\b|aiah\b|esh\b|kumar|reddy|\broy\b|gowda|gauda|appa|\bpatil\b|murthy|swamy|murty|murti|svami|natha\b|kumar|nadha\b|venkat|devi\b|rav\b|narayana|rava\b|raju\b|dakshit|sinha|nanda\b|avva\b|kant\b|kshi\b|ayya\b|vati\b|raja\b|esha\b|nadhan\b|nathan\b|ishvar|mati\b|ratna|nayar|jain|goyal|krshnana|ahuja|dran\b|reddi|veni\b|raj\b|nanda\b|shetti|singa\b|helavara|singha\b',names)
		match_m = re.findall(r'siddiq|ullah\b|ddin\b|khan\b|nnisa|abdul|abdus\b|begam|beg\b|\bvasha\b|\bshek\b|\bimam\b|saiyad|ahamad|shad\b|sultana|\btaj\b|mahamad|ddan\b|ddana\b|ddina\b|unnina\b',names)

		if len(match_m) > 0:
			rel = 'M'
		elif len(match_h) > 0:
			rel = 'H'
		else:
			if not set(names.split(' ')).isdisjoint(names_t):
				rel = 'T'
				# print(names)
			elif not set(names.split(' ')).isdisjoint(names_m):
				rel = 'M'
			elif not set(names.split(' ')).isdisjoint(names_h):
				rel = 'H'
			else:
				rel = 'NA'

		if rel == 'T':
			idlist_t.append(str(vid))


		if rel == 'M':
			idlist_m.append(str(vid))
			
			# print("updated {} {}".format(vid,rel))

		if rel == 'H':
			idlist_h.append(str(vid))

	chunks_h = list(chunks(idlist_h,30000))
	chunks_m = list(chunks(idlist_m,30000))
	chunks_t = list(chunks(idlist_t,30000))
	# print("{} {}".format(len(chunks_h),len(idlist_h)))

	i = 1
	for idlist in chunks_h:
		updstr = ','.join(idlist)
		try:
			cursor.execute("update %s set RELIGION='H' where id in (%s)"%(table,updstr))
			conn.commit()
		except pymssql.InterfaceError as e:
			print(e)

		print("Chunk: {}, table updated: {}, rows: {}, rel: {}".format(i,table,len(idlist),'H'))	
		i += 1

	i = 1
	for idlist in chunks_m:
		updstr = ','.join(idlist)
		try:
			cursor.execute("update %s set RELIGION='M' where id in (%s)"%(table,updstr))
			conn.commit()
		except pymssql.InterfaceError as e:
			print(e)

		print("Chunk: {}, table updated: {}, rows: {}, rel: {}".format(i,table,len(idlist),'M'))	
		i += 1

	i = 1
	for idlist in chunks_t:
		updstr = ','.join(idlist)
		try:
			cursor.execute("update %s set RELIGION='T' where id in (%s)"%(table,updstr))
			conn.commit()
		except pymssql.InterfaceError as e:
			print(e)

		print("Chunk: {}, table updated: {}, rows: {}, rel: {}".format(i,table,len(idlist),'T'))	
		i += 1

tables = open(tlist).read().splitlines()

# with open(tlist) as f:
# 	tables = [f.replace('\n','') for f in f.readlines()]

pool = multiprocessing.Pool()

for table in tables:
	print(table)
	pool.apply_async(proc_rel,args=(table,))

pool.close()
pool.join()

# table = 'VOTERS_7_044'
# proc_rel(table)
