from PIL import Image, ImageDraw
import sys

# first img is 'com.apalon.ringtones.png'
# first file is 'com.apalon.ringtones.xml'
if len(sys.argv) != 3 or sys.argv[1][-4:] != '.xml' or sys.argv[2][-4:] != '.png':
    print("improper arguments")
else:
    xml = sys.argv[1]
    image = Image.open(sys.argv[2])
    draw = ImageDraw.Draw(image)

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
