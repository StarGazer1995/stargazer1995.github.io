---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S5BDJYXC%2F20260919%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260919T234435Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDiZXt2EKa0H5Pv%2FKA1axK5tTSgK%2FhQqL7Pb0iD%2F3XmDwIhAM1%2BFhbHFRYXQ%2F3dZQQGjOkJzuril5J6PDGRaGq6xg%2BoKv8DCGQQABoMNjM3NDIzMTgzODA1IgyZJ0eFHa9PzP0btdwq3AM7W6nlrpllvZ9xOfZ8P8u2wH8QiZ74FcOBVLLXCM%2Fv6uHH5nVzpjVFR4k%2FWu3UGZgbo36bcS7BECnnWAX6yLgSFJ%2BZPqEU2IiDSEz4LUZaUpudczbSUwprLETL4khuF2w%2F7b5Qq51minREyhVfIVo1%2Fc2%2Fey2AB7Zrl%2FDUtmOx0s7e7PxIKKWJ3dcKlKVtDbI8qbG4ruoQhpyu8tFTHkpVu%2Bj%2BkGr2B%2Bhm0Ofuka6VhWtTeEx92kfIc6TPjhvTKAfQX6XpKip%2F5osAhroXeHF6luLslwV8QTWrEEOIeMelAmhWMvSPBEZerPbmnFyVDFgYfrLyTtktd1tBU%2BW9VQl%2FX1fO%2BktBbk9xkur%2FYV2BETP%2Bc5JeJk3W05We5ocup%2BhFr%2FAY5TX9Ho9tmHodg9RpP%2BiOvELp7f4DCGu%2BK5ZxtpFnrXGs2eVWhEUKYI2KdpwhtC7F4GzMIp00jkWJYzWBzNrtW9xMGtf8aF7%2BJndPIVUgkf7TxVTVsvnu2pTnUpNAr4zi%2B%2F9dgWRBSL7xak0L8IKervV4pUc31KlUiL2UvcH377Sl8p3bEPlsYfbiSnmYXUcmy%2BCNYC1wjeOgbE4PXLC2YRuP%2B1Ps94cOuotuuWI9Wtoa9Y9qLrc5wTCBrrvVBjqkAQtvkWryaexXsIgxzjeWAeezhAttbbHfVhoNMbFyRhu9o4YuQjczcsweGV4F0kSOTZH5SKSTTyWQ4QIPD0shKaYEzC7OAkx6ScdZXVpfUBdnOqVeibjaJO5yhZOqYNOnjUPFlDNuxu1z4UJFiUgj4gH9CKzUg17Oa%2Ff08MvOVn4M9OwtvwvmIJ47i%2Fo9G0z2M%2Fsg5jb9VNc8Lwqopr9ocbyPph9x&X-Amz-Signature=fbfdf220e2a9aa04fd6b22be484decd61477822074d554ff84da108c94a0e03c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
