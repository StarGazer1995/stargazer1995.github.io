---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WPPLSPFN%2F20260715%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260715T152036Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJGMEQCIDpdG8s5pIt14dTIkeR1%2FAUWYAlVpYpWZ7iAai0OtLwXAiA%2BCvHFvuFBfrk1v5YBPAgxs4OdXhnuu31mFAnFt9B0Jir%2FAwgvEAAaDDYzNzQyMzE4MzgwNSIMl3mIrHoojpBDt5bYKtwD7Q%2FCfpu7igRJn%2BBl2SRd5ZBOAEcP9OcKizJY9kZ5uS093CrIKxiDRXc1yzvsqk%2FDzR8UzI9XSSaJC6aLRlgVe3P7e8h1VVidoRCrkLsdSvQlnchyyV%2FgL1tJkg0UVE97HStpzq55MtQQ345O2biQtCevJaODadh1%2BmhIEaxW4PybVqInLCcqtA%2F0fmmCwZy%2Fj7RlGLq9pBlrmQuEgYhPcEH99x0WI%2BrWByE3%2BMtsdz6QfudjpKdtumQ%2FxD4cnOW9epeDviqlRfiAJDRbUCzINLQEcvlo9auRJSnLGKHXBwNRF7sD8K3bjJtxdAsx2fPMita5HvQfVyeWklT%2FYTxdVtjpWibOAWkbupgCrTQ%2F%2FI5M6WZyKLy0EFrmDLQcHJ%2FA9d2P5E8wbF2YELsIG%2F%2FAYtx7GRqaWc4eUnMl%2BQeFIG%2FEtMsXIBzh1EMvavG5fvweYGDn2W22HblVH8gKYTWYryKf%2FCTjFAjVNS8Zl7f4fOJXykVaJ%2B8donQUEapvPde18%2BXmZjKWwFoM6vZ2jVY7Eq6PRHA3uFbmldShFWG2fmrSdE75ND6QuBPAal1bGW615241PZqMRtob9POwHSXhviPWguntVa2ubtS3Kaj1EBaOb02qXDtr670ZVqYwnqze0gY6pgGXbgG0umxzoZjbzbch4TlLid8caKPu1Ei5Ny30UXIrx8eWGRl3FsBWXqdd%2B4Wg9ERV7Cjs7fQzIH%2BSWgvAqIfdFIMEQTNumgY8ZgQujOlyb4ikHpXhfktnP4%2FryyTLCkrOWCETiM8Jznam%2B3ToE7tGxFCR7uKZwDoc0fLnoQq8dq3FatFWV0LAVsR2Ch%2FrkaPOpxkL%2BXVAoqsH8skEn1SovPpBRYLQ&X-Amz-Signature=cf2cd4643e62d775a45f842c063f26461fd911c134de4164b709e222ee170586&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
