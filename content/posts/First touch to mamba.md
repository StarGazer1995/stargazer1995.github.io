---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V3VAKSWX%2F20260715%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260715T170322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGkaCXVzLXdlc3QtMiJGMEQCIAslsh8sXWvkVGFyz5xDaJWg5LRjClZfe4LT%2BARaLsbSAiBIMDTnocg%2BLorO0tQwdENs62hA%2FmyVPoX%2FKSsIWLtzdyr%2FAwgxEAAaDDYzNzQyMzE4MzgwNSIMp3vFSahMxc78MOrPKtwDwVZTAY3VrYfV%2BjMpdPiHdAVYLVqcsIUkgODDRteISThj5kJdR7VlgBk18O7%2BWAPrDqx02YQ2rTs%2Bn%2F3%2B%2Bb5xu9rsfAMhdgWz5cMxzIvQrs%2B8xymGsw90grjB9FmpFYAnk9dr4YjuOfoChdastFFfDo%2FzJSMhxJBcPZP2%2BkJu7QbQaiTMBPiHWhteVGOuWtLvqdYwu%2F1xJZTC8wrtzTpZ5X3cMK2Iq1rzJMy1lpVwmScWagqZWWpVngsLUPwTiNk4raM%2BedCZ1egGQcM7%2BltUCQbiJmMKogeJkwSjDvF2Mu1zIYnDd5zRfqkM65ofZjk9SoiWbhDewFuE26EnZpHi%2FY3T1uneZm2fxwvfp342SEEwqHMHuNzBFtZhQkGGFgD61e%2Bb4lCEo4%2FH%2FqaEaVZyLtiDB9WcTMuhMMCjquPA3O8ub2LEomeqImeGrIQ9XOxZDiYQPHVNqj8jkSJHfti1otqXd0OdEPuSPExxtP5Q5ZLUfIrtPccZ7zz1%2BsV%2FGWh37ZPf4yQJAx27CPE0RiObuIU624w9wgq8li813pP9nlLpR9eCmHhl9Y08VQVi9Juwn4fkYd7RI24764wyq%2Bq%2F9CVYq2rbFHqvcOUkoHF9kfIhdjYt6NiciidOLjIwjOje0gY6pgGDTscB6SDjHHU%2BYoj2LiPT5j31kCXWdujmeGSu06hFx0VZZS8qKzigJb2yu7JKLkuGCs40RKYzcj3rFhYmBq7v7eyhd6JnlJAQji2uFvF4yX0aDfCNkWrFuYXFQfgPoGn5faxoBRdxxxrdMmTDxdCoba%2BfdL9nJw2%2F%2F84pAypz1MH27svU9aSRShIKPbSRtWJtZN9WAYXPLkcecpnRZkGt6WaktVhG&X-Amz-Signature=688906f0a1229dcabf31670b3e84b910f7e28ab9da647b910cbc87a334c756cf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
