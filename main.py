import os

def rename():

#le chemin ou sont tes fichiers

    chemin='/Users/massino/Desktop/redha/-_COMMENTAIR_AA24056577/'
    arr = os.listdir(chemin)
    for item in arr:

      filename=item
      base=os.path.basename(chemin+filename)
      print(base)
      print(type(os.path.splitext(base)))
      nom=os.path.splitext(base)[0]
      ext=os.path.splitext(base)[1]
      print(nom)
      print(ext)
      newname=""
      for i in range(13,len(nom)):
         newname=newname+nom[i]

      print(newname)
      os.rename(r''+chemin+nom+ext,
              r'/Users/massino/Desktop/redha/newRename/'+newname+ext)


if __name__ == '__main__':
    rename()


