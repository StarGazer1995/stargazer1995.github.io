---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZEK2ZCD3%2F20260626%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260626T104309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCbtr%2BQiLd%2F%2BChbYv3y%2FPbIH%2FsYFLq6C5iuQXWr3op34gIgNCL3D4U0AHFj4XRa1xzv17%2BR%2B0511egQu0Yw%2BSIKNMcq%2FwMIYxAAGgw2Mzc0MjMxODM4MDUiDKPy8xuAhf%2BLBxeydyrcAxxwltgEu%2Baop9rlqLFm2BjNwZqP6zOQOWiFPk%2Fyf60uQAUioG%2BdwY8UX7BWhWZmYjByL%2BhTGzwFrilD%2FmX2LDDGux7GugtLAx8qGoaVqmql4iiikAp8ZEZj4l4%2ByRDC07gzPgnxBXdtLRPLWqW2ET%2F%2FLJVT%2BGhCsZDITSBxiy7dbyl6xSP9gASE8I%2F3P%2BP%2FN8%2BagIcvv0pmQihEnXu5zwOZfT71pqz09fWWLKLwHzCoOVCTP3VVVvh%2B%2FdCdnY%2FFxUJsnfX4UzOU8Un72tNzDFx8ytAs9CApnG4ukImv0ZaWzvgiX1NNUJVjG%2Bnt4Fdca6oVSdTYbS3aPVVtoA6KCfpv0hhrNDQ5eCYdbkDpWJd5u3cKrwJRnOtviS65oXTSt2g2XzPXd2gbDAZD7q4xLVS7yYyAWMwW4QDppiduh3ZaeiMWNRemRWH9GKIom1hict5jHDBzd9hEe4e5%2FO2WBw4iP1CAw0%2F%2BokJP0JNZyxjgaG%2BJIvQj8kPsALwcHepXvSawqxdATHXw0O0jWd5e6xfy1Ap%2B4wPJ17fA108R9gENrSfLtavhvHxmaZX7Lma8VBvN%2FcvwMaeg4xuNwIooCb6IELPTeMHhsxMtmydVCuM8mjT%2BCFpac2osleO6MLCd%2BdEGOqUB%2BdnT8%2F6RBDdEMSxd%2BsrdxjpAnrn1oMdUUsd9DNNlJ8eMWD7XyGU6F%2BwVHiu5hORRo6jVrlQZnrd0yQeu7DG7r4K97j3SrXGUUzVde5jgZ9Py9rLSx6kzMKIgVIhSMR51Dh7wozpXHN1QFxyGHFUt%2FkGwluDhm%2FhC7GeFu5nj6hmyVKlb3Kwaufq0sgvPEgmZIxo5FoTtZdmlGHGzVgP4Zrwwo3gC&X-Amz-Signature=6e0352ee9f6a919434fe01237238e353386e9fc9fb9ed884bdd72f488809d9e8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
