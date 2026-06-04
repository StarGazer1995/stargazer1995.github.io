---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QOG6NDSR%2F20260604%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260604T023145Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDdWyq4noA%2BzC%2FDDkUm610CSDd1PsP4x0ET2tV7S%2FTfGwIhAMl7k8FYnFYEOsJpVhij%2BOMFQJrHuQLMZX0Z4jpCQoxGKv8DCEsQABoMNjM3NDIzMTgzODA1Igxc2V9K4kSHtWkd%2Bb4q3APJ2gREeDgkorabKla0O%2B3U%2FqAmemSlTgwHhH1cZCQsdvCABL%2B1s9%2BRltMON4u2ANfpvuONZcssbc2O3HVYv4BdcR3VhUMgvAS0f6%2FaEvv4AiruRHdEBO8mhzmeSscPxef537pkwbv7n0QlIi1GXYtKJJgchDZ24hsCBhdqyS49dI5GJ55iFRuyAaenMhSAN2E%2FVq0MNaRqpkeLK18obaXCz0p9xqbq2kybHcdR%2Bc5Kg5jUYtFjstLEel0KqFPY5TxhFpOOzGVbEIVkI5%2Bty%2Byel%2FCxW0kJ%2BmgInj9DJ6Geb1nbn3xMvZjIRYBNjwehsAOTR0r8vCUi2wWlRVTzVq%2BSIcMSlhTs%2BjhItADpxxrerqynrJYCp7LN4pH564wv0jip5AYuYuUTa9BUl%2FAfnTVOmd92%2B9hCBdQtw0HimRUBvSpndJmQAEAZAjBpPr2XyZcz1zJwXTSwTtiWHXjhw3iDhLrBeXK%2FVoYx%2F7WhrWC6w1oBJMNvUg2BTWInF%2Bp1TpwFRHpknxxrUBFYDWjp6D6QzKUYLLJBhWBQDjGyHtGAauHLjwvhPbliO5s3KO00p7SFhhzh75vxM1RTG1ugmAeE4FzC5DuaVknVzbRy%2Bt0gLNZPW%2FcSKbqWnBDVEzCOroPRBjqkAWXt%2F36tusA9ewfZgiNtih2XGGMr1Q%2FMPEaR5lDqy5wXo7mbNBNcy%2BtZvNVyHRAN%2B6VM%2F2U0frhDd90QU4fPp8tXNH2oNFnk%2Bzgtla3w3eAlcPLduKcpePGVzXTqz2XR8xkJzgg1yOtewKIg3k6cy9DMG6WJOhu8C2TGwd%2BxbYhCLgX1OpS%2FAmm7H9Wp8Kqd1q4ClxvJP0aWn%2Bz0%2FQ8h8oozez4l&X-Amz-Signature=d56211c056a6da9295a7a19c134b074ddc2b10e8c51d9d89cb3fe245eb8ff6ee&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
