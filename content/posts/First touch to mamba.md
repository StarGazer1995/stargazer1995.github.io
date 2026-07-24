---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664OXYJRV2%2F20260724%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260724T205502Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJIMEYCIQDnMoUgmtHciOuRzxb9R%2Fsj0l%2BMl5rSLmjVWM0YBYvGtwIhAIFVD0FMtiT4oDYRZxSuHEPwacxVYTTBtaLM1zygelT9Kv8DCA0QABoMNjM3NDIzMTgzODA1IgyGkDRc4gPRp4QfqBEq3ANRrNP5zMOOEA2Bha9KketzywREsnPNjK8JETlSjYVRA9AiHU0j%2B4sQeyew20eUJ5CD8Ohlpexz2lEXME1YKZ6HZS%2FmLM0kv7l%2B7MF0E4AcrclVpw6ndul8fAJ26tgu2sxndlovxKDoVBdelUDyrbLKa40BfmgDZd9EDTr4zohC9YwSyA2n4uP4p4LOBIT8qv%2Btf2CxAGkcDxcB%2F8VBdNrsmWGDDVQEDsCA7rAMDDtD8o1rpkNjt%2BBjBXVeyOsOKM%2BTVIu0M%2B41FYX8O8AqQw4FOnmrA%2BL7%2FKNuoTjt9uWT92TDGkcHm2lgRiweO%2FnzE1pWbUt90xzHVKdrYEIUCa75AFCOMuAjE6SN1e%2B7IFEMPjTzFV6Q08srW%2FrIwD29gWxdCWjncEEawx%2Bq9mvBlm5kI%2BTs0REGDZlDMnhiOkmovYVbt1v18JcHRZXBktsTGCyJPanIPjyBeTEt5jhMGsLtP1VQqr3qw9sbaP2lrDlHwgUc5ZZrYHYB6li2lL2aScVGPO67H7KCe4eU6GlyuT5CRomv6ESWiziaKp1nWLsqkewP2%2B%2FzsbFkukQo5O5easCCNZCVhl3Z3j0W6Fi%2FKI%2FGz6NS3%2F3OqfQEmqnA9EKsPQYawcCgfxOqKHPw%2BzDVj4%2FTBjqkASQZCnmNQRAXwuPdQM6Hkmxzk1piYY5B6txANSIuo6%2BK6P5I43AxD0HTejArN59Rs7HYnG3Q8azQc%2BikwhVSbzQ9rnNNFt1vLaLxjM5ApYF7MeNwvJYIKyXdD6l9W8c3EsM5Il3kchTxY9U3%2FgldDycehvH5tW537zI9kqHeE0gwkfoA3vCsuHVBdZqapnmegGzY5XjqSrvUnCUdECegHcB9WXrr&X-Amz-Signature=b4d091cfd9ca5bab45a5e8b1dc92072b2b0b86c1f40788ed9d5a28c4b23236d3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
