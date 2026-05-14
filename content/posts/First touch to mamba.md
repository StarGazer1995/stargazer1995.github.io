---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665DO55WRQ%2F20260514%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260514T210318Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDhvkZqzYPjdhzAOPVt%2BekOgli50N063ZPPOkTGzbdnqgIhAO2xfAj4rCxWRU4URfqPm1RJyZL7roQoHSh4PD%2Bfl9z%2FKv8DCGYQABoMNjM3NDIzMTgzODA1IgxXtpWRtg1lmMNFl5Iq3ANOApGl5QHs%2F7963wpbc9SK%2B2XjlaJGaqdF7bcBSeaEyS8sp7xml3IIJy58vgIB3y2vspSBxPRCOuGon8GGgaqXhSDByRzQxQaBim%2BCg5YH7sV5m4bugHu1jIAFVYUmxSSExnoF5NltCYz12aRlymC9XB32wkjUq2jQcTQwgFTIyKbrOBkxOkXana9pMM%2FSwJ1bCIYvme4t50FV1Nlt12RAccJUNPr2BmIUZY4PD9pegaYnSFa0XTs1Bzv2Zlas%2FSX29lQNv354hBnzWJ7SCZWxPoktxfxsGbLoYNCHUWiblYhv7DfeMP79pbLnHpKkerVy7PYz00huihuQJ7R9ZbkUjHne0R6722icn9Au1CBSWGXi%2FFK1gftMIzVfCNmAF7qIwVhEQvH8mmCDLYw4nmq3LY0tjzlBdq1sYVhGdx4CTmYLC5LYxpdAQ4kdZppU9ik0%2Fel6qrwAWvw64wOxDqFRZ5bLhtxCz4n4YCgG8BLX1BMjEq8V3VfvwPetO8LC9Sy0g8DN7G7Uy68gk1YNg%2BzP6Ax8iiheJE6pHEd2HV3ZilXpNiYBWMA6BLczM2hm6rm%2BSRmvWZdeu1bad73pMXoGoGx4%2FqRcvPXnE2wq%2FDqtjnH4mbn4io9AimQ%2FDjCp75jQBjqkAY2quvv6FFNnV%2Fg9DCaDMfZO8vesV6hAgBnrBROviCwxrdZ%2FHJoRcSgHPiGvRGQ5iD3142dvXEqevHJpFt%2BuNOK92CQeV2zkUMgqKRscmVobf5klgtP5SHSY4Ce3FjG9anmnw6ctSXHKhpWl%2FQX7uF%2FmVjML18pWgFqfenGAL1WTb5Yr0saMi07prR%2FUBumkGLj4H23ux8YfozeHuXzD%2FGLlbFbC&X-Amz-Signature=38158f198850fa49dc3c8e41e48267fffdd3a62c6ffe4cebaed10da2b2850926&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
