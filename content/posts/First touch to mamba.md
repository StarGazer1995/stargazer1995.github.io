---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJZON7ZI%2F20260816%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260816T042504Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQCVpVI5LFea%2FM39QNw3CWZ3%2F3Ktet26fDd%2FrGtDDLK%2FYgIgNW6f38ySQz0gsF5T5LFTr%2FV1ohAtZkxsxK1IDCZ2EuMq%2FwMIIBAAGgw2Mzc0MjMxODM4MDUiDH2wSBJCIGYT5yQjFyrcAz9Zpp4oTegF6VKikE98acXXWu7Vc4wCZ7swBua85YZ5ytx0tL52ZXMF3zZqGw%2Fu4ZqBVuAM83hpYWzKX23L2jKdiMW7Li5V5n6YdDITDakr5Q2OjY9gMJKYbgVEiZ52QER93LRRwA46mAbuabQcbEOcrRRSJSqsGKi4zu5jIP7SNsLbZ7SMibAplHd8MJ40wPEUcn8LhXGJUwrOdjKgz%2B0k8xu5g7%2Frs%2FUNXBVb%2BcIYK3npk60hcNmwfR4Y%2FjXZnBdlmcAGgd3lph6WybPIg4JJlwGvK9Wzq0Llrd1FROODkqoLN%2F7VI2RBC48eQ%2FwUj4K1%2BxYL8G3H4jD5Es8XEO4eGQoRbmv93fY%2BGhDbupNBwFtAScMAWYooBEtuQL8kPtKqHK1uqYsWs3zzeFpuH9ZaRoas5Xy8Kg4bqdyt1Ve%2FMWKXg%2BE16OjOzYCiX8N8Yb%2BDwdQRIFdHdgrnbjuQKoR9%2BHCmNrCEwA7SHVT%2F37Tf0O9%2FfB4SrPzkSNrUgHf6YIQgw%2FxceZFSWF4qhvxnNUZLbxWe4EGUI0sjo%2FmQI1PilM45n37eorf5wDqddwunxWYH8WhEesmfncgAjAdLlP8OqgO94KNKtN8Nn5CdB9qd%2Bi8zydW8gUMTU2VgMNbrg9QGOqUBBeT4yNPfSlmBW69ax2EVS44m38fHgwPOneInmDT7eot5fjwrU30wrfdXfPidLYuGRibYUkwr8fNpKVNCunpbN7IQYUOR00fDGmzsOLJwevMc%2F%2BYeRaiZItd4Re4lJgSyqryQy5LlVtpkVC1nFPbnK3BFEXqAA0z%2BYSzVV76azU%2FAe%2F3bwhWrTNfbjpsTSpPb%2Bx9Zyt9JUM%2BcsJvyoKzBaRCvE9jL&X-Amz-Signature=a91b5e1fc39323ac70a65e9f53e7beaa0ab190a920b0a52e1cedf2e71e889f6a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
