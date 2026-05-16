---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VNHMZP5C%2F20260516%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260516T184658Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDkyT8UyWGsg%2FCE16y67MDU0u9YII8ljv0okuftQQT%2F1AIhAIkXdPrjPPivQFsK3aSbbqyhuUXKzgUlqt9aLU4%2BO2LZKogECJT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw6Wtqr%2FbLzyqJW4JQq3ANmMfzOSHRbnQxbn8hA%2BO%2FVSHzOAf63HzbWOsvhGZiZYLuRn%2B0FZm2hDDa81HLeZ0yZnRyPl%2B8j6BKOd5RS3s6dtI51eptZGJ3vWBZNl0cVqVQBQNceBYwV11e6518ceLSSqchWelYjEE%2B%2FZfX0yws1YD5YIdJlTrzH%2BQUBOPVOG%2BD13g5t05p6J%2BE9Xj%2Fldr%2FoYrPa6UbCP7Tvo3V8ALZElAm2%2B4oaVYsojNR83Xv0RZydY9wVHsTGH%2Blh8C5AOrpxamcCniO0epsIgK9m6sNGdMLY0g5mE2zIlrgXKsNRlp2RbkNVh9%2BZBRDTQ8mY%2Fkh6l4LDFijGyUiVFIoQYB2zajFWITnSi1fPZdg27Y8hBYh81KjuwtjyfLkNjmvsi8jaHEBKtu%2Bvzzxm9sRZtQJOK4PCj4D%2B4TFJUXm3dvsZKWbEUv5xhYe2cEbO44dVY6Vo6TDPjwTdX9UVwQHsK4m1AXz6TCC8m0oaPvWZtvYAGz8ShZ2TUyTWTcMxHatpIDFUjkkQdYuGRayXedXte21Si2MzIZBy8UEgeFvmeaUceliylOLO24LxwrxEKOj9iOzwsFJGs0G1sFx929iqU8x6xdiNE7ZMZ%2Bbrnz3W7T3U2gPZHYgSskc0pdKMPTD686LQBjqkAVXnWLmettIuhVDn03JuoKk35pfKV8yN9qb6%2FRFHdHsFKg1IKu5BCaaiBQkbx8iuL1h05DHDX2wX%2Buf6kwoVq31NtQYHcb2XkBwoPhUlkFSzKJAqbVM5jBFV4xqRhhiN%2BGTK1o3G8jFanKmnAzcJH0CKZ%2BjCOKNWD4CtSy7sBJs4aspTVLM56XRGW3Kz8HZMwlCdQPjZo9YQsQZzaN1Nwnep3ACd&X-Amz-Signature=31dcc252bd14afb30ead5dc37649c672898bf9853c396e75c4cba1bb1d695da8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
