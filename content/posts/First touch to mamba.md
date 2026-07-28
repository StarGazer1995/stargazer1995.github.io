---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QJZ53MDH%2F20260728%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260728T012105Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCmqyaSpm%2FskfYajMGmMYfs%2BCoaCtalcF5l%2BRgtcHh8qAIgULDylWW309ogwJhJIbEEoSFVyEnWkViEec1sRQxmZqsq%2FwMIWBAAGgw2Mzc0MjMxODM4MDUiDPfGFkXsdq3BkQ01JyrcAwfEqskJZmVdkvkmaX%2Bo2lswvw%2F9fUZDVrDuONYMQ3bo1JRHnjk6PtKDYADAkgnNoBTLuvzaFrTdSx7hgGP9SVSRvvcq8wsNMA16hFUtBLYSWUJd4vlHuS5uTL%2FEduKsKr%2BxZPqvWq029dnBfTfm8qY2TBfoS0Vauu21ko29InqAt%2FqbEpvdgkJwfBfH6TrXy0HoRvCOX8jTG10gIdeE7UWGTBXIVUfKyoHHkQxD6VAl2x2IqbUcpzjUN8WT%2F64knfhKq5Lap05DFLarDd2geXaL3DDqg29CK%2BGZtNcmgfi08L8ivmSdxfoq1iRSfbfSMz%2Be4UyTvGjfMtLL6yOdfrdVUqngELgIOmhN%2Bnx7dNEVth51Zt%2F4voLrh5eONIvwE0xj0YqHaHcDTStGTNzwITVTba4B0Cl3nR2q7Ghuq%2FzU6n0NlIGMdZ9Ws3Ai3cUVijcVT123MLPsDEk2iphA6F1qOq9S68AM8YvFNhgj6kMdgwD%2F%2FDd59Jj%2B0fP7QHC3NjhTk%2FocdlCfg40Ow6ir4VnmWozgZgtxXCqkq4pHPpAYIiJt8nsRQEWmOc0yU7TF5h8cZXImJwzRjkOstAXERCJD4bPdCvtDhsckwQp0N69rxgb29sm0XXCWlCbRMLLFn9MGOqUBPgLC3d5dgWIlNKisYE1GY8qZMhcqux07XMm6oCr%2BhtNLSpLibFpx416yxo6yaIQ5c%2BH9kvWYt3a6kcyoU0tJ15t9RQ1PzQ0THPkdNdvZpDjABG5NUwCe9anVrVaiYoQtGMAk%2F4i6FU0Il6BZ7IojoNUFmu%2FkZyp92Vr242KJ%2F%2BpsxArExJQbPBSFuvbdlCgmtbaOp8xfhPqabcoyTO2QdeIVVkvj&X-Amz-Signature=b3b3fcd7c326b6f60346ffd203f291e044e3b63b29520a91a3a1ed033d91cde5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
