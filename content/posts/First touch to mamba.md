---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663OABHGTV%2F20260619%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260619T224336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGMGyUvbCIaL0GFClj0rY43eFrJUzoeBll64DWWgpV6MAiEAsgHFcyCVR2MJneouqjSlGgjpnE0Ajw3qIsTV4AMK0lUqiAQIyP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDM2K7CE3r7LgFVCMWircA6qxBH%2BXssZmrcgblmnC9L7ciY%2BfY2xi5paPkAwpA0kFpDLb3ygzHci3ytgqr9GeW2a1VtHWcOyV686RXFlfpcwGzqDKk59T4almggStq8KlbARwhZjInyZ%2B1dC2zbUy0BeB5w76lgvpXveTFfTg3iDF8S3VMG1sXCwzPvo0ElrPokBNoonOp%2FT9VsENGDDzKeIz5OQqDBwTtPrdZVRCLHEDpM9Y6CYmHWbaQauhU0QSe5tAiH0C2ujFtBlqGQFzVpr5BIefQ%2BF%2FMw3NzKJCvPiDBwexGY%2BqE9wGoWVXv6lY9meHZQrJVBM5%2F5HdNKD0dW4gxCNA6fsjxiZrV0hsxWLZxGkkRlKTm0Kb%2BCKpFqAGebfdBLjKU9xtNlSCNwe5tEfUJUH2XcVZd5xKBbuZtKm1c8NwiI7bdnBiTSENK9MDTXgJlTLAoGJlNaEX0NxujOoXRdubWWdnGAouP%2BpCqF8jGOyJzyl0KnqrSIoMoZyHsGIp4Q5nAqVBR6qe7E1F7WggnjRYjKGAHdu%2FJSXwUjnryljYjuFZW%2Fdk4j7x5vD%2BnhiNkFccBkhTV5mxHqAQBOjzbbEZcxZdvLq4%2FpcmnhaRWn1%2FC%2FVF0aGtpIBLkY4SPDxIWJpsShFBb0xlMI2H19EGOqUBV6m0PYtOZxGwgSfG2KR7kWKB%2BkkAFbxvis9yXiBuebY0NsLdQxD8UKyfEtEz%2FRvlhhkY3kTClgl1RgPu8giS5BKk4kJCyZWmkZa0Zvz35FX%2B3XNX%2FIGgLtCrbCZYTtp92iLkwgzOS%2Bl04zPoeGKsFGqUAAl7j9wlMK43gLBsrYZ66K5FxYvs2HUd4Ag9X%2B8T11d%2FxgqWx9FKOR4DPWb5wclMRS1S&X-Amz-Signature=9e1202d9f71fe04a80e95e3275514c31fc84f648b8e51bcaa8df555982fbfc19&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
