---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UQ2R5BHD%2F20260806%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260806T011926Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGkaCXVzLXdlc3QtMiJIMEYCIQCa4Gx11aQlFhHXUDDsKGMunDOKZsVocm%2B6JWcOqfHXgAIhAMWR4esitSvoyWmlTY3mW20426z8q5BVb%2F1y3XhG8kM%2FKv8DCDEQABoMNjM3NDIzMTgzODA1Igzn2SavtOu6pmho0%2BIq3AOQYXpAmgImbXLlcmRNsVwnDnn2b882k7TcnfGLmwWYhnHJZQAgncb6QcFoxVKDS%2FHy1aqOajviaavOOx5FYTPmjAwU1kSkffAJdl81rsbH9qYw4ZF1b6b4m00LX70fWkJT25zrh9KiYpNRt8eC2ta%2Bv9Eyz5f5%2BKLp8wE65HfUEYG%2B%2Fva0C4775y0qiL0ssUBzJIdsAH34v3HFFwK%2BID1P%2FnIldxeKILIYaOr7JcrGUuT%2BchXpjnUa1njoWln%2Fm16lOphxZo4eu6UIwPIvywlcXNlB9e%2FSPYfeEr%2BSV2hluH%2BxCiedixCVbEctlWf9wSYEf5ajkbydO2B5ofvtHgfNODXW%2F5FiJIXkMKyZxj4m7DwZXySDxmA%2B%2BClqu9fgj5IK3GADj0I%2FFkSu0V9oP3MevNn%2BVaAOsu2RkiB6vaKl4YK7ibrggErXlucHs9cBKtOcUUn0yIPt6ZlijD9K95YSH0A0dYaKJXHAkYv6mOAPzpZgEp0nqGxZtrQm%2BaRivsO1TM0dvxdv1Z1hIag%2B5WbZ%2BWoEudCBW%2BUU3TYByrKqjk49MNABGtc8b%2F7F%2F3%2B3ANE8nt6YhA07tQFCBkmmF6iq7FFJFtOBub%2BDLuMJmkMTusAdATd0l5jDbphGjTCUqM%2FTBjqkAQV6mam7XqgGGh8DgyYfCKPp9SlmVlOJv8Nm9SMyK2Lr1D0raoQc5yuiwdqg8anohG0bQ5YHgi4k%2BtpWUbrJylSjShzmIFGMMFBHcLjLex5dF9TRUutyU0qqO8na18LQ69Ux4K1HBgBufkwFGVdr32sBhN3Tz0FhRo%2BRueMTpgey6rLVfQXQufDXGpaf8P%2F0Ttj8Lv0sRTR9DjSF4ihauhMMLiEu&X-Amz-Signature=72c352667127a957e7565154c5a4389b3c1835909c187994a2715adc6936732e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
