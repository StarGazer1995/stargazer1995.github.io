---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667V5ERI2H%2F20260703%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260703T225337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE4aCXVzLXdlc3QtMiJIMEYCIQDr87Bbw0WNP2qWtVaC7NlaDLjgLUhJwN3q4peLJpRLmwIhAJDjf%2BapkKCvHQxHdcGU7XjyoSxIXSGId9vUfh20CTcaKv8DCBcQABoMNjM3NDIzMTgzODA1Igx8krqt623zZ%2F0KgLIq3APf3Yw1dw9bGyglQhvGEssuBy9qt%2FbeK32hk9TWC5IG1sqF2AEe3j56r25C0uoDp%2BBqWs1gVYq8AxaWK7Qh0j3EGmlOJymw9XtkQ7iiujtWoHx3ncf3emC6gaZ5KeZoWmZ4Q4bzV1FJPmBNEuABVRFdSHO7VFKai6Mvnurk6ZQReWmP4u5aTHJKl49ED8YdbxD1tLBR5nmqZ3uMQoOUjZXDGPDsOOQqblmUoRK9N84PAkBvHjLe53JQLbTdkklRwpTQ0c5zJWSOmFnrWTCnptWJCtcnKcxDXGKbiNfbQA5OyaCQPDrtIuWWO4VRFRg%2FADoHv9ZpyacD2AML0v8mUaw6%2Fjz%2Fr%2BsqKYvHWIJREqLPM5DqY2aa48f%2Bf%2BVmT4z9H%2BK%2B50RpsEQSxBEIypOD2NlT8kAJcu%2BEdRZB0nkl7r9dkwLsr9EqcbUJCVgSQWIcGhvG37X8qviaMU3zfF01654wladOZDuKhtdTKcM5CzOv3NPW0roI%2BrgqMZLTCrjzGywe3Gp8pBp6LtZCR1tjP2qqd7kqEo%2BpG4TwxqQYYA5BiY7ssWtuwcQ%2BGxXcLTFKMeyWPFsu3bLP%2FQ5QKBFJCmbhIklItAY8kgQ77LLDJG%2B%2BvflfP7tBlzBoXhMv2DCn5KDSBjqkAcaIu9ZC2VC6gwmobpmnsQ7N2XtvPlSBJUQgINZEaZN%2BEQhZgd6k3fGRNzd%2F0DeCA0bK6H7ZX9ZlD3DlMjHDZeIIzp6lj08%2BIm%2BcgHiJDyWJKGP8APNBrwFZ6nJOXeMpGDQ0a7PAHkSag3jw7Yqtmjmfc%2FwusBAlId%2Fldk8Dgr96hEdLPPJhKpMYzDozcwBt76eRIAnOMDjQSWZNs%2FJP6Q9j7LaH&X-Amz-Signature=e46ecbd4ae2d9c5afa3179e571f92b8476039cece7a0e3d941e3e1df33108781&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
