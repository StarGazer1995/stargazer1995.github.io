---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XYHG7CFB%2F20260928%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260928T021634Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJIMEYCIQDs27vuvjKGtH2aEZ7Qx5njatygKtyxqgGk1n49Qht5GQIhAPBzSnnmo7Bn34SHIORhGEWvJwAvbxJiP1Oxg8St%2FypVKv8DCCoQABoMNjM3NDIzMTgzODA1Igwo%2BY2UL33Ia3BZ1Vsq3AOwRXqtJtiKkXCISHHAKVUNwXgQ2bLVJ2FXT2pfRqeoA0pj5DJvVTmSZ6wMQCYrtHIHBGwqmhgG0IBBGLCpaBAOWVf7IEWNuXnbPnfKtEsQqr8Q7Vkg49OejkfQ%2FN2yTqgv8eMKDM5q7VsIo3IZLFd8%2FLIEOmeCvpKL%2Bhz1hEMPL4fZVK2U8m%2BZLz6qPQI5sLoz9gvSh1c9kYvia98qohJ8WKYl0VJlHZeFBi9%2FiXsWzPU0u%2BTuedUN9Hw8rNwQe%2BpkqMm41nlYqT4KvRH9oVwRVq2EZ8SwcYQ%2FArWdyUAReuUd734B3x6Yg7Cb%2FGZ%2BYo0las4Obps58zc2BJ1TfrJjJiGwnDioE1Bi7IRQkfgTwAGo9fFOKsPHNd2MMTlC3xhujNpQMq8GRYJEIcuXSO47DdEKO6vqE%2Bj%2BspeHOWpT7DiGiWc69WIUcvZtnyisJ8Wm8g%2BWAOAcMjgOHVNyTs5OPQWcKYrch3cGmCBj4u91LjEWEMORX8%2F%2FGl4FS3h7KgUdH06uBhxIG6Ym4LR5JrZeToT4UgoCg5LGkOo%2Fwy0KoVXJGdCqTrg75EU%2F9c%2BXHyQY%2BOYaWW1bsQ4hbvKC%2FO1cDX8go97u2LaaAkx98s%2B1KoGWtT%2BBv2h35xzrvjCY%2B%2BbVBjqkAeyMUQz7AwvOcHxF2NDu2EftNrlkdgxgTqQx97O9i9PZKdh4wcOInAwfD%2FZiv2WHQyeHBqDSPdIxvsIFadLy9U2XVo%2BtR63KKLESJUy%2FBj1KQB%2FbgqD4k1rPisFMR%2BiTdAQt2UQ04VQHVAntWcu2UEhenXRKSFEgzcpXvB0mBlZy2CJMpqpHUHFaCfb42HOxqLi5BJrg6oHCXX1PTOIT7BQ8IN1h&X-Amz-Signature=2b5bf8a8b7694acc921ce0c082ea51fbd3e2633612131213bcf3fc1f5e887dce&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
