---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S6BZ7LA5%2F20260803%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260803T093016Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECgaCXVzLXdlc3QtMiJHMEUCIQCtF15PXQB6sDElk9GBAc6c6ZRnP129xfZ1fInLVlMnWQIgFI9NF5c5zkabdBjjSmZr9Jj1hCQrFJo%2Fi%2BBmXGulyvkqiAQI8f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEa2w1WVUV4PGhWbLSrcA19BuenmTiGVIl8msrm%2F4s%2BjqCIG1sS%2BFj%2FBJhIjpMfqsua5k4Fz%2BL0Uh4lnIt38bUu7JGCoI90B6XquvfkV%2FThhrc5REdIQ4j70QIzvGszJpZeSz%2FZ%2F%2FZHDya1aIWvQgh8%2FuLanEVmBXxniyJpTvCSaF0uDyc00N5thzyUkuoc%2BHAsyChD%2F6gVzzDT%2B1KRsYPNPVEpSIvvDTgxQSUideJ3p6EvowdgshLy8HPBSjfMxTn33cZ3hnV7gaM7BhagY3nQH2hJqfwgKepfgnUSokVt7BbvsesxS7lBqzCkzM001ihaAy7zksriHZ2EYXFTOQvCZueNH98aKB0h3j5qPEqH2okBd%2FCM7XOY%2F%2BwtLW4sd1JQ3B3WSaQMuuCNmZqtBzeKQkOPpyROCYRjmzipHizoWvKacoGuzhel8zwCmQS2LlUEIoO4DHmg1JSrtBmeT5%2FTF7AaNWf5sg48WnB4%2F3a4mHi6Lh%2BoYWDZWcKLdhlf8LlhhJ7wSsIWaUIAF3EohPdxBhzWgg7mkVTrgl2NcKQzaI08fm8lkV0BWzijtnAf23vHsyJk5nLD3gXhOQIf8yEJ1YoJvx0dSYofl22MNYb31FvPbJ3mNAvMFw%2BDCGqR9Fe9sX42YsTxXRvcUMOeIwdMGOqUBzEkz1FWPK9IZBZS7pP4nqK4TnWL%2BbFxUjXZmQzVqlU%2BXQKlQLTm41HplMEKE4Hi1QQ0kiiVFSlOSzfxZUJCymywFgvRE5x5tlmDB1mZHCK6FlplvbAUAqlpGw61VW%2BqnFqpUM0d0mPDb4vAvElbp5AYHykNo9RBhNFUkwjZyQyzuhMEchUU%2BRYiF2dQYiDyMzccbDW1RX3%2FfWHZPrTPx33VFnGd5&X-Amz-Signature=96b1e5d7f19edbebf680a8a0469d9f9f657e522b8009452e6bf426bc3cc5855d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
