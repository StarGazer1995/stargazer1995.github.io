---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WKY4OCXR%2F20260513%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260513T211624Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEcr0ZMlJxsPlJzWQko2diEsvgI80J%2B6NJHcAiaa9dA%2FAiBNRvC1X4zVocRkwng67VUxb0h5yZlAF9oEzeCUFNOlhyr%2FAwhNEAAaDDYzNzQyMzE4MzgwNSIMBK0jorzEKXIt5KOaKtwDqKDh5gdVFTGVpBhcO%2BpS4yzdyGQ%2FjeuspKvxLmUqDnNAXpk2aq6z4qAqcbRTk5VcHA4hSThaPSsTM83NVxJaT3gcdcTjtSf3l0YFFf7UvMJ7xFsHy%2BT%2B7Li4yZOFebYICgqyp9LxUscrkaWaaEgwJOSXalZYCuCTbc9mPqG%2BB4hYLw2uz3aVvmiA4WnQypakVCsrSIyizKVW%2FujruW%2B6J7sG0Hb8QQcv%2BuRaKwRz0c4SlZvO5rxsa14d3zxDTzKSbv%2B7OrVuvLWbVl9MHyU92XaCWdf3DP%2FcWWhKWtrAod7VTJG6c04p0aJ7ELcdUWx5WI4FkcrFctzgI5L%2BpgvNxn4fOudtZgvb%2BSOChEgFYLv31Uc6eAL4dCVEE2VnP8u2TNBMxKoZUgKKpAVtiUUsUZYErRslndJVH7hKAkPXEdHTyzqNDav26F21O1fTbWxPpm8QMk7aHUjCUvyPX31OkPLNQ4PweDvHYfqHg0Yz0FVnTHoh67PBckb1bNqz7xjXQHi6eVwLqbCMfL3uOQMi00QVhmTsELjDdIXzer29mXdPg89PAx7Wwj4KyO%2FQRmolJqD8o3ReqjNb7Gaztm55D%2Bl4Yb7IVnjfoTKOHjMk8uxyxD%2B%2BfBEppIL4FUYwnauT0AY6pgGbGc0N6wvendqTFikzqNvaalLMym9Dw45JPnJY2juO6Lq12VqoPYPKa3dSBqSCzFaL0Eu0ad%2BqGlTE83HVJTEgKhy%2FulduPTGUqhHTBqvowLODNz%2FQZbx0Z73Ur4JeK8xgMEsfSoi3kTCaJUnFsatEiYtZXnckacH%2F3ZHzEexViuRmZF8K8Z2FzLoXzVSUZLosxc4laP5b0Ui204oBxVVhB4jwfba2&X-Amz-Signature=8546cba060407ccd49c784fd99e00dc2f7e8964e44f01f5f71f5698f2c16bfb7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
