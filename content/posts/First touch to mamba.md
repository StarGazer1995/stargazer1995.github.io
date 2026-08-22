---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666IVDRHVD%2F20260822%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260822T101152Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC%2BjAT%2F3nYuuq8el6u3w3uyr8UUoBvCGxFGA9f%2FM3TU2QIgVkEJMvsxCfgZozbwJtFM9C5BpsQKmw5AFc5Bg%2BflwQgqiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDlJDW53gNfLBtsQLCrcA%2BRZbsiIzHaALpwy5sPt1Neon1UEh7XV6KaAlaN1k6EW2aIJnzSOYZQvJmfCpc5A8r1N7l5yduwCWlhL0hCDltuDxq%2FvTvOToH31f5gP15jLoMay9C%2Fo7Ee45j46wUWcp7%2FGW1jCdTXkLfKnDXy7OTCtJMXZkUT2mbiEYlzx%2FDHAxFKI9j88KmNc43H0zYqBlqMDqcNai0R9Essh2QIB49lhp9%2BxtQuaT%2Few8WZHrKs%2BleBqYQPDxF5mHeMwFs3lzo%2B0mYqbzqkFZznN9zXPHI0FWkqqvSUkzkWMYn3VkHZyjjALheBgsB9tOSe%2FtT8LcRSUclEN1LRlljIn8WkXFTm2Uwjivs2NW5LMQS2RQcsIMLwYgtMU1kMFDvErtORUSlNGY%2Bh%2Bk41tIHRH%2FIdTVEOk9PUiIAUoEougx%2FyMZ6KJ4yeu%2ByO8pRPjrFnQE%2FTvFWLqv0ATZsI0yOaftvewAZaC1wWQSc55RHXc%2B2ZCTSEBbbBjAtKgpJAEh9dtW6Er7tWfvTmA8TNgJ7Y3ByDMtyhDqHCe3uO5z5WuskM3WKhpyh9n2F7mq5wj3Diu8EKGrfjLs3JT%2FMMLjd%2BCBUw685CWGpodKm4tTeaOfQ8xWV%2FnKTFsqGQMa9VYlizeMPPhpdQGOqUBm6UZh0%2BN%2Fuxy68ok%2Br6%2BOFNLIQySHJvPompmSwhnhnb4c1rh9fVuq%2BnjNoLv7ksFr6bNOfWdzIVt4oNKpyoZMUrrCgDFMgwljxA3zSoeW5hwuh1jQJa2QjI482R2roG9Lgq8XXOlycdj9tSZOUmJvUn0o7ULpNsW%2FWUQiKBqmITA2odHiXopSAE%2FPx2qBqd3uB6gnPbb3OEf3EPkaPTrt57neWXh&X-Amz-Signature=802ca077fd0eeabfe0fba66942c0114384e0c192cd05bfcb4cc04064351532a3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
