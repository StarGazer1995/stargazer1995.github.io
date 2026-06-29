---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T5OPGM6P%2F20260629%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260629T165136Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBb41j%2BkdLFNFlTXSN2ajQQu09IggnHaDNVIhL30iVqeAiEA4F4wblLKI2wdFdpewaQEi%2BWb8mTMIz4kQiFjEac%2BGyoqiAQIsf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAPRQTMJrKuEEhH26yrcA0ssUVcArVwZxil6StKT1bPfM009xT8m2yZRFw5mHZmRG1DiNVeN5UyfRfU27u5w7q6hN9CEVPQmJzckPWQoxXWpN%2F7Al%2BQuoKd48B94KUdBkQcZ3kJ%2FR18xj0O8UwkqFLggaAdI3sjqsofYTUsF9lBBEd0LvgZ6ncXgj4p0TBU7rmVWEwKF%2FTtWIQj%2BfCvsvsbk5qBqTNmjmf4SESyt5Yl8HE3UTFsTvG0pBGYuZWBuPb7noI5oymiJymUteOt7EfO1N%2BJpjQR%2B40QCYZTyLIxbSUvW3YAiokwdMQLflIDWzdy0KUH61cOFQvhHV7sTq4GY3Jj3PA7DuRsn3nH1IEnMjJUsrnSj%2FYM7X4vv7uDujET6eHuF8gz0njTuuc02MeBe7jYK6Z2MISYfl4zVypYYf0kvtnilu0W3S8vb9t3DbCKCNes5nHLQt2hE283J%2BWcNjSq4k12pnued44fTiW3pzcXQ%2BGVA11u09CpKORR7bo4uvlytAfh0o91GN8crLliyAF6OdUPmv74pc6iPzAcGFD4SArsy6VkPA97LQ5w7ZpnUVngNKviSnD8FoCJkdZO5Y902AY5vqYB3JxsablZ2yCjpffIwv%2FVssm1ysMOFEvk9zBEGeyaF7yK8MJ%2BeitIGOqUBPPT89buBQruOvf1Az1tOUFdoTM0d9vXkcSaS67f%2B%2Fv%2BqdAccpkFe7cRtsQlokk3Hxk%2FLYvdBq%2FwXIshya4a9%2FHXDmpNMucH%2FF1BOMBi3HvUrSWJCeA%2B93j%2BTLAn8mb4zJ%2F2ZdIqQpvYhpWG50BjtD4WMnOI%2BnBVEP2%2FdAZPAHQnwXRuBqife5%2FIQ0i8DB2GpHr5O1BxaQz1PbSVp7Fcmnumq34VK&X-Amz-Signature=7125dc64cf9d81a5303db5ffc7208896cd3c865ddaf4233d8c83dcca0a85f332&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
