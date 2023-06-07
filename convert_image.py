import subprocess
name_lib = ['Pillow']
def install(name):
    subprocess.call(['pip', 'install', name])
for item in name_lib:
    install(item)

from PIL import Image

print('\33[35m', 'This program translates images into text')
while True:
    sel = input('link to the image: ')
    h = int(input('final height: '))
    w = int(input('final width: '))
    img = Image.open(sel)
    new_img = img.resize((h, w))
    img = new_img.convert('L')
    height = img.size[0]
    width = img.size[1]
    pixels = img.load()
    arr_img = []
    arr_sym = ''
    for h in range(0, height):
        for w in range(0, width):
            arr_img.append(pixels[w, h])
    def save(array, array_add):
        count = 0
        for i in array:
            if i == 0:
                array_add += '██'
            elif i < 90:
                array_add += '  '
            elif i < 120:
                array_add += '░░'
            elif i < 175:
                array_add += '▒▒'
            elif i < 225:
                array_add += '▓▓'
            else:
                array_add += '██'
            count += 1
            if count == width:
                print(array_add)
                count = 0
                array_add = ''

    print(save(arr_img, arr_sym))
    continue




