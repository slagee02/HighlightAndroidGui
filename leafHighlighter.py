from PIL import Image, ImageDraw

image = Image.open('com.apalon.ringtones.png')
draw = ImageDraw.Draw(image)
xml = 'com.apalon.ringtones.xml'

file = open(xml, 'r')
with open(xml, mode='r') as file:
    content = file.read()
    lines = content.split('<node ')
    count = 0  # just to count leafs
    for line in lines:

        if '/>' in line:  # leaf
            # get bounds
            count += 1
            bounds = line.partition(" ")[0]

            # DO THIS MORE EFFICIENTLY
            bounds = bounds.split('"')[1]
            bounds = bounds.replace('[', '')
            bounds = bounds.replace(']', ',')
            bounds = bounds.split(',')
            bounds = (int(bounds[0]), int(bounds[1]),
                      int(bounds[2]), int(bounds[3]))
            draw.rectangle(bounds, outline=(255, 255, 0), width=8)
# print(count)
image.show()
