import sqlite3

class DBBUild():
	'''Helper Class for building the db'''

	def __init__(self):

		self.conn = sqlite3.connect('../assets/tldt.db')
		self.c = self.conn.cursor()
		self.w = WordParser()
		

	def initialize(self):
		self.c.executescript("""
			create table if not exists words(
				deWord, 
				enWord
			);

			""")

		# self.conn.commit()
		return

	def insertWords(self):

		self.w.load('../assets/en-de_11.txt')
		print('doing something...')
		for tup in self.w.words:
			k,v = tup
			self.insertWordPair(k, v)
		print('done')
		return

	def insertWordPair(self, enString, deString):

		self.c.execute('INSERT INTO words VALUES (?,?)', (deString, enString))
		return

	def makeCommit(self):

		self.conn.commit()
		self.conn.close()
		print('commited!')
		return

class WordParser():

	def __init__(self):

		self.words = []

	def load(self, file):

		with open(file, 'r+') as openFile:
			for l in openFile:
				self.parse(l)


	def parse(self, line):
		# print(line)
		l = line.split('#')
		for enSyn in l[0].split(';'):
			for deSyn in l[1].split(';'):
				self.words.append((enSyn.strip(), deSyn.strip()))
		return



# class DBInsert():
# 	'''Helper Class for inserting into db'''
	

# 	def __init__(self):

# 		conn = sqlite3.connect('tldl.db')
# 		self.c = conn.cursor()

# 	def insertPerWordPair(self, deString, enString):

# 		self.c.execute('INSERT INTO words VALUES (?,?)', (deString, enString))
# 		return

# 	def makeCommit(self):

# 		self.c.commit()
# 		return


def main():

	b = DBBUild()
	b.initialize()
	b.insertWords()
	b.makeCommit()
main()