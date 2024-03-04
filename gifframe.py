from PIL import Image

num_key_frames = 7

with Image.open('cha2.gif') as im:
    for i in range(num_key_frames):
        im.seek(im.n_frames // num_key_frames * i)
        im.save('{}.png'.format(i))