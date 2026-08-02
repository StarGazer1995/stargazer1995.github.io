---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VKQEAYYG%2F20260802%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260802T012744Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJHMEUCIQCUOknIcOuCcgCka5pw4ZMonxY4PdvumlgtW7gPNLSQvAIgJEgJsQABJfup%2F32nx3zix99ApRTPR8q3a7ZNj95eoBsqiAQIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDFgzlMrWSZdFgHNzircA6rFDH5W%2FLajiAxMxGH%2B1yLmbbutJIW%2FT6eg8mEPDZAAK6ViRZlhgaF50WD3467HjMJnLefv0eczqVNGm4V%2Fb2t0K1lN1kygnDrEBitgZrJe70UJhE0GFPD7z93AKs1JEjsaowQ0JLLW38crcjOQ%2BL709vXp25FNHs9sUgBZm%2FLFA41m0Xm%2Br%2F8kcjiHrTKBe2naBLgAqvueP1spLDdCtM4OBnahiuYyrcnCpJkeFd3SQQpPAhuo58xY7cL1%2F5RmBLcN8MgBO98n7%2Bu%2BbdiVaGZC%2FdwHqNkUAEt%2FvIvq2vAcR2l4Ldt33EoNELduWUG2xowP%2FMDKIkA%2FXfP%2BSoF6pjQooJ3%2B6n2sXj50JSoo6znBPTk3FZ8HScD1M0u3Y6Wgj%2Fc3SfZ8kAd1NyNZjNfxgfRZM5huZmG0mSkplcAUBIgVwtUOaUB4ddOvoTDefYKxIBDGHf4M8HQlFDDHsMRO2wg8%2F3QREYGW2Yo%2BpIthyKVf2AvF39WRWxNRcmil9NwW0CoffVKlL4J9GwAICJ0BcvRDviLr2471VGq%2BaxwQAXcpWgwh0esdMyrJVh%2Bz4voN3g%2FPW6S3LeIHYcRur2dgkEMILoOrkqXZTwwZMdx89G8faDsN2XSx1PKXNGLYMJnQudMGOqUBT778ZnBFz8HHmfQwD5q81Bf5HpBDNg%2ByRMjAFMHZCqlnb5TjaF%2Bb%2BfrPsNAsexosIPNJttJ7gf%2BBwCTtzoQhCgpDjhrjQ5xvNcbcUfb4ytx0rPvSxLDeRRnCAzOuvkXDNQJtWxqmnUq0qzgMc5QpKFNFs0dhfaNtw9PjJwLucCuyJY3%2BjMeRnoBILcyQQPihg0yj9Ra%2F08ZHMtFCWRawoL6G6qin&X-Amz-Signature=ab1ff8a40193d10209455fa8adf82de63d09771e2d585101593e03e7b37e09da&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
