---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XT63IP3D%2F20260713%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260713T084338Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJIMEYCIQDb000n1OcRqIUb1cv1etMiinH05YR%2BtDfBMSCj6y88%2FwIhAIVw5E9uMf7T%2B%2FkuN36thCM9X6Vzvb9sJC5V%2F6Kn813TKogECPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwdV9T%2BHEavPslvyCoq3AP3spfB0alPIkdozZ3oMwkbPF9TddA2mqp4HabA0h0TS60z8lWgqM4uX%2FtFAbhxAqW6M8QJ3O4Xbvef%2Bv34HdWN3nZUEy7sstyZgCTq7iihXzKOKG3CsPp9E6wI4xIbwTRP1o0FBKOFzMGDlpmVvXpgAEMlZuSceCAhbYC16urWWE4cQP33hDkaPn67OI4r9USlUwL2wtowql%2FwxxiGo1HzPmg0h7U98lMFJ3TTzDV25%2FyPw%2B3AyOXYYMK%2FN7Gp3P81DJCtJ1etz87SBr51IIJBi51zBMKeFMF%2FASms7KVHWK8iii7gWT7L4IGmoi417vnHflLoPtmkSKt05anAMZ%2BECbVmcJ2NJS1RDEvVuTqWq1S%2FbIm48pXuzoj%2FtXYJ80FFX1hWWOCJR2z80M4DP7bCczeRcSudsmaN0IKT21E%2FeQnwFDQ3XXvHkBjx9%2FCBwNmUrmVysU34hPxVm6d4YqsIjPnXt8rXo6Es3fhqdjydKdOhSS7aHIfrwrcDeAWXIHfoaasBSnf2ndMgMPsGWUGuepkXfFFTV4MmiaxiIQvn6Bpa3QeAUk65okiagxjo%2FjbK%2BL90JWCLfYbuTOGm5G%2BZX%2BmPmNpOpbFmKYk8JJLN6JkKnz1KDN7ObfWWUDCOnNLSBjqkAVgj3mULQ%2BhDy4rBKGyljw%2Bs1bnwqEswnjz5S0aEak57TsfcAN7AC1F%2BEKoNiEq%2FyfZvZqBjR4ulhpAXf0bUGA6HKP9OZ5TXOn6wnvQraGbYhr%2BTCDGbhbAWZniVq7wl16wTDrIFgan%2BXjGxFrdm3Hx3tFx88J562U5%2BslAcimgFW2vbaol5GJswgH5S2mY40Sme8Otqd7UK84fMxVNib%2FfedDk1&X-Amz-Signature=9b2144b7477b83ae1fe252a999fdde04481e48443c6b81b4148a6c58910883a5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
