---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YBYEKTB4%2F20260726%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260726T224824Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJGMEQCIHN6kqQlGf3dT%2BwAgn2yF%2BX%2BurzC0fgl1VNgBeMso64pAiBCzdbPwfD1VAfehNscmRsOLhS6BCXB0gmqjwm73HyndSr%2FAwg%2FEAAaDDYzNzQyMzE4MzgwNSIMQEFSH%2BFENWPEzm%2BGKtwDqjyQ2t%2FxzD2GIxWSnbd4YeNUZeUeEMuYYTLjUfDAlV7pqMkFS%2FsyJr9aIQGDCeA%2Bu6TPvjMMw06ji46nrHIWC2lUpOBiitg%2B1jPuEhFiLBA1TGdDvn1yrbx2Wyb%2BaE35Sk5ONO1j0GqFXOHhJoAbGHGLognvuIK9drxHdQCgMFvLyewe0fO8Nf71PccwC%2BKeahWEQQAm%2BoocCgB%2FLauyJikm8oJnkRgki3OxPt3V9YJH7BS1ePtmFl6rUJpwVej2NFWrWibK4v8EYDBX1adW8QeMRyf%2FO3tc5ZcEHixaLlD0HbpZMYHjF3s%2FRSr%2B8CYQz8OoOSa0hNcerWOyeZhXbTLO07zL%2BTo%2FW1Uw1oQZ1%2F9BOw9rRlkzqn79jvfxR2%2BYXC7eKpqzzX6jZhOxdbWnrRdmPDWP5Rv7cMTTIxls8dj87oIMFvJpmZ6pr0CO2qWR3vRb93Wlsy3bRxpd6jExlFs3MZeMPYsXGqRYwNxJwZ9JSBmDP1KobXCs4K2r%2Bp2riR8C6lV%2FPZ3Os3KjW3n1kJAV5KuH5jqzSkGv9la7mQxlMtkK%2BqX3wyICwPHx3p36%2Byp4bOY9iBg7LrBFGCc%2Bg8h4KayyyjMIBYN40jM2eFPSGOof%2FlzLYabXFmMwsoqa0wY6pgEi%2FqclTL%2FYBafvKvuxcXJKeZxRS0szg9lCs%2BB1GuZPZEfaKNPAd3vKOpCmFOZnuoUVe29FvybcpB%2BhODpdmcQTzY8dYpnS34KCJqp8QBXwi%2BGe8YBrQIU%2Fhs685QUMnRLaf%2F9n0MCfVB4GmcCm1TJhOk26f4hEwdHrTHrDvTg9%2FQu48x7y0ToOAN7u2A3azY80E%2F0HGZKInQe%2FVLLSuOO6GGLaPXgF&X-Amz-Signature=dc418be70b8428214ace21dd5371436f36b4a86a8931261439a0e22cbdec7728&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
