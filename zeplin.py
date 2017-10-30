import shutil
import os

folders = ['drawable-mdpi', 'drawable-hdpi', 'drawable-xhdpi', 'drawable-xxhdpi', 'drawable-xxxhdpi']
multipliers = ['', '@1.5x', '@2x', '@3x', '@4x']

file = os.listdir('./drawable-xxxhdpi')[0]

name = file.rsplit('.', 1)[0];
extension = file.rsplit('.',1)[1];

for i in range(5):
  shutil.move('./'+folders[i]+'/'+file, './'+name+multipliers[i]+'.'+extension)
  shutil.rmtree('./'+folders[i])