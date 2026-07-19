---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q27PNXHC%2F20260719%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260719T094305Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCwll3QRDGYGTnoBOqpu4f%2BJMPXapJBB1hcBSlgQjvjoQIgU7ToM%2FMZvgK5l9CNPSI9djTmLPRtgvhpkgLe5KZUjrAqiAQIiv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEZbg%2FqY9e8c812WyCrcA2gSLkipXjxYfmJGl%2FbmInQ%2BJgJ2nKOK%2FP1RW7VgvNyzuZmRwVHBo%2FLIV3fbqlg3Jp9M9gcdGDa0UKilXoe03EyEDNK%2FsLx%2FYUuicR1F649EKffc%2BVSGTwrdDRxQzOB0myTegwlfDTKckqOtGuiLtWjk%2F3aNVZGQ7vKzuxG6rpWcrZj2ORFANd2%2FFf%2FhJaHPwPXhZuddxxznnb6vfChVLp4it20hbz%2FEZiee6NZGTC8HBQC0nBO6yk9EqcrahQYLf8AzSDkdx4po4ieE2sp5khNpd3naF8L23pKAYAZlO1U%2FX2sB9Q0nhvbVmgr2jEnh9V8egsrxkRd3FZzPm9LXVC4QNDQshzidi8eAYcsCUnkkTJQ6xTiVeeNDevhgyRsOc8xzizbg2ZZMVu3vXYChbG8F%2BRfBtIDvxWsC7ZMyoEUD4VeRPOUCR5O2r9eaaott9Bfy%2FaYnfGfTOmQkRg4Fpzx7NmK1FVhukwJ%2BM3QrQz6R0aI0l0jpfXA2RW9ukUv%2FPnlAUXN3zAb607Y07vRNz%2Fz9RMP44DYfAGqTfv6Zuj7llsGyb2uWZ9MwsP%2BZxZUpOfyknmu3LMj%2B9s95JohglkoAOUHhQLQl3Gll8SP4%2FV4UaOr4oBSlF%2FAoGcqYMICp8tIGOqUBHP%2FI%2F7HOd6yEuh1HrGtJ8G57M0quKC0SX4p2VHUZ7nbaxp3zvnYKcLiwjBtjv96oI6astH14mihiWca3Y5jXaFhMi16WfHSclCNtJcXSO38B1y1n3R%2BV82XDy6ulHgGT4GPSNhDrNyvzWRMEHxI%2Fqr9S%2B0bkHF7dW3iKLdu9Rge6frJ46xE5q4Wdrdh%2Fx7G%2BvFVnnun2e1Xpit41VmiRodx23V2T&X-Amz-Signature=6b6b63764b7105e8a61bf843a6efbe6a56917f27709e976c66ded77036f66fb5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
