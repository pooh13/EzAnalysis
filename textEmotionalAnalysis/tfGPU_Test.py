import tensorflow as tf

# ----- method 01
if tf.test.gpu_device_name():
    print('Default GPU Device: {}'.format(tf.test.gpu_device_name()))
else:
    print("Please install GPU version of TF")

# method 02
sess = tf.compat.v1.Session(config=tf.compat.v1.ConfigProto(log_device_placement=True))
print(sess)

# method 03
print(tf.test.is_built_with_cuda())

# method 04
print(tf.test.is_gpu_available(cuda_only=False,min_cuda_compute_capability=None))
