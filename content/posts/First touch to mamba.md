---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XTINJZ6U%2F20260825%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260825T143400Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED0aCXVzLXdlc3QtMiJGMEQCIFuEyeVIBv151JeH%2BdMrT7qNNJR5PoMoD7Sa7kDya%2FEhAiAEXszzT4rdVMBINjzYY5zCvBt2mWdM%2BNzHBCUOhJrVTCr%2FAwgFEAAaDDYzNzQyMzE4MzgwNSIMrFeCC9aPBsULD5jlKtwDdevRVE5MKiPXvw315pnitIPkvXJlRSJ5fNWmOyoiBufVvHctmNJgaaVeoR%2FYxinqZCkSqd6c5RTY6ARd1IXV8Ea3WFf3reCJFWh6xF7OL6pDPVNkMgxfzqoL%2B%2BMYKdks1egcl8hyp1jDNiScDh4EEB8WLnbOkz1FXo8n%2BLSLvcVA7y%2FzMKIUT4P3vWlJ7hsLbqQOkDKPrV0yZsV4KVdT5jivOdZSPKxUkWGgu4opCtMa5O3U0BBa30DLikOiNzhAT%2FuW20yriJGAx%2FFeb52DMPSD3U3GCx7V%2F7KFmimtlEJ18KEvUtoeuQ1NCN0Q%2FIusfhONI2PJwzbLemNSFMSWdkmRGFhf%2BO6c2EuHFSZNIK3dGr1vYwt6R6Dq71rQI0iu8%2BbgyO5rEsdCAJ7hj8vG5wIRWfc83l%2FrsrC5fUaB8QqJoS6bDc%2F%2FmKNjX4aYSLckbr3RuThh%2F6B39DNavz1jPgD30YcBBRk4wx4YdTgmfDznQ1nIFw7XVktH7o4247fRPrmPmsC4b2VH%2F2bXRjmiGr21xWyWcesyIsI0HjXjqnfVQTey8%2Bd%2BE0FFDeT9LC9W1TUlh3aLJqz1qBxE%2FP3PiAfZzp0Qa8kQVagR5lPhVjqQGokzNTWhgzRqehAw9ZG21AY6pgEqZ8x7pYvfiiSWknc%2FiXr2ivF%2BkZWMGRaRRfQjQqnS2vdmDBe0s5VcVZLeKmtKfZySm9w00eOa9PrRnrWWBqHiD6F%2FMGnR5SHdq65THvBOwttHM5CBZjCEmIAj5t7%2B3wmKFKeV9dryRY7FZiqTLO2NgJMpAiqjhGQF%2Fpp7ejtn3mmy7ANkh9Bvutm%2B8Ut4UrmLvD1MB0m79ANyYcR8AsOk6wpzR3Af&X-Amz-Signature=5f513199a9b609b3604a71f0e67bfb3949156215f88cdd39d3dd05834908dfae&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
