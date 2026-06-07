---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJ4EHEMB%2F20260607%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260607T131706Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCsGlGhqHjKShBS7jM1ngq6p1WDqMFZvbT19qj3bMJkwgIhAIBFULThkCL%2BS%2F%2Fw%2B6oGgs8YIx%2BKWzIjhgGSpAoYwnwNKogECJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwvXN8aXTKU7jWwBHAq3AOPQkBXraJCEM4nigeitMDuQZaG5pd5twbiMcSpDt6TQXxTRFFZCl8my9iMujWPyYC2ganbs62cUen8U9oDfdbo1SQV%2FRAEQcqlrVsaBqD79dDxp%2BAAAkFQ9HdxCdb0pqQYRaZ4bwhyyOJKMln7W7vUHyQlcqmH4ja7%2BTAHqettrjhn3ShRfTTYqWUpY%2BWQwwmNS4MM%2BvNaZjfPj4HdgBiXM4Ep%2FS2NMnB2t3CXA%2Fij%2FRja859trUXFAYwEDJP%2BCn%2F3oo5lkFs7wxIdBwGMFLPzwSOrPnCNm3UJl3%2Fl%2FuuxMvBdGv42rvyFzR1OElytQPzdKMMLb870wm6FOnU7W%2BaYjgdreBnVReaV8FHdQuVCn0L5nf9X%2FGu4eQQiOAhwewCM1OjnKU3IrnqVFjyrKTSmm9Cn%2FDu0hLk4Q9vgOLczZM6o06Qf12T8E6EoSDV69S0BuQQZEqdTKgOd3Pu0W0TXjVqdeP7dfZGmSSFDnC5oidFDAvpDmk5KO2yBVu1cfaxywflIYwHsY%2FQG88bdoXR4qOb%2FjGITrWk0BriJbvIKyahMXoJpDIZQ17QZNRG8IeBx25Pn8oMXAh%2BK8ryWec8TAJlAVdQki4DsBTUx%2Ft29%2FuxY8j2Xw3f2B0cX5TD9rZXRBjqkAbqUF5dojsOrSnzRMT5n7ZEbodCk0LJknWE4CBsc%2FvNJC14BUkDCnRMsJj07Qew8L4e6ScC9EbAIvwxi%2BxK5if8NACjqcNPCpZpU4bslsOfiaVFryqpNQ8GQMNCF7KTjplOjGwjT30vmTcOY%2BWMZwxoUcJ4fmpBov86AhdwKVnHhVaU7%2FmLiT0hrRkxpTbtXeCtJdPbhjN8MFvqP8rEP5IAY2p7U&X-Amz-Signature=2ac026bedf6d97abc0817ee28c4f793a85573a80ef92c189f515805ebb83d262&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
