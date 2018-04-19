"""First program in keras."""
import sys
import keras
from keras import layers, models

# Add visualisation later.
# from keras.utils import plot_model

def create_graph(compile_model=True):
  inputs = layers.Input(shape=(784,), name='input_layer')
  hidden_1 = layers.Dense(64, activation='relu')(inputs)
  hidden_2 = layers.Dense(64, activation='relu')(hidden_1)
  model = models.Model(inputs=inputs, outputs=outputs)
  if compile_model:
    model.compile(optimizer='rmsprop', loss='categorical_crossentropy',
                  metrics=['accuracy'])


# Use argparse later.
def main(argv):
  compile_model = 'dry_run' not in sys.argv
  create_graph(compile_model)


if __name__ == '__main__':
  app.run(main)
