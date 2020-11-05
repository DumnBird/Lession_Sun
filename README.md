Demo for network implement and modification

1、ResNet34-ImageNet文件夹

image_processing.py: imagenet_data.py dataset.py 这3个是ImageNet数据导入部分所需代码

convert_Pytorch_pthFile_to_tf_npyFile.py: 将Pytorhc的.pth预训练参数转化为.npy文件

net.py: 利用导入npy中的参数，构建Tensorflow ResNet34 for ImageNet模型，并微调训练4个epoch

rerun_restnet34_orig.py: 利用net.py保存的模型，进行前向推断（不训练，只推断）

2、ResNet34-Cifar-10文件夹

resnet34.py: 修改后的ResNet34 for Cifar-10模型代码(从头开始训练）

cifar10_input.py: Cifar-10数据导入代码

cifar-10-batches-bin:对应的Cifar-10数据（约170M）
如果下不了，可以试下百度云下载
下载链接：（约170M，下载后放在ResNet34-Cifar-10文件夹中） 链接：https://pan.baidu.com/s/1n8MKFO_qJGydwb7uJNnkrQ 提取码：bmnd
