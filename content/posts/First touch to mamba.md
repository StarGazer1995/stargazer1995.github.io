---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662SSZDA2N%2F20260514%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260514T132612Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGuWyCWIWHUeo7etzpQ9GuxlLKhULPskacwv57m1S45YAiA9VhZuwdJotp6wHszX61NWziVBMWefrhPzKo7a3jhgGSr%2FAwheEAAaDDYzNzQyMzE4MzgwNSIMECBZcLkpZ3DN8boXKtwDbkUQXVh8znZUFZoax9Wj1TZThuBsJZXhkeVDoFOP9PFIjuTU5qFMujs8eox1TU6VrVjvJD2sPm7ZP%2FxnlrOVJEdphlqc%2BTWeyJu0H6P1BkXlQm6tQ6PZ1TJXWh%2BU%2Fq6dqU3h5nGA3JEgEN4gvg%2BLCDT6P1Zww%2FVS107H8SUGJRyuoU3nyVdGJ%2FxnaPOHyHi42isNYTZl4mtZl211bLhFNGEy5Bdmecvw2wbmSwB%2BSFxDY2Yp2%2FXYujOkEUoG1X%2F1RwsxqlCYy3bU9DoaYaDBP4TX7w5%2B9EL0z%2BsBXHlnarGJtG%2BKQGLYaME2SB4B8tRtmAXA0F1pZV8DId0YRbRlhvtFvJO0JlDXFKVDl5OMJM%2FkgX8RpJ8JUrHg3dr0jorTym565dklPIYZ8hbsfBDlaZ3Gi%2BAwer2BtDSzessR916jpLXrciu3sMwoQ9ZlBryVU8dWrTH9yHcJd%2F1MtdMoLz8fAa7V16uoiK6XLI1kyRcJtqMifpsaprqJ6JP8Qt5O8HCzkdxXkId0RNmvHhW2yNwDCsrLHnqFC3oZNaSXAg2%2BPf%2B%2FqEGm4fjdPtRnPYXiyFmdbekh1hOb0i0iHlpg%2BZ6bfCXfBe5%2FEBVSXb0HXmddrtFUZXfLQJHdcgEwzZGX0AY6pgEJ%2Ba11c84TnT1O4qEiVpUfr2HOcp5w3%2BdDsPtq7wYUrvyIUaJDLIaO2XNDafclpXiYoUZ%2B6CMVqusYjb9F3SeIlj4ZKEaXVpqUlaGqOptX2VBDhvF04SGuu1CKSgJzJUdATUtqyaNf0cObcnhEGLSNPmq%2F0QzC8VWoGnZJk9QZHVN1k9uQgWsxR8lbBEEtT5eWsA%2Fs2oVPewc0yJePdqrL15qg8a9V&X-Amz-Signature=531536e358426cf5ca1354134b24a7ae282081a23dbb3ff519bad2daeb14f136&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
