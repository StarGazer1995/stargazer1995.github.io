---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UIKNB4VD%2F20260829%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260829T185846Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCzg612xpTpGTVjgXLg0BJ6DoL0UwrKYhnx%2F2SFL4STKwIhAKMWfwEzsU365ghl%2FEt6w0anp0dOwy7cdxnlZrDjMRc1Kv8DCGwQABoMNjM3NDIzMTgzODA1IgxmJKXUK%2F%2B%2F8YyUD54q3AOoKDeHbM%2BDbYdsxu0UgNUzQWTG5jXbNgrmzb8Nfz08lH1oTDTUw0PRAp4QsmUYz7HbbZb4gcYjfJAMCePyQFZLzgrhYim8PEy0jD0dF2cc5In2LnwIIFSBMUPyIFJxxP52lj3L1fu498lwJ2Ym6d6Gkmdwp3MQQri5Z13JhNmB7KnI5vscJQZkQ%2FRCpm%2BGICNxM3BaVxYO%2FfxK3JouH7oxbsU0mLdWnxyJX2%2BWyHQ2Vv%2FDAKLQ962Z8gpR97Foct1%2FxI6zhMP7qLwI4GY0eLZCpHCG%2BtfAGdz1fOCTAaS0wIV3qrsFepEsJmlWfxNuJ%2FK7oJ5fFTXy9JUAD0%2FjlYOlwRYfhHeCod2Qo7kDPGoUsKUHJc0shArd0Zsx3vrhn6kQT9Iazv2KiCili5lVTRu%2BnDSqriULUMzQcXor%2FebGNxPKqjwBWOabVYuGsw2iF%2Fotad%2BykLKotFSWQWc14JPTyjk6cBCWI3CR7cLyxNUcQZUBtxS4fg2wgnmLb%2FdKseIwDILwqVkLYyb0zRiXJuNhxDgc34jkyk%2ByLA2aIuFuXSOkHpgLllloq6%2Blu5WAb%2FfYqmis9dqXjeSQDdLrYcbgO78t4%2FR%2BTpyMEndNerKTXKrDR1%2FRUordU8hKTjC6yczUBjqkAd0y7oVZ8%2FsJJ%2B3c2Wm4nqFkWUiqcpkGcgVIeOYqkWCRwtYJFsxp6ymzBIKT4%2BpFHuuMtu0b1P%2BtcE5zHvy%2FtxGZjQkzQBtwxgv48kWg7HgE9OiAxjufl%2F3d63F1CQFn4I4NmrqjyFOn%2FVYUWSPLsQvj0osTi940225q3MVZovGdLj4nJCRCRqtGEV1IN0QDIIDlXKphqRF2IdxgsyF2yGuGwm6b&X-Amz-Signature=2e74d90576832ac72dc45bbe20db5f87e423bc45c8eb74203d5ab8001ceaaa27&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
