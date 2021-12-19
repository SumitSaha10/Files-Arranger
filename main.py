import os

#creating folders
def createFolder(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

#moving files to folder
def moveFiles(folderName,files):
    for file in files:
        os.rename(file,"%s/%s"%(folderName,file))

files = os.listdir()
files.remove('main.py')

createFolder('Images')
createFolder('Media')
createFolder('Docs')
createFolder('Others')

imagesExt = ['.jpg','.png','.jpeg','.gif','.tiff','.psd','.eps','.ai','.indd','.raw']
mediaExt = ['.mp4','.mp3','.wmv','.osp','.mov','.avi','avchd','.flv','.f4v','.swf','.mkv']
docsExt = ['.txt','.pdf','.doc','.docx','.eps','exe','xlsx','.xls','.otd','.ods','.ppt','.pptx']

images = [file for file in files if os.path.splitext(file)[1].lower() in imagesExt]
media = [file for file in files if os.path.splitext(file)[1].lower() in mediaExt]
docs = [file for file in files if os.path.splitext(file)[1].lower() in docsExt]

Others = []
for file in files:
    ext = os.path.splitext(file)[1].lower()
    if (ext not in imagesExt) and (ext not in mediaExt) and (ext not in docsExt) and os.path.isfile(file):
        Others.append(file)



moveFiles('Media',media)
moveFiles('Images',images)
moveFiles('Docs',docs)
moveFiles('Others',Others)