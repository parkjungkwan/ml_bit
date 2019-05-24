import numpy as np
import tensorflow as tf
from keras.models import load_model
from sklearn import datasets
from flask_restful import reqparse


class IrisController:

    def __init__(self):
        global model, graph, target_names
        model = load_model('iris/saved_model/iris_model.h5')
        graph = tf.get_default_graph()
        target_names = datasets.load_iris().target_names

    def service_model(self):

        parser = reqparse.RequestParser()
        parser.add_argument('sepal_length', required=True, type=float, help='sepal_length is required')
        parser.add_argument('sepal_width', required=True, type=float, help='sepal_width is required')
        parser.add_argument('petal_length', required=True, type=float, help='petal_length is required')
        parser.add_argument('petal_width', required=True, type=float, help='petal_width is required')
        args = parser.parse_args()

        features = [args['sepal_length'],
                    args['sepal_width'],
                    args['petal_length'],
                    args['petal_width']]
        features = np.reshape(features, (1, 4))

        with graph.as_default():
            Y_pred = model.predict_classes(features)

        result = {'species': target_names[Y_pred[0]]}
        return result