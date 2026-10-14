---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QQPXZRUZ%2F20261014%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261014T090659Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCuuUVcds6YXTtKzfdhItpvVGDpVBzG4B0BmLHtoTr%2F0QIhAKVXUgwL3HvrmoFmIvo2YrA%2FoyjuTukI8fyeoDiLt32VKogECK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyU%2BtSlfd1gKpPaWRMq3AMHtT9xB%2FmdVIUndGW%2Fm6YkKsKRZBZbnaVFp01ohPT9Z5qXn3Er5wLk%2BFqcJaKCO7UEgVvK5RGVh%2BNJFOQQDNzDsMcNUTTLfiJ73SxjPLmECDNpW0S9PDu29rYiJ%2BHEcl0Ahh6COfdXGc4efGvZMgkm4BaQnAWjVwP6iWkSl3ityuFgPStfyNSzP5qXAm%2FI34BKVBlMAdyn2dTPBsXQ3FWN3G8K5CFfA41PzbX5CDkp14IVYVDlqXfgZkicHcPoBTZz9wG3Csu%2FP9n3tLa8CVTB0VfKlGW6DYBoJmgAxuFmOU1ZiU08qRE7hwF1Zf4JUR95FYPV81CIZ83UCu%2FThKn%2FYSPdgiQX%2BAGfYPXM%2FACcUar4tmXq6Cbl1htzdiHym6KT4fqbduaYrj5PFn0biGkr1LytOt5fUuiPljGyUlwCN20tXSnydCIcF9wa%2F4SKj3CSRJFuqJSQmu6wC5AEnQvGe0IuHYkH%2F60bbdiuhKC1APKYShXD2Z9B5F%2FbYG1f75xiJo8xLO171fPZcV38DOix5oyjO2PwsRtPR3AbPVLWHHJq7Q0ZqnLWFjx2k4X%2Ff9jREqZ0Zj6UfNGtC03vocHgNzwVV1eYZe5gxSEJfKdHONv55KbOPxwgLTEVPzD50bzWBjqkATI2UcdRwatBGMt1%2Bmxj4cJQLHGJq%2B0R4qCLH9lkWpF%2FaTGydkAhCZTUT7vDUjG%2FiEJPF2H8Uee%2FRul2GlGxFJSWSZ%2FF7XeWW2vqZWCIQqojNEnDC61BSHcx8a5KZhcQdHJlbhhqRSyG154S3kFDAogA81%2BDLT8s4N6MrlDjvVU8rGWR8n%2BGTDs8sXT4po023SJUlDucqwc6oNnJw0778MVfxafs&X-Amz-Signature=7798f659a6dbed43ac9221c48e49b1432a966561de36ed599bcfdfbabf58f7bb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
