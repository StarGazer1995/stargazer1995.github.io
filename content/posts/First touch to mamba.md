---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46673ZFNWXR%2F20260520%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260520T073540Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB8aCXVzLXdlc3QtMiJHMEUCIAsxSCiOrZ%2FTtMmzJ8mSO1WHWZbUHxFV0DshZUDES0vDAiEA2xvgAbrZAHuLGtvYnPUQ0wN9JXTOlORbhC9HC9FkY8gqiAQI6P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDFmnIEg0qC7mwK5lCrcA04qL%2BFIUn5WOQpx%2FCN%2Fw0%2FTA3Er%2FO5R2x62D31tAKSulslqBwDk8EytrGk8uwVDZTaOchRJRLz83%2Fgh%2Fw%2Bp5PYhiO0kcVrKcIMP%2FprLY70l253gcmrzWz1EMk8YKLNaWRrwb85qIhg3u%2BJZvbrErmWN2Yv%2BHdb1fSTV7AytTFnKvgpEjxH27X4Dy0VvyAlfSeF9lmegvZwCuP%2B8UWdN0y0sT18%2FA4%2BKOe65CtU%2BEvJn%2BOdUJXwjmNhMMQRgleWtpf1ekCZK2A5lThUJqVf09WsLkfgWuRRl1tmPDpJpkbOT7Vx2N%2BNhgxx%2BFl9%2Bf%2FOzPZPturiagkQLRa97mMaghaBRnrEnopv3p1cQKOoFFeuokl7RveT4RxGxLyH0yAezXf09Giu6cG%2FfuM5GsLRwF6hrkVSa4OZOZDsVWhf2bG%2Fu%2FP1ab%2FGeASjbmvHUUz0vatOhF5VZ7i9WP77v2AzwVskVxkyhsgKBGFoFb5fF9GCngkuq5K%2BeiGYklJ8cI%2FFe3yvL1dW8HJ%2B3aD7MvNnNIyHtHw%2FTG8UizP4kKiW%2BUYPpglej3Ky2vsVh%2BRcRgxbtZeYt8hs0TcxzJlSmBmQZ2pFYOG%2F9QY%2BpkBiGbygORAambDzNLJ9dkVUgBtxfMNmrtdAGOqUBjfiJAdzDmallqDobBVQ9DRUbKFzrNocApJq%2BGeGTHcxxscLBtpe2Ik%2B%2BBlENis3j6KYl6nTpqxWIjGBqe4czUK%2BaoGbtWtmMfXqmstc8bD9W44ellMzTNUuX5BzcxL5JO7Tiw7rCixZHpLR9Sne0mfrP0yD04v9ijzrmRaj%2B5nRzkmyY7c3fcKwstIf9EfBFTr9OfpmqCFAFToWgLzpPhv3Lbyqc&X-Amz-Signature=b00b1b950f50228cda66d13a3a718f778dd04314cd46c1eece4cdf71aff3b848&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
