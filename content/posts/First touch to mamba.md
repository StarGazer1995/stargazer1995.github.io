---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663APESL7D%2F20260711%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260711T184256Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAgaCXVzLXdlc3QtMiJHMEUCIQCt0Nu7RKIwQmr52LAdAtcpDuZ9uKyxb96zCrnttwpHcQIgSiHOrmNxsdWu8aFDCxlZ6LGASHe0lX156y3QQjEGE7cqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKCjvNi%2F0RkVUBYA0ircA1E8EF%2Bp%2BejgxWRc0IBPW%2F9j03FGRVmEnSRr7%2FYVtVvscmWoeS7jK0hbsJ8cppDNtnMAxnKuAqVpCfkHF%2FWeC03JvKfHF5QZddyj4FbhlZTm6J3nxgojbCDh8GVNMvnrOwR2M%2FruoWZqgUZhmXbh3XMLqp1uuJCns2D%2BznPlILIlstFiCcJxXuv542urZAFv5up%2BTu1LtJOIrnQQELgex6M4DsJiHxbiGOpz4FSStYo4c2u%2BXX5eU37rupp1rf92lPzTnDEeaCdyER6K24d46yQmYaT1QwOtBzRT1E%2FIh1b6TrCEYFAlSTey2iyDWHm%2FBcBc3c1%2BlEF2s0A%2FUUDjkojZGXcgA2gxP5ePPX8FbCIbvYmmqpegCjK66%2F5MxlzRl8NVHD%2FnBzrr81i0YUWoRyVRcsjXEY9maTw8q%2BoVoy%2BI0gRXEwaioTfAEZTUAbI%2FO1Zx9jXXi%2FCFBLuDFqHpLJFa4yEMu7HS9ERevM0L0OxYHEmQZhE79YUOoq%2B%2Bf%2FKtpAKifwHdZNa5A2vtEP6LdB7gpkaujN%2FIIHfXZEoETokJ5LAW8X8aZ8W6jCWHEyhKLnAhzJINoFwE2gGSMDefmoTnjqcWHovAWt7%2FalNv4tts4kmEkhKpzJ0oCEQrMLrCydIGOqUBWtE%2FN7PZEqT7CU3OQTaWjmS9hVh6iSWtmzRaBwFF%2BhG8Wm3fbE9%2FxUOsIB3zWIzU1581ChWvlVDcK2fnzcxu6JYLdfIwCJb3AYMang6QWE6u%2BzjUtsXBewcSG9bnuksmX1Rri4xrKBZEZDPo9if%2BRnxdbfQ6aooxCcYvV%2B3p84TRshGC2GcNYzgIjL1re48b00qaM%2FouMfxVEw1MnU77u0LtEpV%2F&X-Amz-Signature=92f22cf6e634640b442cb911fbd98cdaf66c0681a223b26c0d5faac10907a8b1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
