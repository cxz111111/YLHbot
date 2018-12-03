import tensorflow as tf
import numpy as np
CAPTCHA_LEN = 3

MODEL_SAVE_PATH = 'F:1/model/'
def get_result(im):
    img = im.convert("L")
    image_array = np.array(img)
    img_data = image_array.flatten() / 255

    saver = tf.train.import_meta_graph('F:/1/model/crack_captcha.model-1200.meta')
    graph = tf.get_default_graph()
    input_holder = graph.get_tensor_by_name("data-input:0")
    keep_prob_holder = graph.get_tensor_by_name("keep-prob:0")
    predict_max_idx = graph.get_tensor_by_name("predict_max_idx:0")
    with tf.Session() as sess:
        saver.restore(sess, tf.train.latest_checkpoint(r'F:/1/model'))
        predict = sess.run(predict_max_idx, feed_dict={input_holder: [img_data], keep_prob_holder: 1.0})
    predict = np.squeeze(predict)
    if(predict[1]== 0):
        a = predict[0] + predict[2]
    elif(predict[1] ==[1]):
        a = predict[0] * predict[2]
    else:
        a = predict[0] - predict[2]
    return a