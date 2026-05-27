---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466723GRVH5%2F20260527%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260527T075619Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGRZiu5CGH5pM2CHw4hlicrZEvCraJOZpFX08itCS2HDAiBDLzQwCw9ReMmLv7iFQ9q1BOYzjUc0oyfDu%2FbkOjo1pyqIBAiR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMzZUd8GAGpd4TfxDvKtwDfBA1angsj%2FD4%2BzGI6OHRRzujIN0eZt8mBodURZNpCRk928lLHJhEDHH%2FpAbpkKmYTGTv55TslueZNALND9neuSTXR4TAF4CesKD4T6RSGPcXRP7bDgrF6Iagr7nX%2FPbG2%2Bt2crKbANzl0LBKKyFdpwGxoW6oRDzth6tSve1C9jGKHLdqKOkJMo1avhky2clKvGXrYLEmQ77hLcKYZ3qdSG8uc5mMN%2B2KIUMMEkrdlNO0GKvDumaRdSdxAnrfNX0xuNcnDXMcbpUZCJnCtiQhUedb5sxPLCQCj1U7te9Fj61HrA7hL11UcwCSUIlDHAzGn3kkR4am9Zloyb2X8BdDpuk8nAH1teluV0Y%2Fg27%2BsDpM880KZVie0ui0AFvL%2Fwq4WH4b%2FfoBwvqcFviy5LpUzVQBnn6cKWYGddn4GoKqtsH1jztCcpJoPKi%2BBbayskzma9y3Y3nCvCw0MlHVy7KfJOVdELmKZMfu62D4yCDhacsqiZvDCVziKgqcvqlmrZKD6ItTCy9E5EwVRGuNOUhxEdCv28ZrD7HVSkixm8TjLeUm6FLwEN5BoyUU2E%2BEnNoWPINg1NoZPZ%2FNMd4NRGC6mFuDvhNDUItbANKGsCxd%2B2cLNzGTj8L4U6rUReUwgrra0AY6pgGeGVde0F%2FEz7jBoHzzrCfNgha5DeW4PmXXiwz5KCUGDp%2BlGdRL877k4MOr8b7OmGAWSz5dZiFELtiDwethlhMHMIRlhgf2AQzGeDuNx1X39QfxG2ZVMjIQyv0wgMEpBRQGFkv2609JiNgkLolVXsP6OnsFbuv0RkZBQFPgm5wDxgDtJdBlRBDDvFMJkp7SPRj0uMZyKNX2VUxIUnULEd5FhpGlnUeA&X-Amz-Signature=d6ef9916cb54a9409f646c8e2ac961df310a6c65f3a0e2744768b432d8119d6f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
