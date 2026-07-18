---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZYNOIMDJ%2F20260718%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260718T203654Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCjpCI3vPMblDfBZKA0J5djJyTBm1pRoZvfNMgABF6eywIhAM2NsUsVOHGTbjAAL15uOOGV1lCfEXAsT0shjraewX58Kv8DCH4QABoMNjM3NDIzMTgzODA1IgzGjZb3fqL8FXuhtEIq3APmZOFcEPCWeCqNvDHi8hdvQuJAvHpgvmqi%2Blsk3qiWO0LLArkSQ15%2FC11HsJ2l2d8qxKdJ47O8rj7N2QbT3qWKWRyrflvdOLeKzhIeMMG%2F44ZOII0h27csQ8JC%2Bfx3PjUdJrY4ntWCxmSjU1QBijqCLg6rWVSxFiwRO0rmIfSUSz8vctdnERM%2BqNkzkpU5zoePEEN4Y6iHZlUmvbZuAcfWypUFm8fiQUSMW2YhQh%2BdFNIUthBjVDw1a3QUy4mxMCbbzQ%2FaQD6GvLUibtrblI2Zc3vC4kbWMD57OQBXoRDIQPT2a%2FITrNX2PzLHQ7CUgckbANZ%2BGTxlQw1SLHLzKiVX%2BypYze85E1ILGw%2Bl78Gd4BjJqFzfiDSa5RFsHaNK7MffrIxlfEYCri4aNU0Mj4XznUh3pz3xluaOfb0IPpJhiSTwWWKB00M5eI%2FJBQWPoE8We4DU2wcQ%2B%2BA6QMdvAIjnHGtsRWtHMJPegACDjCWNQvC%2BZrq2DILKdApTkuEtrR%2Brullvi31WYsiTNfrlZfAWxZkzA05ZtxUSimOGO%2BZTofBp%2F%2BpOv7W%2F8OdP7fzWiGKPrKRBTZHcUSXv99unYCq4JPbcCp3p9nSaxNMHXAXsCqyDjhuDx%2F08aL443DCdxu%2FSBjqkAUcRBhhcNRBdLenZiDHWHX8Bx4D5sKctTr6Lp2eHWmE5MEqouxZPXD9ggkxd92qfBMOdGc81KVi42cI8OZgj68ttwUALpULXJH1HjNRvcNALMFmwHguviVGIblimpLxOUh%2Bmf7JKJXIdb8KJm9Kx%2Fr8i7g%2Fdo2B7rct23zBnNd4uRSwpiqpemY5KWaCAhvGpZBdxVAn3iZ2ZxCyhEv7Qkjsal02w&X-Amz-Signature=654344db9022a5e081370fc3091df467335675e01bece17be04b88cb1da11061&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

From the perceptive of the structure of mamba, this is a discrete selective space machine that runs in linear time using linear space.

lets say, matrix A is a state space matrix for the last system status h(t). we then can calculate the next h(t+1) based on the following equation:

$$
\begin{equation}h(t) = A*h(t-1) + B*x(t)\end{equation}
$$

$$
y = C*h(t)
$$

Where B is a weight for input x(t) and C is the weight for output y.

We define A matrix in a HiPPO matrix manner.

$$
A = \begin{cases} \sqrt{(2n+1)(2k+1)} && everything-below -diagonal \\
n+1 && on-diagonal \\
0 && everything-beyond-diagonal \end{cases}
$$

By doing this, we can use SVD partition for reducing the computing demand.

$$
A=V\Lambda V^* - PQ^T = V(\Lambda - (V^*P)(V^*Q)^*)V
$$

This can be done
