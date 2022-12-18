#include "linear.h"

torch::Tensor linear_fp32_forward(
    torch::Tensor input,
    torch::Tensor weights) {
    auto result = torch::matmul(weights.transpose(0, 1), input);

    return result;
}