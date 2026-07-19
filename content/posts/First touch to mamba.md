---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663SND4ATH%2F20260719%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260719T224015Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDUhgMZB3i9nSte3L2xOyGU%2BUr5ejuTyGElRe2GnKLJgAIhAPMz8KoOdo7xI4dt9W%2FWUTMpaR%2FXL89zrxv14U0FwL0QKogECJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyL%2BhFNWOir1hYfjS4q3APKsB%2BUKggAJtlJko%2F2khVjTLMUZDn9Ma1dtngy3uBJjpMurYwDU4thpvQ1%2BDWY1odl1e%2FuVQYIUVZElf9u6edRZAYDt%2F4bhlXVYajzEQHZE8PChkvhhKDElHW7AJ0utrChahRkiMQCVO9WjByJy4T6ItP1V1hBdWLZ9EWSaKqshXwho5oXW4eL8%2B52QspFc2MCaOymKO0WP1hmPKbgkkmrAPzrqCcLPFcOx2pcnWKQB%2FOSxCdswtVwQ2wzCJ4eXA2geif%2BieY0AXJcPFM%2Fmg1lnHKSDjbaFSHnyRCqkTvI0jYHuQQxZV0Y8mjNVIVyFESfBJZFnsMT%2BhNeMwljp7IAzA6Gn7dyeo0rzY3YqdGeZO5%2BAhR1s9DSXlqA3gX3y7GEFrupqA%2BFzKwNj1%2F34zNFCYbzsCf%2BkJ0GXo8V0mAJlo0pwaHeWVWm2EosLk0XC3abvQBCF165YfZYZgSc674LKVdufrGC2219Fi9EecOBGWQaDcVjHgEpmfT5Zxk%2BSRzsQXbRF74wuTpQ3KSK4b%2FNoEVVFkqi2IgWlNjRU1OEiS6ECCEOzSK4EJHZZkYOiTh0O09xR3OfWEvWfvnPOt2KzzgzLxisMDKsAVyJtyIFxErlb4w1vm2tYvR%2BqTCd%2F%2FTSBjqkAeUW5AMfl4Lq9K7m4HhzNHx8QJC2aBuTbbjPsp2jPqQPMNGW99LjQzdflB1XkNByTWcvYxzW5Xpy2tI9W85Sq4RjxhETwbM%2FMqhBOtwDt9tB4nDhsmddiZe9Zc1vzh2%2BDRzT1wzNR%2FXK69GMmDDwpUHA666aVSMYkPC6CaziGRh58qYQKDoMPBVyk4sqCSQ0dXmu6Y1TA%2FeT1oNulKAlme8%2Fr2m5&X-Amz-Signature=b117e59459f4338cb6efab1c64a0d0c2f015fd71514ec157d13dc157e7b3f605&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
