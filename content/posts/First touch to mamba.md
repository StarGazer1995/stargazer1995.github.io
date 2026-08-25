---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VRFHIXJB%2F20260825%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260825T201551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIEfzhQPbtCJXeh2xSuSxQy7Wy5Q7GLjy%2F2VGHwckcxKjAiEA6lbEoPKB6SpbDLLKU7dNFVGFybriaXPns0AcrtBbYdAq%2FwMIDRAAGgw2Mzc0MjMxODM4MDUiDHOf6WkXK6DGDoEhoSrcA%2FdEHqADtLcsRSHJRRy0vqFmUTm0TlrqoWrZap08GjjXKf6cjY%2BYPf8UfOxfxaY82Qa5iT3AGfEczCtDkOSNQrjBjNKw27NRDd1W7tYhCInRJvjzZDpBIGjXZQzdOdigZEdIFpAHgb3lFRj8VFJ7oTFvKc4rwnItZ0DtTz2qNmdc2kvobMsiYHvBECu4XMTVtY%2BBAT6b41xYN5msBUFsW9xqEMgR%2BMItESOO7gZFEIjk1vS1dprZbaI8jebGk0S%2FSuhBEz7u3JwONu4c6GvhKlwmdPMk4hEtZ15S%2F3PU3GEhFZ0%2BPIh5%2FwDCOPtGVbfXWoG8yckVFCQ4jyhZyaaoE0b4Wxw3FeHJbbsJfFHniLz2rN9BciMP333PpuR7gbPm0sq3JUF%2BOpNZYSsp9BNko1Ls%2Ff3dFvVs7056HF7ysR6Xbuap7NiWjAKYqhvQNoIXw6ZQABrDmI89haRJJWPNcA9kwO7EXBB8330pJkCQC15ezXrdbSJRU7NhZ9nlhHvc2OTOVmsrUydQ5J22RHi7LQy9gUc0%2Ft12l01ddupLYuAjEixJC9u8%2B4x%2F9xgyCyHlwluFasX%2FRZezEK8pt3aciXxL%2FsUh%2FcF%2BVfRBHjACqcXNIpDJ5ehnHK5crRDdMIDZt9QGOqUBzM9igs8XC19vks%2FYP6P9Y7Z11nt47PFRLomjpdeHuwoQCrO5TekKKf8YvN5w3GlqlMo2nbkFgrKQn11m4jGTqEo4bVKESugh%2FHBOzbekJD9AzgFRmRTcyikUuvmJgHs%2Fi6nWdQ85HLaO9bRM27gJbGGbjjtBaoXPw%2B6GvRJpDBnI3nh3Xrs%2FKi4QjM%2FkRXt1UkACh8XoabOn51QoQAK7aGPB8vOY&X-Amz-Signature=778c5d9f0564a56692549f83eb04a893f8938f22ae242bf844a643eea4e517e8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
