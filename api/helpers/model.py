import tensorflow
import tflearn

import config
from api.helpers.singleton import singleton


@singleton
class Model:
    def __init__(self):
        tensorflow.reset_default_graph()
        if config.LEARNING_MODE or config.PLAYING_MODE:
            net = tflearn.input_data([None, 68])
            net = tflearn.fully_connected(net, 1800, activation="RElu")
            net = tflearn.fully_connected(net, 100, activation="RElu")
            net = tflearn.fully_connected(net, 2, activation="softmax")
            net = tflearn.regression(net, optimizer='Momentum', loss='mean_square', learning_rate=0.01)
        elif config.LEARNING_BOT_MODE:
            net = tflearn.input_data([None, 268])
            net = tflearn.fully_connected(net, 1800, activation="RElu")
            net = tflearn.fully_connected(net, 100, activation="RElu")
            net = tflearn.fully_connected(net, 2, activation="softmax")
            net = tflearn.regression(net, optimizer='Momentum', loss='mean_square', learning_rate=0.01)
        dnn = tflearn.DNN(net)
        self.dnn = dnn
        if config.LOADING_MODEL:
            self.load(config.PATH_DNN)

    def load(self, path=None):
        self.dnn.load(path)