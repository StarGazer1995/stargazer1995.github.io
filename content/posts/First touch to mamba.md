---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R64IXLQP%2F20260710%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260710T055213Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDGyqM3JnCzpIh6O27rLx6KUUQhrCWc0G%2FZqCbvkJtMLQIhANOUIJtEGJpSghyfIYRp%2FvEEHRslzhxdCLdQHKCyoKz3KogECK7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxnT3EuLtVVvZibO1Mq3APuzTaBx1g3zxWdRGISGzugDGmPOn2R92CkIWjg9NIVmG2OGNQkOpCGhe9IavN%2F%2FIOnvzkSuOiLMI5buInfj%2FoLqqR%2BcYhDl8TCmMyRKsoK6%2FWfu6HMM%2FPJD%2BXK8bP%2BrY6qJuCRcyUIV4wJkBdrsAvLSbn9k13r9l0ZsXEHsmarQy1LtPQp8PessUQ0%2BiRa9pl5dCflyMzFk%2ByatPzcCuvP65hwFWqtjvwJlvkbECbzXnRGLJlwu9Y%2FSMcrPJ3I9pGVPu2icR4ezemNJ7bSuMA9ObokUvOZl8RHKLFx4SGeesEwSOSDumKiwOEacOf4Gx8%2FcSPLM%2FiAdXp%2F4%2Ffi3nkUM9sz2Ecik5mDx18CzUGDKjqO2tw2cTo0WWXvM4ZUpZVvso0%2F1%2FtQl0jmgyXkAfqopPliIWIWJ7A%2FUIemjgh16za%2BkAGKpecbWZFs9E5eifHrmgxBVT7Wev6iAHj07nDa3h673Y39%2FEtGw1Vp5Ho%2BT6ocxNtyCIsrwiFE7Eqsgh3EoNnG6HwDj%2Felj41HEMPQxcTMeEyNMKwcpJ4uVfrugoir7jqgavVD%2F24J5uP%2B7fWNJm1t%2BvgDzK5cnJQDE2knrZu61WTQPYlUqVpBtUd7q%2B1OZk%2Fic3J4OuDqfDDO7MHSBjqkAUAAIAU3NfSKsaXoSRayYQT9Z8IsmRaOYIcHgu9qKRmyDkNI%2FEx9ZVGBGSWpz4nstK5f2pdWTYKGXukR%2FyiCJxRMi1r1LlTqyY1SNwchgFkCTRy4j6s0%2Bb2hXfGHdnq%2FjgrRy74L1NZFph824QY8z3kHvl5GiGfBnELvzAcg3SxMfmO5alrWgYMagy3mHIknF9lyxrahCKXNJwU0dc%2FgqbG1rjLA&X-Amz-Signature=d4edcb42bc902b0bd8a52f2e7960200de04b2ef63462db11731815c38b9196a9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
