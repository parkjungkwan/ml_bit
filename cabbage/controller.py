import numpy as np
import tensorflow as tf
from keras.models import load_model
from sklearn import datasets
from flask_restful import reqparse

class CabbageController:

    def __init__(self):
        pass

    @staticmethod
    def service_model():

        X = tf.placeholder(tf.float32, shape=[None, 4])
        Y = tf.placeholder(tf.float32, shape=[None, 1])
        W = tf.Variable(tf.random_normal([4, 1]), name="weight")
        b = tf.Variable(tf.random_normal([1]), name="bias")
        # 가설을 설정합니다.
        hypothesis = tf.matmul(X, W) + b
        # 저장된 모델을 불러오는 객체를 선언합니다.
        saver = tf.train.Saver()
        model = tf.global_variables_initializer()

        # 4가지 변수를 입력 받습니다.
        parser = reqparse.RequestParser()
        parser.add_argument('avg_temp', required=True, type=float, help='avg_temp is required')
        parser.add_argument('min_temp', required=True, type=float, help='min_temp is required')
        parser.add_argument('max_temp', required=True, type=float, help='max_temp is required')
        parser.add_argument('rain_fall', required=True, type=float, help='rain_fall is required')
        args = parser.parse_args()

        avg_temp = float(args['avg_temp'])
        min_temp = float(args['min_temp'])
        max_temp = float(args['max_temp'])
        rain_fall = float(args['rain_fall'])

        with tf.Session() as sess:
            sess.run(model)
            # 저장된 학습 모델을 파일로부터 불러옵니다.
            save_path = "cabbage/saved_model/saved.cpkt"
            saver.restore(sess, save_path)
            # 사용자의 입력 값을 이용해 배열을 만듭니다.
            data = ((avg_temp, min_temp, max_temp, rain_fall),)
            arr = np.array(data, dtype=np.float32)
            # 예측을 수행한 뒤에 그 결과를 출력합니다.
            x_data = arr[0:4]
            dict = sess.run(hypothesis, feed_dict={X: x_data})
            print(dict[0])

        result = int(dict[0])
        return result
