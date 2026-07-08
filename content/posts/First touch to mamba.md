---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666DMO2EFU%2F20260708%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260708T080541Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCtNFetJnHbv5wrElY5di52XDrF9hngj5wwYxZ0%2Fst6wAIgPbRRy07fYZFX%2FtfbJj3P98vvP%2B4HY710JQ1%2BbNrlvhIqiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFfGACn5NeNtkEr7jSrcA%2BhF44Uk1SC17kUR%2BY6Xpu19vLN0GfwzNS6DnWSt895F4wMLmR7sbmCKhRX1URQYZYyml%2F%2B4k6ioZGcIqoXkkEEPXvAMPIka7k1wDEQGaXBzlcN4r%2F5g%2Bhgd%2FOrgubz1kJpNDezzKTjJWgrj%2BYDxVHkRjoJc9cSvUnACCfG9bF%2BO3yAmOG0eSDeIKnt7Wx7tsIByGHL5RVP8uoJh7q7wqLcdLJ3nxRWwrF8EsxeJQfUTE49Kf1dMW%2BJq9rUTJ56tDYt9jrTYECXjRg9%2BTdqJbGxgTx5CyktSrk85R9%2FZzLQKJCO0YvUn9FcYgPr292ONk7D3wxh4hG1DPRB5OL%2F2CPBIsg7Wo3TxM1w27kTo%2FWV5JlWR7mR0ED%2BrXZLg0%2BO4wfSo5z5nfvMYh7IjFhUQQ9qzCP9P2zaflm07Otoj9eJ44W6E2QCj3BDjMqRwTHmAwdIyVuVJA0m%2FOktd%2Bl%2FZY4RlLqw0FLak%2BtHXNMdRzVMreI7mkTUVnVBnBKgzfaRbjfTs26QxjLFY7mJ5B3rZhRpRtxqt2hFDmkFCXZ676PRXWdmdgKMv9s4YC6PFbsJNcV3iapGzpZxPgpz4v2AnHZo23G%2B0rw0tTwGvdzWIqarqDizxzmfvqlXRidHtMM2HuNIGOqUBdlYusH6pxivJSaboNhkh1XFHwSjWvmc0peECSeFzpIapzR%2FyQETxmYr8Q5xvB072wZ%2B5hb%2BGegZQdvCX6MWTv2ZdNr%2F2xq7QU5YUTDz7UQ0aNgdtMX3VfEIFEkDknsyBuDuGc25hiruEF8nYbnf266w0q6Ye%2FGZrP6Mvx8S%2FlQz1UW5%2F8LeWCW0zkD5o1oyRrcpXosLiaJxQafnVSBgjVgcIMURD&X-Amz-Signature=6d573a1ba61cd05f4dea207a7d031ddf4ff23ca5b0985e2a5cdfc362ea2012ef&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
