---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666KHXFW2D%2F20260725%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260725T110052Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJGMEQCIBGdDsLxBiUlMxQUd5NwCqnVt4H7WHN%2BlWXibCRUaJDbAiBQnfDoQzT%2FaB5Tw6b7Vi4gkKiv%2BT75TYOsUBcKAZg%2BLir%2FAwgcEAAaDDYzNzQyMzE4MzgwNSIMmHWf18IQIkObGcMdKtwDsjAZL6H0q82lk%2B4Jn54WQ34Fizqit91HEpz7bNrD%2FjGasNjsUEuwdqm6IPGJiWcuUJ592NdsAV2FGh43ZbXAoVckrr%2BK9YdmnjZGXLqDRWi85kEbFzVrX9t4GiGj9vYrquhKgXLKiPn%2BmxOBysK4zmn7V1%2BFRLAkaxaB1OfSzmKEQuR4hS3h1bFdsJei3Y%2BoVxxudMb1MPAQ6HCKcUjrniWt%2BjQHBZHH3BHGLhd7k6sUpc1OC5ocMAEhQFzwYL5QS8CQ6JqlI3rdWrj4hyfcoEFbAqo8hwtvpYTFohMR6TlnY%2BowjlPUaUcVUS6OI86aZcewVu2YwUs8OkyP6E9zFfYLPSl5rzZKb5vlWlUAsL1J9%2FSX09YJtnn0qii62YPsKPsiar81xwpmm0Iih1LQSGshBVHelGsVYmvUNmpZxI0xi06G22wEfO0309oR9NGoKW5F%2F1XjyL3MbEeoLC3YPphcSoMTgpTD8e4bNw0TTzOzDL6DJdN4rqnWlD6x6%2BxoCbCPgaysHklXhG4L%2F8mxhGsKnsnVqmUQcKI6Uom0CAy9Pe4ZirjoXLTExeaoRvTQECfr%2FDeB%2B2vVv89bgVf%2BDzJ4nSHF91F4JWB0sqnAZLQ28G3jEbFTB2uH7L0wzJ6S0wY6pgHnMEzRT04Lk4nNGpDnbTHjF2adfxl%2F8TwfDv%2B7jWbw7LDahX1s%2Fqf%2BTwv%2BNDdEM9tCEvgyO%2B58hNjptChNDH8YHRmXIMZR35yiIlRh2Z%2F8q326AZdRJof5u9DGIjgfaY4ZZkwSBxqUNPqF1u9ilrk1mjL8Rzocnf3G4GElJActnNA0HcNcNzMopEhnuOehVhicGBW8yTK%2FWpAhfFdlPPmmGh4VNhYF&X-Amz-Signature=4f4533e5be7a1d516c49b5f8b204dd4d778ac06c9d043187ef15a57935d5a534&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
