---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UV4CESH7%2F20260821%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260821T142319Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDSeAPy4g%2Fkr5Q8ZKZ3bOMtATZ%2FZp1zTkc8lQmtOe85PgIhAKp99ppjWKZGZ%2FKcL3HWVl0iPmWY38itLFJOm5sztVAGKogECKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyWobKNK6VxdXBNyEAq3AMV62acEn8EX%2BBFXe8kZ%2FC9qLx6Di0A6dRwUzG1CG9YNibwCGlZbHJKTmKz2jMewuA7RQVnZoKY52y%2Fu0O2ZcylSFfw%2BTxz9rlo7mQ2tFXoCVGQLY3i1yhDzrtIcG79F8xNMSdwKgdgeQCNIWvqu6Q06fM8sr1hAaOVQRb%2B6kGaLF7AV98KCAFe8eMqTuXskweCm8ijkB%2BytcQvfiEXMvBwUrqo04WYaXrDfPbakuXcS%2F%2FXCRMRQpF%2BVVIkWlt9j3T3dcuwyWblT0EmOlJOrULd7bF08%2BjtuuslG0jMvUWkruDSSt5WhB7UjpUqxrCubnoq7qrzc5i5RTfsMagRLCoN8x5vHtU%2BANkq7pTE0Vi2TU%2BQytTTq8dgJSWOP5l5xvawbBGcaWgbtOTbC3QYVrerBe7sis455biAu07fdDjbPc5j1adrT5TCIUxl%2F9ZnqfhYXpHjMgzH08OzRZPxClU%2FnZRWmyyWgEqO67fGq9sMh4gv9ZEnM%2BISEEfKcb%2FQ%2BElqNZZaYuu7DT0S%2B1bIpGflHPbJpa4YLYtM19Jpe5ex3gGcws1kWhv%2FPhNPyzr1SfmJ8Rqt8WXVwaR79TGYVNEf2Z8bI6HXOuAbMx00q3DAkfK41LbXAu%2FyZyfF3zDLiqHUBjqkAWjWK62QQRKAUFxSzYh%2FfIOb%2BNUOLUHH%2FVjLmFO2mWFWT2uyM2KAuT1PmXKltDpXyxlDgYrdhAbFueowAaKpVi5YBktXDbXAWa1hVz3oJ5t1ErRkxvoHOhip2IF1LMtqickSc5pjo3kDcVSGx%2BpHsRkPEDBKaNGHHOIhQYpLVwzp28fAf1kEJR2uc07oEl3pCiyq9E%2BBqzXG3cSEf0zrJ%2F9ZOA%2Bh&X-Amz-Signature=fe9072957866b73ce51c1674e3c7820e7c51e51947c56cce808267d3be03fba9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
