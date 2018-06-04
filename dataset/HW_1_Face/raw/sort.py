import os
import shutil

dirname = os.path.dirname(os.path.abspath(__file__))

if not os.path.exists(os.path.join(dirname, 'train/')):
    os.mkdir(os.path.join(dirname, 'train/'))
    for i in range(2000):
        os.mkdir(os.path.join(dirname, 'train/%d' % i))
if not os.path.exists(os.path.join(dirname, 'test')):
    os.mkdir(os.path.join(dirname, 'test'))
    for i in range(2000):
        os.mkdir(os.path.join(dirname, 'test/%d' % i))

for i in range(2000):
    train_file = os.path.join(dirname, '%d_1.jpg' % i)
    test_file = os.path.join(dirname, '%d_2.jpg' % i)
    shutil.move(train_file, os.path.join(dirname, 'train/%d' % i, '%d_1.jpg' % i))
    shutil.move(test_file, os.path.join(dirname, 'test/%d/' % i, '%d_2.jpg' % i))
