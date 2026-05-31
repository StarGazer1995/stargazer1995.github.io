---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QBLFIUEL%2F20260531%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260531T073815Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECcaCXVzLXdlc3QtMiJHMEUCIQCPA%2BvxJMdzCyuHr0mgM3Dm4%2BHHXArdc5nBUOhZARplkAIgbEnwO68AEzUJq6pOqm%2BmzvN5vlJOHGF%2BcfM4bTecxM8qiAQI8P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDO%2Fg5AB0Oj%2FjTCtLcyrcA%2F3YA1XhTgYcRyNlBrVBrHJLtWVQN7qjqSgWSxa6X4hCDtJP9OcjTAU349F6MCU2%2BQHW4Wt8cn96ssNgsFZ9OUffz%2BOcdCsrHTuWmvndrW%2F87L%2BfXbx4w%2By%2F4W4u5C%2Bm01fkJDQGDOiCKDTiycPxf9waf22mrriQ47kjaAeNnWZfuFsA9Qrw6k37gjygzBB22e9iscX8h2unc8c0NGsOMRcDxPaUWsDB9Xo9CbFN1aKaO8NMRW8imRCJSqBiLcOmfn5nFLbE7pMZVdJ1Sepf1kDa%2BRorLtZfmvzz6prNSZo5Y801gI%2FIpHZl3%2Bm996ZS6lK4NVy0nl5YuIC1PGp3Q3mnPzm5kNQglQyHBWKF9X5owNK3ZkQ7jtZN03eXo5E3QmUybOMmnjWCkDmgkJuYaZ7NmATOWJfvnPQ7bmg7ZgZ9SUOcUGCS9RPgwxoRW6tbSmU%2F2C67QJrYfsw7lqSzt8%2FlO05tWoOSC2Ht22kOqhD5zmf%2Fd4MtzGddhCwVy%2BuB9h82KDYC%2FcLKjI%2FfMlv5pgia8fCJC7AM677EM3Qa%2FcDvYTecUu87UGbc8L4BHp4tdbPepe9R9ILaGDY2A5ND08xQum8v2woh8CTKdpcCheeOwqHSwSRCAo4bIBa1MKyo79AGOqUBHm%2BhiYQgGv9M42ZQPoCHeNV0Ojh2of3L8e5ezbdylhmdjo5eSriKioKjsPt1RDLc%2BnOPkAZPWtavm28uYDyg97ShRHasjkbF%2B2sntSf%2F4pPsEXN5%2FTyjBYRmNWPjjrN1HefxDUT0SjjvK2UyWTskrKpK520TQRByFJxf1Tpqu%2F3OXdQqZnB5HH2bGrNL9nBze9Xpx5Cw3yykS%2BLvLMqeEsHuFnE5&X-Amz-Signature=de13b6a3333fc05d7f120b2f17570ef6b434ea4aae8cab72eaa6c195c74dd029&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
