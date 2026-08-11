---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665LLGFYER%2F20260811%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260811T032603Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHQwPxx9n4eWuecYFBP8%2FQRTbDTQyPbGyODGID3lc0hgAiBDxViKE7sqwyDClep0RtF%2Fh9w55SIXlTMCRu2M2ye%2FMSqIBAis%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM8u7G%2FbpMzcr8bfmnKtwDH4qhAophrKjs%2Fo%2BU7hTFrY3fYOoNjoHFkSpMLtZoaE65oGREsBZGS9nqTh3E1aY00ZPr4X%2B%2Ff6EK%2BiNQOsajZggGo2Ud7zo0%2BgswG5CQ48p3XbwmacKqD%2Fb8%2F6U7QOW8lKLT4oVT3FdODqquFd9EBtf4oSJh%2F6bq6gxSDBocLULhzvBGAnr60ZoC2rAzXW1ih%2FSA%2FFwurH6qqFulz70lWcQcaogAxjT4WbhZWS8jb9ZLc83Pk7rqXJYqSsPbE%2Bc7hXceAXp7dsNV01HuKJ6axgt0%2Bq0eeeua9aFXD99oanA0jTCqh9VXUPGroTOcxnsLP%2BefAhEgMD6cpkcjTo8pfS9G90w7OXs%2B8tALRvksjNG%2B9tciSC8ZMUlHyVqhRsklzYHbR4zBXLXkHZz9yrSI9sS71ZcVm4qItL1NDoGeShczqdOpb7GS0gnCvELeiYKMlueBs0C3UnYUB3T0sbgL2NextDW64lhtmzML7U0OElPCz%2Boe3%2FrsyXUFRccG4reKFt0xNkY5N6rXiZo%2Bes3J%2B0r93Ebdj1jRQwdPpZmaDvjhyh8VxbBDDWCn%2FUCFaR77j9VsdIOHEK0eRlqsgdWBBmp3uvt8xIhDjdsS9Ogo9DCisWiHDXs5gwSulyMw56fq0wY6pgHSab%2F0WDDPBCg3UHm7G2PdajR1iQG2IyAJxl7hQAotlUvaKXDasRKJqyWJOtt1aCAS8LdqFBNaP5GDEpInoqIQUXasRG5MJ%2BdlR3OTCNu3MNNw4WmYKLTchZ4Db3RLeKbIj2m6bJrCzIZtCbXadrCTvJ50pClpVgxtLoJmLioyAGEGmvrzQ1h3tId3OOUE9BBrORC9LPKVEdq%2F87kIvLnXQRq2JXQd&X-Amz-Signature=2dcf5dffab6e8d62ffb26a9f9e56a3acacc7ed33a47d4135459ffc65a770fcc7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
