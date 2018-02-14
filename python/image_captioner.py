# coding: utf-8
get_ipython().magic(u'matplotlib tk')
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont

# This is the same array of image filenames we'll read for the caption
# generation step
images = [
    'urban-438393_960_720.jpg',
    'the-plane-3114468_960_720.jpg',
    'electric-locomotive-3114443_960_720.jpg',
]

f, axarr = plt.subplots(ncols=2, nrows=2, figsize=(20, 10))
for index, image in enumerate(images):
  axarr[index//2][index%2].imshow(Image.open(image), interpolation="bicubic")
  axarr[index//2][index%2].grid(False)
  axarr[index//2][index%2].axis('off')
import math
import os

import tensorflow as tf

from im2txt import configuration
from im2txt import inference_wrapper
from im2txt.inference_utils import caption_generator
from im2txt.inference_utils import vocabulary
g = tf.Graph()
with g.as_default():
  model = inference_wrapper.InferenceWrapper()
  restore_fn = model.build_graph_from_config(configuration.ModelConfig(),
                                             checkpoint_path)
g.finalize()

# Create the vocabulary.
vocab = vocabulary.Vocabulary(vocab_file)
checkpoint_path = 'model/model.ckpt-2000000'
vocab_file = 'model/word_counts.txt'
g = tf.Graph()
with g.as_default():
  model = inference_wrapper.InferenceWrapper()
  restore_fn = model.build_graph_from_config(configuration.ModelConfig(),
                                             checkpoint_path)
g.finalize()

# Create the vocabulary.
vocab = vocabulary.Vocabulary(vocab_file)
with tf.Session(graph=g) as sess:
  # Load the model from checkpoint.
  restore_fn(sess)

  # Prepare the caption generator. Here we are implicitly using the default
  # beam search parameters. See caption_generator.py for a description of the
  # available beam search parameters.
  generator = caption_generator.CaptionGenerator(model, vocab)

  for filename in images:
    with tf.gfile.GFile(filename, "rb") as f:
      image = f.read()
    captions = generator.beam_search(sess, image)

    # Just take the first caption and display it
    caption = captions[0]
    sentence = [vocab.id_to_word(w) for w in caption.sentence[1:-1]]
    sentence = " ".join(sentence)

    plt.figure(figsize=(7,7))
    plt.imshow(Image.open(filename))
    plt.grid(False)
    plt.axis('off')
    plt.title(sentence)
    plt.show()

plt.close
plt.close()
plt.close()
plt.close()
def show_captions(filename):
  with tf.Session(graph=g) as sess:
    # Load the model from checkpoint.
    restore_fn(sess)

    # Prepare the caption generator. Here we are implicitly using the default
    # beam search parameters. See caption_generator.py for a description of the
    # available beam search parameters.
    generator = caption_generator.CaptionGenerator(model, vocab)

    with tf.gfile.GFile(filename, "rb") as f:
      image = f.read()
    captions = generator.beam_search(sess, image)
    # Just take the first caption and display it
    caption = captions[0]
    sentence = [vocab.id_to_word(w) for w in caption.sentence[1:-1]]
    sentence = " ".join(sentence)

    plt.figure(figsize=(7,7))
    plt.imshow(Image.open(filename))
    plt.grid(False)
    plt.axis('off')
    plt.title(sentence)
    plt.show()

filename
filenames
images
def get_an_image(base='/usr/local/google/home/smahabole/Pictures/', path='background/'):
    img_path = os.path.join(base, path)
    for img in os.listdir(img_path):
        if img.split(os.path.extsep)[-1] in image_formats:
            yield img

def get_an_image(base='/usr/local/google/home/smahabole/Pictures/', path='background/'):
    img_path = os.path.join(base, path)
    if not isinstance(image_formats, list):
        image_formats = ['jpg', 'jpeg', 'gif', 'png']
    for img in os.listdir(img_path):
        if img.split(os.path.extsep)[-1] in image_formats:
            yield img


def get_an_image(base='/usr/local/google/home/smahabole/Pictures/', path='background/', reset=False):
    if reset:
        return None  # Should clear the for loop below?
    img_path = os.path.join(base, path)
    if not isinstance(image_formats, list):
        image_formats = ['jpg', 'jpeg', 'gif', 'png']
    for img in os.listdir(img_path):
        if img.split(os.path.extsep)[-1] in image_formats:
            yield img



def get_an_image(base='/usr/local/google/home/smahabole/Pictures/', path='background/', reset=False):
    if reset:
        return  # Should clear the for loop below?
    img_path = os.path.join(base, path)
    if not isinstance(image_formats, list):
        image_formats = ['jpg', 'jpeg', 'gif', 'png']
    for img in os.listdir(img_path):
        if img.split(os.path.extsep)[-1] in image_formats:
            yield img



get_an_image()
foo = get_an_image()
foo.next()
def get_an_image(base='/usr/local/google/home/smahabole/Pictures/', path='background/', image_formats=None, reset=False):
    if reset:
        return  # Should clear the for loop below?
    img_path = os.path.join(base, path)
    if not isinstance(image_formats, list):
        image_formats = ['jpg', 'jpeg', 'gif', 'png']
    for img in os.listdir(img_path):
        if img.split(os.path.extsep)[-1] in image_formats:
            yield img



foo = get_an_image()
foo.next()
foo.next()
foo = get_an_image(reset=True)
foo
foo.next()
def get_an_image(base='/usr/local/google/home/smahabole/Pictures/', path='background/', image_formats=None, reset=False):
    if reset:
        return  # Should clear the for loop below? Kinda useless.
    img_path = os.path.join(base, path)
    if not isinstance(image_formats, list):
        image_formats = ['jpg', 'jpeg', 'gif', 'png']
    for img in os.listdir(img_path):
        if img.split(os.path.extsep)[-1] in image_formats:
            yield os.path.abspath(img)




foo = get_an_image(reset=True)
foo = get_an_image()
foo.next()
foo.next()
foo.next()
bar = get_an_image()
bar.next()
get_ipython().magic(u'pinfo foo.send')
foo.send(reset=True)
foo.send(True)
foo.next()
foo = get_an_image()
show_captions(foo.next())
get_ipython().magic(u'ls /usr/local/google/home/smahabole/work/image_caption/DayInSmokies-12.jpg')
foo.next()
img
def get_an_image(base='/usr/local/google/home/smahabole/Pictures/', path='background/', image_formats=None, reset=False):
    if reset:
        return  # Should clear the for loop below? Kinda useless.
    img_path = os.path.join(base, path)
    if not isinstance(image_formats, list):
        image_formats = ['jpg', 'jpeg', 'gif', 'png']
    for img in os.listdir(img_path):
        if img.split(os.path.extsep)[-1] in image_formats:
            yield os.path.join(img_path, img)





foo = get_an_image()
foo.next()
get_ipython().magic(u'ls foo.next()')
show_captions(foo.next())
show_captions(foo.next())
show_captions(foo.next())
show_captions(foo.next())
show_captions(foo.next())
show_captions(foo.next())
show_captions(foo.next())
show_captions(foo.next())
show_captions(foo.next())
bar = get_an_image(path='g')
show_captions(bar.next())
def get_an_image(base='/usr/local/google/home/smahabole/Pictures/', path='background/', image_formats=None, reset=False):
    if reset:
        return  # Should clear the for loop below? Kinda useless.
    img_path = os.path.join(base, path)
    if not isinstance(image_formats, list):
        image_formats = ['jpg', 'jpeg', 'png']  # Try adding gif here!
    for img in os.listdir(img_path):
        if img.split(os.path.extsep)[-1] in image_formats:
            yield os.path.join(img_path, img)





bar = get_an_image(path='g')
show_captions(bar.next())
show_captions(bar.next())
show_captions(bar.next())
show_captions(bar.next())
show_captions(bar.next())
show_captions(bar.next())
