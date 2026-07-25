---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W6IEP4TN%2F20260725%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260725T092602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFEaCXVzLXdlc3QtMiJHMEUCIQCg7M%2Be0v2njZedC0Do5X9yoYPdOxHjW0LWn2HGG1daEAIgLWDSpY47hrRVgHxFpZ6JQ03B9L7d0KgRzLRL8m59jwwq%2FwMIGhAAGgw2Mzc0MjMxODM4MDUiDDKk%2FhcBhaYqhdioySrcAyjNA9Njotfrcm3wqilVS2FLhUqEFYZJDpdNdcPjc2tmDe5d7C8mgf8IN2iAZkPe46m3saS5CMQdr2b5etj6Fqg%2FaDYO3D8R8pTFkNk0yyTAqFyoO%2FgQ1HwRbhxSqEadVsPNt7hGC217y9rkyUIqZSGRNBvO1JZni9fGSk5narnrZgTZT6sfAdF4ZENbai9m1LaiuITNSrv5VN7lM6OuX%2FgLjcqWIJtzEc6MfmG5PE18s%2FQEMsRnvIF%2F7gtfESITmLClV%2BcCgAyJ%2FAefw%2FdczZspCwNjpeVNaEuS2WsyzTsE3aWqwT4bNmiKAeP2COgqW0F4YVeoFWRi2PZIUtRce7DeLQIWJp9T%2BtNorkBLU3i7Fk%2F4nu05%2FwZxqwiGKqjucCn1y6gPNz7%2B3FAF5ss6IJVQ6%2FvCeeEN0X0sE2Ps9yzmsF%2FFGj89epPAekcmF7OL8iuvIFEFNB20xonik0slks10e8yHB2EQARJGRxIs6Dl9JoXMSV76m5wz71szDdvLXReQyG5Q4ZTDkszaKPreVGE7GdJ7MixP32kl2GxpiDOJyboRYAEmXxhvt7ieLgK5mKZX0u%2Bnw3ihvdri%2BsGK71U9uQKb28eVDu6mFAkBLM9dTfOgycjg0kSPDnniMJnlkdMGOqUB0PYC%2FJ6ORIWz0xWAaNsSKiMEZ8T%2Bc75hszwP6qzA1M2T%2BU4EAiD8MUwgg6MllbGF0GIscO5LCogJ%2BZnesb3y6MRBzVxNar8afz2tVSpnEdpmDXiTtIduhgT%2FgXtcJ86WUaqfXx5B4Jl%2B9iL4BCnO8y%2BYiFsIJwy%2FUnyKvZAyTj3Z%2BxBpVoueHlleJf5QRn3i8AZY1RM9p1zrhvakB3JOcVxb%2BnQ4&X-Amz-Signature=d1bd12e9dbdafbb65c4765ab8eb8e4c6a5b6f20e115caea34f25bd86f8d2d05f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
