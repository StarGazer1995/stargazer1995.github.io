---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46674N35MGB%2F20260831%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260831T015854Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD6uHkzEEW2e6i1FTyHNmshcYeWD6VhYonx8a3bsuMIGgIgP%2FI0%2F8JEoLVOgXH6aWjtjtckBWxRBF7owaFJBpxdmMAqiAQIiv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFJ9hXcpSYLO8dFEmyrcA66fBDUA1IRALdtEbu0KNdOb%2FDoAqIQy5Fh0e5a780asOsQiUvJHQwU6kKg%2BhL8UvF6ulSvoAeAFj1eNdK0teGkhgFSRuQhae%2BSNMRdvz833zX5O%2FvwhDOFQ%2FJ%2FCRSlCYk%2B5IjZ4ldYolC2Yzj22Vyq73ez2uvmjgH08MvrVtRDhAtvZ6C1cE6Q0FSUjtUI53Hc9KiR9bitnhwxGFMg23fKOfJkpSbF2X2jUyfolatq0wYZtXn4soMLDBUFmz%2FIpGQg4x9Mee5nYjAiaWi8dWy46frdtJyqszecYWRZhbsCT0FmzMCAu%2Bru3H1s9hReGdVFMs6KVcDy3H29W339KyARZJJm48BPpxPMfpnEnD4B0PWyrTSWUpehapgIYH%2BGye1sBYyeI%2FNeoc30mwCHtfIOW9mOsGKe2r25IV0%2FgkK9vJ8SihbR7SIhB6q0a%2F9bgKjQAFMGXGjrdXCaKZMv1p50eqUWp1vUs8qa42R%2Fma3IPWhHxq8y5qh3iCvs2VcTBRZQmqDmawecIdgPqSHIge4hmzxdYQ5VN0AiQQvTC63Wq3KhibyulEQrX4ajfiRuEqr7HlqcUmHUyXKYKMIMNBhh%2B2ttAgFrEh1%2F3q69Lb%2B55AGtoRcnmSC%2BYCL8TMLSp09QGOqUBaGqBMlvEMc86Plr7IizxLdSo6Q3OhmcsjvqQlbeq8wMRP%2BNzik3joTAlyuEVJTWl9RkZLYoneJrkeYfOnz%2B3jDrmptRMVqGtSIqZBEZamuSgsrM7Q1qX%2FPKV%2Bnw%2FtmZcN97uGV8MLHkGrCpwJfP41sFR91xNWsNq4hrfxvfIQzIKFtRBEqvgroRxgX%2BNz8OPTQiNFoZTWGkz%2F5PuBbbeBQuKIAEv&X-Amz-Signature=1c299ecee3410bd5e1865870302b7c24075a97c3dd878d7120f268bf28ef8f2d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
