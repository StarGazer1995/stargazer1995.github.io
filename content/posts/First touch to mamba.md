---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UMP4OMRN%2F20260815%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260815T101131Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJHMEUCIH31KXcMVcVcoim6argMPPpHVYRIhudXiaHqo3LKMJYTAiEAhtwSS9h%2F6JFe35cOYUt5AB1gwxrqpW5U0ojrRm%2Fnodsq%2FwMIExAAGgw2Mzc0MjMxODM4MDUiDH24gLJJFyLWTGboTircAxw9gRS75B0k9erA1VUlMLeYlEF2eUbv8H%2Fa6Ohm5Rzt4eGKMU9spfarFs2VqrxCBKQsbOb3N8aZSBlO7GGCIVsaWjtUlqnpoBTm%2BhLumQ60%2BVFXPx%2Fdk9oevVKootApWDHLlJXFFNtufAsRZAv8wox6yqYqckWEQIn7xCNWv6mfID0tLbsVZgkICXdjUE6Kk6rYSgGp7tWmNz%2Bp5vku%2FPqX7Aktw%2B9YiurVS2RFX8uZDhipjn3E7%2FrB4TdUvh%2Bk5ebYW7pg3WHdfJmWE2Ev%2B8Fh0hLzUMInmRDm09S0sMN7caFAKE7nSssjlYWck5E9RfnLGMxtmNGTTCNAK64ap6OIpB0OPNT4ZR337aMk2gd2n6CIjDOT39Eb2VQf9t1yiR%2FAvMPfB96%2BAPiD8Noj4aoxP2QJMhPNPRBCdEUQ6p9qu%2B19sl7zw%2ByFJ8gPNGpjoYEMRSJ5sVfylJJCyd%2B9X0c70c%2FXnvWEGSUVtZuWpc16tEvQRrC8o0j0i4v%2BPm9gZ2sW1vaA5JSaLSKo9WMWpfSZoJLMA%2FtmdPdOvopO7H28irng5w6uFocWTXApdCxXY6CgJQ%2Bo9nCCO6HBS2KESVegwP1PluuWqcxMNtP3b8f3aatM5WtXiM6%2BAR7hMIftgNQGOqUBoZdrH5f2YFUpk4brA7QIb0bOcTRrldRJ9xjWBLCbzFc4EGrgoFQ69vC06w2e36E1ZpFBCcycuOeazcVpElV1Y8kTt5LW03WxhHoza%2FE6OS5Vkk4YaFDtqD7FakgPskZvxj0rGuY6jpnqc0a7G1XDQ%2Bz211FPugFwaF4F3X2L5vbtlMF5Gn0dJKL33Dsv8GhPe3lZFmgrnKsTVWM66PXplKGwtF6P&X-Amz-Signature=78dfe35c7fa4a3f97de52b6a3caddab1f93cf72262836b681b4cfb41fbaff27f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
