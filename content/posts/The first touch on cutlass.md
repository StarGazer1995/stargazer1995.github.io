---
created: 2024-07-04T01:57:00+00:00
categories:
  - Blog
tags:
  - Notion
updated: 2024-07-04T02:12:00+00:00
date: 2024-07-04T01:57:00+00:00
title: The first touch on cutlass
id: e919ce11-7f73-454d-9b73-0e363e10990a
---

# Introduction

This is the very first touch for me to learn how to use cutlass and how it works. Until this moment, there is a little textbook teach us how to use cutlass and how to develop with it. So most of the paper I read are from Zhihu and official. As the first touch on cutlass, I would not dig deep into how to manipulate the cutlass.

# Why cutlass?

I try to avoid cliche. It just because the cutlass is the only high performance open-source computing library we can use on Nvidia’s chips. You need to master it if interested in HPC( high performance computing) or model deployment.

# The first lesson

Official examples are good for us, the beginner, to learn how to use the library. I started read the code from example of `basic_gemm` . The core of the example is quite simple: achieve gemm call.

```c++
/// Define a CUTLASS GEMM template and launch a GEMM kernel.
cudaError_t CutlassSgemmNN(
  int M,
  int N,
  int K,
  float alpha,
  float const *A,
  int lda,
  float const *B,
  int ldb,
  float beta,
  float *C,
  int ldc) {

  // Define type definition for single-precision CUTLASS GEMM with column-major
  // input matrices and 128x128x8 threadblock tile size (chosen by default).
  //
  // To keep the interface manageable, several helpers are defined for plausible compositions
  // including the following example for single-precision GEMM. Typical values are used as
  // default template arguments. See `cutlass/gemm/device/default_gemm_configuration.h` for more details.
  //
  // To view the full gemm device API interface, see `cutlass/gemm/device/gemm.h`
//----------------------define problem dimension-------------------//
  using ColumnMajor = cutlass::layout::ColumnMajor;

  using CutlassGemm = cutlass::gemm::device::Gemm<float,        // Data-type of A matrix
                                                  ColumnMajor,  // Layout of A matrix
                                                  float,        // Data-type of B matrix
                                                  ColumnMajor,  // Layout of B matrix
                                                  float,        // Data-type of C matrix
                                                  ColumnMajor>; // Layout of C matrix

  // Define a CUTLASS GEMM type
  CutlassGemm gemm_operator;

  // Construct the CUTLASS GEMM arguments object.
  //
  // One of CUTLASS's design patterns is to define gemm argument objects that are constructible
  // in host code and passed to kernels by value. These may include pointers, strides, scalars,
  // and other arguments needed by Gemm and its components.
  //
  // The benefits of this pattern are (1.) a structured, composable strategy for passing host-constructible
  // arguments to kernels and (2.) minimized initialization overhead on kernel entry.
  //
  CutlassGemm::Arguments args({M , N, K},  // Gemm Problem dimensions
                              {A, lda},    // Tensor-ref for source matrix A
                              {B, ldb},    // Tensor-ref for source matrix B
                              {C, ldc},    // Tensor-ref for source matrix C
                              {C, ldc},    // Tensor-ref for destination matrix D (may be different memory than source C matrix)
                              {alpha, beta}); // Scalars used in the Epilogue
	//-------------------call gemm operation -------------------//
  //
  // Launch the CUTLASS GEMM kernel.
  //

  cutlass::Status status = gemm_operator(args);
	//--------------------retrieve gemm results-----------------//
  //
  // Return a cudaError_t if the CUTLASS GEMM operator returned an error code.
  //

  if (status != cutlass::Status::kSuccess) {
    return cudaErrorUnknown;
  }

  // Return success, if no errors were encountered.
  return cudaSuccess;
}
```

It only does 3 jobs: implement the gemm function based on the problem dimensions, call the function, and retrieve computing result.

It is quite simple but far from usable. It hard for programmers to maintain the code because they have to remember every input parameters. It is nice to have a data structure that wraps the data. In the cutlass, it follow the convention that use tensor as the basic data structure. In the example of `cutlass_utilities` we can define a tensor using the following code.

```c++
// Defines cutlass::HostTensor<>
#include "cutlass/util/host_tensor.h"
// Defines cutlass::half_t
#include "cutlass/numeric_types.h"

using half_t = cutlass::half_t;
using ColumnMajor = cutlass::layout::ColumnMajor;
cutlass::HostTensor<half_t, ColumnMajor> A(cutlass::MatrixCoord(M, K));
```

We can access the data of tensor using the following api.

```c++
  /// Accesses the tensor reference pointing to data
  TensorView host_view(LongIndex ptr_element_offset=0) {
    return TensorView(host_data_ptr_offset(ptr_element_offset), layout_, extent_);
  }

  /// Accesses the tensor reference pointing to data
  ConstTensorView host_view(LongIndex ptr_element_offset=0) const {
    return ConstTensorView(host_data_ptr_offset(ptr_element_offset), layout_, extent_);
  }

  /// Accesses the tensor reference pointing to data
  TensorView device_view(LongIndex ptr_element_offset=0) {
    return TensorView(device_data_ptr_offset(ptr_element_offset), layout_, extent_);
  }

  /// Accesses the tensor reference pointing to data
  ConstTensorView device_view(LongIndex ptr_element_offset=0) const {
    return ConstTensorView(device_data_ptr_offset(ptr_element_offset), layout_, extent_);
  }
```

Then, we can call the gemm operation.

```c++
  result = cutlass_hgemm_nn(
    M,
    N,
    K,
    alpha,
    A.device_data(),
    A.stride(0),
    B.device_data(),
    B.stride(0),
    beta,
    C_cutlass.device_data(),
    C_cutlass.stride(0)
  );

  cudaError_t cutlass_hgemm_nn(
  int M,
  int N,
  int K,
  cutlass::half_t alpha,
  cutlass::half_t const *A,
  cutlass::layout::ColumnMajor::Stride::Index lda,
  cutlass::half_t const *B,
  cutlass::layout::ColumnMajor::Stride::Index ldb,
  cutlass::half_t beta,
  cutlass::half_t *C,
  cutlass::layout::ColumnMajor::Stride::Index ldc) {

  // Define the GEMM operation
  using Gemm = cutlass::gemm::device::Gemm<
    cutlass::half_t,                           // ElementA
    cutlass::layout::ColumnMajor,              // LayoutA
    cutlass::half_t,                           // ElementB
    cutlass::layout::ColumnMajor,              // LayoutB
    cutlass::half_t,                           // ElementOutput
    cutlass::layout::ColumnMajor               // LayoutOutput
  >;

  Gemm gemm_op;

  cutlass::Status status = gemm_op({
    {M, N, K},
    {A, lda},
    {B, ldb},
    {C, ldc},
    {C, ldc},
    {alpha, beta}
  });

  if (status != cutlass::Status::kSuccess) {
    return cudaErrorUnknown;
  }

  return cudaSuccess;
}
```

Driving manually:

- Smooth — it drives better than my father’s F18
- Quite — Because it is a electrified vehicle
- Easy to handle — familiar BMW feeling

Driving with ADAS[5AU]:

The feeling about 5AU is complex. I love it can save my energy on highway. But I would have to take some risks or failures we may encountered.

- [risk]: too close to vehicle when lane change.
- [failure]: going to another lane when curvature is large
- [failure]: do not change back after taking off.

We would engage 5AU only on familiar highway. So, there is no over trust. When comparing with Tesla’s system, 5AU is not that smart.
