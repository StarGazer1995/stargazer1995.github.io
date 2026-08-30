---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666RY65EU5%2F20260830%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260830T185447Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGHda%2Fp7ilZhlXEZ3tPwFMeKbXfznf26jC5BEz4IapUlAiEAqaGP%2FvZL71r5MU1aQjCzQCJbw3fg4pIVgsEDzwkBfjAqiAQIg%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEDEkqnWQqTwZVFkICrcA%2FpSOb%2FBRcgHgjL2znVM6sXPUUUgIrqi77t1DJaLBlUIcd1FEftga%2FtJ%2FpnBnZ7nmjiD3V%2FM3KraPyfx80JXwF5tftk1wfMyrs3MybBtQdTafcnTz67IYA4XN7HiBzTLcqLqQpdhWgM%2BD3ILkDzy%2BhczQ22sqGdjCS1xzoRKzj9sL5i1Pc1TxDpAbZVcTEFSlKdaz2MtuD6yvSDvdx%2FHqe6nS7fYKOPMIYW13xdOqjB3%2BsbQKrRZ%2FgOyCQW5bMU4LYPESBGLb1t3w%2FtXVwnZUEbWBaR%2BbIrFbuzS2kr1UGKbVXcoZL6b8MxsX1XONq2lOKqr6KCZ6MtLbT1t%2F0sjS7qO2JyCrRrSr1nF9d2TdhaCGMS8EMWXepERnQxqPUDF3IHdkIMfbQNHNreLlKg5V%2FW311LpG13YdujUseSBUr8ZIvK1saZSJva6kYCzPPpzP7h5GZOYq2Xp3K0s%2Fit1yZgxj89pxUgc7Wlr%2FftqaEhI9xOj2HUSP61SlAdVot%2BgRBnIA5a1mdcLlId7hM8mtGpN3%2Fi5D34JLxQZRafQ8XYXtC1MZHO2gL7zpS1aWUuvpTEr%2Bwy1ZngyonEB6o7X4dHbp3ISlun12iCZlDatc7g4wvwqAdxNDY2EjRBpMJ7g0dQGOqUBilnxfUl8unHos0jPVvnOLp2HvI6mz47jIkNjFVmTUsMOk%2B1GUnFFa1vmAyv%2FG5zaN%2BSWyLj2XVcMh7rUV0sX6cRqIc9bF4BaLKzLWJSidQEd93Rf%2FAZZqe5CcWxkcay6R2InEW6qxg%2B4UCLTuVs25MCIwYv9tz%2BenIeRWC4MOAct%2FnvJPjxnAY21%2BXbcpJbGUenEHqsivxwTarXTLhyaGsWQp%2Bj%2B&X-Amz-Signature=88e1668c6203062b0ac97a28c2b3fbf3f24f29ddeb7be1f136455ea35a134a60&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
