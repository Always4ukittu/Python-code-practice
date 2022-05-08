import os

def createifnotpresent(folder):
    if not os.path.exists(folder): # check if file already present or not
        os.makedirs(folder) # create folder 

# Changing the directories of files
def move(files, folder): 
    for file in files:
        os.replace(file, f'{folder}/{file}')

files = os.listdir() #list the directries

createifnotpresent('Image')
createifnotpresent('Docs')
createifnotpresent('Video')
createifnotpresent('Media')
createifnotpresent('Other')
createifnotpresent('Audio')

# list comprehension
imgexts = ['.png','.jpg','.png','.jpeg','.gif']
images = [ files for file in files if os.path.splitext(file)[1].lower() in imgexts]

videxts = ['.mp4','.ma4','.avi']
videos = [ files for file in files if os.path.splitext(file)[1].lower() in videxts]

audexts = ['.ma3','.ma3']
audios = [ files for file in files if os.path.splitext(file)[1].lower() in audexts]

docexts = ['.pdf','.docs','.xls','.txt']
documents = [ files for file in files if os.path.splitext(file)[1].lower() in docexts]

# for other documents 
others = []
for file in files:
    ext = os.path.splitext(file)[1].lower()
    if(ext not in imgexts) and (ext not in videxts) and (ext not in docexts) and ( ext not in audexts) and (ext not in ''):
        others.append(file)

# Replacing the destination of the files present
move(images, "Image")
move(documents, "Docs")
move(audios, "Audio")
move(videos, "Video")
move(others, "Other")
