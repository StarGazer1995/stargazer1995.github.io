---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V5AQOBVD%2F20260614%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260614T154252Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH4aCXVzLXdlc3QtMiJIMEYCIQDxB7ch9AraADlLqFEx3s3gQ8EhK8iEMPJ8WdEnRP%2BlVwIhAOY%2BqPMSrZkhZ3Qw6ZcjjxuXENlLzn84AjETnSsP%2F5aRKv8DCEcQABoMNjM3NDIzMTgzODA1Igz0zMLIj9Dqni7oIdoq3APsfUtp4e8B7Vm%2BsT5cPt8Ql21qFl7X0gTM3PLnch%2FC2kFlmBSpgcxqt%2BpLOh3ypaKnIFgkzaapdujf1G7kM6a76umQ5txWtMDJO1ljmLkUu0YUJS0YP%2BMP%2BsqVwE7lr2ZYlNCwFgcg1g6Wi86Te%2F9dDeP4tnUxI0NDMgR7J0Lmb8QX3hrqdDTEkG0aD15%2B2xM72T8fECjPiwC0mdBoMz7ccGFhdlCGWAm9bxPrY0x5uUL%2FViCGr2%2BQhxFbhHzQzypnZPsucFfZrVatDOxRKmEdJOqHyH5%2Be5seug4wZqRr6TGFA01Ne3ycMzua6jV%2FEzFvrx2jfhn7ASr%2FTLW3HVSPGl0Olk0%2FrsPOeP1W6u0yRcZLuwK%2FWCHt76w2MDYggOtfh16ajPqbp0FWgaKOLPNQXHu%2BZhXCoex4ZYkpo%2F4G%2BTqPNxKqAqhZgUspfrg4aRTiFkc%2FJwr7Myk12V5t8MlTNszfVNd4HfqoGXMxv8bVlKvv9%2B3lj0MHH6OPnb9%2FLVOCxbphPxJbSUEbmETyeBOMMsTOHtU4Q8U8UxpprSqGjR8ttgDHoVcp4M5tkkEgnPWs04NpG%2BgWs%2Bd8FhgFhac7sGJ21bPcxNVtaX63uEjMVtbXRJtZ4PAhDaXkcjCe47rRBjqkAU6jat%2BTQ4oK6SlkcDPIGkKybzxhjR7Ipw02KIe%2BoLJkDjZfxkm2Q3dCjxQodkOf4sLtT%2BeNKmH7JgA745rkQvXahRqi2H%2BYe41RAFivG8cqGQE2b2HIac90WECb16oxEgnnO%2FbpXZ8b2lJ6hdd8Bx3LYE2vDmpShXPw5Ew0ELmce9K4NtYFom6azFa8k%2BltPlV%2BNZxdTKV1mq8RIGcuMqqclcWi&X-Amz-Signature=21784694b7dc0faf623b54fbe8c443d0de72bd55ad094f8db8857989f30a96c5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
