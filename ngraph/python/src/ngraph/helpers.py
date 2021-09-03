# Copyright (C) 2018-2021 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

"""nGraph helper functions."""

## @defgroup ngraph_python_helpers Helpers
# nGraph helper functions.
# @ingroup ngraph_python_api

from ngraph.impl import Function
from openvino.inference_engine import IENetwork

## @ingroup ngraph_python_helpers
def function_from_cnn(cnn_network: IENetwork) -> Function:
    """Get nGraph function from Inference Engine CNN network."""
    capsule = cnn_network._get_function_capsule()
    ng_function = Function.from_capsule(capsule)
    return ng_function

## @ingroup ngraph_python_helpers
def function_to_cnn(ng_function: Function) -> Function:
    """Get Inference Engine CNN network from nGraph function."""
    capsule = Function.to_capsule(ng_function)
    return IENetwork(capsule)
