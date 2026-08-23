---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TCA3RIDN%2F20260823%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260823T042641Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJHMEUCIQDTGx4xJ3DK4TMc2kC%2FtDIIK1%2FgDK5mQo45GeFsG3aLHQIgZ0zworUUbvOF9oeIJzetCku2HsTKqZy7k69Gq9U6xhwqiAQIy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDN1pkfT2WMSg%2Bx9ttyrcA7dAO14rvRM7YZqzKCMjVtmAGX7StwK%2B%2BtnN55emlj1%2BKC2qgKZJ3dLb8NFH0yjRJYd023HYq7dMtXylLewmapQpWii26aZEkTocFQ17AY%2BMt62L07KkAXFf%2FhuDriIfULEZq6qaVYXlIjNA1oiPMVHfLMlXjbOMoPUCqx7TYaybFdQPJCpi8LyJ9cPcJlyHf6wOy12M0KZBg1StfHFHCnkZTm%2BPfmUcwrj7o26nMJrCS5rUBrSPyBg2e5Esi8W6Sl8iCSmg5dlZP4BnlxQCrgiH%2BzvRfn6SE%2BXs6WLnEXAldBaBhX7OzqXcZMoaBk3u1%2F%2Fd%2Bm2VA%2FroCN9WS4CCbE5EJx0BVn7yGVG2T%2BqdKx1hux%2FGJdx7oH1d7Q837tN16gElLPtT4UvJJ%2B9UkVknL5X2f80nch3tsOAQaPXNyyfyW59VbancYMZFVUIziPTrHyK%2FcTsJ4Cn2tPtt986xTR2FU8eAp%2FrOQOr4QSbHFpkFY1X7yd5Sso%2Fy%2F9mOhOTed%2Bq3sLQSBNPV%2B%2BylLQNsfQ%2BI433sv5%2BjiNFC6iJWVfrpT5SqpP5yCjM06zleLRVEnIicR73unUKDTbYUb9aSfcbn9d4103Umi%2BSkIkTL3bQRqOKrLSweVqn6kaJFMIW1qdQGOqUB7ssyh3L0tTvEhWBYIM50fVqUTTcAYXXs33yc%2Fu%2FtHWPidTBl3zi%2ByBHZfGeSiE1M7O%2FfoubV9gdUXh2S7ND73bG%2FnlBBud59hvPb4wwYlhn45HOm%2B8zs0ijhmbTmLT1LtEmf571g%2B%2FfEF6%2Fq6fa7f1cp1KBS9ol3uFfxNwJSoR7aVQ8wikm6aOTYBPta5tD0PGvVeJ2kzCe5PIu0U0nNBTbaijA1&X-Amz-Signature=6a9e7e8a1393dce40de75ba19fedd4c2ba505cb0f73f9e5f3a4091d6601839cb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
