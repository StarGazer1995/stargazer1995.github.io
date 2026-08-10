---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RP662OWN%2F20260810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260810T185412Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCAiwr3aLvlGNhjR6iUk%2BqaHhG6oScaQdGlKNsp7kETngIgEXDDsjH%2FhTGwqXzJ%2BWVmLv7ICq%2Fjm6FLfm%2B5TzsxUZAqiAQIpP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL%2FNtz2C6skjV%2FSYNCrcA6S9m%2BjussOOOiqHU3LAcftgNSKAe0d0eQPO8h1Vumk6hzB6%2FCUCcUzK08fJswUyYqR4BjXtxD40FlXGslJ0PeSD9e4w4MPwCd78o%2Bl5vP77v3TnO7YdU2fCB4GFNebJW8pncMYQOzNCPBJ%2FA0Lr%2BvYu7fdOeA8oZt0b3kIGLp96oL5E%2B0xLBPifoBLiIdHkNwgFD03zbugyuhWZAcF22mEFu3K1WB9yJLOEzxWS6qlROFHp2DnwkalSQ99eUod7pvxNzIkzNXP3FkskovSxxfYTyNeijFuIJuYFwJLMRi4Kh8YmzTYD9EvcvE4ZdYf%2Fuwy2XxYpVnJ%2BlF5YPYPURHHl6DUkMtYmmJ%2BWgP%2FrragQWkJ8L7dEg8HkkjaFC8mAImCUmC8%2FBdifJBavMTfHobIPQ%2BTe9Y4qD6%2FP6rAmPVDuhuwiiXkCFOvRqiXPN22v6ntYSooyOCCkp%2BqlVzhpbBvrgPUKQcJfWvq2F6otm7dLAHRlaq8IcQtlBEQS87tC3FtT9YBUfOGs7AjSwcnl9uhZU%2FK74kfQf%2Fhbnhsisdim0Pe52QgWOMYXCGxFXcZKhRc2lRKUlPce0RIYDsfCQDAwkIsVzp9KjUn3oxR94L3A2ssdbTVpkBqSE3y1MLq56NMGOqUBg6lQtWko5CrU%2FNuMcgCLBYQZe3RpY7QndkYXdpp%2FF6cy72phNlJ0gJoWp1xIft2HuOi79z9YS9dif1lWF0ji%2FpDAi3RnZVoU5iqhyxOvG8kDivsBD5gPIUQ%2FI6Go3WI2hhwzp1D7EGnIpXCXeX1qBrEEIqZD2rjCr%2FBsiFc5eVrSA2Zv6xwna2L3reWrW5BzeUejOGf6xBn%2B%2F7VrSTxZe17ilQde&X-Amz-Signature=9a6a9b026910aa0be023aef7f5b4c548d4f09cae9c319c85a84de62bcfb040cc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
