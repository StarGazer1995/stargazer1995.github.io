---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663GMOPMMP%2F20261006%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261006T173152Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJHMEUCIQCbyQjBmgJ8Jdt0s7T6vJSdB4g%2FSN3kchf2yoZiy5xneAIgfSMAYbSij5xW3A6%2FddcD7M2%2B09s75aIR14AknMrpAVsqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHHIzUXdbP7J06lOmyrcA2T%2BX%2BlPn9xLFsR%2FaQ91MMTairFluG9CxuZclZ4m4iVf4HME4ybQl7J1UVsiSzAz4J%2FJoOYGePRQYrTSPduX0SCIqHcOM6Xb9r2msGtCrHO4ykrPgIuUK%2FjLfMXO5LMxvp5hzGr3CJY46p6ZW2CNhmSzWkSIITw7T8SApSqN3ofuHQm9zcGQUVYVHXTWCVmHVtQrGZul%2BKaI1sm72ZWCrT2lJODQOFxY9aPBQS8g0ifdcIPFMyvInu%2BLHHwzLSP3X9ObmFs8knrR6oz%2Fw20IFJm8V7BlMVhD2tBtnpKWTuU1tZqKZEA54jN9yJeDb3wlkVyU%2FQ6ZpVdhHUW1IsEJJBhr4uSdkco20u1fQ%2BLKoW%2FyPU3e2qqJQHrhmzVkHdXhujUrXVVbM4RP1Y13j6jwCgvvixsQXwMvHsn5VlYYNdCA4zjP2QJT4BsSzXqAtBtlx9wpQ1ErZWntpPNJFr3Py9iQhgDrYZDGoD27peasGLGSu8GD6YUdPVSwAmg%2BGgJeYZSdaYpTSkliUhVBeijTrT3XJrRSvvYi0Kuy6KSL47jSFf%2BO7Ur8CSnwyOcM3g6n5JSZXfZPz42EwgMzcX03AiJJKQJXi7JXqIM7hUeueJ3nvDlPssBeahhHJ7I5MLWXlNYGOqUBt3Shv6Y6jwuzRbLmHFr10qG6K%2BlOix6Syp%2BHcrA%2FauMijixYyxElnrKhhpXeVt60wBfWd%2FohKhnMVpoXQaDBFELkBTUW9bjndZ0EqwsQi0RkLsdUvhqKk5mCbbAD6NyG6bQEkWfe%2F%2F8Jb55X7FXDCMb6EghSdSnAa1pJkrqC0fxppNXWJg7sj98AR5EUFd7LDDSxrtj7RXiSQ%2Fq8p5ZhctrrPEce&X-Amz-Signature=3639ebf8cada71c2437c4531c012602142204db075bce326f8bac9585a192328&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
