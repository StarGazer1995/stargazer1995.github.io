---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663KTB6XMK%2F20260822%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260822T003321Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCq7SUsyJK8uXxX6AEe2qEAWpECwuxwUAqdRq5ksLt%2F1QIgKXXxHKyune9KRNkfG5cU52kH4WXtdx84cozucDPN8ZYqiAQIsf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDP5tSOOpztBfKXus%2FyrcA1BcubyUuaxqY%2BsnrceRDQpDe7Ds9hLtbg9KPt84nDKP0vX0HSAXW0StysiV95nSU8K7X%2Bkpb45O%2BpIia7d%2B51Q5GPY66BX9KcqETptqzJLTdapgzfl%2FfN9NQanv5WOvlnD%2BPn3IxOkl8WyjPtpgaJUryv7WbBFCmPah1gSeGhAOSmo4AlInBirZ679MOEcI9z8vCnPsi7pANzpJAfHG7j%2FjqINwmfTeDr%2FD6N2gkaQ1b3P6m3gJQpYalwh7joX%2BGQ%2FshXxIRXHu2FzxjTxcNwnynE6vzhwi%2B60OrruFEK0GdCRo9LJTPs06MShTQrIh4O%2Bun%2FdErk9q3MCmjxV9SDHnm24cRGjtfNo%2Fsn1iJI1m4I%2FQMOw1shmqRg3Q6%2FrX8YawppbCLy7%2BFqbprsKsDdzeDeFHij6rTdjkc4boY1OjL5BCti4qYAn%2FgTXYFZt%2B8q5ozzJFEnaMbwRR19VD7%2F3g5Mz5lxv0v3Ktmn5GcBYB0dJGxmY0hyMfMNhoSubNRPMqT2ekysbrl%2FijriuEO0W7fUegGRDMY2ZpRG5KsV2eEvsNwZLZAXWfmAiQ593m%2FxUVIIdWSFYb61Ho846%2FJBeSOwDko%2Fxd31gEhdQrNtaTJ2Snx02iHsqvbh9TMKnFo9QGOqUBXRL8KJ1p18JaW2CfygCu8sCk1%2BJaDFmJ1RFi9lOeS0GzRHy7mT3EKX2DZ6x4tZVPt8h1rrtzQnZwVYNJYvCihZGNkscy%2FfUwKli0N83bWWLp1W7IYAiNVT2fwLe3yYT4XcWeAF%2Bz4B%2FvvxVBoKCcOGl6ejTpWvfLnp3gAYFJacRKS8%2FA%2FKkoJd%2B6GsodeqiGJWlkaLBIEPSKCd5ZucsdJJ7rMwpB&X-Amz-Signature=b92af4ea07c9b5e0a5a7ae133a276a998804fe830aeec04bca6becee284fea97&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
