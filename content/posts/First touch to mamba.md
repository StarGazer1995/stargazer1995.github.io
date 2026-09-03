---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UG3QA2ST%2F20260903%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260903T121932Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJIMEYCIQDtf34ZPKPo3WF%2BnRHZRANnwQPdJpzBvjiwzVTnFpoqtwIhAIMQ80AbctPKw1sZORIyZdG4MYt4GYwSJ%2FfJ8M7SC%2FjDKogECNz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyT4NzoD2onxfPNDzIq3ANm8RlBTEG9r90%2FxAYbAmH2l8PMP%2BHZp0oVmz3sMw7HKaOsuMo5ecaDg0TXUTkzB%2FvA5WaIc35ZXLGJLGD1HjyZg7yhko99WFLB0JHWuipLdRH2H1w%2BxwxAopPzHGgoM2V4%2BgEcpoqGR1i%2FyZB7HPOQqZzVxfmQM3YzUJDiphMX7J0MULaFY%2FeqX7wqhLr1w%2Fzh7Ldv3T3ru%2BUiHeQIbxOAJawFiOplGdnEl5iN%2FzLOQg6HD5g342hXuqkpCMAtplwVszhPZkGLilyNlTwe6ZoIu3iu7vGTF7CETTOmNfxt3AdFh6bu5ezqiZ2RucL3GfuAoqEj63Uz%2BrBkvW4GpZHsy0Uvt4T0%2FlI%2FGY0ZK06w66zqGt1sJ67sLL4dRsqrLPPl5fTu4oK56fDzyhGlbvy7GZ%2Buvg1Fogv6pYLTuUf6Z8SUqNN0JVtKcv8RgwX%2FEQjQTpgq8ZUzyE5aFA87K%2Fh4pLgMwcR0ajIc%2B%2FqOQOGSuPWVepmQw%2BDkp7kmMV0fWOzze3viPPr9TTXmqv%2Fl8El0D2MHxDNNJNr7NtLU843KrMCOapuARse1Cq%2BAkfHnlPGbDJJJqAdxS1SRBxecATTujny7XZx3xTfO6ZugGWtbhYnXGVv94dDndHj1fzDKquXUBjqkAVY0R66otOT4%2BWnTQQOt%2FUsKv%2BkgxnBMafgqceEQIQ7%2FGRPcozY1FynivgXAq64RxhySuTz909EINZi1bZUv0iNPneIke%2BjgTxAtTPZ75dm1jAavLZbEpKDSUnpK%2FDw7Anc7ZiNL%2Bz80sABAJw5ltwbaRk66bXidESZK4M9kowUbDYty5U5txMrTJAU5YjsJxOKLZkkxWxOVp0S4nlUzfuhlSGes&X-Amz-Signature=a8dbcde3b9b39fea586b25e3fbb06943561f300e72b6969ec353de6337db6c15&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
