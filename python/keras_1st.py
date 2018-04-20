"""First program in keras."""
import sys

import keras
from keras import layers, models
from keras.utils import plot_model

def create_graph(compile_model=True, visualise=False):
  inputs = layers.Input(shape=(784,), name='input_layer')

  hidden_1 = layers.Dense(64, activation='relu')(inputs)
  hidden_2 = layers.Dense(64, activation='relu')(hidden_1)
  outputs = layers.Dense(10, activation='softmax')(hidden_2)

  model = models.Model(inputs=inputs, outputs=outputs)
  if compile_model:
    model.compile(optimizer='rmsprop', loss='categorical_crossentropy',
                  metrics=['accuracy'])
  if visualise:
    # SVG(model_to_dot(model).create(prog='dot', format='svg'))
    plot_model(model, to_file='model.svg')

  return model


# Use argparse later.
def main():
  compile_model = 'dry_run' not in sys.argv
  visualise = 'visualise' in sys.argv
  create_graph(compile_model, visualise=visualise)


if __name__ == '__main__':
  main()
