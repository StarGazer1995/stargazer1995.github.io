---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664LUXGD7P%2F20260816%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260816T003354Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQDAvZJdtC%2BZHoVQ6PNdG1%2FeE0I6dQmEDXmmwklpqLUOBQIgcumRPg6FPsEwNCCYhg7AaTfEN6laEjIcWBjKGC15vU0q%2FwMIIRAAGgw2Mzc0MjMxODM4MDUiDEh6FCGiAbKq2%2FfTLircA5q%2BH%2FQj0inC1pgvZd4VtgrtqWqjUxK%2B8WC6UZeDQGkEIs%2F1WmuxKb4h0utz0LgzpR95Eq2Z4yHSlrcbO0UmVrDtiF6eLBQwK56vul1iVkm%2Bde%2F8k3MmWwLGKeXXNExXr9FqHAegMLrI7seJPCSnyLgPfQtP81M9Xfz9J%2BH4vOyKfRMyy8dv8epkhwR12JWUeZ5lEjO4skVui5cocUjGYokoUZO8l4rCZ4DBrFxtwVKQtfKyqR2newvg1blIYXVIos8Q7GkTONH1LzdpmWqNI0nXepCXBSegNU8UodTheIfR1zePfW8IOzkbR%2FeIksfWVGgK94%2BYo2FoGy9ip48e8aflI5idM2JBOSSRAI34Z23v9Y3I9PyDyCp0KuBEBdBDwgySDaMY5DyjtxJb7hG7R6ftPhd8WGno8Sh0ujDh6AVKjOKXOEL1%2F35PR2O5G1MGYlCVx45HJzaYBpO9Ao46xLft3AXABvLVXsV7nII1af1eC%2BAPAppDa3Hqkx73CI%2FQOVmLuEU%2FruQUteLdOfVaA3nwTTCUgH5uNvnBTMGgTjemesLZIYPc8YRwI99CysZaLKB%2FL%2Fj74MxlAG1mIRczYH3VQ52W%2BsCH7y%2Bbrt%2Bk6Ff2LFZshOBgS9iFJNYZMLrrg9QGOqUB2WK4fJLqORj2SQwsXmVpu%2Fn6%2BTI1J3Y%2B%2BOSMscbezPbI6jLte2fnSlFmVeXWJm5jsgKjxEt0XnEEooGc09swlsW2N4p%2BSDdHSSXszSAC8jScvvItsxxdmLsS7tdx3IpjhpY7%2F4i%2FugV5im12Nc9yhO%2B57doyBnBnMq2cjplLUYWTmm928tdFZcp9TA4FxV4Ypq5WQsujENJh%2F2NM6%2BmNG7GeuzTU&X-Amz-Signature=9c89955564eb187d4bcfe775ec96bd3e7e3eef74480edd993286eeb09244c816&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
