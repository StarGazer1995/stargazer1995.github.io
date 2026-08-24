---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T3CKINE3%2F20260824%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260824T201748Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECwaCXVzLXdlc3QtMiJHMEUCIEtTLWfVb8wgb79gnX3ROMxNrZ3q08mUJKl74%2B1cram8AiEA5IH3IuA6X8enI7DfSvdbYCPYze5avrWFkpMmJ6Dyw2AqiAQI9f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG6FJwUxCM4jEVgvkircA%2BMVYeRasbpGwDfucLwWiMvKDs%2FSMciNGROrZD1XlXVJvCvvhR0RlMRZfDODeqhQB7DMM71E%2FChL159LgVZlq1bh5YHe1KEarO2ARiU1JTjiKUc48WnTsTL81Ng1JL2U3Yy9V935uxVPBWXRwSSstTTSnKB1uCT0fZfqTbOFrOF%2BvVryjMIG6tRtuxTNsRIuhpu%2F832OJBY2lh%2FYOr0O9TAjdy4f5kqt1Nk%2BBQ1EzxS8CkMU1CQZEYe3IIxigNEtH86T8j%2BGKVrD997S9%2BOdHQVMv8gk3Pu9W5wGRddIQpnYXizXW7TymZeH5RxkvpM7uwyk0UZ1V0IWe22P2rbNXq%2B4%2FtbwkLYyaoE%2BoecwJP73A2Jh3hU2H2ib%2BF4wNZmytG49o6TGX63OgjEjr%2F3rJKqILSEookLF8UeoodapoTDhOGpoKlL%2Frm%2FNUQoybcnZocMTHnEYF09BhhRHZYPZ45EK8bBmgCQ5T0K%2FcbKg02qhbD6CQedH%2FTaEKyIeLBfk6hsJacbydGkldwNzj8Ndpm0PJQ1weas5%2BQ6RLnLU1XxSOgxKyQz0UI%2BI8As2nx8S7tPQHjhrPXCtXHG7%2BrRN1sbHLusbu7oLcsCBdttJoWmarsLzRO%2F8avA54x03MPfEstQGOqUBVD395bVYrY5rcv5AQtQJE4nNq5A8fHngcXz3KbfFay4ladvWFbpurolUPKTZ6XiPMvuzNBAlCOfOSUhjZPsL8ruJN6NkVonzVSRTb7A9wxAr6AARFvIAn3NK8KGB6XMcElc6%2FoqeNScvJbSVHSQ7WovJLF9ITDB19RbXK%2BPj3kXf8dv1bVazTQGOK6gLtdFVsL65XDZ9YrOBBEDJTUUGh2BU1HWy&X-Amz-Signature=1d5458a6ab9152214badb6c6bf047d5a751a5c79a0aad5598e837cd3d42ca0f6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
