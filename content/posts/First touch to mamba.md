---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664M3ZJE4O%2F20260901%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260901T201513Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGA2os%2BTA%2BpYxC6VEFavcb1JAvFxX%2FwafgBGjG4%2B%2FfG9AiATEVQ0YnSxMOc4CRLFbm%2Bpc4R3vt0BSVKBoIl2hpSK0CqIBAi1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMnp4amurg8zUpwVuhKtwDGJppy255%2BuysHUr9EF2YNkWuq7zZkQVJQZvY%2Bwc0NT6TXT%2BRgUoXHbQXIWnXAPdsazEZl8Os%2Fu%2FMM%2FAst3rz79BQvt2DCr2RaC6q0JZk%2F6FgIAOaYuRyBqrxupIHTd%2FiZ7yFwSemIK70mPn%2F%2Bk7B490R8TBj3DSP%2FV0bDWTgAmfXKsETnos1U5wgIv7NeGhxtZuU5tte5mFcfJHee03QG6DJ0pyXtlf%2Bp1VD0vgHnPL3n3pCtADqRpoCXVFtyflq%2Fjg9Ng2w1pUwB8xKF6iwN9s8d%2FPsZq%2BBHkDX1HaAKY16ZydVM3AHz5Kob1GswNatPUafoGyBvoKfVSI01W4MXMe2mp%2BS6kwXV7CxG6KOMSxMNoh980ROK2Aw5lS3Cxduv7bMpUlrISKV4I9p55bmz7qf9bgIKd%2F43fWNaTqSZnR8kIWL18jfnhEVlCbOijswMiBOH9F8Vf8buiF0gBvnUvPVTXJ%2F0OfpHiJE7WCsWv2%2BHlj%2BW1hDiOAy%2BNh0mpsKxJRmup4CP%2B9EiQpia%2Fo1PaO3DryIZwPXtH2kwU1u7zQSDiCfSNYIfa4o2lcH7KC%2FzFtGeKMHrs9kPHKlrTJB1qEqMO1wG3GSwpUtiIh7Bfndz1BVUx1VSkfa%2F5Mw8Nnc1AY6pgFVI%2BDON%2BZYOHRdEuRH9%2FJVPMIbjgM1Uwud4Zre2VCyeRG%2B1zHU6RhAMeJAjDn2RH0ltLWtbSarm%2BbKc0oWQvSVTp%2Fo2kjOMI%2FP7Io41FO%2B7v%2FX9%2FTXifU4WBoZu%2F%2BwHEeeozZdzTgIAoWaYHncKY9%2FugTf8s75fcKm4gD8RHnF3udlqPZbtDJ87cR1U3WQ%2BRFHj3gSWjrbjwosv2Zh%2FAyay3G1WgLO&X-Amz-Signature=9f2fc3190ff56da4192abb878b79c70468f12ff5f4050c866640953fea65242e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
