---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667YIXKDV4%2F20260910%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260910T233110Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCup7jlkSCnb%2B9XICUP1VO%2B2nYGXZ6f5fHdFW6Pv972zgIhAIlFNpLQgRhaE4bYAj%2FQrfikj9FgkRKztvLw4QD6bC2uKogECJD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyC0gJstuFptKfq9HYq3AOB6O8Wkv0ZTaM3wrynGjSSDdQq7pGrsNUL5dACfL%2F4yb9t4R7Yls1fhb8qUh75OVnmGrSk%2BAGVV%2FrC%2BuYYpQtxY1ozxQ61u8mWy8zsw1My3ta6pD3vit9XzVVlQKTJiN7h2GCUpIiyyfIcEovEQW8VhK0M%2FpHeWQ1ORm33eYdLogeNuz8G5kPoPLZDPWjiTGyn7xVEgsBsv%2BG6Nseq9k%2BE3KYGQs3VF6UpUjgnKShMKruyCAJ3eD%2B1lAKktm8LRQ10Ut2keLi3kLlVH8AGHxvW2DMAVDnXUoU4L7prt6u0IBdz%2FW%2Bt0iDBGAtXhcA5PBzkMRJX2%2Bt6x9uN8o%2FFqAe4Yg83fNGQzVpGIpSDoR%2BEvF9hD4IiO%2BORMo%2FHFDNcMcdwiijXFKHqH9rKhwVHBimT5hXls0hfCoogVLOSz0pkv2CB3YhNgI1vY4Mdhck8HRJ2OuggTb6tLhFGVxDMl4aSLTVYu9PhZElPqXiAJ6%2BSMvXoYaTH0DBpjPM9lnoG7a4dmYDONsw4mlw6K0blCjzfn0CAG8PJ56V6Ouai1cNYFQVx%2FZPeq0w6o975Esj5T1tjmGDs2mJ3J%2Fo%2BrZLDTsGz0VQBSo%2B%2Fh3me%2F%2FrNvix2fwGKq%2BklCfT669dKgTD28ozVBjqkAdIpoYUExnspsW3pifAV7n4gjvqg66ONlgFTsf9WZ3oDgSlLBRx729I65DO1zSCA51%2FdOcpbIZ%2BPRdfYDuMjIrld5mOOYrxaI6Inm90xD1boaFE32e%2FMhEpxDpRN7jqRtP4VxjkWPK3oofgFGUJ8YonjkKkktz42FT2InmnGUOuvBI72I1ByMfAoE97cn5SjI0rF539G5uz%2Fuoe2QmYd4tIML0RD&X-Amz-Signature=31aa7932d98bc3d94ba881ed68389e4b1f8459afb05be4e30e1a07c40aed47dd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
