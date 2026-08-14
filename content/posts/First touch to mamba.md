---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XFVSMARP%2F20260814%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260814T085641Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJHMEUCIHeK88y1EV08LQnCU6Ax028mTW6Q50dYOPkEWKR3J5PGAiEAi53bfY6q91QpCRrKvbD3PFNP5z3rDEggAHflEfTrjy4qiAQI%2Bf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDILtnYoMo2dRxdFHZSrcAy3DvDsIAIKn2u5Go0zeUTBdD2IVtQoBjpk3DCWZhWD%2Bge5Twyqf%2B4kQdyGBmwxEkJUEPMELpElFydgqZOfcVhDuR0DLcdqr7pVY4KVbWSKeBeyM3oKH%2B%2FNFWPpVkBlW%2BQuYCsSPOaV%2FWpoNssEPm7BOWzE%2Ff2F3zsoaae5CnHlaqhs6G7R1fXhSgJvReJBNYlPcw5gEbnAF65GsaOjW01uvXQ%2B0GpN2tZw8XNplpdU8W1HMzvCPXeb7D4o6MiThlU6OXOK2Dy2pPeF%2BkrzMMU9pH%2F7YANZzXCxu6KZtCpwmgqCQ%2FrdabMUjFkX2Ins2j7oCbY4INW3Q6riEhff2IbNLnSZuzNHB8weglJ0ExtqW2rXqmd%2FOsXLluUYB2G%2F7eeE%2BRBbE41zmL1hdRMupDIlv2DTdMw9qx6V90WNS2owlCcLR%2BabpAJIQh%2Fb2jp8fUjFnSrayf1x9lie595VeBVYUyic3T80doGty%2FkxWJkxZzC9ybHlKq%2Bd1WiTyJ%2BGXISSgRK4aL0i2B1nJSy0ymlaTj53xWTTC1vQ8n%2FSF3ANpIOPXbLUqhrh6lVHtTMF5C5H986BcSEKFzngju4iS%2BsM1%2BvG5OY9vPUWSatJnHgLSr60HgUggK8DBh7HuMO2b%2B9MGOqUBPw%2BZTr6Y9NArqVm5V7BTNMqPldp%2BO%2BTI1HTCguTGJvfKyz92yUV%2FBa6lgaYah8PjsRvfqgCp%2BDIlx%2Bx1ny4GDGnbSaAsL%2BA8g%2FrEVNJ6iuAb8HOZhJpeXnHmQoNI37BWHkULk26PWWBAnQRbW3PAzx8QOHwdC%2FOB0okz9NTEbQ1Ww60ghHUjWYIcFh0pvkJAdhH6a7O76LxVp%2FHWTzQHRFq2E6fV&X-Amz-Signature=c797a381f22afc48025a34940cccbc8ee0cff8c3e3e88768944e6414497ba44a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
