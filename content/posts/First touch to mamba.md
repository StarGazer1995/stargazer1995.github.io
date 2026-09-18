---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666FCVUEMS%2F20260918%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260918T234308Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHU4fohUCEx5ipWEX2mdcRkBJnS9eE8rkHJLS1LR3BZ2AiEAxf7AkItKSljLC81Tn2IZXuTVAyEbAXyvwBGHcGKvkUYq%2FwMIThAAGgw2Mzc0MjMxODM4MDUiDInIpggCTVNt1IqaICrcA9QIR1Q3O97PnHDBvVRUqbxqQqCqUUJC9FgI3rmPPN8rBpVlV%2BNMHGfY5xkfFCOFhgLEGzHTBXRt%2F5QxV7sIPHupVvULutL48V3qtW%2B4pHqny5gDDsC%2BebiyhlF%2BUZFqZmZFizUXfMy1irmq3mQiUKlM3aqGhpA7wT9t%2FTnGkyih5kK9rMjKYQJNTMgdOj8iwAG9HCVuqglM%2FHl%2B3DTnopz8dsH0LQLF20yAIrOdjw%2FbA13IO6RGuNjOwyQnuQ6WtNbt%2BtRMR3gFozBzdWZYr3hrLULg8WJqSkKYBN1TaT0UdGTOcf0guoQvf8afNARA2fv6xLTOFxcoAD%2FgyBX2iE%2Fj5%2FBPfXxgPxjfeMAY4pOixANlw%2B%2B5DZfUegur37XkmieAYSTIimgfRz4jyh%2FzfSWBXsWd9H2Pu%2FKvJot9zzHYLdh%2F2qaz2Q%2FmA3xTvZUwgw5rXwu3pUPb1qisk9dRxoU2Km8J6mwvXoGxIWmBbWia4r20o7fFU%2F4x93vo8gBV%2BOFPyEvbsHnaLfqQSKqxe9P1QQlOBjovfca7OmL%2B8qx1Zi0eaZBvOwJ%2BF6KSdj9sWhM1pV0AH2LkeMPmuwf3Q4LFciZvjyiFfTo6LUhbOK7rViRJzh28afqng3hUMJ%2FIttUGOqUBZj05b3E6xF1JZM1XJEz7oBHQf3J9ln%2BuNm0DoENElzjzVc3Io6uRPnBJsmsF6YAWLW7qs8UYwMNLbkuJydr7SVjFJOi9aHG%2BP1UJI5tXkdF4C51FyKUeUqDwLkkG9t1gNcq4lhwWd27WZI7kIhVnkyBKHjDbrO%2BJiug7jBtdUKUGn85AQxKe%2BYGkEj5tIv%2Bb2UlRlBU8CSSBuxrvquyFx4X9%2FPch&X-Amz-Signature=5006129a45adb55a5ace74936cec501e64b18b05dc99ddfd6b6defc7ae15156d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
