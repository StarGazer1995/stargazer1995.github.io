---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663OSJQWJE%2F20260630%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260630T074137Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCTzzesO97pVmuA7Zc1CXoEURK954hpgGrH8OuX3kIGpgIhALffuSHP1MHkYlA2tGPesAFZxZ%2FZhvE8ftpHu0Md9O28KogECMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgztfGF3u9WslIOZR54q3AN7EGKqTE7kjySyXeghHxMpznpLdg4aJeuJQ66%2BJlAdaSkJ%2BvxNGmORglMnfIFKjFEXCn%2FQI06Gmu7pJ1seAE77ykCZ6JYS%2FDvwwY%2B%2B78fVUnN1CTbIwQYwo8siLpKi%2FxwsVeHQJtAu0KRbCnd0TDv2jONbTSKgMTVa%2FPJcTQyGuO7udF0ecWdAgEJykNerWBs%2Fc%2FGiMkcOLPCL%2B2fgmPBVTEeDToK7gA1WT09dYFPeCbA%2BQKNAWHV6icIoQ5lEWZie%2F0opM0fwWOX05Ggcdfx5nCyBbvro%2B40LYOFng64hOGqglg5lgvLiLlfE3pO2ElTp2tUNuFkul9xS5pOtN5cZ34m5FJaLqDSyR4emJxQUdP%2BrbuV%2F63qj%2BESr3Xcu74gqXiWf1dxmPKknZJKaxA3i3FEIZIl%2BK5pddhgqz5RzukIrDUmE1zTlZRJbgPRYflqayfG4VU4Q40otVJtMrcI3dtCK8c0ScJoZnHeexU4usw6VTKV%2F3a3NDFoczb3%2FXt0XbuBgACNJWixuX%2FKeChvjxU%2Fw81Q5e%2FQoOoCaKLl8off1o7x092lYpHQ7rJD%2BIPmzgB4FtOPTkDCnfDXWxqveMktMMojoOGMyTS7xKFIK8ZFeDnRsOB2CmwJR3jDMyI3SBjqkAeCpXGFzfnfTAOKOPTdbSq38CwO0%2B3%2B0qEC9%2F5iQvMgWCzf07RcAiSRY0WFN%2BPVQ2%2BTJ6w4xUnm2IXQPjoQa40BcA%2BKKA2tql4YQnSSNP3hTDR%2FHl7MbkNynZkMGshUKTxCH3WNUuyhM3nU7ISF7yWnQ4KZQEnW3CZpQK9MfWeqw7yxt3r%2F264oKuZZb7xS791ElqPKWlVzxHnOdTRz2912hDBoU&X-Amz-Signature=fed28b43c6d8c2cc72a7f911fba4bddc0aaf846e6fea14a94f77056b34fcb751&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
