---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WHG3SF7E%2F20260801%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260801T145231Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICWGmWriLAq3iz0X656jV3mIk5cLLeIllJeN%2F3Gx7FVmAiEA7IAymPOPMRb2pGQ7RWMft8dECLJ%2FHQmfyECq2JcZGS0qiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGeRAtxghq71CXGnuircA31sViMFf8%2FPf4HuI8qUiv2GlfZALyYLEPvlOdMi9pEaFwazgAlhY%2F1ZVWOwGsfLwYMWOdW3ocZ%2B%2FA20HBu%2FPWtiJKgQ00Orxb%2FFe9ePHapoYRQAXY6wCeOxYLjdsk46JzdHYBcbR7qyzUmmD8hAE4jE4PSgtAA9oWnB7H3Bm9UOkyM0lxKwZN7pC2rVkeUouFThYHSUgzhpJjH9JOnKVD0r57kTSsPWeTqcrKDAmEvcCRafpOnkY8%2BluHVCKL%2BoGNe4A1YkEsTxEQe6EtI%2BfY95ih0UunKZso3xT3OtcYrAQpz1p0NjAhht14PCzPkyTN3D%2BlgGbEfiy9B%2FhM0UvkP9Jm11UBrN1pjgU9eyZbp%2FJREFTNfugU1CfC4gRn1RUGPlPszmW50ZiMhmFB4%2Btk5qEVqtOJLLI%2B6oAns6%2FsxYBKT8grmZqrdNxO%2FI3aAvIRZ37G8XT4WncL7bLVHEGNsucxmSXJV7mA4WT4nd0%2B7AMKQSY9UhNCsVr6GOo05gshxstzUPCfN8y21Q27btM7UXM%2BgtgX6PthbKCCMgrhGL40W8NjQ1ujiJj3b3ZMlvN9%2BA336ResJtWWRFWZN4F%2FnWv%2FQz%2BPN8JbIYp7KbL59yJwdnr6IBqtEa3rGBMN%2F2ttMGOqUBGaja5MqptOwuEQ%2B%2F8b07Vpc7E%2BdSQqQRZYEMS%2FOb4C02pecNQJArQ82iPB64V8rqGd1lnli85COMSEnqGwZiDCMrw7%2BR5XUFA7YhhZyVhzfjVd1xsg4%2FQqGoeb1dejdLGB0bVw2Y8%2FS0UASOBMAhnGHCLiFplImH0wF8sx0QYwE8SS%2Bn8nsqzCRDDxffwD%2Bb1Pp102JG34gTPHXiZ3bhH68%2BIFS5&X-Amz-Signature=1c00c82d086a00a4f639bb5edff6256c98b68d95fff69ab9be6a6c17bc31d992&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
