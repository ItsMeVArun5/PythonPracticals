import pickle as pk
def learnData():
   # data to be stored in database
   dict_1 = {'name':'varun','age':'19'}
   dict_2 = {'Data structure':'dictionary','pickling':'serialization'}

   # database
   db = {}
   db['1'] = dict_1
   db['2'] = dict_2

   # binary file open using filepointer in append mode
   fp = open('Newfile', 'ab')

   # source, destination
   pk.dump(db, fp)
   fp.close()
def displayData():
       # binary file open using filepointer in read mode
   fp = open('Newfile', 'rb')
   db = pk.load(fp)
   for i in db:
      print(i, '=>', db[i])
   fp.close()
if __name__ == '__main__':
   learnData()
   displayData()