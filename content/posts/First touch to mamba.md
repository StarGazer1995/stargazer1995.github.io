---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666UDJYRIL%2F20260519%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260519T175724Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJHMEUCIQCHLx56DCJClc2hZ4TMYEFNvS1uhtVr4kr%2FvSu9fG8xhgIgM6RK1mP7iH6qnVvdHVShTEaG9Er6s22%2FSOqS3Sg4Cp0qiAQI2v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDICCpEhgpmhQwjTiiSrcA8CyvNXOa1%2FsRUO0KZhKTeoAvsq9hCdZwH%2F30e1rdZ%2BwgehD3npwfvQDERJoRHW8122md%2F4Y0L8rIyERxD7xuuGMco2ukXcc8BZNIYgOrLGOCSX1V2YxARTtnLz7AOiRRpprKcBKjPcb042RiPPS3zHaP2xPbear7JAImkLJnwGKIQCL5yM9CwL6nlu8QFqwv%2FeROPuGXZj3eVOXr2bmHyHG17Ltlpcmf7CTfSoxrnyJ2UxDPLqdlPA8cz0pXfWcaI4ynAXaaAvu8efSv4068M1C646V6DYD%2FnHiytF02tmkBImPiKNK5h7LALVtG6kN8hPVumk%2FvccZlbhrLA8Sqgd9x7bB21jMGiCFoBKDo%2B2pJtaTIeQngMZyQho0bHpoZxamG3FE6hVpADmrB%2Bf13szklvXGm%2FKVX%2B1%2F%2BzSYLiSwAjWxuQbUb9m%2BMMxuNzX%2BQwuxsujzQUZfS6rKtiFRKAjvNIFNu3TCX0%2FfMh5%2FEWEqitX6FpvTgtw42Ou9l%2BYLClsUzjwpKYfsUfteloy6%2FoUOTD540ha4VtFQ9zb8uZcylZKJ2BjFXTqU8LCLQb0pQcOJXHnrs0MzetdVuQgZxocepAXwva%2BoFFOW9Y6X%2B2%2FiS3WCecGEPsCFQ01kMPq0stAGOqUBxX7BDSjJDUvD%2F4mXAquhy2qeEqOkTbsnfl%2F%2BlqlmrFmTX21rTYqf2gpJ9wfC3WPvVoD2dk%2FAlCxn1q9SXxk%2FaejP3kWs5Xja%2BtU0I%2BtfuQO86hrZjhBZ%2FK%2BIr3Ooddb73L5S%2FwrH4JRdKVoRyZWZor1A5j5xQQp7P0JCONgPt%2FXMGcvIe%2BIyngsF%2FdwEiaDICjKUwPUJfpQ1lT%2BZrHKInCsockes&X-Amz-Signature=058331a79cf9bfb3264ccbd43e8550d5415155b574a64c5ad270e8eac3ba4bf0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
