---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VE7WPGPQ%2F20260626%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260626T225900Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID3Lcnh0YYRx%2BRiE8pW7fduFA%2Fq%2BuYnG7ynLgPoUtaASAiBPtkukK6xJOIk8h6r9qhkrQvh8qs3H31yRjk6tnQRwFSr%2FAwhtEAAaDDYzNzQyMzE4MzgwNSIMjIJr68x17PtkE3DRKtwDwMu0LFN1h%2B3qfQtTLE2vFtU0tfhktmULZq48z%2F%2F8wryrW6mJ3qgLKVjhHfibBkXtG4QrH683AB66bhSHONl19SZBChK4c40v%2Ft2lWz5cRKIIsLgjfYI9U8ybGzl1%2Fra%2B%2Ft%2FSTgrRQqpGVPKnPfhD9ieubyHkK7T4SR%2BnWawWPQo2h8hjOosoPbUEdNk53aw0ql0zdEOdK1zBm9TECmQEj8yIB0AZtXyXHnXWROLdjS7p5acvxw%2FNmwHi4PGzY9LtFz70HDvauK%2BQbybj3xrYTfBdkpmlnGottcfLgh%2BElKzaAzf75u4goZWkKRvuWRbXfNma4bVzehFFo9Aib5oi6pItscLttTBY0yITe9kJxsdMqVJllAGaXlkOpx9vvN5Jw8%2Foe40C8Obr1fbd%2BwiO0VBgJ5rTDXyrj9rcgttVuoQrzivMASEtYwxcepZY9sVN%2FOwWTpeSgaNI7xNabME9ZxrMfuM8NYEvhBxmQu3jjIel6FhS38QHN%2F6gFtTaA2H35D%2BtYLRjbm%2FnyDsSNS3CsYmiHUlBTyjXXkRCuW1%2FAUpWTV38hwLjlP%2F97qKcsqLpfYuYy5GeOE9ZprDaEHaUyrw%2BOLw8qm4WvCHPfgvzMelhWo%2FHZskIoBBlvY0wtL770QY6pgFEMGxVc%2BvDGQ4S1iT2ZZdcUPVm84yZiIMJ1tnzKPEpfJaV6rEuqXjj9CmoBh8hkKPRRZ9OCRI8v9Hlab8KRnPdj4rAUthqaiRRpxM2tLgcXAxSIIQ5Ohw8Kf78vfWHpeSc2IFzaVSXjrKs%2BOzo8RrIB%2FZTYqe5YdN8HfZAgcAAe0Fy9jkHsY4An5N%2BiojRkugoBNE1fJMa13ZUr3Sb8T%2BmmKUqE%2FS2&X-Amz-Signature=0e40b17a4e3686aa7a8d692d05e50280f51367c0dd3b129cc4352d5697567c8c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
