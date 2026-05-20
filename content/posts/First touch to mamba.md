---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VXKK2HFM%2F20260520%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260520T104201Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECMaCXVzLXdlc3QtMiJIMEYCIQDLqjubNvMMv58dwGugz%2FWotLtVnKsDQRqhbiGsXlaObAIhANlK054%2BvFyrnl6y4woXwoN7r5CcO%2BBFacu43JOFW7kxKogECOz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwBHdOrJ2g9sX5k8Iwq3AMhnaZrVaeXmp5B%2BI8LVB7EpAkh9IP4Dvc%2FaTIUYprPMeYE2bLvfRylZRSN1QaEknh7kU780kNRIzWIxWrKYZTcK8QP74P83VIstcjBteDQmpiW6PLAPcCZxdWobdBw5NnMBDrjP62RsTV4n%2B73HqmGPH46rzKsWmQ5mIGkcsq61ZVG8Ayie1%2FAlHJkAEbkHGR5k4XW3aDmIdRzFLmhQM4WDoqN440KVSO7eZWjCUKnLb3wmgZd2ASB2y3eERa%2B32cliUf2LMTsfwaQTvNGvtXIf3YcRR1mcUKjgSLqA5fowuP0WOfFj3MF%2FNvpOkn9t6Eu1hYcl4zh7%2F4fWrung5zFiRav1Qjh6m9nR6Nw6A2hYXRb8j%2FLKnaqf227lTggsw3aMyAf5ZzaVevy4IGM8Oe3SvgNMicKXkJ2hyM0bBAZZSUw6IWbY68mt9x4YK8DFMmgo3HpL5xiGxwAZoWqSGJcrPmM1Wqwqqbs3QyoTfHcNEirOaFjZjWL9ZmbBNgJwwNFlQ1VI1SlJMzdu6n%2FmSL27P9t%2FEjOkgfRvZ9QS14HZfmUzEAEul2FeMjtMqCzDh3ao%2F2NZTlxZwq2jKeoRUA%2BIgbyMjKfKykUrFqZI8ymImFAVIwCxhc0X%2Fc8ETCynLbQBjqkAVuKV1MKvhW%2B7%2FqjF0loF46ZwMPZhs6Yq%2FkC7TKRzH1I3yU8NEs2X5pX0aZwx9LaCbQl5aHF6VVg%2FiokBi3DAOEHlYAn4Bh0RCV%2Ba%2FCVi%2Fh2TBCw3qh0349w5t%2BGi3y6ha1rn9%2B%2FBFb0O4tTuFSoKtrlQn9btqpm8pJB1FD%2B%2FG4CztDFMSX5hEWggr%2B4jCCvgg6cP6wXkjwkWj1ZFW4GonNQY%2FSK&X-Amz-Signature=fb64b04e01f489d93dcedb54e0f9a097b975eb590b4c3a99984f4b24a4e71e59&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
