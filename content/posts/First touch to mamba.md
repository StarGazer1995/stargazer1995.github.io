---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46665NXDLY2%2F20260703%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260703T155037Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEgaCXVzLXdlc3QtMiJGMEQCIEawN01OG%2FwJViE4afp%2BU7PmDbcz4%2BKRxa0jLQzpRoXSAiAG%2FGjbXdoESiFU5oDeQo3xATC4WDQd3WAX%2BbGMxWOo8Sr%2FAwgREAAaDDYzNzQyMzE4MzgwNSIMGKeHycw6jWvj4%2FjSKtwDlkRNUHc%2FbU61mlvOjHay2dAPqWdVInW8WRHR6tg0U1NZojLqtqqgaHJSJed1t1PIru9nuw3Ak8spVo3n5s7oFRV4gCSPENcJ%2FDgwtvx6AvUmtLLzTU%2FraImInA7Ld9OkXYMy8HFLgkaFj8G%2FzAmV9KEe4J2icLQ2aAOu026Qd5yeenTzc1mwqOj6g6kfZwq1gkdx4eB7FMIHoyA%2Bng2AlcCs5w8RjECiQFWFNxmQmA3DUO1sLr9dlVF52vXPRM8tQbQIQLac1JDLLNWNM56wuCKy3tjyoTCAXQRs4Qj2HriBSQGrdLLNXUr0V0cR4%2BMCAHIn%2Bv4I3mFUz9ecSyD10h9kLjSwnbO4HU315g3ybYQvO%2B2%2BC5f%2B6BCGsHryo%2FZae5J73i2F7TQyRtOtT0wqLgDh3ViTu4fT54jPdafM%2FztK9o8oFrpO17a%2Fc4GOvnlSPvo7VCHSOERN6SZae6VtvI1Ocy8OW1TOPbqh5kCJov4HCxtBJNrO5Oiypeqmm%2FkrIavvnqMumgem1E9v%2BfGpJqxazRtvhiwubYcsLLNFxX6q1iu3EyVR%2F5uXgnGeRss4gaEGZpEtivJOFLuu7U7%2BzPsYqCpFbQc%2BaqeruJNV%2FOn4ze9QrdUtpssCxR0w46yf0gY6pgEdTdd3M9Y2YIWddMOPSHDPtP6g0WhZQWK8pqgcb0sxOOf6FIA1v3E%2BCy84b%2BaWSu7zNhxNxqSpaLI0VHjbQlcZ6bhW8cuHeDqI%2FAQoiFEX%2BRnFQcrDg9Gmls2aP9RUXtMKLXKOkaQFI1CzLV3gqeNx346QqtPlzZQ%2BzNd6a%2Fy9PxxTU46PYrV0lQi2kJgLM2ZIeXJaTPVZC%2FmHkw0FOVewMo%2FrDIq3&X-Amz-Signature=11aaec3aacbd37a77b0b6d76b446627571fdba42920126d52662b4cb28ce1f46&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
