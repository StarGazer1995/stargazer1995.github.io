---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UAAHAJZ7%2F20260802%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260802T095913Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJIMEYCIQDIhCWUDpucLuoOuDNe8K6n7Xc4XqNUBIbkO66K83LOkwIhANqSGbDiWLIf1BBf%2ByDZ6yK5NVrFOcIVgfMfQ%2F2Ot2C5KogECNn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzHwIMgm0j133vDtd8q3AOBxmsIqXNobyLlOUvCR08oR%2FKeEYLeoVR45RH7nNkAuP66cRb0nJK1LN8P%2BBBiE2OavkzE8aWBscC70TEch4a18hlmdXkTYASCJp4oy%2FMylrDXVtZTS%2BWFzJ3vVfyfRh8hZsHsFq6VYafYKEtvKYamn35f65llZBCGrcY9VBjjyQOJqrlChLcjzrVJ9EQoAX35F%2F7mkEca%2FqVWhD%2B9FfH0qsNEbagiNXY%2FVlseaTOTi%2BOrdpx7lRespr8JPp7Ic%2FzmCEaqrR81fOT6MToDR6kUkakhnpFzyjkidVnLCos18Ic1xRBYCTojpCAu%2FnKKwdEzZMbmbgNRrwyHF0ytHwyDG7SLxvGqMe%2FR7Zd2LT3RCwyeuzpgvHhik6n8%2FZXkeLdiGyzhRTE6F6N8w8XnyfKlW%2B%2Bpcly51H9teDgxe88%2Fr0SRoSICqHF0%2BwFDBIC9IowXTLY4UeKb82ucC7ItpmZXO7wHWj47ClLDCVxCfwqzdEkUDCer%2FYEXXgxksp5qKdxeLr00B%2FabSPgk9m%2BXhF2IW7cqlucrm%2BUOml59GmTu7YIc6BdiSjqIK8F5iaWlwwFYoVGcokBMQcYODhdQsJTEGkvZ7VPG2uXQ4QwNZwMTAgqduR57n8416PdM9jC08LvTBjqkAf3MZ6vwfPwwnPZ%2Bylj1e0ykE5NE6Ls3ZCk%2FBaWPfHxBeU0UEubnPh6MIAZ%2FDfa%2FIRYplfelI2NMJ8N85ZEKdTHN0leSC%2FKzIN6wAwTX9xYQziQ9BlFCyWbEFZTxnPVpeBQeFDxWI526Ep55L2Nbcobb6EkD9WqwGADp28%2BgH8aVoSkcNzWSqyTYVvIdngHNnscqaG6CuV8w9RdKY%2BRxpvI3N9eS&X-Amz-Signature=bef1ed4b690c3fb8ef0fe68d909ba3e187d5d32a5e576c149c9f9e79075042cc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
