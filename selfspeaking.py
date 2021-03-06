import click
import keras.callbacks
import tensorflow as tf
from keras import backend as K

import dataset
import lib.log
import lib.model


def echo(*args):
    click.secho(' '.join(str(arg) for arg in args), fg='green', err=True)


@click.group()
def main():
    pass


@main.command()
@click.option('--name', help='model name')
@click.option('--resume', help='when resume learning from the snapshot')
def train(name, resume):

    # paths
    log_path = "logs/{}.json".format(name)
    out_path = "snapshots/" + name + ".{epoch:06d}.h5"
    echo('log path', log_path)
    echo('out path', out_path)

    lib.log.info(log_path, {'_commandline': {'name': name, 'resume': resume}})

    # init
    echo('train', (name, resume))
    session = tf.Session('')
    K.set_session(session)
    K.set_learning_phase(1)

    # dataset
    echo('dataset loading...')
    (x_train, y_train), (x_test, y_test) = dataset.load()

    # model building
    echo('model building...')
    model = lib.model.build()
    model.summary()
    if resume:
        echo('Resume Learning from {}'.format(resume))
        model.load_weights(resume, by_name=True)

    # training
    echo('start learning...')
    callbacks = [
        lib.log.JsonLog(log_path),
        keras.callbacks.ModelCheckpoint(out_path, monitor='val_loss', save_weights_only=True)
    ]
    model.fit(x_train, y_train, batch_size=30, epochs=10,
              callbacks=callbacks,
              validation_data=(x_test, y_test))


if __name__ == '__main__':
    main()
