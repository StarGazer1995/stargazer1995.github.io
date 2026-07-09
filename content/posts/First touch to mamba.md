---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y5MFC6YR%2F20260709%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260709T230140Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIF3fVsSoZkxxiCQIJn82I6UTDN8yLygfU4pznReHTYiIAiBPsNAzUEKb8h%2BV3APA5ViGas%2B%2BwcwCGj%2FsTXmmCYdl9iqIBAio%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2BG2MzEQLIIClzq6oKtwD4t3qANtrULad%2FKkn2hcUKteeotmnuFEC172I%2FmTtL2l%2BV3TqFxsyplUFJTKa7omxlZ1HEgndngHiNZF2%2BGeqtQylqf6ay3aFyStm%2B%2B4rEALd14KC8txjIkeOSNh1b367O%2BRgL5VxDrwr0fqfk0YR0niPGJq5JseNsl%2FW5%2FHXk9bBzrnAIeVwP04G2BqkEk%2F5ulplaai66%2FvNAlRIOEe0pJrsNeOKxzJ9xKPZLzZmXmzh6qjKYxLIJ5BD8snUfVIuJDOd6uMKZ0nGpbfOuO2cQSAykNRSExxGG4U4MkeuiuknOnhp6Ku5SrjPVUzhkmeZ35Z2NEY5pWqSfaF63XQQ3OWnv7hTIREXV2c01ZBJqVwG6HfF9gQZrLOAOVBwNeFNl8vNDrgliFoRXuoQJxBOJsOSIJAWG3PiEQSUP3XmYU3cjmW2hG%2FxQXAv8X7yVZB2V1rlxpFV2WXoX48%2FTX%2BUB3pTNju%2Bqqd0kgC5prNKG%2FwDSWgmHymI8lJ60y1lfW7Q4QDu4rx1GZhlWjNVrkpp8v%2BeqfQqFvpzusKiOrTWAEZRzcVwErplZLeIC8MNllhZk8BERpMUmtA%2F2z6K8oqEKUpMsxwE3BQtXxkrR3LH5HzPnyXuZB2lDPkewpIwzMPA0gY6pgFOzo83YaqM6djlxEB4nKuA%2BLmbMEPGfTcZle7CdVBU6gxP74CPTmDLddDBM23hRxyOiwy%2Fs3yoy%2BK2XaFzjl1E%2Fm916tgjsT%2BfxyZ0%2BTI9Frg%2BZN%2FpijxvK3ZWaJbpHwJ%2BQnSLLfSvBoDEVnYd%2FJ3XuSg0X0NlcLqiFM9xaHD6kBLS0dzjj3JewMfW%2BqKJSncw7omBsrBmC1ck3pUg2YJmV7AWlWzU&X-Amz-Signature=792b98eaddb7b7528cecb9fcd083e1e824cf1a961a2a24d3852114cc56c419ff&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
