---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666HY2SZSU%2F20260925%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260925T225445Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJHMEUCIQCoGkLjz7uNw%2BeGIm7GeepfvEAkUPFU4MxLLmUrNC2kdQIgL6bPPpuWWVTCZmX9YE9IaU3hqmRc%2BVsiu1%2Bg8gCkAQQqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKijueSQU%2FX1q9XbYCrcA1forKoBgVT4Pk4LmQrBK5wQZeMxi1G2LnkxZKr6aXZmYVgLE7KIWzwNXj5VGFG0Xl8AW2fRXe2C%2FTTZbxVhECkqarvnJKp3syT0pfGFjy9QwLrukOl8T32nJb305dfQDMUkIq4qo%2B6uEjDHUbUThlpznV7u79MeWvhYAaYDMPOKK92soKHMExeUOZNQBw56Msa5fVj6OY1W0qN4vcdjx9MhbopRR%2BznL%2ByO4Hfw5R6fPhmaV1a9dQgmHDQoqZchliLTnqnrEXxqiBhzmHdksbla4q72bMg3OddlC5uQAahlfnbCV2ZCvQIoyEgOIXwJv1VRv9Ah9AXCwo8zhEN65ap3hZM4Ey%2Bqyy4JpUPDDtFn2P1UAxtzF0NyqYyqp0vDhXhSBBjiO%2F7utuwnvlxedrFeMIH3rnF5umAgJss1XkRkYeoHlkIvDH58xunl4YkrGfYxh0y%2BnBAvOa2vQxJ0ZH8WlRQHe3bcz7wQDpdnxfloTeIAVvW0JLTbjXKUaz2kYRb8tF4OjZMjidJSHQ3%2BsE2s9gbYyYL%2BsLNipNYkXd4cPa%2BUxR80Ki7RvqUXNtFjzVcFcfPN0%2FjkE4n7YLHeSNQOOHLnE8pTDOejeRci29Qjb%2B8CjQVXoK%2FEdDaxMKTy29UGOqUB3%2FQ106l1LvKjBV7NoDKu7PQS%2B0uvyxk5PX30OywoUKCyRtQV1z8XrUQFPjXSN4RKAo6lwXxWgFHZD4V%2F1CtAyXqNcx2g4ed7TqpLsqHOz7RpZia6nQGGjwU4QEXM3ndNWFi6lCO84ofU5BDXCoSQBXKu2CmflBJs2MgkrM4qx%2BrzWzlVko7IpIxWlPpKCx71bbVIfjlisJfhjt6J9cZ%2BC2Q1cC1m&X-Amz-Signature=1fee8939f7d5a7b9fe1c144914cf29d894e7b3de811074a399425785f9c76b87&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
