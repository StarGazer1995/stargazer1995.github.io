---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QIDPRHLP%2F20260817%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260817T141720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHwaCXVzLXdlc3QtMiJHMEUCIA%2FuTqaNUJrBAdHMFhnqrvMKfaMMkjrdSA4Yr1tA8ybcAiEAp%2BJMDuxBtkDN%2Fxx9mLaV%2BlikzXx2%2FKxfU%2BcQa%2Ban7yIq%2FwMIRRAAGgw2Mzc0MjMxODM4MDUiDCYGlzNKm75ItI6styrcA%2FSISyU1YQ%2Bx8u7V9%2Ftp1B3oSErrmr4ozWxUMEx5sqa7e%2Fuz5TF6gteaj4HM1%2Fp%2BsyuQbPuNeX%2BcF2HtLiD4GALwpdFgO3n5Pwv7KFGIOsBkMVpqZZHeLk%2BCB%2FTcp6NqUjRV7K5dL9wBNf%2FnhIJTFOZUcdBFXWC500jha8wg4OVJiH4nPXbVRwM2u4e1T1TUrPD970IueD2%2BAa3zsrePDQBj9nGSiMD9bZGhu1ZDzY2xlO1nA5BDXY7ayVeQVCT%2FwqKfl880HHAdNY0Us5rD0bTtKaIGDPnvN021WM3YpuB2%2B3Mi2xIc%2FH%2B%2B3m4bvs5BAhxTc5lpvUN3EuAnJedjWW%2BFVb9rvxqpSccapjEwXcy9irWd9XYY0GKsawgfi%2BXy3B8YaoE7e9XuTcLAAAISY8JF5KlcM6kumX7GBosubB1jl5gZK11WUYxxSo8iyTg9Whc3mAZqvqwP2ka8VbNoqnEoHwJ0bfHiiNoZXEh8KXYUl%2B3%2BjGzphltgpDjgyjDXBFzD4NWOKMhXIqxHY%2FjcOV45kfgEVCAEt%2FH8UWHY48%2BFFt0QFCndp82DPdAoaHw6BRku9ah7NSmZTYgGPXlFozNqJuR7k0NUJzbtQVUo6p5k8%2FywtJT3t2Awyxw%2BMLD0i9QGOqUBkNOERLsyOD73oVf30UNWRb7%2FRbRowMINWDv4f%2B52sz6DQH1DrHUp6jgXzy%2BukUp4NFPZVMgTHSRjrXtNj1LPUvw6kzWBaRV5J7L4PcVNu1bGx5R%2BFXIH1dlpzycYKkD6VffYrN5tZC69ShOxIKZHH0jQAn4sTWbGA9gMNWnBrAoKxFl54RHRLLA3vBQRx7u9x8MO3s%2B7VyxA7ku6dNDxt5wauC7X&X-Amz-Signature=91bca21b59b1695c8e20538e039112f57a51cda21b4feffb150082930e0b6596&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
