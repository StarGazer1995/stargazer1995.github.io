---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XPG3JASM%2F20260512%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260512T082138Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJGMEQCIEyAtqRUb7s7%2B8bXtB5S661mp2ZRmX8YkslLleKbVXKqAiAzT3iHUeDfxYI4x6z48u1PdboJEhWyrgU7Bwwyqzoucir%2FAwgmEAAaDDYzNzQyMzE4MzgwNSIMru6lH%2BHVAEpIkHqGKtwDKIUUxf1gcn9%2Fjfd0HrQhEHiM5Dhp0f6ii7Vt4FKFXdsnkQvy1vLJt9xFNYUCIJc%2F6nApN1toDpC4WXUkbypuxUMZSlwsBNwdODs6BIezZhXefAUvZAUqe0q9Dc1iUMMM7Ex8SGVWgQSCbYi1deVkRW6FdINXHzT3b5aYISJ6r2x3cjNHxzEb0PJq2jSjGG3kTwmSaEqG2aunbIW8CVMt74HkJITzbsBar2x64EGyKCqM%2FGLQDsoJ7fXG3NG1aDuSDS40kAphZQhLR2zU7PmmYtdFFmHhysAi99YbQhmk5In1mo9OJGY4CJMcRyRKsC4F%2FS2BzohNwVJOAPQFFVNjUpNJmHnsu0WYHeM%2F0JBhgoEN6Qp4dhlKmZkP3qywJSRiNWY2R%2Bp6GelS2ov9Rj395%2FmKL39MozxdqJVRigxy5mw5o%2FLonN6SuaptFAg1mMfkIh7F1WC8f5NiOJJgN1%2FoGNvBaldpaAGdDbW%2BK%2FiuJRXZkkH%2FsI2r3tgRKWNuzkCXJXX1iFNzJ0a7dTiJ99lWibgjRe5JAOlyLvbwbtb2K9C5c%2BJX2VCjdND3uuvD6l4qEQyjKLY6b0hE4w5Zrg2Aq2N6PwV33Nvzq98SeuKZxFUDezW6DvVSbnwxVS8w6u6K0AY6pgGLq6bAmvoDgffagZ8UJOan54%2B2Q1nHNgPpc3BJx4A7EQdWPH%2F8gaZacxjcs03FnXagaAPDrST49PpCL1YeTmTvjktdsdmjpYprw%2FEW8ssyNzUasYlD6eS8bpZMIjhTkoQ1w7RJWnEDhrwhcJDeRAUE5K7%2B40Cw2pkndTHUWApIxYVoPFWY0V5GkJUkmAtBi1RupChPHUYHUq4dey4A%2F%2BhdJH66k5Zi&X-Amz-Signature=89957451924b75f000b147c595e2347a2a9eeb3da9aacacd82314916dd32ccd3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
