import tensorflow as tf
import os
# __file__ refers to the file settings.py
APP_ROOT = os.path.dirname(os.path.abspath(__file__))   # refers to application_top
APP_MODEL = os.path.join(APP_ROOT, 'ai_calc')

class CalculatorController:

    def __init__(self, num1, num2, opcode):
        self._num1 = num1
        self._num2 = num2
        self._opcode = opcode

    def calc(self):
        num1 = self._num1
        num2 = self._num2
        opcode = self._opcode
        print("컨트롤러 내부 {} {} {} ".format(num1, opcode, num2))

        with tf.Session() as sess:
            # First let's load meta graph and restore weights
            saver = tf.train.import_meta_graph('ai_calc/saved_'+opcode+'/model-1000.meta')
            saver.restore(sess, tf.train.latest_checkpoint('ai_calc/saved_'+opcode+'/'))

            # Now, let's access and create placeholders variables and
            # create feed-dict to feed new data

            graph = tf.get_default_graph()
            w1 = graph.get_tensor_by_name("w1:0")
            w2 = graph.get_tensor_by_name("w2:0")
            feed_dict = {w1: self._num1, w2: self._num2}

            # Now, access the op that you want to run.

            op_to_restore = graph.get_tensor_by_name("op_"+opcode+":0") # 바깥쪽에 없어도 가능
            result = sess.run(op_to_restore, feed_dict)
            print('결과 :: {}'.format(result))
        return result


"""

        opcode = self._opcode

        if opcode == 'plus':
            op_to_restore = graph.get_tensor_by_name("op_add:0")
            add_on_op = tf.add(op_to_restore, 2)
        elif opcode == 'minus':
            op_to_restore = graph.get_tensor_by_name("op_sub:0")
        elif opcode == 'multi':
            op_to_restore = graph.get_tensor_by_name("op_mul:0")
            add_on_op = tf.multiply(op_to_restore, 2)
        elif opcode == 'divid':
            op_to_restore = graph.get_tensor_by_name("op_div:0")
        result = sess.run(add_on_op, feed_dict)

        return int(result)


    @property
    def num1(self)-> object: return self._num1

    @num1.setter
    def num1(self, num1): self._num1 = num1

    @property
    def num2(self)-> object: return self._num2

    @num2.setter
    def num2(self, num2): self._num2 = num2

    @property
    def opcode(self)-> object: return self._opcode

    @opcode.setter
    def opcode(self, opcode): self._opcode = opcode
"""
