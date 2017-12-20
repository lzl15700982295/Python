# coding=utf-8

import argparse
import sys

from tensorflow.examples.tutorials.mnist import input_data

import tensorflow as tf

FLAGS = None

def main(_):
  # 导入数据
  mnist = input_data.read_data_sets(FLAGS.data_dir, one_hot=True)
  # 创建模型
  x = tf.placeholder(tf.float32, [None, 784])
        # a 2-D tensor of floating-point numbers
        # None means that a dimension can be of any length
  W = tf.Variable(tf.zeros([784, 10]))
  b = tf.Variable(tf.zeros([10]))
  # y表示预测
  y = tf.matmul(x, W) + b
        # It only takes one line to define it
  # Define loss and optimizer
  # y_表示一个样本的实际label
  y_ = tf.placeholder(tf.float32, [None, 10])

  # 用cross-entropy作为损失来衡量模型的误差
  cross_entropy = tf.reduce_mean(
      tf.nn.softmax_cross_entropy_with_logits(labels=y_, logits=y))
  # 然后使用梯度下降的方式来训练模型使得loss达到最小
  train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)
        # apply your choice of optimization algorithm to modify the variables and reduce the loss.

  sess = tf.InteractiveSession()
        # launch the model in an InteractiveSession
  tf.global_variables_initializer().run()
        # create an operation to initialize the variables

  # Train～～stochastic training
  for _ in range(1000):
    batch_xs, batch_ys = mnist.train.next_batch(100)
            # Each step of the loop,
            # we get a "batch" of one hundred random data points from our training set.
    sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})

  # Test trained model
  # argmax函数可以给出某个tensor对象在某一维熵的其数据最大值所在的索引值
  # 标签向量是0,1组成，因此最大值1所在的索引位置就是类别标签值
  correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
            # use tf.equal to check if our prediction matches the truth
            # tf.argmax(y,1) is the label our model thinks is most likely for each input,
            # while tf.argmax(y_,1) is the correct label.
  accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
  print(sess.run(accuracy, feed_dict={x: mnist.test.images,
                                      y_: mnist.test.labels}))

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('--data_dir', type=str, default='/tmp/tensorflow/mnist/input_data',
                      help='Directory for storing input data')
  FLAGS, unparsed = parser.parse_known_args()
  tf.app.run(main=main, argv=[sys.argv[0]] + unparsed)