# Model Optimizer Developer Guide

## Introduction 

Model Optimizer is a cross-platform command-line tool that facilitates the transition between the training and deployment environment, performs static model analysis, and adjusts deep learning models for optimal execution on end-point target devices.

Model Optimizer process assumes you have a network model trained using supported deep learning frameworks: Caffe*, TensorFlow*, Kaldi*, MXNet* or converted to the ONNX* format. Model Optimizer produces an Intermediate Representation (IR) of the network, which can be inferred with the [Inference Engine](../IE_DG/Deep_Learning_Inference_Engine_DevGuide.md).

> **NOTE**: Model Optimizer does not infer models. Model Optimizer is an offline tool that runs before the inference takes place.

The scheme below illustrates the typical workflow for deploying a trained deep learning model: 

![](img/workflow_steps.png)

The IR is a pair of files describing the model: 

*  <code>.xml</code> - Describes the network topology

*  <code>.bin</code> - Contains the weights and biases binary data.

> **TIP**: You also can work with the Model Optimizer inside the OpenVINO™ [Deep Learning Workbench](https://docs.openvinotoolkit.org/latest/workbench_docs_Workbench_DG_Introduction.html) (DL Workbench).
> [DL Workbench](https://docs.openvinotoolkit.org/latest/workbench_docs_Workbench_DG_Introduction.html) is a web-based graphical environment that enables you to optimize, fine-tune, analyze, visualize, and compare performance of deep learning models.

## Install Model Optimizer Pre-Requisites

Before runnning the Model Optimizer, you must install the Model Optimizer pre-requisites for the framework that was used to train the model.

```````{tab} Using configuration scripts


``````{tab} Linux

`````{tab} All frameworks

````{tab} Install globally
```{code-block} bash
cd <INSTALL_DIR>/deployment_tools/model_optimizer/install_prerequisites
./install_prerequisites.sh
```
````

````{tab} Install to virtual env
```{code-block} bash
cd <INSTALL_DIR>/deployment_tools/model_optimizer/install_prerequisites
virtualenv --system-site-packages -p python3 ./venv
source ./venv/bin/activate  # sh, bash, ksh, or zsh
./install_prerequisites.sh
```
````

`````

`````{tab} Caffe

````{tab} Install globally
```{code-block} bash
cd <INSTALL_DIR>/deployment_tools/model_optimizer/install_prerequisites
install_prerequisites_caffe.sh
```
````

````{tab} Install to virtual env
```{code-block} bash
cd <INSTALL_DIR>/deployment_tools/model_optimizer/install_prerequisites
install_prerequisites_caffe.sh
```
````

`````

`````{tab} Tensorflow 1.x

````{tab} Install globally
```{code-block} bash
cd <INSTALL_DIR>/deployment_tools/model_optimizer/install_prerequisites
install_prerequisites_tf.sh
```
````

````{tab} Install to virtual env
```{code-block} bash
cd <INSTALL_DIR>/deployment_tools/model_optimizer/install_prerequisites
install_prerequisites_tf.sh
```
````

`````

`````{tab} Tensorflow 2.x

````{tab} Install globally
```{code-block} bash
cd <INSTALL_DIR>/deployment_tools/model_optimizer/install_prerequisites
install_prerequisites_tf2.sh
```
````

````{tab} Install to virtual env
```{code-block} bash
cd <INSTALL_DIR>/deployment_tools/model_optimizer/install_prerequisites
install_prerequisites_tf2.sh
```
````

`````

`````{tab} MXNet

````{tab} Install globally
```{code-block} bash
cd <INSTALL_DIR>/deployment_tools/model_optimizer/install_prerequisites
install_prerequisites_mxnet.sh
```
````

````{tab} Install to virtual env
```{code-block} bash
cd <INSTALL_DIR>/deployment_tools/model_optimizer/install_prerequisites
install_prerequisites_mxnet.sh
```
````

`````

`````{tab} ONNX

````{tab} Install globally
```{code-block} bash
cd <INSTALL_DIR>/deployment_tools/model_optimizer/install_prerequisites
install_prerequisites_onnx.sh
```
````

````{tab} Install to virtual env
```{code-block} bash
cd <INSTALL_DIR>/deployment_tools/model_optimizer/install_prerequisites
install_prerequisites_onnx.sh
```
````

`````

`````{tab} Kaldi

````{tab} Install globally
```{code-block} bash
cd <INSTALL_DIR>/deployment_tools/model_optimizer/install_prerequisites
install_prerequisites_kaldi.sh
```
````

````{tab} Install to virtual env
```{code-block} bash
cd <INSTALL_DIR>/deployment_tools/model_optimizer/install_prerequisites
install_prerequisites_kaldi.sh
```
````

`````


``````

``````{tab} Windows

`````{tab} All frameworks

````{tab} Install globally
```{code-block} bat
cd <INSTALL_DIR>\deployment_tools\model_optimizer\install_prerequisites\
install_prerequisites.bat
```
````

````{tab} Install to virtual env
```{code-block} bat
cd <INSTALL_DIR>\deployment_tools\model_optimizer\install_prerequisites\
install_prerequisites.bat
```
````

`````

`````{tab} Caffe

````{tab} Install globally
```{code-block} bat
cd <INSTALL_DIR>\deployment_tools\model_optimizer\install_prerequisites\
install_prerequisites_caffe.bat
```
````

````{tab} Install to virtual env
```{code-block} bat
cd <INSTALL_DIR>\deployment_tools\model_optimizer\install_prerequisites\
install_prerequisites_caffe.bat
```
````

`````

`````{tab} Tensorflow 1.x

````{tab} Install globally
```{code-block} bat
cd <INSTALL_DIR>\deployment_tools\model_optimizer\install_prerequisites\
install_prerequisites_tf.bat
```
````

````{tab} Install to virtual env
```{code-block} bat
cd <INSTALL_DIR>\deployment_tools\model_optimizer\install_prerequisites\
install_prerequisites_tf.bat
```
````

`````

`````{tab} Tensorflow 2.x

````{tab} Install globally
```{code-block} bat
cd <INSTALL_DIR>\deployment_tools\model_optimizer\install_prerequisites\
install_prerequisites_tf2.bat
```
````

````{tab} Install to virtual env
```{code-block} bat
cd <INSTALL_DIR>\deployment_tools\model_optimizer\install_prerequisites\
install_prerequisites_tf2.bat
```
````

`````

`````{tab} MXNet

````{tab} Install globally
```{code-block} bat
cd <INSTALL_DIR>\deployment_tools\model_optimizer\install_prerequisites\
install_prerequisites_mxnet.bat
```
````

````{tab} Install to virtual env
```{code-block} bat
cd <INSTALL_DIR>\deployment_tools\model_optimizer\install_prerequisites\
install_prerequisites_mxnet.bat
```
````

`````

`````{tab} ONNX

````{tab} Install globally
```{code-block} bat
cd <INSTALL_DIR>\deployment_tools\model_optimizer\install_prerequisites\
install_prerequisites_onnx.bat
```
````

````{tab} Install to virtual env
```{code-block} bat
cd <INSTALL_DIR>\deployment_tools\model_optimizer\install_prerequisites\
install_prerequisites_onnx.bat
```
````

`````

`````{tab} Kaldi

````{tab} Install globally
```{code-block} bat
cd <INSTALL_DIR>\deployment_tools\model_optimizer\install_prerequisites\
install_prerequisites_kaldi.bat
```
````

````{tab} Install to virtual env
```{code-block} bat
cd <INSTALL_DIR>\deployment_tools\model_optimizer\install_prerequisites\
install_prerequisites_kaldi.bat
```
````

`````

``````


```````


```````{tab} Using manual configuration process


``````{tab} Linux

`````{tab} All frameworks

````{tab} Install globally
TBD
````

````{tab} Install to virtual env
TBD
````

`````

`````{tab} Caffe

````{tab} Install globally
TBD
````

````{tab} Install to virtual env
TBD
````

`````

`````{tab} Tensorflow 1.x

````{tab} Install globally
TBD
````

````{tab} Install to virtual env
TBD
````

`````

`````{tab} Tensorflow 2.x

````{tab} Install globally
TBD
````

````{tab} Install to virtual env
TBD
````

`````

`````{tab} MXNet

````{tab} Install globally
TBD
````

````{tab} Install to virtual env
TBD
````

`````

`````{tab} ONNX

````{tab} Install globally
TBD
````

````{tab} Install to virtual env
TBD
````

`````

`````{tab} Kaldi

````{tab} Install globally
TBD
````

````{tab} Install to virtual env
TBD
````

`````

``````

``````{tab} Windows

`````{tab} All frameworks

````{tab} Install globally
TBD
````

````{tab} Install to virtual env
TBD
````

`````

`````{tab} Caffe

````{tab} Install globally
TBD
````

````{tab} Install to virtual env
TBD
````

`````

`````{tab} Tensorflow 1.x

````{tab} Install globally
TBD
````

````{tab} Install to virtual env
TBD
````

`````

`````{tab} Tensorflow 2.x

````{tab} Install globally
TBD
````

````{tab} Install to virtual env
TBD
````

`````

`````{tab} MXNet

````{tab} Install globally
TBD
````

````{tab} Install to virtual env
TBD
````

`````

`````{tab} ONNX

````{tab} Install globally
TBD
````

````{tab} Install to virtual env
TBD
````

`````

`````{tab} Kaldi

````{tab} Install globally
TBD
````

````{tab} Install to virtual env
TBD
````

`````

``````


```````

## Run Model Optimizer

Use the <code>mo.py</code> script from the `<INSTALL_DIR>/deployment_tools/model_optimizer` directory to run the Model Optimizer and convert the model to the Intermediate Representation (IR): 
```sh
python3 mo.py --input_model INPUT_MODEL --output_dir <OUTPUT_MODEL_DIR>
```
You need to have have write permissions for an output directory.

> **NOTE**: Some models require using additional arguments to specify conversion parameters, such as `--input_shape`, `--scale`, `--scale_values`, `--mean_values`, `--mean_file`. To learn about when you need to use these parameters, refer to [Converting a Model Using General Conversion Parameters](Converting_Model_General.md).

To adjust the conversion process, you may use general parameters defined in the [Converting a Model Using General Conversion Parameters](Converting_Model_General.md) and 
Framework-specific parameters for:
* [Caffe](Convert_Model_From_Caffe.md),
* [TensorFlow](Convert_Model_From_TensorFlow.md),
* [MXNet](Convert_Model_From_MxNet.md),
* [ONNX](Convert_Model_From_ONNX.md),
* [Kaldi](Convert_Model_From_Kaldi.md).

## Videos

<table>
  <tr>
    <td><iframe width="220" src="https://www.youtube.com/embed/Kl1ptVb7aI8" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
    <td><iframe width="220" src="https://www.youtube.com/embed/BBt1rseDcy0" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
    <td><iframe width="220" src="https://www.youtube.com/embed/RF8ypHyiKrY" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
  </tr>
  <tr>
    <td><strong>Model Optimizer Concept</strong>. <br>Duration: 3:56</td>
    <td><strong>Model Optimizer Basic<br> Operation</strong>. <br>Duration: 2:57.</td>
    <td><strong>Choosing the Right Precision</strong>. <br>Duration: 4:18.</td>
  </tr>
</table>

```{toctree}
---
hidden:
---
prepare_model/convert_model/Converting_Model
prepare_model/customize_model_optimizer/Customize_Model_Optimizer
prepare_model/Model_Optimization_Techniques.md
prepare_model/customize_model_optimizer/Subgraph_Replacement_Model_Optimizer.md
prepare_model/Supported_Frameworks_Layers.md
prepare_model/Model_Optimizer_FAQ.md
Known_Issues_Limitations.md
```