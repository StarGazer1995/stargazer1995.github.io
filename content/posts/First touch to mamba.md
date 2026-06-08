---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z52BVQMA%2F20260608%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260608T135846Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICnnw63%2FbVrNY3UHJJuGPLcSzjdQmbEVIvMDcL55j%2F29AiEAkbKuS9XRPF4zTaBifICBGt6HXje4AgkCva40TPGkrLcqiAQItf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKBJ22Bv7NXrkN1%2BXircAy8JBmjMhMLZUgZ%2BDXNQUAlf5xxiNSZKC5pPBbAjKM9vnWiEmfgPsWkb0NXHdBwtl8HwKbn%2BYIpR0Qp3R6f7qmE%2FzgWUDFsm%2FBwbV4iCTqEJLLgdAH4HG5JrNiflZ55ELPL2Evh6SL8FbtvTFNKjehZFMCeueE%2FJWeEXNiL%2BFJchF2yg8baz59r1c5BbJ%2BStFKFKF5e%2FKKRYFhXU8drjzyrV6SGz7zUBFMMCuTmcBbrsMJ6tKB4XOvPpJNLxr1SoJULMkPTbx9WdocIB2WRclyaCqq%2FUvz1rG5CLzp5ajImtMOYDEn4jzME1qs%2F9NrjfdvXEsqspUA%2BJuvQ1tIWve1tVACII6dKT6r2dikbRza6%2B5a4Biyt4BsWdcBpQ13nwGkrKR5CORJizlHXe3coUiNao%2F6oZ2jmgLFIFa6qJTAHKSkyzBwOChFJP14utu3Kn067aGR24ZeAUzE%2FP3EJZH2WJWVubDHqSTIRa7F9Q%2F3sPFirA7y1TLTesOxF9tBB94gQf9z3%2BQOkmlCmwxcMKXdKDILzjIPvWtwVti%2FDTm%2BkP5O%2B8vaZkSyhNuWAkQszqd74Z%2BPLuEesaejFvicyo328hGCdAFiZ2c7zx8MFX6nckyBpPfkbPaRYfFS0gMNXWmtEGOqUBFQcF1Y0Wc%2BeHZjq0xL9i1WwehqoVmgDA5%2BzOdmihVaLpbRhPKQ3f7oQHXrhl2pfRbMrhvEPrZPulJCFBIiocXyR%2BIHJhZOmi6NgBrUdG%2FGKlASGzBLKmgu4ScQ0YESjpeOiieI%2BAAfY7xBdFQeJQSoVKerMztN3DjoWqY2%2F%2F6Z9HTI1eV7QpbG4K%2FGoLbf6rdqvclcI6Ab%2FaMNajkH2ANTFdP%2FSR&X-Amz-Signature=06ce54aaa9c23f7ab67bd970b41972ca2fd42fd31b86f7f06a48fc62d0941870&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
