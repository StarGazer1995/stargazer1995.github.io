---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VV3BTNB7%2F20260526%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260526T015819Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCm3XhjMGK2qDBTA165RAj3x4gEFGHiM14cMCxzYdMPWgIgBbXLe3gtZCwVZvMo6iHUKDdvZVHcjQw3Ue6sJAwsRFAq%2FwMIcxAAGgw2Mzc0MjMxODM4MDUiDMUSfeQ3aY1F%2Fn9IUCrcA3bBxstaJcyPq5%2FcxcY2xmsjOx4yC%2F9ksNd8BFiAfCX7oUC3C2aFqoqqXzvNdpKzl9L9XY1AA2aH2MVBYgUjXAVAVgbgJNgduQs6MtsIrmg%2BNTN0VTFbwgzYxYRMHeycuD3zT5XLUHaOqipukbjRP4Uog5Wxyu99X3P2Ri1R1QZ4uSjXI6WpDo6ZwuFfMsHewokH%2Bw8oTXSM5HMKgsaQIH9kR1EGm3TNo5fh7H4IKzrfc9dv8zKIN%2BT7I6XqsvITJdglotwG7%2BJzicpX8C7pv27GPFVzgjJneFMvUOhl4sZCDpIOBFZ7NJF2Cr%2B5SIMH%2FvqTxfI%2BzfyTqQfst5HrF%2BQXOyEntzIUcx7HVIhe9x59lH3Ph0rmCaJeKOHm83t18mIBMeE11S3PN1MfZdzeF05Beh24yRg9zxw3gWcIQnNDFluZS5ZpT3KfeZ5kemHKk1RLz%2BVD1ZfUUsxJotgGfVnSbd14P%2FEzYllnVKUlmjWVnofEmkwOkzMmRgOGJqCJE64IK5PiAU2sdt0WVPokkGkNUHK7fI8t3zKBKCdRI3VJzHg2EjEUCe1kfvaBBrKi1VTogjFlVS0nDMckjHJC5qVUHR%2Bx4UwLXtvm7uifW8nzN4jrbsC4Aa2V5GSaMKj509AGOqUBcmD9COfgyuOMlK%2BCf3uBnsxqNZND55QOGIqgf2pG5goNWSVs%2FYPYSpLwculSWXqBqFVcwj8q9K%2FE%2F82PltixHZhR86uybLd%2FfVymay%2Bywf4JoO%2FtQ02zngfE5d5XiAtd1BnKFK8FXFFak9Y0aEXxddkwOrcdvpqVpTgfREtcFrtgOdIIlT5%2FQ69h2X8JCJoNECV1DuGlMueCgFUWBUG33A7Ec%2BJW&X-Amz-Signature=42c006ec7942d20e56635b1bbf2927b923073eac0e8208756d91813db951ab22&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
