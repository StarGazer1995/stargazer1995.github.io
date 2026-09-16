---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665PVIXX73%2F20260916%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260916T085448Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEgaCXVzLXdlc3QtMiJGMEQCIEimPrKhDgpM2vQeVF7Pp6xq78n3GQ0jlqj2q2K%2BaXVgAiBAa%2F6yJ99X3BEZE3MQyKkqSXHQiORr0FhPMmCLGuyx7ir%2FAwgREAAaDDYzNzQyMzE4MzgwNSIMd9BpQJaszJaQDvuEKtwDDe65F3hjJf88qApTU9UBmBNBgZrk3h6z6XdiqEMFD7%2F7o8OtWiklJEZ9mR%2FkQquvH1CP2BYsmlile4uHKTizvmqAcVeBoQtLN1%2F0OswkHyGwHOQEvcevX1PHK68MxXgBDOvqo%2BRMAuBcrHtDuZX9bXgAzh8NgM05IBWYGt9XvNaLQ1qx%2FeSMEtItZ9M%2FuB2AJTqJQvQ8jzl1ppOk1CgajCIUd5JwIEJGNbyLBXar6i18YAfF9yui6QnojLGa2Vp6O1Kc87zmHN2a9egeNB7O9USsb6QFY8saUESHcwJEdjKx5iyd44UWktozEu4fzkD3NbrCgnue0tCMClellym64q9P7ZxShR5OnXYOOmaaxFdRvhf%2BmkabsSTMqwLGUtqVbXXRlj9B6ZNfScTYovZeVNC7kXnNkupHD83yq7nLmJsZfJRP%2FQBz6JbjtiKb8xUjCBmyw1RQDp7Ak5bJQD3bP1Xb%2FRvZUbuQ4amkCKv1%2Fa3eydn3vEL2BGOh%2Brnk77ADZm7TPcerSPKvcKzC65SffD3iSF%2B8Y58%2FwXu95wyLlcFRurN0%2FnII6YWxn3rdM6i0yy1T5bH3sEYfJAQGTAqK4rr3sgo5Bu8pZOWOdH7XwYnk9glTljHdEM%2F7jMkw%2Fpyp1QY6pgEOgElyPcvJGkuVVIO7xHzvkPBML1b5lXUSL%2Bw8i0JG8hSjZbfjyksjVpGrKVBzM%2Ff3ang2%2Fd2eA8%2FM6UzA%2BX4p3y6NXpXpupfL7Dbp3hQzlPtsboK8KUC%2BTUlzaZeHGncey14O87jOSF1jRWShnjkmBGj2WsI%2ByC1bK7ISEjyYNLSUdE1qvJFSEyR5elIqeYDbGcdz7fZw%2BizQg3myMty6Mg%2BuQXOk&X-Amz-Signature=86d415559ba80fff2ee62fce0b6337ad664203b819b53a992b8beb40af8d1f57&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
