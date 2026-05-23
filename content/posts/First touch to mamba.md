---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XPYG6VG5%2F20260523%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260523T080440Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLXdlc3QtMiJGMEQCIEH%2FdmxdD6J6ccKDTH036qPTt4Yep22ctmDtPRXOX4QpAiA1Z8ZdZpty4TMDIFRwwbRYZwr6DYRZuLmcYE0EyoQxnSr%2FAwgxEAAaDDYzNzQyMzE4MzgwNSIMJSdhDEY4bFE3dZYNKtwD21p2GiRIT0%2Flfa6bURCsaP09gBvUTpXyCgpVnZpKXoUWNSI3MvN4r%2FgZaiymN8qNlZgHUEj2YGwWOt32Jsu9CL2v%2F3%2BTOCtjTfC%2BBFTX9giDmNc9y1UkxgVud3QymmIvt6w5z%2FkkGQN%2Bm3vcw7TYaKzNqjxo7BOLoU7KI3rohWkV7oaMrr93nCE5Cpm46B0Hrd7frdcip8nKFbCUIHoi%2Fit2hZDQ79EZax0yQooGSm0mNf7T9n2GRh4JHXC6e03FPp0G%2B%2FZBdYtiYq8V4J2EHI7jLuYDORDzXeqXaWIclF0bsXkE8mU7r2qNie5Gplb9YFZB%2FMMyy%2FjnHzh6djtJXH3WlivRix%2B0HE0DQCBIvZhoJZGfPmxpyhZG700t7S%2Fi5Joi%2BVFTyMSSXwiUxg18jJO%2Ba2C6nAvVwHbnJ3hRgMOSzIpcmBprZaSQeX8F3P2ZgIdlIl7TdlLBnacuzHbXEF9e5EdDKiz7cmh5HoTazaA8u%2Fr7WBVapajuUJSKRbm%2FRhCZ8dx7u1euy1zsMzmZWWYMNnppJr6rmjudmhfOjkV1tjF28GGXD%2FXzK2EdnsGrCrjES%2B13UyyM1zNfT5fv1HGVzYAbddTuQ9JrZwFr1YN4ycSK%2BR04Caw96XUw%2BbXF0AY6pgF5Wb2mf4A3bmECqIyUvpdStxUAfh%2FcBD5bEn%2FXR9gMYRexnvVf0gqgtM0EPQvZi%2Fbg%2F5bHnMt5TVUhgAL9nOV%2BOITjHWWUzUps%2B3YF7ZqVLQdF5iuk0Kmgn0U7OVgBTfGEmGzJaFeC%2BEK5b3X8qaqd%2B9DFSkhL4KJ2EpPW7xqX%2FpF82MZmt4ZzEpPOWLgjPnbJ4OjPByygU%2F1hhZKaLyzqzFTtCSFb&X-Amz-Signature=bc67cc775627d7b7bcd13484adf7fd05506c3b404d3eb0b041bde64e3d495166&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
