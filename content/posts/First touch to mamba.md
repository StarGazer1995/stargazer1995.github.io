---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WL7YUNS5%2F20260522%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260522T174452Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFoaCXVzLXdlc3QtMiJIMEYCIQD%2F6Sb0F%2BxSGlZC8lzp%2BU2Qn4Z%2B4ddLyNonRdCG4Kc91AIhAJEuQU4zT30fQu%2FJhEH%2BoeFhSa7AyB1JSPiQ17i69XXWKv8DCCIQABoMNjM3NDIzMTgzODA1IgxfZ5SZqOTzri2HvY8q3AM7%2BSlg06dLV0cnT1ZM8NLAYQ7loas7fOWZK9h7KQWtTC9RHvye5ZoPGwbdxfcflUSN1t7%2F7SkjYIKyeXm3ZJt0XlzmKWoB13EWAADe8FAqqcURkxUyOxHC1tuZtMZdiVudv7n970RsAZ65Qe22qKT6VAQg49upKJitjgMUPvqh2ur%2FzwhbRrS1Hv9zkB%2FFbOuWdq5bPOIJq3Hq4aGeAioY3Cih7%2ByLyIk3%2BFi9MLX%2BzbEVMTUDxlfgIdAMUKK9uA3eSI2iey0grEovPK8JH0wWRHbaqmC3fAmvkdcj8YuAsl52aLjCWonKUeVG7h5e9FdFLWOHSK2Yk7%2F4ODMc9R0p3cXyDhqJUUyMLNvxNL8XWaxuMYLQwDqYgS39S8lVwr6oBuQ5p4ZleWNhGMVN1ExO94Z0lMN8wT2xswVRW7O9U6Io36DKIdRp%2BPBE6VuE0EmHGRd3XjnrnH8U7FbOo7K%2Bm%2BHcP%2F92TXaiN6%2Bgn0w5lR0lYkbtJ5lGv%2Bl3AAFMnRFkRDD11wE7qxQhVoMyliXqYLpAPnHd1X8Q3o8JI0AJeKVLyBEGkj%2B9ss85nhml5ZbJToJUwD0tzyFi%2BI2S%2F8iMA48dlZCt6VyY264DKklajcnM12VGpSeU3pIV8zDjn8LQBjqkAbNyQggWEaJKUpzNlr7rz6eoGLs2%2FzTDRBeJvkP8P9Y6j%2FH3sffPWO3EmxU9tJIP%2BC43ZxtSmcVANnxdup81qIOg%2BEgHVm%2FcE4BL%2Bn2NGmPHUlo4VYjcOf%2FV3Gx2CXxkC1fXeR894t7JRHNSgDvRNbU%2Fh6Ca70HYGDPmTwSamOGFBYZGONl%2BcnuVZD3Gqn%2FI4hJnkbF9BOVdc3nd7k7j46IvGFpZ&X-Amz-Signature=64bdf21c0b90be7d9f0df4bcb2a8fa38e62526776d1e557fc4ae85dd9b1e1465&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
