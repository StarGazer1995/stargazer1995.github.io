---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YCFDOEZF%2F20260610%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260610T231911Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJGMEQCIHdFuE9K%2BIrR%2Fp0kFXeFocbVRO2V%2FeKPDdC3encj%2Bfo%2BAiBq4QpF49itHW0qJaQBjyAy0OKcYZmyQQVjQOT4DBabPSqIBAjv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM8PKhMKfQIE55irTSKtwD5EjtLVFU3VJ5DbFdLGeXXk68aGek5y4EXvNVQJmzbSKvvR66ibchAhHCPeE%2FlcHlHB30WUhvjfBXg2wjQ7cz7vnUnX%2F7lfYiy8cM9pPdDlZOADSvl07DF4yy0daYvEbQYMP9LD8IsSbo1TCHKqBTxCTIDU2mu%2FHhX5mQu9v9dd%2FFsehTK%2F9gVC7eJXHHT8LEimoj8GVcm7pbY6yZBGKL7xikzWVoIecmxA5iY6jhDMCTr6ILMfn2nPF3LZ9khLUBJntd0LfcY7HRwrqAG4Runu76qrER0I9GY8%2BT7HxmidZhYTdNoend0WxQykGZoIl0JzLoaE7NvTXS5nGUL1Pq%2FxONEjGKHMb2qi8l0nUI0cWgs2VDkPBiAly2P7%2BLTnOoX4jlu9%2Fuo1preQlnKemPImb%2FmW3wUpRiiW65HUrGNYHmeN9Q3kie%2FpfQxd6w40nL4CBorKQMLgT30UBJeNyotFrAgVJj984du8kB3BkF3JCfS%2FBoUugvxVCbZxAR05Bv%2Fbnkqm4Rq1vbVddRzd63OoOyR2BDe8gJ38EODDiqSFrYsh2fGfB1B1l8ReNtJBauRWhnXJvcJGGYd9QIRe8zbriWQciz2yWFt7Ll7%2FeVjAAGSrxTFNIS9dC0dQswhren0QY6pgGrtarpKKKO2fok16VnLpuItn7OxC0ua%2FRCdCEkK6jMgmmouaQ8xAfMx0qfF5aWbkcE5X8l%2FY%2FZ5pSITQy0QECPrg0Xx1WBbHQhNMLp%2BFTZuQjG6PQx3s1yX7sqdyCwNEpBGL5JJgeaVWWVwSMU%2Bzs9pyuR1s1SVSmcI3wtLZGIxHthI96k6bLBPTMiGBHSrzY%2Fs64H7X2w1ATnHNtchY%2FbZlqOnYsP&X-Amz-Signature=e5a90eec6315341e3e45b265644b1841363edb77d8906096c169b744a6a7a7b1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
