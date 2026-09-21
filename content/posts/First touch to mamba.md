---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VWTVFCOP%2F20260921%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260921T092255Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCzKWihZkVAAMNZ%2FWJmsdETAuDIWW%2FcHmMZvI8ejvTcLAIgY9qiZhwEEKhFyCNzWnka1rh%2Bg47r4i0RPvaAYNLDaScqiAQIiv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMSbAJeKTCq%2FSgshAyrcAwUk0XtZe4jDGIf2MzfE01Dzsxen0uicMMQw1sg01wxtRkY5NkbE7Nt0FQxa7brqmF7WSkAAQlJGF6b1hOIEh9jxL7GK45BB99DEyp1%2BXWusmaXbk2grYdPZcn8Tk13Bo9XQt9MxiPVhDE4%2FQXzdfxHTn%2BrNIHFf60TohqbymXy%2Fdu8M4ReK31kNHRKZ2jDtg5Ppvp2nH7oWBuxdOaD0CfUTkA8ghOGcaYqH5Asnsk9wlSyiVSwANcxoA0VDVym4H24%2Fwo9dl0CQegf3ujzDMArBYzpWtiH%2BDRV3JgPvGJuQXc4ew2dj3%2B1olcGU2BN1TnQWirzcx5I2u5B7xYmAJqJOWsikrHNu%2Fvo%2B76UWIh%2FUQ1BerILT8%2BIauuQDII6EPMZhqdq%2BV8x2Wc5GqJ%2B5edoRIqpudr7Az0jkc%2BWG7l5j50hPRjfCLjVXmsFnbfyHgEJtC20w%2FaEu1f2GWa2CYb88%2FR36FP56lZ0%2FJB2E4%2BkZUhGuQQnTAlrPHrnyuXA1RAsCeyaozr%2FW%2FG0Lnt7a8PAu1ckASotqJWX0LLB9ywxRET0m58s3P56y788blU6rTBOp%2F29lafUhf4vEw8HICvcJQoAx20nFk3lDRVwrW0bdCaSZqKPaafM7c%2ByhMP%2Fhw9UGOqUBKSFZncw9le7kDGrP5tXKZ%2BM4yYHDRXiGHh93WAYvhlXklpdJmFU%2F9tTp1knf77d4P5xYwoFXAqXF8dFhoylXxUdVgdDyYFuYO4AO8cXNZF322E%2FVOQCDKK4bazyRr4f3jdcnMuZ1EAk%2FNJ1ZKbKGFmotfM8ynoAAzcbWUQGwRLmw0vlsmhd8VRiOoCNt8FfzNQTenYaDp6u9dwpE6dHvX3nIxeK8&X-Amz-Signature=43fd298e6bce5b43f1b9509d54364259efa0095e1bc1099140403ba8a9e11fee&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
