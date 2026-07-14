---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662K2PMB6J%2F20260714%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260714T151517Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE4aCXVzLXdlc3QtMiJHMEUCIH3fWDwanaXjkmrNdhBgodwmcNKwlehKCt%2FDGEzIpodBAiEAowpNWbuW7Ij86oxpuMnOgrIeuZ04A%2Bp1uQB7ZrXq7Cgq%2FwMIFxAAGgw2Mzc0MjMxODM4MDUiDOwqLxOc3BqRqeZRQircA5ZuPgTG2u%2Fq2k%2BTnmUwu%2B9XCUgFl4EO9xcgUuTojlmlewy6OsMvscIKHFslzF%2BAgFurkqLWNdWHep6r6Dc3FavF1cXSLrEDOiZSohGYq1loBEOpLtI0mQ9i6lJC3Yhpa9eK9IvP8fZ1ZW%2FQ3G6120N4k81Tl2WtN7m1%2BZy%2B%2BNrGD2OPZYDoLIie96bBNlXOiosUTQTvBtdXjU1rvwRWMkfCjetCjeeCzQJSBsXyWXpucnu4AD5YUwKJ44DWbfE79yIFfmbR44yDISftkmcPcP38Bs%2F6u6m0AqzYANc%2BxcvfyeIK6XJlqlmhoMLHfwQkxHZVZV%2FvlOZu4f0oXq1pqVDH2gL7wMzCbzyjTcKdA8WRD7nL9zyF46k6WaG%2F47axsiB6meQoTGeHdMrgh05tOOFQONeq1%2FnHcK6AKlHI1Qv%2F0ovIYx8l1S7AHMcNPuxErwTg%2BduuBS2DQoIKihiA56Ozpx9FuaDtszKuASbPFJ16hztw58s16WszPkXramyG%2B8oJW4PKlebFJcMWofqTbbwSTHSe9j7yx4Q6Mr%2BIaenL6p1spxuqsynJAw934l%2FkwgsDGpvYuNHysnGJBM9jqzg6FRHNUREyhqSzd2%2BVv%2F297WdQBpmj5upi67NfMOX%2F2NIGOqUBfJjwE6xyWgQWZkAgKuyAeQrBwR6SfEzXMeK39Bg44DPCG6fv1oA1Fl4HrP%2F4febmQKEMh0f1HxPnI83f9BZcrm0axkYnlS3KSz7vpTQtZ7%2FNRCjnG%2BXS8JgBJkJjNUDImrfmlhhUAdBSQuob64Fel9zwufaPZy0habRhfoG7kcefHZ1Y33Nnocg4mOEc8CYYLRGhr2UCPTHg1B%2FtYy1oAr7BcZ2h&X-Amz-Signature=a1ad564515b27728bbcb22a21bc8c41f01c4cf76722c280a70db6c4f21fc78eb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
