---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WKBYEILX%2F20260731%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260731T192240Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEaTWIzqa08b8Qpx9cXm5k%2Fq%2BWqQev9g2SzVwqr2XQJPAiBI2MSKQ8ej9GOqieOgGVLFbWVYKZKKrR%2BIXCCMv9LZyCqIBAiy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMgvJEzF7xulQiHjmdKtwDanAaPwyQbnvjbiAwvGLVh%2BUu%2FIKovsE%2B28WhYQziesYfL%2FBFnpHz7NwSGXvn67g3IKulUfwzM8DVEutka0qIP0fr3jWQykwvBI5TowB6FFlHArq69%2B%2BNIw6XluhMAn6dYU0vgVWYRTuAQtFqWnPRn%2BjeqF23%2BnPwbXcSfUqbRvh0lHC7H0hxKP8aQSRj2Z78vGut99wcCNOl34TajC1WqAO2XHqlF%2BvpAyxkF3e6ozVc3HoATiS23g7V9r7eatHJHJK7t5uYhw6Xk2tOr1F%2Fl35XUXTQ9l4Zfitkl6PcjxTWF9amPfVf3AKS3c9p3%2FeCTARASyKwoOeT8zGLCxo3G1rAruO2ipX5kF2s69T5K2hsXJj9ZkMwyjq2eVoFtF33UOIWqgjelCWlmZS1AvBn3v8iq2GPNuL30hNagNBSWntcCA%2BqYBWmfNdKNJMgOkoWJAPYrQDKWR14PQmubT3z1%2BKPfWtF6j6vgatEoGiW%2FfmFTcbmZBnAjD%2FvoAiDAxDTycbW%2F00r7zSLHJKwzQN0kplktq%2FZV4MHglC3s3%2FPcoStPtYgOSalRLD4MeIZPQh1kBeH8Ui1CdG2y%2BsYQLyB5WbFy78FbPWNjA%2FiR0BijPgMyhLgGv0ZMYnFeFIwnJuz0wY6pgFKeGBifu5w5m3sLc3tx1BY%2Bg9LlG1WZs4ZFD9qrQDyGZFpXJbSGbaurBGef2g%2BlHpPxt%2FGiJWO1doIEBxQtWzxkHaXmQM%2BfNcISMMrSgIKltQsHEuSlY6kKCYwEDX2D4zHTdXXvM8pyQ%2FGTomYqHUd4vIgHg3ys%2FoZBpV9nTi3jtbf7EHo0OFLNKzwljk%2FASNDBCZJ%2By%2FfFLIG8Z%2Be4f8Xpl8a7JG0&X-Amz-Signature=1a9ec9bb108b125d4b69069bc9f02452e4fab59421ea45f1694b4fc953355856&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
