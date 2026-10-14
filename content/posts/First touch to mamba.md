---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XYFUSOOP%2F20261014%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261014T144623Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD0OLMZMXveXX0%2BosSUn03QgbLjncRFNg%2BBSqEUdbWJNQIhAKBCAgEucjuQXohDXqe4FqjH3dgppxaBPMJuSF6wn4yLKogECLX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwALMLQhEqx0ahQtEMq3ANY2puqfgjnilhi5J5z9kUyqepj0l1qe1eg6JVMNuS%2FEPGgVHdntyhjb2rjBitDf0Vyjdm6vkL%2F8SrHL8NVlGbY%2BsTV0%2FjSqYkoOe8gr51WcV2sXP56ViWJqz0fdkHE4cTjccbZHZGhsegm2bY7zrOn3PtFdTfHkzKS214E1dlZ2cg9FC67E%2BYvi7%2F%2FH6P%2Fcyr%2BVoE%2BU2qcmJd57N%2FHtkl%2F4hZtfdUPRZ2h07eqBBqKb4zuGw42gKpohkst9HwJU%2FyqeH9BtShH7L%2FEje5HdCwX4fBPMqnvapnCVmUh4O6f6CPNqRDEJ4RMdJPtY%2FeS7mhlGlJUHc%2F02Td6H5YLS6aaMC2qwG9HwyISqIWtEqFRebTcxYNAhzmHHLiufK2qrowAjghMFvzoVv2dzrletbL0sfKh0plbQbCc2HxOdEhtXLYhNLgui4Dc6D0pWKRLid6nBWoj2u6VAkHJ4BQZ6m8DxdBUYxYyCfvWfe1S5m%2FvLfGDKzFYmvjjqYusdRRJGYs7MsE59lJXih8RaGJxSLxb%2FMY%2BPRWYa8%2BG80NCm8jYcU0hVfZ0aU9wdjCyEkYTv1KQVS6PfTOivoagCJ62nREeBqTyLAGx4%2F6aGfvlJxslVHkr95HnIribLdCKDTCw6r3WBjqkAdEZUKajCqRDDURRATQ9tbW2BKiKN78yxJqOwsdoZWogTOci3wwV32l1XCKpnvZfgJDORG2PPhTkUUHWr5qzhaDK%2BEUntjvXGYdxcfK3OhLBO190bpVswLjMkGAG6VTNHWLdUi7OAGVuhjjz%2BIGDhBs8YtOIrbmsLKXXKD4CM6YPaDym1Z6um%2BPZqtcZapiPc1jfSYFSrwBlIbXlT8JUGBxjCVjs&X-Amz-Signature=d2d9e39684064a82a41307aef7b5a46258b8474f2569fcf9568d44c9b207730e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
