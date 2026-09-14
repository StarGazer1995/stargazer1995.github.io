---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TSLQ6YP2%2F20260914%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260914T160257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIQCCCRrvlsgvgjBkprEx8nq1rIrCGEernNfMDcldjSqrCQIgAJdMizDC1Km%2BNSh2DUuEQWO1k7ZoUTYMbu05z2w4GPgqiAQI6P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDA8VFysX4e3XOkLABCrcAzHKqjapKiO7cuxOQagVEI6JfOXmGXnI%2B51OEASEwvE9%2F76Q8It37P%2B5FkOICuK2a%2FmfUG4Wy7Wtgx%2FRcDfnzZT2dK55pt0iuzqDZcCZD9uIHeG2duG2GudpHlIa5bZQO68YbP2H%2FCn2Lr3P3Rb9PlC%2Fu%2FQqNj8jzrlVdnOr0WN08vfGVTUv3upGJDvZAJMouyPLQwM6JXUKrBKz78wVXrkztleVIiERdwDRgZJotYlbJkp3F%2FMvhA9vTsWq9ebWTJ2wfUegAXQsypZs7LGGybcS9s0Q1npo7M18NPUVAlLtBCq5fVqVsv97zaW1JI5cIKI%2Be%2F3RimCTKGOW7PQjKQsZXADCAXCTWBZ052Amj93w9YA7BpMWw0BllUJegler4j1yTZO9UaiRO406v3Pwa3SLneUSZ%2FCAbzm%2BwpHNNSBQ4EJNVcApW9Cb044BLf79aC33CLeWBdfZhJuezsURgA2M7kyD8dGhR%2FEh5GFwjjASw5YRqtbpCA6Nynb0SVwHAc%2Bt%2BfUgSzxzOvhjINwvdZuwEuWVXO4HWasrphjIBeJjLe3DSXY%2ByU3mB0gKwN3JG0oMgagaYrBUZEVm%2F7A3nPojtZRZLg3I9%2BQidfx0uWk2zNNoJku8lnabM6yvMO6goNUGOqUB3Fg3HHl2AbARK%2Fxw%2Fpfc4oyEZxVb1pp9wFUKiCyjvWQlhVxhkGy5u7Z5L4H9SEunUjMCkaMn5jIYYWxfyGAX%2BsAfazr9vdM6yWb4knhKqhMwF91qJ1dUUkGAzCUObG6VqF7IDUsORdm8rYNBoSFhYiVenirwYY1Cq3hAM7bzXPkLcKHDpWVbUwB8GOLkY8gw2CtYWSQEMqnkph5u0AtHMb3ROkX2&X-Amz-Signature=035e614c08b9e24bc1eb89d77e4c8610b37d8228a4a39fa59e6475c2d5591889&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
