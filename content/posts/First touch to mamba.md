---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466544ZFSN6%2F20260728%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260728T190344Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAZEVybd7muK7gnr6ETz6jcwiDWX1Q3bDmA%2FiPhd6fFFAiEAp%2F%2BGCI%2BO%2BjpO13n0wHn4tH4ev0MeZF9aBXZiHv%2FfaUkq%2FwMIaxAAGgw2Mzc0MjMxODM4MDUiDIxK%2FvQdBOWR9iERBSrcA5doEd%2B6uB3kmhpEyO%2BRww%2FVN%2Fm81V6TqHVG0QYfd1sU6Z0VTU%2B9EUf2uaneGVj%2FEMGmxZjuVV%2B9tztsjjbgrPoXrT3Qns%2FWhVLB%2FlZRpegbChA8ZC6Qgjqw1jw6dJVRQAD6eqPSFoDBcNlYjkXDBirXPbCfJ4r3A6yTTuZWlIV5%2BNCdtN2Ud4qLzk0ceMAd8UtZ2StxFZ2Qa1%2BOEsgARtK174NtHhuNpgzwzLyI61c4KcfF9nGnB%2Bj6pevaH3fxmaZrgyQLkdi4YeNS2TaUBB%2BavPg2YFBLi1lmBVNYsa7w4MBaw8lZ1UB56dTfS6Kq%2Fw5jnHpEC5%2Bl%2FraSzhVIYsTL0o1Tjxxa6nMGBMDWsDWgtQZuzkR431uDb0khk75LBeivAmmEkYEcpvwPYzXXvqR31hHuP9fPGGLksg%2FUqLaMOyU1GrdFFJEG5rcrtf4vHUPBvmHUSs6BMkcH2LNOt3NYpwuDpn2Pa7uqt5W1vZKuVYouEl0yq7kj29RFrmfWMyo1jwY%2F9pmfL2YMV%2FAB3cAmoRZXDOrQ%2FZaw%2FG3wiAWdUzVDUwHFtH74jjk8xO43HRA5gdpVHrV9L2iPdEAf0tondKlbBkH2YTETTtqPFnXFhwC51Cv1rz7BqncvMNLeo9MGOqUBAspEUsScVhEb%2F2LJFmluoBSFbdllSsMm8gisgkjdK4nE3XWwxDSeOV%2BvyqaimH5HuCAuGIehBKN%2FPWCsIm%2BYke%2BhUffk2xe92t7fOukuCVmTzy%2BKtEd%2FZ9fN6eXAz%2BHGdT8mcxSW%2B1VAvhjBFickXw4yk03OlNqNhOOuCnAFhiUo8d5PIwVtgke2c4tageLhDAH2yKm0ouQ0aTIzt%2BfDmIXvJDCT&X-Amz-Signature=509570383fc28ec3ed130f74d69551c8b3f298fd1e0cc1b6725acaa45b756c1b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
