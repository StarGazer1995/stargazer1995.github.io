---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y3RU27TY%2F20260602%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260602T021728Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE4aCXVzLXdlc3QtMiJHMEUCIQDFZg8ccxkgY8qcjJOIh6%2F%2Fhe2c0fsUVwAZl%2BAcstAhuwIgFOvf5on8pGAmRX6Oq%2FkTC7YPupwIVyE05RaC1jUDN0Iq%2FwMIFxAAGgw2Mzc0MjMxODM4MDUiDODKNY9zxInH8cOxCyrcA4VWhtoq2QjzBxNTnBISFxmcEMVrpYcG3R%2BQt7tBW%2FyzARlYnlIcxmpsYxONVOJuQyY3%2BcXSgIxGj29RRZQvJc6H%2BYnqv%2BmHvGMzR4vdfffKKsYDRKm1cFfHCQWJgJu7Q6cB79u7%2BmqeuGwhRLmfvqEEWyo%2BpsGUapi%2BtvnKZK8xQrSlqT5fuPiQoQbiqyqoqjnpB7G7PB3o117Gi5N2vOBKwyjwx%2FO8UE6FL46nUnhok1CyGi7NifqQZmv0jtcHppKlhxp8VTBNYA7SmusEpl0QaHsTyJSsAGMlbxBR0hOupi%2B4TtxiK51ehrVVd%2BKi1TPGLgzJuaqerztfRnWn6s1D8lhQbUv%2FJEDZe%2BznPl949f3RUDJoj4GVCzETwQVs0WZMPoZri55C%2BAD8wAs4Yq3chd8R5zuXASAVCrYPJwW6ZPlSioPimXGazAyVd0VNAcnjGYCnKFcX5S69zfbLjc844pTnvH5gb5urZZrnptQBFIa%2BQGbJGC8j0KxmESLz%2FM7U5GAnJsNCH7J39OmM3UlFbPKcEnVtWvVdD5M7yhUNG%2BaQba9yfSM6bwyte6UWIaGH%2FRAQLhPBDMzQE3O%2BNa4uLaO0xJR1KgpEYFmqsx1afWlN6LZMlTonZLVYMKWI%2BNAGOqUBjJpUCMZMJTIug4DP6n6k3eVmuDgfwkg3Nt4wxwMmtmuSxuY44lU%2FwH7smBiQIojWqe97jOCTDNQmEC8HAMPOpmZabgrZJvwC%2BWCKdW3KJdWmc4JwJrFahhxeYxn%2F2djYSgnwcWBr7Vaq1CJyPjd5MyPKUS7jIzeJEKntW29XJuTrQGhFVJln755wggDp0NgqVmAWWLVIx3NLEIYVIXq348L6krJu&X-Amz-Signature=4dab04ead753ff7694c3f449c304a09884ca7d1c7967b3c8e7044b8aacc185a0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
