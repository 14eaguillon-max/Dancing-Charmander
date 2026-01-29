import imageio.v3 as iio

filenames = ['charmander-pic1.png', 'charmander-pic2.png']
images = []

for filename in filenames:
    images.append(iio.imread(filename))

iio.imwrite('charmander_dance.gif', images, duration=500, loop=0)
