---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z2SMYLJW%2F20260811%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260811T104111Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCUwkXrF5yf%2BdAQPTUzgRLcGv5ntW8FEwraCeabTvX%2F6QIhAPKgOWVzIIRiOeLOJgzFpJ3oycpK6pOz4VSa7y7a4DVsKogECLL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxqubQbfU3LHNcoJ%2BMq3ANQlnJ6HGwpF9WjqbcEXe%2FLCD%2FF9AlyyKJN%2BaWW8TczsTxdnsyqZttMakio1kKm%2FpBU1vNm91UjHYSgUmTTu1u5%2BzNSU6AhnT7aQM%2BKBNOvQCyrn4ySwvOOT3%2FjyG3kuIh2KYgyq%2BqstHkEV8VSdjEdio0dTEmOs2tkkwmwdKMghIVCqOL7u4P6BF6hR%2BJOgdR8dRsRv3cmj3%2BSO71%2B6iGH50WmpwlG8c%2Bp0eq8PF%2B%2FHemFe2LC2TxEKWYIacSn4%2F%2BfZdlGdAG8hEXWTsQ96fAoepbGE8Hlzzhmm17XPPueiTYxQpO0CeZ%2F9zGOiTiXXKX1yYpuM%2FVNLX10GUZ5W9GlWSd0yAKR8FbqRWL2wsQBEpF1J80%2FPbN1C50aw6Ztn1L0v3iua7rK%2BOIfejuEKqdtGfQVmIU0ktmeC2wSDtvfG18cBfjYKnsXXDuujz%2BlzC7uYMPoI2fkYHAuUD0FyJZJ9fRKGfqOfakSx%2B3IdOzB4C2WjkpHMLofWJd9qEzRK3Hkgl51P2KwKGt5yrcPKM%2FEd8tVIW7%2FXhDD2Sqfxb%2F0txTSvhTqeYkBX2FoBRFrafzmxYdErEoCs3MrETghPOykb%2BYzu%2FnRWuXA2jQC4RCaFiWbVS9EYZj3IR46XDCPzuvTBjqkARVe4YDsxNMv1Ni0e3mUi8syB5LN0J%2FZd1tOqqtcHopALaXfruT5wnQQWSGA2uLEmpJZt%2FERWP0N9E7ZNn6em1iKMPTfL5hBKfv1nHNexhy4298CaohtVo78tIgeJ6UW4hcBMj3PIggywcHVYTayML8%2BemqlaWrp7yt%2FtwmYeQBhXscDhxarHCPSTVZ7UhfOrnjrmOEf7zmgjB9XnyJIUcxDPaCP&X-Amz-Signature=c62b8102d4c783ca0486357a38bcc4018f866ec5b572d43a0dc2de9050633fb5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
