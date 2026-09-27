---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YE3INYQF%2F20260927%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260927T033356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEgaCXVzLXdlc3QtMiJHMEUCIQCuwT4wPWQKZgYueQ7g3tIIiWOPgskhsDI7Eggr3UFhywIgYyGQcxKdOUoQSe0V8GoOHrcbQsfCxWZHoOT1IVJAos4q%2FwMIEBAAGgw2Mzc0MjMxODM4MDUiDK5mt0f22sY6vFk2NyrcAwQjPWcAIWo01ADT3a3sYXgTVAeP782IQ%2FCHK9luxYU0PXWCJk9rPmi9gEUgVbCvps%2BtQbezKMz4i1F0osA1qBuYBjkq7R3%2BrMEjVLTLhtGdCYHqRJ5YUQA7P3zTxXeX0uB51fAAlHpPEMJlTRwmqNf6h1ix5Ag0xEQ9uQvLlwRKr4TVXTWJoCXTSd%2BNhXvEE%2FMzFRZHdvaNLfGNXLl7jPdUrJulQnxMb4qe84Ktd3jo0XIepivN%2BoYRFVqOZFms0lU0S0SSx%2FFVjHKqcR7WRLfuH%2B6JvNXc01hOSZQyO2%2B1UVXq0sk%2FGgSKCJlxQoaM09ks9QVE4%2Fq5duVGlQkixpDSxnu%2BpI2jsOrFy1cAkRGcd8274Ug00vVPbM87NzrPAzTRb%2BkC5M1OniJzLN3s0Y8sIWrAjPeIZ54ZpRRxY96BbBSHiHuqzLR4P%2F7GIvyIkIADgnuVPaDBVsKYER%2FQwKEEsKp%2BX%2Fs5PbazztiYYtegou9mEAyHnYEISitvSIoU0QZ7vGDcsyliUqTdgYy0uuZ2qFYj0j9JKZIQMO4H%2BDP1blSSQGyP9Tg1GICgBTris5PXHBJT%2FKFDTPARnISTiRAhZzTxJj%2FE4jOKn6KCuLz9KMne%2BmX6OJy5pto8MKem4dUGOqUB%2FV6RqHKHljRuUtTbLW5MEg1o%2FPLJLK3Bid3HNVCvYC0EpCkLIrMZKRXI9f3BZdS7NjONC8xGDhu98ZmzfkGBzclkftDcsKwHlC1L3YqtKvD5rAVjdAQHA%2B2xIg8WYZwv8Py5Mk4hlmvx6Rmxxnqb9FC0eTaCdqY7o30XpKkbtmNDSRAHGUfnyx0SmFj2%2FeQ1hioxTEZfRVs5ueh7HL4AqBNRiuss&X-Amz-Signature=c9dc0e5492c7b252782ecc4ac24b35f9f9c7225566bf9dada98a18c0bd6cfa23&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
