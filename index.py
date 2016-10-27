import os
fileindex = dict()

#this function creates the index for the crawler

def index():
  #the whole directory mentioned will be checked
  for root, dirs, files in os.walk("E:/majid/"):  
    for file in files:
        if file.endswith(".txt"):
            filedir = os.path.join(root, file)
            fp=open(filedir,'r')
  for line in fp:
      for word in line.split():
       for root, dirs, files in os.walk("E:/"):
          for file in files:
              if file.endswith(".txt"):
               filedir=os.path.join(root, file)
               fpp=open(filedir,'r')
               if word in fpp.read():
                  if word in fileindex:#adding index to the map
                      # append the new number to the existing array at this slot
                      fileindex[word].append(filedir)
                  else:
                      # create a new array in this slot
                      fileindex[word] = [filedir]


def search():
    myword=raw_input("enter the word")
    print fileindex[myword]


index()
search()
