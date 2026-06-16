---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SUNWZCGG%2F20260616%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260616T023543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDlgyHHoXj2GT6W9kHe40NAJT9Eaku7G2Mq0Sqq8rGR4wIgDieebw4BIs7IsJlnYrfeJNYystttAOSxc48JJz8JHWAq%2FwMIaxAAGgw2Mzc0MjMxODM4MDUiDEagnwwPmaLrFdRNCSrcAxLj9dyTPnIbTR5A3uRnNDRgB5OcIfNinCPm4AD4G4usaFOOI%2FuJxoE4a1CCQSByF6W%2BqLpb5qbqJtApvybcoX0kvUO12RovevWgT910cVw4NPKSXeyKNLq42UMVBzgD7N9k9S3aghCzDj3cHPQ%2Fiic1vZsyDjFusXQXtChBlrceUy2CUrpSU13FisGN5oJz0iwyJ1SHhbjprhccWzZVUDthjxE3elJ4x2WvbogohhEL8rocML5uKviYZ%2Bhm9dbsdHXyev4x%2FvwLUDz1QAglMn4WYMU%2BC0fPSXEOkMxyZj9%2FHcWSUVBOnKQ9JvjtolKOypSlZCqIs0I3yNPZTxXZ3YrSibNglAML2xuEUN4c%2FcK5qWGCgYivwsu0I29rmucLOjEIvcVaXGzHDmPy%2BzcjyhE1ZbyG9E7C1AAxS%2BJ16XF0S7St%2FsybFn0JqkLg7fz8KNAjaizd9c6OIrSBV3%2BJrQpPl6NNaw1K27T%2B5bxmzr8JuJgab9HSBgswmDjev28ueh2NhKhEnhx3xfDBeWFqoAf1MmaXPctZPOVr2G%2FQXrmYRx%2B9hj5Qqw7IbsuIv3fE6y%2FJqaF0bEdd0PwKfJIv217ziVejUSxAPD3ezhYDPte3rNllIM0wr%2BjZjbMhMJvfwtEGOqUBhkmQbyQZXdBi4cVdYhhPzL8%2B90B%2B62Gcb4qRh8ErP2RNipAutqYDTr5gKBqA50IeHAOwLdQCDAMx4G%2Fq2BfwBEGrrEAQ1S7w9Z8dVqMgdv%2F7wBiOi12J3WLqvnZMR0ClYh0KS86TMcDnQXr3uwJACTjmqNKZVISS4hLeLiSxex2qFjBNM2kbf2GavnknSPCrAIpGOOtOXL1I1tAC7X5g4ZfmOC2A&X-Amz-Signature=7d9f4e4d65787f9f9578106ec68507a7fd7f29e8d67af09ec225daa2b4cb9184&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
