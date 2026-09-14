---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q6KS7Q7U%2F20260914%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260914T092020Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJIMEYCIQD4dgo8QmsWvTuZp8Qr7t4AftWTZhoX%2FdyDK2lN%2BVjlWAIhAJZbbAO%2Ff1luCmx%2FJ8z1XbY6RYxKvo1WjFA4bnYEPGqNKogECOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw4rE99%2FNyvELOY920q3ANRH06XvRiuubRpI4jyklPW5z0PyDJ5%2FsvHulPfOofswMK4xYwNTPSEzT6dvIiYQdaVRuO5lACLjjj%2BGW9%2Bb6RGkQO32X2fSTzh2vSru%2BlZGL2rORp2MxHS8vSe0WmUwV3nUc%2B8fZfZ1GHWI4vK5fAAPMxFTgwEI4blcx6OJ05LTZF5a2SQT1ULXgoTa8zLd%2FAYXWsn1Y6mO62Pvicgq%2FJ7Cl7G5G2nF1Ie1jU%2BdZghQwcerDUz7hZAD9w0ZiIql9gnRDbftc7lKhz8PWHnsd0N6c0m2JpD177FT9eMfeYptlNRqJmVSfPozDwELguTbPupDmRZTPbwQ1%2FgRL3lK3saoBYREnw6HZ1Fu46CvOnP29XpUKfg4fo8ZzekUtJbwIc5WT2bB5uAaJgQqpOiVGracgqCTS5lJTep%2BkTMR1hMWQJD1%2FVkd4Mua0p2qY4RBa3c%2Frwbp9u7Uacet3bjl4upLLTF9gQknfM1oJ2uFI6XKrfXkdm4yKWlO85OptdRnFf%2FuZ0kxC9Ed%2FKglR%2F2TlbpJnfQ8xSdPO9uqNvC4vQp0YBt%2Fl9udCLcwbI1pSN4tY%2FVSFGfVth6wecER%2BeRGj%2B1JlKNn99GEnAmx5xisK8xJDlsDMFG%2Bpl6OBvEnTCe7p7VBjqkAey9b1B6m%2BInDg54FyxFQozuEBLCOwmkJ9N6cBl%2Bm2U3AaKq0o6EekVIK3paICl0viER%2F7mEZ9rF%2B%2FcDN862OFz26KjK6hQ4cOxw6CEvAJm67dTYh0jSJEzoYErhA3ecB%2Fh20gBcpPfjLTxrwSnKyGE8w5evFVMJqRj1qI8zbIhUoDH%2F0ohXfZeuJmqREMyxFYBbL6ij5O6m%2BvYZ1ISPtxLYjZ%2Bw&X-Amz-Signature=b913801087c66dfef06bf3d4bbbae3eb83eca994cb841cf2d931d8aa42ace1a0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
