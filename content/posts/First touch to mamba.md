---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SZ7WP673%2F20260713%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260713T204759Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJIMEYCIQDtYXwfoZCpkhMvv0A2534%2BFC%2Btl635x%2FflZlZFlkE%2BQQIhAOw%2FBvio5cLZRvlDJYV%2FoL57HvR1124ostDRfR2fh%2FJ0Kv8DCAUQABoMNjM3NDIzMTgzODA1IgxYZ8anwFu8ItUegB0q3APk1i4zCf3bmw3fM%2BrFym9Sjz3C14i5KiN8At%2BA9XWa4iIgx%2BRCCTj4NdVa6jJMvJWNNTOH8DOcIjTbhtOqbrlJMrG1shVZijqBCyMSWvURJf45L8rFbcu01TMkjWjlq%2FbW1k2SjbMjp%2FjN0gT5Mrxla4eedqS9qrvgAf29aHeVYL4wdrSubPPXr2G%2FgrfppAfnP1W6zlMv16EJnUbeG0UfFsMgS5u7Uvkzdj%2Bjj77eMsuau8dKS%2FRPgBc4IgsoxtXOiJ3LlSyygIOqD2%2BXWs4GkB%2BeMnZsoSCC0hhr%2FtII5b7Cx1m8MrJYCJaFHvpKEpiRPHqyyGo%2BZDYjAATkGyRrQgup1CIZoe2xZHuiSiSjsmSRRZMmBaNwaCfbuKtulUwH6Tpl%2FDau1B1LTawj9VeubIn95GQpQo63VF19l8OGs6CtsfVD%2FFjg3ecBgVLnKAF6LYLJc7MiUbRcFWYRwxG46AuJcJfXfYFaqeyKG6gJl8BsfCJTeLz5%2Bjr3S5TUBQuqlzaQD%2Bv1KEh8%2FuMQt2X%2F3qqcK%2F6Pvt0CKcOQ7M57B%2F%2BYcSbQgEfIbBqOFantBoep2QuauVsH%2Bx3%2FDwBFcHg3A%2FwPccO3eFyYp76Wd64VsXZ5%2FrtXLSiV1sw4IjChiNXSBjqkASimXtFp8vChAbAEC6Rv%2BZAs%2Ba%2B48Rs88FwgxhSmK%2Bh5f8vOrf8YD3gi7VeUxKkYyes3WYTEQ9MXTy9d%2Fu6gHcNvOqlnCY4%2B0x%2F2wtotRL3nK0ccsECWT0TLt0EE%2BdFPfyMLxs6Vcn%2Boq9kT9VDXIOrgUhdfxXhBC8R2POiYvSzwk8ipbnBl1gO5DdnpIM%2BZC7Ifg5kDsb9Iv32hR3KkYVXdK6cj&X-Amz-Signature=aff7e215720e65d9dcfdb6fd3943335aec76cd222dc94e83cf56f2f168ecc5d6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
