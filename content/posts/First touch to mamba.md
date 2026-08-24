---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667KZQP44Y%2F20260824%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260824T102641Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJIMEYCIQC2LcR7LqiAT9e5F191aIZBVRjJt2n66is7KIpv1KW8ZQIhAOOiUs8dlqneerLmFg7TChvZCqDZVqOHcSFltwwmcszHKogECOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxJpwGc5WHsiAqTSYgq3AO4x1vV0o3tU0FSM1NK%2FcMDu3q2%2FtrWexFVyx%2BQJn4MV5%2BEhF1sNTFxANKZaw5LlAmvhoOb2kVUMvN%2BNr8EmY%2BhHLviPn02TxXWQaH2oVLO%2B%2F%2FvaFWEgdEKRsBNVgRD0r%2FVDOq1C6zO3tcF%2FmHqicd9TV7W9S0dcf3iWAIco34VCldXy94Q4IAgLlkMkW5hH0YSp3ifm7KJ2%2BDZVClbCGZhxFi5KVsKxx3Br11iMdPg1F4q8%2BrwlNyNlnZUNr%2B1qcHLQKlRBeecjVrUuiDE1djBNTq5mz%2FO%2Bdt1ud9pdAUDPG8sB%2B4NtTQkLMJ%2BYPUjFDAUHObsgoTXVkCuLN92x44AdobjN5M6yLMFtk9sOQ%2BAi%2BWB7NjaSXUPWiAuP4HDFBbcCGM0Qxich8QqhRZDksWk3jRPHsi2zM9wELMf%2FEtn9zyggqmZvPqhwgGxD7RVE2mnQvVqMr%2F8nnyhDnVEK%2B%2BzbUSfLBx1AnerxmzQk9GGVYLhdxF7Tfc0trw%2BDPwzIGW8xVTj1hsYTyzLELDtRQ9%2Fr7hUSug3AgPz%2F0bd5r3tXBc3Q5DFOZDG6QJYFMvr8zFl%2BROrRKbLfRGUK2CcVbI7fhLvx4JVBvb68NNLgTmuoyo3p%2BKSFLGQmQaX9zCEnrDUBjqkAe4E%2FI3YUJKBzd1VuF1%2FwiuqP6MX3Jel6chYf%2F6JQ75qNg5CEWf%2FMBIq%2Fqj7%2BMK9Hvv71NN1mzyi2UrVkV35hADwy206qGCXwDlD6TpQy2tHOO8Rv1MvMZO9SzVtRut0kkdHpAJT%2Bn48najzwtICjACnR7HNwiSmuAyG%2F1XtSex%2FMvNXAO3bW6creewyeREKEDdvnOMUe%2FonsNFJ6eQHg%2FiQo9wu&X-Amz-Signature=6051fe2771c63c19eb69cc6ed7fe485c93afe406c3f1236bdd8b1b92889ead94&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
