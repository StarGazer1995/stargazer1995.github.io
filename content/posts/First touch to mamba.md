---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W7U7ZOLN%2F20260904%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260904T014158Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECEaCXVzLXdlc3QtMiJIMEYCIQD3hzLl%2Fl3SURyN98CfrZ9DId8fqF%2F3nuJDXGXntcl8bQIhAJXvMPEeozr7VeqD8eqp8T7keUfnOvhDZSVm8CzfiCMQKogECOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyudKzdqnw6KkDcCL0q3AOGixLzn36DuwF%2FLXeGOdYYphsVnudzD%2F8Gb32ZQYWaqu645QCDU%2FhBBUw5HhXZbtZNabEMcGUC6J7YX0ALMXJQ0icFL3otOeH5bO7W8qD2%2BVi6UA7GZZe6ZLKConzguIrOormdmbqNm16nrlunWa0B8QTR4DTjVYmVIaHckSJX0OX6o7%2FTtyLVPuwjNeWNnDq92QcxlMS2SIjP495aWlfLzGhOEH61BXDUORuyhOrocfPb9kmGTk4TsNOHCCVmkmM%2BCzlhnicjUAmM2ZH0F0%2Brx1dgts%2FbP3MDyBpFVCdsuH3Gc3axwoxSG3KNz%2B7XfOK9bZ%2F8C4YlRkIkgKmVxFd6ljku3PXza1gLaDXadmWaItj8lmExCR09aPEGG1Y4JmBVPCFk%2FlcjtoJ12XGNG8eqDmJq4bpMkEi9uUZY0k0t5vbpscpIavYNSwtfJGvcicto5rXQ7JuzD05m04ddkbBnkN%2FYLHH4LW4YMe5m1x6CKOXC9IVCjlUbVdGzP1MJiA3D1lNgAZSsVnRTYLCtTTmMRdD9tMD08fpd2ZAztk4waPjBYOOYcQoU0ZvH155Vfcc13dHKElPxMcCDVR9LV%2BsgSzFcWf7fsfHfXtm%2B4ughH%2Fk1MPby0UrRP3ZUeTCHpOjUBjqkAUuPvd%2BCUK%2BlJ8tq9TDdF1LZXpPqJZO6xrM6zn5%2FA24SLm0XUCUDuL6ecmXXUyRlaoPWpT11W6QwsCW26imu6UUrwI6xjaRFRpXrSXqEIjYFa9PUYcK%2FtgK0g%2BJzEsgSEoFzRv6C0MQ0czv%2F4%2FOcGmahgWMMErQmjEky%2Fz75VAdIQIQeFgOry3sbPPCcg3XFvNXWlE5U28g%2B5T6NHknyTll9FbLL&X-Amz-Signature=0c5963b6e41a9dccaa66d1e318ebbbb030aed0e44a2de85b5af7d7c4a26e5bd7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
