---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666JASZMSO%2F20260819%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260819T201544Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC2ZN1d4vFUE2MIgu5BBQoJL2sFmZ3r6joH4SC6bvZ02QIgbmjC2nNWD2oTsyw7ECuX7GYIkigvfkwOonY08T4QN2Eq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDM9VTlrJrSI9NcnXByrcA2Uov3QbBEhjRODtuLs1cIG62jeJOvlmkNKQIeGH4iaT1KFio5r%2BdrXqn2EOqYB1F7NfXww7Msy7PPfxWlPz8Jl4SNPrKu6D9RfwOFtStKMjaGrqX%2FNSgaoWmu%2FteLtD6dSSptJCEr%2FlPfCvxmyvOk717xF5Bk3VoMMjyd9%2FNrfxQCWeR%2FLUhzlaLquO72%2BmsmXPYlI0c%2BuBwmZgYZGF%2BfnLZUZdUgAD%2BircP9wiziYV2OiNXKNQyBc4xIuD4BUmtvuy7QcRtbbKEnhhl%2F17DpqMt5VHaCiq9dDJ1CO9F8NGa128xnra86LjAY7UtJRVkXwKer9qoWWZbpHqGT8%2FFuaxnVaN7uvOpf7Zn2wpveaoFAUsWplvlis68L8mgsyy%2FbQJXpXUU%2FKnwlzvb65zIDIEWRotwKj7JbIbVWen4A%2FXQO9hUDp9nrxoeIVG7XRE%2FPCUw4VLrMAkFJ3WXeU%2Fo5Iadbhv0lgWuSS4L6%2FSmrm6P8wzGVZOhOx9An%2BHlEb%2Brbjj2x9Co2Knm3q0NjlfBq3oRUYWa2ZmdHJn0eqHeisK5tY%2F5XcjV2UQBfWtD6299MBrTkcY2QgWgsbsvaxOAUTAVqzl4XcoAPHmgPE%2BZHgULQfThMFOlVla4iKmMKXUl9QGOqUBfmxn3y24AC2g%2FuGqmVLeJj%2BpJj15ORZi0pLBZSKWB1qKa89yxtslpY8cX7k1gqdF%2FDBHUdBTvFST%2FSovOIvhEFChz9zdVIXMs94xnNM7W1bjI3nxFIBIeUruq%2BUILoLT1vn2JQaaiXGI6CDELYxWdJkLRzUK0kUQte6ONVoYpzMnxBwvwFwpIzfCkVjgurpmWKQPpTvZkwaKOe3AjfqjhcKHUMkm&X-Amz-Signature=fbc08131ab82f244c494635139df127e0e28fd118a669687feb5c74b2f42ccef&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
