---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667WPBUNMM%2F20260822%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260822T141043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEL43GiMgjvCymkV2fcvil%2BLYdb%2Bgx%2BYloZrijKpQz1OAiB6JemAQH9wtUR2TqF10hlTAdyds0RkTTbDEhmrFvUhriqIBAi%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMAoMY9oCkhRQz5bHoKtwDu03E5NSXemLoCyvl3wYuPWUX2skMkKfLkTzipMtyfl6kxpUY8ZM%2FXBpByKw5q6Jcyj6lGRSFKWTOiwtQYLc6HLEZo18UElbLPFP%2Ftf2KUcm9KuLTzsDUvFZ9%2F%2BYkHjPuGbczY6K4jeH59iQ5zq5QvDLJEOQB1T%2BbdkNenJanehTYtc8AvY%2FRx%2FSwP7k70gDbaq0lak1Tzv2pvRjMJzVroZmYT3mzOTF0HJ8uRrByLcfSM6ZyQx1psf0%2BQvxHZOskmamyAWCyyqkmwra%2F47iqBqwhZdzXVtlP49mwWNL7YZAPEl4QmiyxUMS6IEEN4sn%2Be1UJ%2BXYWRgwHwRA3LnQLluNzYQxZ18xi3hMGEmM0X2xB3TZMM99n9zatqWtoyN19M9aip7WKlxtSckBjYJh7xV6kVRRdDbtox0k%2BZwpnk9bIGCm4CEvIC9smRhUy2VTZi5AFBnk5wBPiqXxzoPgiPsBs8yntmVmd0m283ei3HjybL16cFxX1Fgt7vOAlztEMDu1sR4zLq10xjeDO%2FG133OdlZRaaPJTnWFvQMurr3N5DWKsCIg%2F%2Fmfqc9yNs4J5Z2VBAEEOTKx7gOfTdYbvg%2BBwHnOFTqOMZ1JG%2BFs9jjZllF%2B9KjboyNSt2ytMw2sOm1AY6pgGiTRMInHAcczEFYD919SmVOg%2BGE2g1SLLzT6p8FtDcz9D0ZY6OInfsfrCxXnO1CGvGjG%2FySEnqr%2FvD%2Fxzdy4Mjgqs61j6aJRLItOPpg5icaLPufMUGxByyQyiI2WgkeLWRrRnxospaU5QH74ShomWU8dLljV3e9pJXviNGDRGW0hId8acgF%2FphMXlUdVNj8H8WCZcjyhdiBaoxd4EzASCOYnji5Nfn&X-Amz-Signature=e846766450294349df57fe59ee2b9343ea7e5b78fc5ca3f7faea0b9b4c290148&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
