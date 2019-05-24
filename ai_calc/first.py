import tensorflow as tf


class First:

    def __init__(self):
        pass

    @staticmethod
    def execute():
        w1 = tf.placeholder(tf.float32, name='w1')
        w2 = tf.placeholder(tf.float32, name='w2')
        # b1 = tf.Variable(2.0, dtype=tf.float32, name='bias')
        feed_dict = {'w1': 4.0, 'w2': 8.0}
        w3 = tf.multiply(w1, w2, name='op_multiply')
        sess = tf.Session()
        sess.run(tf.global_variables_initializer())
        saver = tf.train.Saver()
        result = sess.run(w3, {w1: feed_dict['w1'], w2: feed_dict['w2']})
        print(" 결과 : {}".format(result))

        saver.save(sess, './saved/model', global_step=1000)
