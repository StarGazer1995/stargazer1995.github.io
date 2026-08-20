---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XSE7NQLR%2F20260820%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260820T024759Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDOTKEqsQhQC8f6E9NDklpQlV7wK5eBhlwZBq3rp0%2BYugIhAKH7E9s3wSDAmZv488w68OuMKiuR8esvqjWW306S%2FJARKogECID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxaDep5tWa0XNI%2FNzIq3AMLSX%2BmFbRqpR3bhqNEOTlSnUH9alJrhTP6IabannIMwne%2FWbk282979QFvAI5rH8rWmh5SNy310IfTs85vbDt5Q9QOSft8Hy9GlnuocLoKRMb8FzQ8qxZTFe%2B0CzNA6TJktmo%2BJ9EhcZG4i6sxBNrnKXe71%2BMThztMpBSNLNuYY2E5BcOzWC8%2B2d9pV5Ezt3%2FI53FA1wRMI7ZT64iokVa3kN9coAJo8wZuitO4PHmhq41afEm6TdFZhE18UWojz1LzlMd06a0EtpqFQl9gyEv3gqy4vZFC9paLALf6X1Zn1R3M59yUrto9QeWYWoRhp8927ZbBg%2FkT%2FWGhhVUA1k5IS8RWkyMV0EFCmxm2OOonWVsw5jtdDDTY9gWram2s9WANrD%2BTNQ3tWjMgKWLtg6ptfhNLfWxFsLFXXH9C%2FKUJxCxnlKaCsHrLtZIvrYn8yMnvQuaAaVSO%2FIFTNWv2KxI5xbOiZtIahVN9ZhWdGyrVDGACJw5DGseFOi0iFpgagIV6pd3xv1IycQ%2BbHbmQrCjLsXa2I%2FsJISRf1dm4hpMBqbKhP1l1zT6OR9pCTvgZ8NsZbF45l2i%2BQHp1ySz9EDh40cfuVs5OzhkiFMNm6ilnPW0VmlyTbQ7YVFvG5zDX7pjUBjqkAal5cwK7r6MZPxuvCMTLErMeonQPqhvxEqb%2B9MA73aqqbLsFtmaCwwrekk2cbg%2Fe6GLZMcUvmnB347H5L%2B1W77fSOWR%2FvYeN6tZ99X11NJEnIzmWDKG43zMP7Kbp1dFKORu%2F1oQlfL7yTQHVpK%2BaHwzAPoU%2BX1oC8kWF%2BUa4RExOShmU76xlWm9Y5Z8mXD82wO8vOyUgBfN4PDaCMjIANq3Ndv5T&X-Amz-Signature=afe01dcab606e5779cac68a8c8a4108c5e1df3f9e54f4c3185ff50723dd1e4cb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
