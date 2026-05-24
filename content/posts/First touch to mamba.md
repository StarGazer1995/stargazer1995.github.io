---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XHJ5F7OK%2F20260524%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260524T060118Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIEv8%2BOMy77YY3YQSqWQp6QzJKwgcWm3ktDGuZUnZ3VyIAiEAoTA8BpIrit0rQGVmd%2B%2F715jYHefbRHTlb4vy%2Bx7mYkoq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDN9%2BsMHdzLi3ZJlPTCrcA8KRtzbvemPy1YoHcuYDqyyFw8gbLjEmFnhyrO0m2ep92XQj9L%2FilEXYGAJQ5DglMaYui4pxCByDcENqYLIWeouDLzCND9oftPEBAWfkCN7gdHC%2BdvPrfHeFs1Qxi%2FN10uTN%2FPEvQNpavRNPwtf%2BJh9G4cSOAlGbdHPBPBrGmDdVAqP9kasDKbLQVCsDAMnOBa3S9Km5%2BIJGDvO68JX7aPAvvCVV90Dk1Dir0z4ogQMP0YFXL3j3MCj%2F6TUOmeACnl9pQQPM9WgWWix20MFWIpeljUZpHKlQ6iAIhdP%2FReF0RBl%2FKABcUwuOC9AWGfi1LugEDW2i5gLkUvAaQivYSNEMNlZzx2F%2FWgxs4%2BiySxyZkEuaOw4GaD0ht54vNDsWCFlaUi8gknAQK0%2B2BlOUm6rwF3%2Fp5fAW0VrJhTGSbN%2Bh5a3EwTeFvpM6lOT%2BGufyvpKKaJ3p9FS8Ezih4iBguhg0GlH95yYHYjm5ict0ld9lSdrDxVcU4nqyEMXpZf%2Bc%2F%2FwpDXsvmLVI5kqlo9U1Q%2FQfBgtpOx700Ky2H7l70MrrPqICccAzvvTxNZLjhLXIoN6Dx450eNN1XZLRZifsPuRfjmxrSAwQdN6IVJWEC2nSS0KBMAFh1vSANen5MKzJydAGOqUBrglP3VySdMui7bm1FSivCFeApa%2F5rUwGC0G7D%2FrDpy6zJGcAK1sOZgeNEkCmAqxp1gF%2BIuR2QpZ1hgKQhDsdtDcdyibJpgDXhqlbdmgjUeNDZoB2Rv4g4doyU3HrY4d55Rpp4eLYdouqf%2FCJz40QIZkin3oueELIYO2rw2ScNVEM4hdsNBUZ3TeXV9MkRcjrEQP1wfT8mN%2FZwDio0mT4HkN26XLc&X-Amz-Signature=491f0a6b1bacf0bb8dbac8be5c1980ed39efe6c19cab1afa8c974ee3e9682ce8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
