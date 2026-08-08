---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466775H4D2C%2F20260808%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260808T102030Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDqEpgVkR43XDvKBAUmKCOzaczWlUMNQd3SoL9M2GICVAiEA3r5f%2FHnKBW83OKvcvz%2BWt3xpaWHfH%2Fw4RdMYAXxb9Mcq%2FwMIahAAGgw2Mzc0MjMxODM4MDUiDOk3LQ1uqNrZhc5waCrcA6yCMpATqSvlQeeYJVTE183m9dvvOvsIBBhBsPFNyqECbzyNHIv1irmVOKdHjdYtb9566SpAgpLWVcjjI12AM17Gb0nZ%2BfsymMOPzlgycdWOzVBFX2MBE1svW5YxrJf2EUuL%2FL5vIk9%2BZbNGXM90Fku1yVvPbAsXhdSffiStICk%2BrCeksFuqnj4RrUQ8x4cqLaYYbB5qzoWXwxiSQ61reXgqvA%2BHO9XEijQ4ImpnmdUzkKyB7XIzqus9fSVOeAX5sju9dEelgMfnAnLNtBpurgzWmCMQDTWGWMoR%2FY2BRwUYbgKNaxeRZLvQ%2FBSxRcn9lLtFsUt%2BvBHJNMh%2FuLRP3vo4LzWDrGcjGlpLOp8OgWZBMRJmyQfNyzo3Jg85MvvvmsTCk%2BgjtYVWz1Xo1TI1%2BkdoWCRrlej7DET2Gm1nV8idJkW9lXFUOj00SvgRR0%2BEJYwsx4bD1rge2vWgW4m2sJwNAOLcaZtYeW8bwqMLPhfN9Sq5gQdBU3Ylk%2F1sIITGl%2FIccYOiorsr8%2FkQhxQKkXFBawL%2BmOAafPDFhm%2Fz4hrINH%2FMOwaom1Mca0srijPmJWAWGCB78ak1wqcfr%2B9Z8b3XxChaWQakoNItSkFwklIsz48pRcTWeGrz08wFMJ7U29MGOqUBCNHUxqw5MRnuezi3pVzv0pwYAfe3oTl76jOf1rXZmglf8E4yUsZisY4HlBcTIgpGy02JoaDSTFmzi5XliMitpP225SCLmzDN398aXuWPqui0bQjSd6ndTSPLW6X84xGU3FKywh6aGk1LaMp0k1jvFMPz6rxbUyQzmebd4GlBfACOEMFKeJkbMhxG3%2FZiBCug8w%2F7UpbxfRGqxmO%2BFQ9YzB%2Bg%2Bbw9&X-Amz-Signature=fcfb8eb60e88b0fb55321914155a8fcb280b59107c64428c203f4bc428f29d76&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
