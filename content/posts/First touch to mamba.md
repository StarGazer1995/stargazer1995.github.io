---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YIQIMYS7%2F20260714%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260714T224521Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJHMEUCIQDMxBGLW%2FTmKBdRy%2FpIoDH%2Fuuk2NBTTgQMn7UeQ%2FDc8fgIgYRyOarLPGIS2M0u7iyzeHXV2hx2ivjHyszfnPNE6M8wq%2FwMIHhAAGgw2Mzc0MjMxODM4MDUiDLKWL20BpVAa796t6ircA6Ag%2FqB7gmIeI83K2d53Hk6fylcwhr364vW3m50NUEIRPbNaFS6m1tFGADb91AtBqTXlBgp2vYPvyMSUkyy5xWdUlNrGLzhnzWvNChPhTKlaiRHoagXvxIXcwsRQCQhFIVYY%2B6VGAZW6EBT3UGYRNuljmzRx2VhHS0Bj38og2LSJIhzqLbPJreGGkcgj7j7vIDBM7PhA4WDmQloZj6uwh%2Fi3yx1dHgFQCWRIEtIkMnLEJTspeMSVejgWm6fY5Z5bJ5vG8NNlp1fm0sykV0Vukj0ongKK%2Fm4SehBVu%2BkYOMSLXtdGuzkh2q7b6pmYVk5MyxH3gWjtpyiaztqp0Nk%2FrDbUUTbDDVn6hzdHKkD%2BIU10TbJVtxi7RHR%2BcZ0hNPKBGSoCm4iyXKXR%2BIBJJgbIt%2BOE2COUKV9lYFWrwOnm%2FwQmFDR0PThF%2Bz18zdqXfT6ICbVNgBy0hxozUrDMeIQDXo1BqEhvt3VzNgnzVopwKUx18ufvYFsPQgie0BqoHW3pdT6Hy64saP9upCYpk%2Bh73qv9F9rzGnUAI0mFjFTw70qRViGZWP8MB2YHsv2%2BJrW1LEfb6cSs0%2BiSm4xpNfHB4OHkOEjrnO7rz6Te3RcFR%2FEEZqAJ8Bx%2FoWGxMvigMLjS2tIGOqUBskrJ5k6CgQguvmDoPPumjh6097fFudcc1SRa%2BSlPCCC0RHhF294wW2iQrkygtbCtkGOXkYxW2XQGxNED5mkxiz2oCLcoxo%2Bbu%2FAq65wpPPsjpTtriaZRuCP4utyqs93M%2BXspQY9zbqhqDg3FQkTJxhnPBe0K3JxcjoYfoQwb7mAiHztgrChuy2H2LVHodfjzKDBImex0WY8kMf4YD2UVgr%2FoajtN&X-Amz-Signature=378393ea18491188e4e7405b0426def35f882a4e8d86d62219a393fead185639&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
