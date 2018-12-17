## Disclaimer 
This is slightly modified version of code written by Zhen Zhu and Jian Ding.

## Installation: Docker

For easy usage I provide docker image for starting up this thing out of the box.
[Image](https://hub.docker.com/r/janchk/dota_mxnet)

## Requirements: Hardware

Any NVIDIA GPUs with at least 4GB memory should be sufficient. 


## Demo & Deformable Model

We provide trained convnet models, including Faster R-CNN models trained on DOTA.

1. To use the demo with our pre-trained faster-rcnn models for DOTA, please download manually from [Google Drive](https://drive.google.com/open?id=1b6P-UMaBBpMPlcgvc38dMToPAa_Gyu6F), or [BaiduYun](https://pan.baidu.com/s/1YuB5ib7O-Ori1ZpiGf8Egw) and put it under the following folder.

	Make sure it look like this:
	```
    ./output/rcnn/DOTA_quadrangle/DOTA_quadrangle/train/rcnn_DOTA_quadrangle-0059.params
	./output/rcnn/DOTA/DOTA/train/rcnn_DOTA_aligned-0032.params
	```

(Note) We also released the .state files recently. You can download them from [Google Drive](https://drive.google.com/open?id=1b6P-UMaBBpMPlcgvc38dMToPAa_Gyu6F), or [BaiduYun](https://pan.baidu.com/s/1YuB5ib7O-Ori1ZpiGf8Egw) and keep on fine-tuning our well-trained models on DOTA. 

## Preparation for Training & Testing

<!-- For R-FCN/Faster R-CNN\: -->

1. Please download [DOTA](https://captain-whu.github.io/DOTA/dataset.html) dataset, use the [DOTA_devkit](https://github.com/CAPTAIN-WHU/DOTA_devkit) to split the data into patches. And make sure the split images look like this:
```
./path-to-dota-split/images
./path-to-dota-split/labelTxt
./path-to-dota-split/test.txt
./path-to-dota-split/train.txt
```
The test.txt and train.txt are name of the subimages(without suffix) for train and test respectively.


2. Please download ImageNet-pretrained ResNet-v1-101 model manually from [OneDrive](https://1drv.ms/u/s!Am-5JzdW2XHzhqMEtxf1Ciym8uZ8sg), or [BaiduYun](https://pan.baidu.com/s/1YuB5ib7O-Ori1ZpiGf8Egw#list/path=%2F), or [Google drive](https://drive.google.com/open?id=1b6P-UMaBBpMPlcgvc38dMToPAa_Gyu6F), and put it under folder `./model`. Make sure it look like this:
	```
	./model/pretrained_model/resnet_v1_101-0000.params
	```



