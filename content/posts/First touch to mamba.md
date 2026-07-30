---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QHSAYPVK%2F20260730%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260730T044545Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDBG81E8vE79Qtrl0vbnVqKcVryOJD3vRGka9KeTdQ7qgIgSeabf9dJP1e%2F4kC0SuPmNbiVC1Z7wCIH1kVnVBsV%2FksqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLm%2FbBzXYygAf%2FuFkCrcAxTw2Vgnz06Rkpvb40mh4Z4x7xvdw1fU4NNyFTFyTZUhiWaHQbFU3G2x8sHwDEDOMyCaLgQ5TBsfPepbJIXu7NMI%2FQ1%2FKRc%2B5S6CRCdNSgLD1VMohdVOIY37lEhFICqrWvHIVrcsluGi9o5ZKecHAiNz%2FcGCGOb44j7C9r4M4%2FXkzms4R2Troxwdk6bPU6CK90yaYCgjFqhj2g9OvowUQ4lEf3fW9XMOK83OMrQuFHwfS9%2FdOVW2gUIeNwrVIT5EnJVWHUsFcQwH6EOe54FcqZenTnD%2FYj%2FPh1pQKj34JVJJSC3%2BTByRPKnMcaB3BS5aSYBvZ8i7yT522kIRmdZP0Z23cQcPLgILdXIjDO2Lz1KvBomtT%2Bxsp0w47LzGiHdOS%2BEI94QT4cb%2FBML1dDHL4Xla14rMqW3W4Yp3wiHzqRiLHb1VCjKrY%2BL9yEUAx%2FIh8oix9ZIhoLcPKK8eWoqEibSwECF31Qho0woZBf1WQ0YhJzRotI4%2F%2BQ964Yxro75TRCklQNMW%2FxioiGPd%2BC3tsbZAv98S7nmiSg353TFYQkus6QUgr5CZGAbIPUqtYHQf0Q5pLOPxRH%2Fm556ajNqHA%2FQc6QIRyuO0iRGBhveNlGbtfMBbATE4G6RNk9%2BnMNCYq9MGOqUBkl97nDEsIoU1epGcXc5XeZB%2BWwKp3eOBrNWfHrrJ25%2BJmIMyc3720N%2BJRPW%2F6yzya1X12VV30%2Fp5%2Bp8aq4XH844G3pSMk1cKu4kIdMkv42pQc%2FqLrlCZ8Ayon3iKLOU%2BGJvQxAKFXZbl6tVmR0skmzMfMPAQllULN%2FZ5wJjaeX7Hc9vHcFAL%2BpUl9DBD67RsKAwRp47MGF8Sb7vzYrIZJAeAko7Y&X-Amz-Signature=0ce53e84fedb31b10136e506100f78ef188810181f4e9c83012d88fd96c04700&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
