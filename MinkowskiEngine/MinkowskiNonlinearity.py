# Copyright (c) Chris Choy (chrischoy@ai.stanford.edu).
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
# of the Software, and to permit persons to whom the Software is furnished to do
# so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
# Please cite "4D Spatio-Temporal ConvNets: Minkowski Convolutional Neural
# Networks", CVPR'19 (https://arxiv.org/abs/1904.08755) if you use any part
# of the code.
import torch

from MinkowskiCommon import MinkowskiModuleBase
from MinkowskiSparseTensor import SparseTensor
from MinkowskiTensorField import TensorField


class MinkowskiNonlinearityBase(MinkowskiModuleBase):
    MODULE = None

    def __init__(self, *args, **kwargs):
        super(MinkowskiNonlinearityBase, self).__init__()
        self.module = self.MODULE(*args, **kwargs)

    def forward(self, input):
        output = self.module(input.F)
        if isinstance(input, TensorField):
            return input.__class__(
                output,
                coordinate_map_key=input.coordinate_map_key,
                coordinate_manager=input.coordinate_manager,
                inverse_mapping=input.inverse_mapping,
                quantization_mode=input.quantization_mode,
            )
        else:
            return input.__class__(
                output,
                coordinate_map_key=input.coordinate_map_key,
                coordinate_manager=input.coordinate_manager,
            )

    def __repr__(self):
        return self.__class__.__name__ + "()"


class MinkowskiReLU(MinkowskiNonlinearityBase):
    MODULE = torch.nn.ReLU


class MinkowskiPReLU(MinkowskiNonlinearityBase):
    MODULE = torch.nn.PReLU


class MinkowskiELU(MinkowskiNonlinearityBase):
    MODULE = torch.nn.ELU


class MinkowskiSELU(MinkowskiNonlinearityBase):
    MODULE = torch.nn.SELU


class MinkowskiCELU(MinkowskiNonlinearityBase):
    MODULE = torch.nn.CELU


class MinkowskiDropout(MinkowskiNonlinearityBase):
    MODULE = torch.nn.Dropout


class MinkowskiThreshold(MinkowskiNonlinearityBase):
    MODULE = torch.nn.Threshold


class MinkowskiSigmoid(MinkowskiNonlinearityBase):
    MODULE = torch.nn.Sigmoid


class MinkowskiTanh(MinkowskiNonlinearityBase):
    MODULE = torch.nn.Tanh


class MinkowskiSoftmax(MinkowskiNonlinearityBase):
    MODULE = torch.nn.Softmax
