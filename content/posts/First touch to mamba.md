---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V7NJUPIP%2F20260728%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260728T045240Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAxFxhWo1qGYaGq45CQToJX33B3LWDy74u%2BWd1FmylCiAiEAx3eBK%2B3Ra0eM155F2OwtgSPxyXVKfNjm10gTPW%2BVAh8q%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDGIZGmrDuDyY3Lc2oircA%2FBshpig%2BNbTNhIl3sTh5Tr10D01kQ5Nx%2B5p98XTGlvpGptwHB1gwwxg3BmEfvTVwfx5T%2B6k%2FVtEQ9hf5GHaGlOfLBXvX4no9naxHCYKCE%2FiOFIpVs9kQhSxHSkndeMfvQJG1RjIHJDepGOoFKBNhYumlA0XmL1Rr%2B8LsGySNM%2BB9lGIRlv%2FPqRKXe1bZrLNljZ8hYM6Es%2FKe607OzGDQ3n%2F3Gj6kgIgj3LwwW2wmqu2z7ZZC%2FxathvQ08oTnbciEQ5vijLPH8ebYGf7Gp6GYKH21v48PIEY%2F4uPuiEEx5B9EQxGgpCN8Bk%2BSfBd4gfEXNUmOQsmitss2gFTGyvSZJav6sHNVZV362enVi35aCYaMK%2FrSr7th%2BQ0Oaa0Ah2L4O%2FECovTmhT7XtmalP%2F6c4Iez1CnadKJYAC4NKA4L%2BpHX3L4xOZHqjOLh7gvQUSGzsS%2F%2Ft33d66QQzegjUwts3iyxiKF0XsUzDSBRX0r362po1B7LhBIx6OEsOZHRNdc3xqhiyfeLK3EbT%2FjyPD7NZl0FtPkrqDwFJToS0Vi%2F5c38V0IwniUNFOpickCYV5Rv0U5w9XEWqlskOikD7%2F30Gn2XQLTwAzKaBLjnXx8PBJcJwqhcv6t%2FbCcYAUWMJLaoNMGOqUBow%2FNFGwy4dKGNxHB1gsNdbK8bfya8H55d7mLbjV0ibrHqH8YFlcyMq6BKloTS6EwbefTvq5lOOlhOj%2BZAxYfA0kfRChuH7EAAJUWN4WZmRltSQAsrUMpCmACluEXD%2BlKpS%2FIzEMP43fiOGMGYGfeqAHhGVxQCJ0FUo5pg7b9jrBIqWgHVx1pUnz%2BZke7a7aGcLNAa3vL21eMJC7dbgeJojNS1uXc&X-Amz-Signature=69482c87041bd934507faef0dc98e0838368e26b74fe4fab7c9c74ee54135a1c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
