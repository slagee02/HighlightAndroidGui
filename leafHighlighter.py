from PIL import Image, ImageDraw
import sys
import re

# input should be filename of the shared name between xml and png file pair without the extension ex) insert file1 (file1.xml and file1.png)

# iterate through each provided file
for i in range(1, len(sys.argv)):
    # open the image for drawing and the xml for reading
    xml = sys.argv[i] + '.xml'
    image = Image.open(sys.argv[i] + '.png')
    draw = ImageDraw.Draw(image)

    with open(xml, mode='r') as file:
        content = file.read()
        # split xml by nodes
        lines = content.split('<node ')

        # gor though nodes
        for line in lines:

            # look for leaf nodes which end with />
            if '/>' in line:

                # get the bounds string (bounds="[num,num][num,num]")
                bounds_str = re.findall(
                    r'bounds=\"\[[0-9]+,[0-9]+\]\[[0-9]+,[0-9]+', line)[0]

                # pull out the bounds
                nums = re.findall(r'[0-9]+', bounds_str)
                nums = (int(nums[0]), int(nums[1]),
                        int(nums[2]), int(nums[3]))

                # highlight
                draw.rectangle(nums, outline=(255, 255, 0), width=8)
        image.show()
