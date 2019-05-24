Tensorflow 모델을 훈련시키려면 많은 시간이 소요됩니다.
문제는 TensorFlow의 Session을 닫으면 훈련된 모든 Weights와 Bias들을 잃게 된다는데 있습니다.
나중에 모델을 사용하기 위해서는 Tensorflow 모델을 저장할 필요가 있습니다.

Tensor 변수 weights와 bias는 tf.truncated_normal() 함수를 사용하여 임의의 값으로 설정됩니다.
설정된 값들은 tf.train.Saver.save () 함수를 사용하여 save_file의 값인 "model.ckpt"에 저장됩니다.

( ".ckpt"확장자는 "check point"를 의미합니다.)