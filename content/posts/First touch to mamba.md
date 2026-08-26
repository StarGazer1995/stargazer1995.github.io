---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46665OPAWDI%2F20260826%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260826T164146Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJHMEUCIHXXeZxHFI2vOJYAGK645cQ07dOM%2B%2BuxPd90cfjjl5NIAiEA%2FCDb0sr5NpsIRN3greJnDq%2B3ajjrsuwrLWfmJyRpUJUq%2FwMIHxAAGgw2Mzc0MjMxODM4MDUiDLfRIo8iEgLtLFUc%2BircAyn9zAXfDgLVabIPMp1POw9BAD9k%2F40UPdxz1SbXovFvHhfJjoyNvQlOMdfXOHiuRC1uMzVm3pZiN2gd7IdYqB%2B19W2v2bRIya1MtKy%2BVYBxY4oOJceavLk5Om7IUQ7%2FLZrBS%2BALHzdJAJ8Pd6nqVEzrA70s8QEPWS65ppaYqix3HB4TFJ%2F2OgQ18bSc4iBGauCYhhjNPfc%2B%2BhAkMdWinc8l1ZeQjrVHUiLLdLKIk10qRcv%2F9DFjksnHXcgzLieBPQTAI7cObS8fyNHZ9gSw%2BPWMyaPZXgyeVyTE0mogNm4oEJrxw5g9tvt8TUlhYWv7152nAACsg%2F7Aeg5RBU%2B0Yg%2Bjdgd1uu%2FqCR%2FReYcTmgqxq%2B81IUs5MgS%2Bh8PCsFfJj%2FHUB1qW%2Bx%2Foxkm4tvXyk%2B3lF85H9wp3vo2IqMkPwXUA2T5AQ%2Ba59H7Avg81tsC5AcoASQZgUvjBwTMXYI9NSYo0YJ6LJ%2BVLjseaUgiawZLzuNPXW5ntibgzVh4J%2FLhLdh%2FG5m4pI6tycY7tWBEIIqAoNHdxb3p2CWxfFrKtcInVAQJyNR3rj6U7Y7MfnwYm6UVAKvGpO34JI4uMUyKFS8AxgzKnehZabPAYnrLw7ImAlEh8AMlclgYBIAntMLHhu9QGOqUB6AAo0opnM6bJMJ4ug0ThaDmcNWjkDfAa5OpBPgdXpMts1EPSJKnzFOwqFaaCCmmxu4OWX0OAKdytSsxISwuhP13keIBA1d6eAmG7M9UpNzNXGm3sBYqowgkHJVT%2Fbe8xKwZS%2BQlAD%2Ft6IP1mwe852Bgcho5qXA28xB1H3L%2Brrs7c4WBUv2952DZgIbLznYeSVTpg1zJ2WH7TPe3oPrm0F%2Bwo0v6B&X-Amz-Signature=da717fba6f2a6275903f026032fc43c4d5ee12e0dcec2cdee9aad07b8f06b5c1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
