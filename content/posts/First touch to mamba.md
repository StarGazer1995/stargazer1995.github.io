---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XAVN46CK%2F20260617%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260617T165151Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHaJs25GdtvRPxDR16GvEJBtnfGcBzxqdgLTN6lI9OfkAiBTQMCzWpMVE7uIJRXxdYbHpTEK75B%2BVZz6DhR1K8U0%2BSqIBAiR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM2aXp3oTRr%2B1hwaYqKtwDgnYNBpnB%2BNoY5WH02qnTcMUPzh5t7IpcWJ5wFi4d5GXaWCldzM5TPU6%2BvwfAuT8q8B0H2%2F2tSDhMB83MUcamYDoC6xISp9QFOWYCZ5Svqmb7LeY1at6WtsYgUlB1R9Oz3UWzzgtJl1N%2Byx0v2w%2BI%2FhQjcXDQnYJnmeP5zmxukh1hli7CSF23%2BIMFLDyNg7O92syYQ32a63L%2FJADZrDP6P1WC%2B3dNwOfIzp2zZi89VhhpxXMxJBqOs%2BgxYREbRSHMgBDA8A%2FpB7b4wFdpApVyaZjTlDIeyCYy2WvYaBRJKT3Ekq2mbgDgUnR7SPK98Uxg9mEqqOdXoWYGZldGQ3zkfBUZdhtqPzgRJ0olzat7neBbRDQ6EzKNv3szWUMGRPV4weCbRJIQUviC2bMdC%2FeSp969d4HF%2B2oWbV2BqF9SI3xNyX%2FptLJcBQuudVIOZ7ip1GMKaqT4Jy12uftOQX5ZjgE%2BtNP4Q%2BdTnbnd6ipWJaFCXQEFA2krHnphb7ihSstusxZQt9d%2BZhxg5XqH1bAVG5j7p5l4RwMHRYErsJn56k3oKYm1yOStNBMShBo5SmoXNiFT%2B%2BgZHtX9bkvW%2Bxhji5%2F4pG%2FnL5ynRkcQwsjTHWkQ0VP0jQ%2B2J3e5mkAw%2FYPL0QY6pgERyly7ZrXYSQwxXDZCAY4BgFapUjfCFFbEn9NQIPrT2pbmRYugiv1tyKqsQZGOmydMRC%2F3q5qnZZ2NirNuSgJSoDCOg%2BO5UGK%2BJQwnAdAdpUbvSMpeAmVAa2InxEqlCqOwoGnZ5bdXfnFdfT9yi3BSZcR4bUmrbGc35v7pE882tOjaBEgS%2Bct1sd5CMvLzaUjxl2RDGYwRxNTHu7F41dlwSaS85KIP&X-Amz-Signature=0ebab5e54b89beab47a3dae1eaeaa012c271d1e44527bb4e55ce17c826a4777f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
