---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SNK5A3RS%2F20260511%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260511T054946Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEUaCXVzLXdlc3QtMiJHMEUCIAzKeXVRGZ%2BwBq3Fo%2B8meaGgURWdJLWSjtOg9NKF48zAAiEA8fHLDNSZFh1TO0XcJLb5K%2F%2BAdUXBKOG%2Fq9olaCqgpzQq%2FwMIDRAAGgw2Mzc0MjMxODM4MDUiDPZ0WReNH7iT%2Bn2bZircAzuPW%2BhhjjY5HqgWh8nqIFfTbQIMU8PdZaavZT0etizvhi8zLed3BrzZAbzXji4pfJzU5tjuHMOh93AbUj0YKdndZKMI2RE6yt3dLD5JFqGEgWoNmFDM2CjdUdmVzjmm7X8rf5OK22ujDR8LVLgM1NfvKN3c05GRYgxdIlApJ77en8BMau5TFKPBMD5qs6gzfwmv2CxSF2mLOMhiNyDEa%2FiansSNdufrMofBn1j0gJ9x1hNSFYKpRz8m2x%2BBt5RGuR9hJ%2BxYxMSBCiwTdiE40O2lOtorCEtTKuDRpVlgAyDuUjayFpwDn%2FiZlx%2BornKMEjvdEEsCCzM8uYMZWR43Zk2d73uODKobqtT7LD7tgqhVALUBJyzAhbEq%2BYt9Sb%2B7GMuuRc42EYuE4uw63Rh6okO8YMNpb7UB8%2FFPt7DTzgOS7XxthOZZz8wWCpyyDKkOe3s6leLHpsSkG4J%2FNUheA445M6Qhi9NezUcZc3VOViTBuNz%2FutXbl2yOTauSvZ5pMDvuWhVRfmvYVyiRDs20nhgOiglOpwX2RN9zQzfRuuJubTeSW0kKLcLh8IpPI5lgCgguTLUpYJAq3E3URjr91gau3dVIFTM%2BW%2BZ9JhP%2B5fqRjJG4iTccQQ9kn5P3MMS1hdAGOqUBJBd3fhlbefQY%2BKsGoRshCUMgjUjntA70vyZEkZiVHrN63GORlzEgN2A3biQhpeSQYEjz7GZIwDX0HpOFlPgRrg1QaKjlFd4UrFLXhqCLjegi1id1%2FtmewQwMFzAf0smz55yRzoxaJSxG05oNJ65mR0toxUxjWHY0mBgEVO6jFSAhIoBClIFXv9pujdbOeQTjLJwJtWy9fPBx55dTFfifMXbWgjwf&X-Amz-Signature=a311514512de0af7545fab10b8ee723e6b02136a5334eaa3220ddfd0c20fc764&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
