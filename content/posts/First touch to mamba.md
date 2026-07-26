---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QKTTVMRB%2F20260726%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260726T125410Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJIMEYCIQDnnmQl6OSvW5C1JRSeRpxZN8wvQaYaX%2BJK4uZpfXdsAwIhALXjugsNNATGJFvtVhq4RvanZCs%2F6qnGic0MYRclW9WbKv8DCDQQABoMNjM3NDIzMTgzODA1IgwVY6%2BBxnu6TR%2FL5coq3AOzA3wqUHWxGxkjxFUdjyNvI6uWNUAusjBptvJ2im7Dfd1IUXx21%2B9PM6FbJo6JgFX9HrcyohCWSy8TSr6TqDa4aJZfI3Gk5pfWcJtJAGIGgboZKqBmhMff%2BGg6QEc46UTAfPdVV0laNLMzPtQwIF5G%2FRtRaFF3oB2LtxKmTHqjSCVfpIN3AU6lhrd0AsvkIkkjRAdSAF5bLAnoMgVgLbmbWN6%2FY2LjvhGnPo8iIoBEk7Z4c40OySicfpZd2BQxotKcBxx16PqE0%2FpyqDMbSDLOpkiWpqQY0iv%2BLdpT4QhI4dPTVrNgNcEyC5SO4k4f93oOAzb2O3a9JwAaqdZxDH4TV%2BqXYu%2F6T4fplUkyRtcbA%2FbLJlJTWVdXryjQMkIFUoeLXUwddkxWt783EjX7V4m23Kse1e%2F5sHizz2XBlV%2F63k09emIhNQNyp5YeboyLX8rFJzYDZXL3riQr7q8VTNg3xv%2B9uWmb%2FkspKA0XBCRLJ%2Fc60YBePskiTZ9O6565dG5LBdBsK%2F7TOpXzWeXFDkUFSjzuwgjYYcJ99P1Yx9BDWmCAcz1JOn1Kmt6QXV%2FmbHJq6L2oAre9qKMBCxkXGNE41GUNpNYH1zdeLZS%2FZKd0UyDzB5KquIE56S1gSjCmx5fTBjqkAQNld924UrZlDsH%2FfPTlI2sshrTIc8TpiMJyk8NZpPuY9I7f%2BntHpjRcSJyMSTGGM6dnx074XK9HkyZWhHG%2By%2BwFg2mDag9rY8xcc3LE%2FGYiN6mZtUaUqH%2FIWutWL7LJ5WLtXU%2Bw3Keg%2FgSHyG1XDWy7Av4JGtVAnGaYy21U2uReofQkXWImq0xENPQ8PXoBNusl3rkGfeb7FyRdfzJXbqUdwXQW&X-Amz-Signature=5960b3ee1f332795af824a0468f75abbd1553a21a0938b7ecffab0c95e9ae096&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
