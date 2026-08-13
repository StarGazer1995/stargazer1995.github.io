---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SI67HQA5%2F20260813%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260813T090117Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJHMEUCIHucoqT%2FRReLo%2BNMLlj8qDD3HOktN8Mt7eenjYQa8RSgAiEA%2FZ2lItrMB0ZupmMLfnRgz5SEynAiNO7lcrUrnmCP06kqiAQI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDM6AUy8lJZMLUIJAhircA4U4GI1yQdoExBLzMGZJInH%2BUwZpLz9mZrwlyEce7tOLB%2ByFWp6EXaU1dtlroK7doqYM%2FRSe1%2BlSUKxl9zJLmlZt7goVzokYFYSfYaephIfxQHfSm6JRYR0ZvxMIAeweDPL%2BZhA4HEAwFznCkIk8mz9Vf1Hnak%2FnyB1Hrr9e86tLqPQNo5jsR9r96wa1r%2BY%2BZ7K3hs41YQTUPdhWP%2BvNCwM99Umo7GSWa0cs%2BYRDFa4J7dti5CCo2N9FmNFXd1W3RhBFrXCRx8lWlkJcHMTwQC3KuzjVR2A4s1kcRNaTIss%2F3sK3lP8XGsQN4di2Cfz%2FYNk0Nich%2BUCfbL7XWgjuKREyp7t8ATX8xNv3t6f6DZwo%2BvSYet86Vc%2Bk8zhka79iR4MlU9T%2F8oCBBP7m2xSoKCbR%2FHUv%2BuNmY8StkzMwK8c0WsvZLUrfmY7FU6GsEo44MNP9luzbFTf4nGfYkHj21sKc4sq2omF1A4LPcCLrZDyGDYDPLtcZmMKPybr0gFtNGs%2BJe2EbaOrXeHfTn3aDssLZvsZtmXc6a25c5M7CJU5QgGpZUDyWOeBvpQzBD84flwGzu6eMZRBWP%2FgJ36F6jr3dn8JeCPTrcbr2ltjssBM7bkizi4qKK8vrj15IMJe%2B9dMGOqUBuouzPV20hUc7FVN3l%2FQrbkFw4j%2BEk6%2FNylDOWkaHCTaIlo9lRszHiz0KXpKRuQ46e8HTKYVfhbVTO4ClEN5PB0OWiyQjb3akvZoUvPhUOXgq%2FIvJLFnVGhYNaYiU3nYn9srsKgfr1mvJJeIiZYz981AoIKjMFkZWGRSU0NPw474FlL7b1jkQUq36Pg9Mdg99dAcU9gZFNTbF0DPvveRVn1sDq%2BO%2F&X-Amz-Signature=d8d3840433ee847dbe3b97e37d988ac5d8a4f3913bd9892b4f705c269cbcea69&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
