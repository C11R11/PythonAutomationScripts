from PIL import Image, ImageDraw

def create_sammy_frame(width, height, ball_x, ball_y, startx):
    img = Image.open('sammy.png', 'r')
    img_w, img_h = img.size
    background = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    bg_w, bg_h = background.size
    offset = ((startx - ball_x), (height - ball_y))
    offset2 = ((startx - ball_x + 70), (height - ball_y))
    background.paste(img, offset)
    background.paste(img.convert('P', palette=Image.ADAPTIVE, colors=5), offset2)
    name = 'sammy' +  str(ball_x) +  str(ball_y) + '.png'
    #background.save(name)
    return background

# Create the frames
frames = []
x, y = 0, 0
for i in range(12):
    new_frame = create_sammy_frame(400, 400, x, 200, 400)
    frames.append(new_frame)
    x += 40
    y += 40
x, y = 0, 0
for i in range(12):
    new_frame = create_sammy_frame(400, 400, -x, 100, -10)
    frames.append(new_frame)
    x += 40
    y += 40
x, y = 0, 0
for i in range(12):
    new_frame = create_sammy_frame(400, 400, x, 300, 400)
    frames.append(new_frame)
    x += 40
    y += 40

# Save into a GIF file that loops forever
frames[0].save('sammy.gif', format='GIF', append_images=frames[1:], save_all=True, duration=200, loop=0)
