---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466633S2W7U%2F20260714%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260714T185945Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFIaCXVzLXdlc3QtMiJHMEUCIQDuD4pIs41TeJ7VOrNNZVyEQYjHfnc8vOwuyEMFjJ%2F4XgIgSpvp15KWKcZPkh93H3DNRBaE2sDFUsEGwj7Ak7mK%2Fzcq%2FwMIGxAAGgw2Mzc0MjMxODM4MDUiDHZRRCnMJS%2FnprPs9yrcA7sKF1oh6umlbGIc1TuvJq8LAJfVc%2B%2FTuwNJ%2F7Uozjhir%2Fvbxc23kXBFD7OtfSsC9Rk4FBmhuseAPwRBvUj9GYKEK9hE2Tx4VDYVHkMsaSlFfxKWZGNOiN6xDkXDuGLRKChX%2BfVQarPOwM7dpr%2FibTNWcp1Ki7YmHolc5Fsbar5SIEisDpDJHhk7bhCBcD%2B1pT4XrNEkGfzM2whfv1ntfljKSHvES%2BMgWYzGZ5rqM7oDhgtKlDXWY1A%2BGlfLoJlfvifWA8WJSNTlLq6QFniMBPdtlqDUWcp9I5Yr80g%2Fh4bZzxScWjUsd227gnabyA16WG2YX0RW%2Bxo%2BLtD1ojRyymiDD%2B%2FKYjLeNw%2FzuE0j65FnN4yitLKSzVIC2oB3yDU5Sx8sjq1IsxFzWjKDPkvjetdg3iNtL8Q46zZ1yJ5P69QKnwK4mWdcZ%2B6qRZDzfQy9%2FEZkoZ1ifwonaC6ef%2FDZPl1Gfc92ZnJUSTl3N3Udy7VPnbLktfF7jVx9eUw6hELJ6vc32qF4qn1xsdUfqpxfj38nLGPVj42ajYzBoWAndW4W83or0uqILDwlkmfJwG0L2HZuV5nv52M1GrBQYVleyCyx9ESmexclehlN0YKLxNhoPoeO4p8H85pSv65MMMXx2dIGOqUBIe2ZFOkpxHJWBkOtHNQZZgoodB%2Fc8hR9vnJO9YpIQP%2BGkJr0sPWc5X3iuBqRWqpMSoEVjVa441lDFa%2BILb%2BWcUGt5kmvusIsVymH2QqRbCLTIKWeF3eLgZheSMggk%2FyY1pxOLh5yTaOdBspO4dBO49eI0AbAyITGnap0%2FfGartFfOhbimjZHbmMUP5mlvwFAT6PA%2BeB5w3ycVeSHK%2FS%2BNdAiqMe7&X-Amz-Signature=1c17b534df38642619e9e288ed7649749e5bad3c402c8a7aaf5ff57215c2e3ca&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
