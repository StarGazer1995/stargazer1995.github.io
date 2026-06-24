---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z5IXYZQG%2F20260624%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260624T140315Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG0aCXVzLXdlc3QtMiJGMEQCIHfLP5XjbXWvE5CqnQb%2FJuHboIuejgFQW8JGy%2FlvW6ifAiAQffKiDFsKQuptq6bW%2F9j6JNkJIfOH6uwpkD2WqyTfmyr%2FAwg2EAAaDDYzNzQyMzE4MzgwNSIM%2F5FQjE0xmoJtOaFNKtwDA21RaETBYMnqQVElaI2aCY9Umy9%2FZ2qfw%2BGuQ5MxpI0yup4dSSp%2BccM4XZQ4OnxevwRzVkoJN2a5qufQ4llDzJZNOrr%2FH5NXLp04NCtScOqxBotB4lwepEKnqAIJS9yQVHUj5UzqQfohIn%2FIAoQ7mh4k7NO3y3r5kzWRp23bq9tD1rJHtzhHmMkMS%2FX%2FbmIT10UadAZm6ZPBMtEjmBQE7BTU80E3vzGbQcRCCn2k76aCaM%2BWdui1Xl68KWlgYt2wWDGT%2BX30g%2FnUCWkTq4yWTeUIYETYgC7BIVRSV6%2Bi94cNn4Dchbh2dkbLL0znSXNGPmyyn98pvmIl3NOxQi1KwcWDU3B6XMPANwneZROTzhrcleVoZpQX%2BwYki80MYwztyy4d21w%2FBzziYj26KwthQDwqf4A3cxzVV2yjZ0gtFy2h0OJ3Q7esjcXtv0lCm5f22UpBzBLBBqjLcvvlLFu4vDDzcX39ibYNfU4iKddaccIekOJehXGJcxqJm5yh32qnaPzeAcH6M5NHzN9i4fIpL1X8%2BtnUtQj9pjIh0TPAVrCms2nFDN91v%2FQZLfR3ODOlhMpANV9dGBTbALNvFj5bEy6MrPBIN%2Bwt604gn0rLO5icCTS267VGfLRklPkwlqXv0QY6pgH8h5oviVYgfA4ODJaFZCL1gJcYr3kmdLTUth%2BmIPKsLuXYDrnw607XOP7HkeL93KhgQtryvwG9H3i%2BAfhfpIPdEYtxviHP6z0KiIlKiNdy93Otn8%2B4%2BrliNn6jQwAMDjTdm9ZDKqUvuJB12ECJ7KPKWSh4IxUYK3Ly0%2BTlx6eXvG8PSlS%2BvfU7bgDj2Ub%2BjJwI7k5qqPu1CAGL9wZB38biFXGrCBVI&X-Amz-Signature=1dd556eddb8fecf304e23fbbbc4a1e1408c086f6fa38cb35211f45adeb637be8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
