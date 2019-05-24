import tensorflow as tf

class DummyController:
    def __init__(self):
        pass

    def service(self):
        save_file = 'saved_model/model.ckpt'

        # Remove the previous weights and bias
        tf.reset_default_graph()

        # Two Variables: weights and bias
        weights = tf.Variable(tf.truncated_normal([2, 3]))
        bias = tf.Variable(tf.truncated_normal([3]))

        # Class used to save and/or restore Tensor Variables
        saver = tf.train.Saver()

        with tf.Session() as sess:
            # Load the weights and bias
            saver.restore(sess, save_file)

            # Show the values of weights and bias
            print('Weight:')
            print(sess.run(weights))
            print('Bias:')
            print(sess.run(bias))


