---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YDPTVRAE%2F20260820%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260820T042530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAhzuXek8wrj0jQaJUvbi0yyUKxtKgIb%2BRSwAvrpGVa1AiEAoddQbijciveYMCNa6jhpU9oXiMO09YY8TPqi8tMtoqwqiAQIhf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB6A0UqQBtkGRzohFircA11I%2BgZCL1VLBSQtcl68BULr%2Fp%2FYDeVMgNfk2ejQx0Dx2iagnRfok6FIXBifL0Qkpo%2FPGGk1FczrDWW25eG9AYXy6DjAkZKkgPAsfr91uflTEGaVdPyY5GJ38Hf2ItZgnVUsCTAD6kCcCLd3ntasNWrljjexPbNuwg4JwyLyfeOl%2BbmSMlyy03p3tfNGZH7nXiA7grZTlfkGc50jIe0XRyUhYc25OFKFNyDQeIUbtE0qtG1tVyEYxrrXy9lmIeJRYpql8DBgKI1KpKou2Wtyw7lUyz4UTznFjFPMOYslreP47BNLUu04%2FrqzhoYdMBzDbtK5%2BzMepx5fHZROcRMR%2FpDvEuz0Z30HYUmAskRbMtuKlBxO2b5yf8O9FaxiXO451zIknSyn1bGB2q%2FalrwXzfN7CNW38VKRBJ%2FOh6HPq%2FOOBxvcGdJu5HgCMlUzTIPkOOtDhtCBMvxBjWtSAd3YyMrEwvo%2BH7%2BdUzOOb9Ki5ngU%2BTpb1im9kX%2FHkaLZUorDOUmI%2BrgKnHVonoFnliUpthpUcNvIZ0MjFI%2B%2Bf3fvVCKi5yrXbaZ4c3uP4%2F3oy4aEqouBqYdVyLS6ncaRg5dTQyhQHO5GsjMES1psCm%2B69MJ%2F4dOvEHCXDlwLy0%2F7MNvrmdQGOqUBFHf7ytpjEB28q8XQqD79U7RbxyagNO0WNcqQbU9FthRPdlj6f2saponkQ5EHgHGu69BU%2B%2B0wxgIzaTztVM1KHRrDYYAG6ZjKaLshA1TgQg1PrtM%2FIId9RAKfMuRR7%2FVVDn%2BmdW8h%2FrcJqQXrtfI7mbpjz97rb8ynfi71OQY4iRqdnObW7xDPxjePu3Su1Rd%2F54GEkXox9xf%2BGvg9lkmX%2Bjsvpwma&X-Amz-Signature=558c342ed48a052423ab4eb09087624338094bd8a90a60da79754d8d4497b1f0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
