---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W2W5WYJ3%2F20260620%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260620T225751Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJHMEUCIE9c2Mza7ObuzFTV2aEpwfIEfh1fWJetIkEO7LXjZ1wPAiEAjii7hWyOoiPUHFfKsB4CvU9jcuDvRG7%2FQFRDnBszzy4qiAQI4P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBkMISo6hRMhWpLeyCrcA0ZO9VpM6Lc3mBSpDI80062z5lUIowgCO6Le%2BhoGX3FgME65W%2FL0%2FSyZAcTUpkq1Sccx0FOqNzn9IAK6QDcW6Akbi7qDalg3DIxpPHu4eqrn8elqgQ9tU0W0MNv%2BpmbRyljGpjSIeBzeSp3YRnvmRZxZHMb4ErShMRYhEaDQ03Rj2jYdPC1Dap4G2PkBx9VU4Fni%2BngtLNfqaDDS1wssRZ5vE688wFgU4wu6OYhDZuOlIez4kpdmZUhG%2B%2BEj4Y7zXOyRvc78DPc%2BlDjDkLNQfxkmebKa3Ipt5LoSIFs1TMMr2Yr1nZI2GUTpCRCHC5X%2BIM5R6hziD0nSKWpYGHMB3ijDwENbBdAWj5s0kidDfEmaBi00ngUcPgIngA5DyOCHpGAKNeFKoOtgBJZhwJ16vzVo3FJ347SMK1igbw9hZem9w18VZej1IL43YE8UVUbDQcogzAogUFyzpEyPyotvxmJGiU85CEUairxs6Wvhw1yhv0ZbvGOxUvZGSdrGkzL%2BZsuUOM%2BWgay%2Frd4Iz8bDwODZfktuaTiCQvjNONh4YV1wzEvlhBaR5a9Eo5x6eeoC%2FFZNyRar1IZLn89ifg8BYGFL5nVjoKtmAEliig%2FRRjSQNev65uYmL%2Br1eIcqMJqx3NEGOqUBiWIaDIdTRLxjr4OZc4wWaEfsCiIT2WXg8PrHqrB3m4kT2aj3ohbptGO%2FR7hI19Tb0%2BmuB4MM1mtMkfqGxgX2ux3Ay2%2BDyqW9UdQtJUT%2FaY66Bid8WS78NjaMW0sKwKdr1zHF0ErZtEEhfz6IYwALqsC6iw2nxDshKVeSYYg%2FMa8PgqwTdn0uFhbl5Ih7HXZP9pgnO%2FBX9T6qDONtFj4hF1IhK%2Bpw&X-Amz-Signature=159412b1b3251f7ce0d049a2f45e0f9c28f775054a2f4c09296485eb8ef45d5a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
