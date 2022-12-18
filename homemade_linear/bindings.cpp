#include <torch/extension.h>
#include "linear.h"

PYBIND11_MODULE(TORCH_EXTENSION_NAME, m) {
  m.def("linear_fp32", &linear_fp32_forward, "Linear forward (homemade)");
}
