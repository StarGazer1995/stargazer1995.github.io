---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z4YDSG3X%2F20260816%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260816T121527Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJHMEUCIGwdjAE9M68DMayPWvdU2tlPFXjmtnutWc%2FzcH5zzm%2FxAiEA3UW6Gh3rxbpVktZ3YZjN1%2B71vNScti1E0p8u0hSPfv0q%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDIIEoWnGRwicUuC6zSrcA3G%2BlCVoGhUg9l0UKKl3dAilqEjKC96CNeIpsIa3lLgbRIYcmmfftd8uYBrqrneBS0s8OhVuKiSfgL7hsMowBNSzi7LPbOVIpyIuXqoY%2FPzk9PmR4WglvmwyH7wYwSnv9fNfOW%2BmdvM8nsHZK5KNZrc%2FskzF9ctpU%2B0bfrUBaHy18inB7vaJuUKpJ1MxwejwhxEwLrypEjv%2B0JRBvHVOUlikxbuykJPJIWiAsjbg%2BFvRq6Fp3IcKzHlXxfFbH3gfitQ%2BJhjeGDHaGIyIvnEENgbJcu7%2Fgn1Xnn86JEMRy4m8ujAdbWfbO8dM0XMDtS7eCJ26waFHAsufO0QTjS%2FT0OTpT1IVniS9xdjTBrCimSsGCs6jR5bo9QileCiSa1g%2F1X6pSTR8PROnWNfEX5qaWjeLCTwBG3k5W7PP8KB6OvIY5b68kWLhx%2F28RVlgX%2FnCH%2BBFeTUGDR4TqqLOPxgITtxz15sEz2aGGjrfoquTU%2BXZZbdoKNiO7otDU6ywBsm1uFdeaXiBZFdXAaDo7cT8%2BG3ldvJ9sbA3qTJukdHIkZvV5HjgWtGHqbaoBTjJABl4iXaiDQ0LKqrX2uSmudz1qF5zI%2B5zqYAOX8zVXpDgGkHx4O%2FkxNX6C3brlvQQMKKmhtQGOqUBO1agS6ozQxfRMEPCuynV8ka0s5jfQoC3mlFqNOWFnRFsAMO8R%2F0cxF2vkPIH%2B9f36wrsXTzmVy3Ap5snvccA04PZVFYBpzUG2M9rf9NBrt%2FduS582w%2FWzjPGYkRUklvYXjW3pZEOy%2FilTulV0INbWtFxRrr%2BBppYHoQ6qU39bhwDVpGYpH85x0svRWtUeg2xls1k1wvbxOgLTfalRSoR5Vnej6Yy&X-Amz-Signature=358841d6d7a78c1083e5d25156278044559925f9116299e72a486e37c3a17acd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
