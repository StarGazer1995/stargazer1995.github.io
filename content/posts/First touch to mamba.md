---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664FFLHZPJ%2F20260726%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260726T185327Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLXdlc3QtMiJGMEQCIEmShq648%2FtEwrYq28lDnsU06uoUkKRv8kX9V8pPZw7yAiA0DFqeMe5gYvbrVbWyJpsui9WI3A%2FyzJoT7Ss9bOwIgSr%2FAwg6EAAaDDYzNzQyMzE4MzgwNSIMmVML8U9epz0AULL1KtwDclmvR5DGsK6xoUxa%2BqZEPK0YoqJkBT3t1WyEqGvCiZRokdvzYwvGr1jCf%2BQSW2QoqdCUdcLZIga2NX%2BzJJTf5LUISuPrsMFuyUDIU8nKkMeLdAyKoaTDchX14UJFAMPx4joAYGWGKBPbvHYso1Kst78tMyx9ATAUmJrNHz8D2yNmUhtRZ2eAdG0trf7brkpscWYftSe1wAMwsu4r0H%2BQXkmlM30ddzt9czWgcYvl2CqU1eIfz1i46RDCowYESyFAlyyYXBhTG2SUoEhcHWkJ5M5A%2FG21p5W%2BlHRuQFytInnVJacUzZBSymPow2KtW1aEyLMpmdH2EVUyaCe9KOUUPHNDH8RsQMYYssZqAaEXfoUS3D%2F3Fl%2BLQPg9VSQyQ70TG%2Fc9yVBG2MoDe1rXyXL8XPosIDLKwkvJ%2B%2BcaCkaNzoE0kYCbEkIEwejs71oKQHHMGcr3sBkLozhmH30upM5zQf0J0wQK1%2FZTZE0vyGw5fdJfoJQXITCtHpaX9O6G1FbzH1VsKLCbn%2BIWv6%2BkpzqmWXh5IXJtYUqVX6%2BiUr7plC4gYvoiEwmQAaJgZT9drvc9ge4vC2mXOkKhB3Ck8w6x8kVK098t3R6tNM7nui8mTHE38kz7YP2FJrd2tWsw%2FOmY0wY6pgFh32AvVsx8NWiZs%2F6ESCuOYrDO4jdrEbumAqMs0QtrwbKd3Y1DioMf%2BF%2FL9PPJgtlu%2BqGaJdqpaePAhiKCU8PiYIdIhqZKWt4kGyVUFBykwv8rxWNTmSAbTDFr6foQ1cKomiPCUJ%2BZXy34FHQfQshVHm8hGs3h1ksNxDgZBdyYcOQ7A2ZJgOCBVyjr9KKep76xu%2FOtjRVTT%2BjzzM0SUcjuFTTnASmx&X-Amz-Signature=77f70269dfa8f65289cd02feba3580c738104334fd2be482015fd3db66b30712&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
