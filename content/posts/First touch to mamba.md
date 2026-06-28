---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663QXZ3MTP%2F20260628%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260628T225308Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEUdYGRHD5GVwP0OfMXAaQUJxkmLdJMzZLDwY1txVT2dAiEAq2O4GGgwCMQa%2BvyZ67TdwXgWXd3jFlta2fSxmBtFwuAqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDApbcKPnPKgHeLFfwSrcA1eA3ep0sM1%2B5os7C87e2aPBCwAPJe%2BUofjvB5716EsiNKiicZPUP7VgNN5iw20ysvy8ixIm8P5gGqzji%2B%2BbTRdWwMVurozrc2RU%2BcUWxbajaqSaZcSm2vqBH4xlEi0m3c00%2FfcHOFxA8U6pah1MkHR5eErLtI%2FMn7QzR2uEQFGGSSiosLG1Qzhj2OrqiL0XX5Bvogn45SsDbetG1mmZ2y0qRYjn6obWyc90hIDBCCgnh4JGjuub%2Fhg3AepMT0RCg2N1asx1oazjvVufhlyM%2FDBEA%2FA1odyHxXHgjG9JO7lxrsnsHrQ250V9%2FygqDk8FCJdml%2BmV273QEGQefTFrpx4GXzeW9RC%2FaakgwI4MUnVktmSV3QcnkZQNuuj6pCAdpMAeNaglY0wIL8ubzKYkX4X5YQ%2B4kPB2tse9Dl6rVQt5Zl0cS0pCU3YyVX99G%2BnUhF6S7bOmYUXU6zdAGf4XTZLfOjOeQ2EhHW5BlX0KMt5digei8sAz4%2BdhZe%2FvGgmY4eEcqA2repDef53UvZPKIfTbc%2BEjfsU0JJV3Fc%2B77EfnGusxOCXNRJ7vroqHMzJcVz3pWFp7VMWJYG1mNmFPY7X%2B1ATNr50534R7A%2B5dKn0KAWJIZEJfVf%2BFZsKkMNynhtIGOqUBd0PbdGPwduQe%2BTHs%2FTgB6a5BDs09TI59JmPRuO4QdZuFyGs7xqiaGiNKAdjLoPeHKozZk0OsfIJX43shn%2BSWWtXjTV8jps03%2F2UjLWPDUBEIdZut%2BFVwpUiPhTeiEmVUtFZXFT7ViE1pTFKgyNwKFv8rMHMqAz%2FYHe6nfqWoefHafambY5KUjlBYK9Nh7%2Bq1uRJ0nG%2F%2FubR1EkcvPafIUwmALBtW&X-Amz-Signature=00ec3215f663354fbd70aaad4a4bbbd60aa92575fafb5d56e138360e03e56504&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
