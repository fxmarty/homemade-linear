import torch
import torch.nn as nn

from homemade_linear import linear_fp32


class HomemadeLinear(nn.Module):
    """
    A homemade implementation of a linear layer, leveraging C++ and pybind. For now without bias.
    """

    def __init__(self, in_features: int, out_features: int):
        super().__init__(self)

        self.register_buffer(
            "weight", torch.rand(out_features, in_features)
        )  # follow the layout of `torch.nn.Linear`

    def forward(self, x: torch.tensor) -> torch.tensor:
        result = linear_fp32(x, self.weight)

        return result

    def backward(self):
        raise NotImplementedError("Backward is not supported for the homemade linear.")
