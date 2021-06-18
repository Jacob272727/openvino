# Model Optimizer Developer Guide

Model Optimizer is a cross-platform command-line tool that facilitates the transition between the training and deployment environment, performs static model analysis, and adjusts deep learning models for optimal execution on end-point target devices.

Model Optimizer process assumes you have a network model trained using a supported deep learning framework. The scheme below illustrates the typical workflow for deploying a trained deep learning model:

![](img/workflow_steps.png)

Inference Engine enables _deploying_ your network model trained with any of supported deep learning frameworks: Caffe\*, TensorFlow\*, Kaldi\*, MXNet\* or converted to the ONNX\* format. To perform the inference, the Inference Engine does not operate with the original model, but with its Intermediate Representation (IR), which is optimized for execution on end-point target devices. To _generate_ an IR for your trained model, the Model Optimizer tool is used.

The IR is a pair of files describing the model: 

*  <code>.xml</code> - Describes the network topology

*  <code>.bin</code> - Contains the weights and biases binary data.

> **NOTE**: Model Optimizer does not infer models. Model Optimizer is an offline tool that runs before the inference takes place.

Below is a simple command running Model Optimizer to generate an IR for the input model:

```sh
python3 mo.py --input_model INPUT_MODEL
```
To learn about all Model Optimizer parameters and conversion technics, see the [Converting a Model to IR](convert_model/Converting_Model.md) page.

> **TIP**: You also can work with the Model Optimizer inside the OpenVINO™ [Deep Learning Workbench](https://docs.openvinotoolkit.org/latest/workbench_docs_Workbench_DG_Introduction.html) (DL Workbench).
> [DL Workbench](https://docs.openvinotoolkit.org/latest/workbench_docs_Workbench_DG_Introduction.html) is a platform built upon OpenVINO™ and provides a web-based graphical environment that enables you to optimize, fine-tune, analyze, visualize, and compare 
> performance of deep learning models on various Intel® architecture
> configurations. In the DL Workbench, you can use most of OpenVINO™ toolkit components.
> <br>
> Proceed to an [easy installation from Docker](https://docs.openvinotoolkit.org/latest/workbench_docs_Workbench_DG_Install_from_Docker_Hub.html) to get started.

**Typical Next Step:** [Preparing and Optimizing your Trained Model with Model Optimizer](prepare_model/Prepare_Trained_Model.md)

## Videos

<table>
  <tr>
    <td><a href="https://www.youtube.com/watch?v=Kl1ptVb7aI8"><img alt="Model Optimizer Concept Video" src="https://img.youtube.com/vi/Kl1ptVb7aI8/0.jpg" width="220"></td>
    <td><a href="https://www.youtube.com/watch?v=BBt1rseDcy0"><img alt="Model Optimizer Basic Operation Video" src="https://img.youtube.com/vi/BBt1rseDcy0/0.jpg" width="220"></td>
    <td><a href="https://www.youtube.com/watch?v=RF8ypHyiKrY"><img alt="Choosing the Right Precision Video" src="https://img.youtube.com/vi/RF8ypHyiKrY/0.jpg" width="220"></td>
  </tr>
  <tr>
    <td><strong>Model Optimizer Concept</strong>. <br>Duration: 3:56</td>
    <td><strong>Model Optimizer Basic<br> Operation</strong>. <br>Duration: 2:57.</td>
    <td><strong>Choosing the Right Precision</strong>. <br>Duration: 4:18.</td>
  </tr>
</table>

<table>
  <tr>
    <td><iframe width="240" src="https://www.youtube.com/embed/Kl1ptVb7aI8" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
    <td><iframe width="240" src="https://www.youtube.com/embed/BBt1rseDcy0" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
    <td><iframe width="240" src="https://www.youtube.com/embed/RF8ypHyiKrY" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
  </tr>
  <tr>
    <td><strong>Model Optimizer Concept</strong>. <br>Duration: 3:56</td>
    <td><strong>Model Optimizer Basic<br> Operation</strong>. <br>Duration: 2:57.</td>
    <td><strong>Choosing the Right Precision</strong>. <br>Duration: 4:18.</td>
  </tr>
</table>
