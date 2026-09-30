---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UMDS7QWK%2F20260930%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260930T073802Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCiDUKnhyGqWKvnFp10zkmlT6J9bA6fHYOh0W%2BSaQaw9wIgb6fSL%2Bv%2B7E%2B2QKwpb%2F%2FNMLLPUYOziITrpTVHdzT3Socq%2FwMIXhAAGgw2Mzc0MjMxODM4MDUiDFf8tvTtOps4D5y10SrcAyDR0mRG9fZQPLFvAGlWjwX%2BZ8AQrwsSAVTuR81x6Vsc4qb7BbdI0dx0eoGNwKkXsMpV95nQafBuDCcrsWrVtfBOcQMGH3perT1OpvhNbap5cv0k%2BKHZnIRRJXueG4vjWB2y2jIpcCJWjUf%2FmLJvWBkgf3NTs0%2FN5o%2Bl0BoGdGdjjinbQk%2Fm8QqeCITShK5Z1Vv6z2Lg7VVwaw5hlu5YTITRHnjnEoVLkFyMWGNMY7818C%2F5d%2BF9OPZNnw9nLngXV%2B0wQgSfcRvXcHRutesNSnw8HqdS6PUXbwfWJwZVk%2FCMUZW1H6l3gGO%2BytC6NzYG1Z%2FnSWfrZNGJDGx0bdKCQQH8illhXL1BJ5XX%2B3vZEisfxUVlfN%2Frr3rRDCxMkPoXzbeF5dAMK4dzGbaG509kq6J0OsHKZ3OB2zptA1vheohkWtR0Df1OZrt7Q0eUp%2Bcetgt91SNefQd5iNNnMYAqli2OOD%2Bm2PytclLLxlWwYL%2BQSKUxeCBtFtOB25ZZK8KBiRlhynxhMWa0JY35o7%2Bnlf5VofEZ81J8A8bQGMTFW0cMmdyJ7oLiwteDY4MW1J%2BXvrnbBuRyUiRpGdl7%2FfjfZRqDGIYzg%2BtH3RDuvLHhcUoi6kVU0tH%2BXC5GVMcpMO268tUGOqUBaaV8O4hYemjNGvhbkt4VWLew6QNTUhm7i3Yy%2BqDIjRvlYmBjeUWlBKc1vHF0b%2B%2BikG3fNsztCrx0fOaBgG1N0yWOKFZjzHevdJrFSNA1dL4Xo8L8vPpaPFWjqAXb%2FWrxfnEjTLXcenBjxMySRJ0hUWhQo%2BE9nUGHeKRF7gPEuUsgipQROKUrfNzZPvFJQ7Y5mqiPta35mToOWsl%2Bw8TkIToSKTcj&X-Amz-Signature=157272e68bd45c7c69d91d3e627aa17fbd6c59eb9938fefa2ee1ae478b144f5e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
