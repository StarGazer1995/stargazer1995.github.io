---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VW76JLJI%2F20260904%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260904T220530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDUaCXVzLXdlc3QtMiJIMEYCIQClmaYuR7FnlpU42KxKbjH9JJ4DhCFNXiV6ggH5iU91jwIhANFremQvZLX2DMk6ogKx43y2FmhCv33dQ4iM%2B86AF4mSKogECP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyLrwIHRlJ3LoH1O0kq3AP0x57eIwj3JJ3wPaUuV5VIVig7XdMZqz3%2BogdGDpMugrdngbX8QnN9q9cVhDWWEJFNV1bMi7uA45eDLc4dO0gx8SD6g7UIVqS8KlokAqItq7k1nCMnr3DljRDOiEtkcfhZJjpV4lOMaIe4HTcg0vIDzqNxfCBQNn%2FTz%2FLOTaDmZLMhfedDFXmEsBdU8B7VOXqDU2A8yh8klgFHwJVhPsUsVdKXZynnBzaBcuHdJHCZh3hZqTHnboMsbRlIA9JVfaa3mgOxY0reTJ6q7BWr4li0biXFhs2Wxk6MptVPblP3TIs1%2FxxbBRzqvkWT4vH9uexsv%2F1%2FMO6TXwpsemeXZBqO8tlYkuTznw3WZyYRrUu7DwFWutgbgp8c4IbKsutDSkvr60M4zFRHDPrkOxbLfmd5qFezGIIil0AZWH%2FMtbwvqxpC97Vq%2BynjRR%2FjdwED8CLTEMp1h4OvRrsIxJYPfwfoSVOYabehq4a9fQBixoBLpQoTPQoMHyOCU%2FCaXpesZpDKpFi%2FDAkOXomt4vAg0uGUGR7xbyvUqJbfOQNhsOqoGOi%2BO6OtHAO1o3cyzf1np9wx%2FFUJT7qcmvgzmH8gczBBI6gKAE%2F%2FeWXspaEXrDmpKYrTeIzt4IxY%2BK%2FayDDb0OzUBjqkAa0DKlkXv5Dgcg%2FGCMwgPlSFl7wvO4Vv%2B%2BrYJsEfTyCFkoD21QOpYSUE2QAP0SrcCLffdk1q8wBb8mLCGTO8%2FcSogEj6fav%2FVmh8dO%2BpUjunIjO2U%2BRL68uVomrkpyuhYl%2FLUrOGBTBZ9%2F0yjsqf9MW9V0DZufKVuip2mzbkOygctEnuEKY%2FVIPIbedFeiR4ffQVCdNDtiT%2F1CjyUz%2FCVmruQR%2Bx&X-Amz-Signature=07ca201dcc2be3ccbdf6fd5563c315d444a4a255240dfdc21c8ec0c6efff2d71&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
