---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UKRU6ZJU%2F20260630%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260630T192950Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAAaCXVzLXdlc3QtMiJIMEYCIQC%2BX6eVkptRl2hEzvc5KuXJ9LRoMEjOpJ8mO2yTQcdQcQIhANr4BEMoSRV%2BWBivAobNhCg%2FxRekvefINSnQQVhtToyyKogECMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyOWwMCA%2Fd5WvSma3Aq3AOceAYYyYHWnTaqamW7z1CHxhbw3oRTWg%2FVQYouXxpuBa33UPDe0TofjyVoR2v%2Fva9OtXQpt3UvFQPRIUB5%2FxrsQHpbig0T5A5KQn3bbCatzUw8wii1Smv9s5CgwOXiuz%2FdtSsRT1czuQCadav4IClZUqn2SkkkEcpvjIzMMpyRdFHLMv9%2FnotSSsn7QI2mZU0QSFNYUiyhk6hA%2BHFTAp4o6ykFv5V7NejrMhvJ%2FMp1AiAyfDF%2FCBsJa6JSxvnkIqPXQktEX9mMf6U7MOX5e%2FKHrLW6Jnj%2F5vH7s%2B%2ByTENz%2F7hV%2Bs6de8DfG8qPKn7ZobkzIUDEMlPPuoDH0t4%2FaH4KOgftKP44JxAmlOsOvANgVc1DJ3GgpSP4zTFiq37FsbMTDYMyYO1mUdYHUQNyslYHTjJ7BwrTWMHgSZFWkt8oLDHML1z0h8OxB52BRA84xT0ryL6siRXEGXTj6B%2FSVrveyIrnCiHPJ96vXnmezPhqyY4uI6Q%2FROJx3BFRLz%2FZ5%2BECTmQZ5gc9WKbPXAHATVWm4pUvw%2BYoSaD9%2BhGQaYE5w5nQlzBILFhDvboN72LZH%2FtKGQAvOR5n%2BdSyyXNKDPlofobSoRgOUiziMCLRO6XXjn1JtUy8u09clpX2VjDb04%2FSBjqkAVavVS%2BpWNWFqGMUAFHVO8goi2sZXOZa%2FMIU70LFgVnaHTYCj51aFZcvjA1aO2W6NyCPPg4ikTgg9T5YqNp2JVgDsVLl3xH8gs0dbz92Y5lSynYpIYYR7RrTy%2Fip7LnqNn%2FKvXHsabjDuL0gHwzswgufPi5T72yqnN56spmGxC8wGmRj1wkT%2B4lGqC5QhMHsytpz8Ku9Z8Vae6z0ksbCH5JwXy%2Bc&X-Amz-Signature=b3b9743394a29f4293d8c98a0512aae77667aae6be5371f3fbf7395d0ae95dea&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
