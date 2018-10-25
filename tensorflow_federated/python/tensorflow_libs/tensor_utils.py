# Copyright 2018, The TensorFlow Federated Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""General utilities specific to the manipulation of tensors and operators."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

# Dependency imports
import tensorflow as tf


def is_scalar(tensor):
  """Returns True iff the given tensor is a scalar.

  Args:
    tensor: The tensor to test for being a scalar.

  Returns:
    True if 'tensor' is a scalar, i.e. all dims are 1, False otherwise.

  Raises:
    TypeError: when the argument is not a tensor.
  """
  if not tf.contrib.framework.is_tensor(tensor):
    raise TypeError('Expected a tensor, found "{}".'.format(
        type(tensor).__name__))
  return (hasattr(tensor, 'get_shape') and
          all(dim == 1 for dim in tensor.get_shape()))