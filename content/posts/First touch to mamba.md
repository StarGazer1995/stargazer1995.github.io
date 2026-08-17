---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SWVDJO2K%2F20260817%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260817T083004Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHkaCXVzLXdlc3QtMiJIMEYCIQDJ%2B82UIdDD%2B3nC%2F%2FvqyVtxxESgJXq8FbKP56awyJBCGQIhAP8vui8iQQwA5lfi9tpMx%2FI4AAei%2Ft%2BYw0Van7cIIY3XKv8DCEEQABoMNjM3NDIzMTgzODA1Igzv%2FCcw2x9rWLmNn2Yq3AOLT6AKd07hMrjoxv02e%2BHAOmNMW3EtC2UUGZoK1RWWQhIjD0ECJWjST9tZ%2BEBD8t2YiJyd0BPajRbDGbdzR7acrHD182ARyeE0%2F6YhO%2BSLjeA8jPHcV2IZqD6HT6qBXic9f6dLxz7VPfL4p1f%2BtKIfv1gbt8rtr5Fm8weAWN2FjLegTBnAjPjri1C%2BcndLX%2BMvMoCpPUfpATNNrVhj31saVVPB%2B%2FTCe898xZTZneIIDn%2F4XMIJisRQklq2iKcLehgiDEDNN7HUU96vORi3yktp5PPZG78Eff8TKZh9B7Jowj8mWi9Bt5F7wYS2cwz%2Fkff%2BatDZLDpWzgRVD7lf%2FjqMRr9xYkKCkGgJKVrDlGepRNuhSjhTqeep54RlBi86soLaR7%2FGwfrdqj8ACblmnnzDxzeIuegti5jNrTF5IYNVrkBK4PxXBjUqb%2FUW%2Btoxqz8dg7x4qwsqWmr4fv4nEPicBQkO7OlSFG8XeJxDUlZxkmvOQhTo6B77DjSUAImo%2F9acFSH5FAkzd6arS9avvqAg01t1fj6EE5%2B1weA6MzR0CtKrNHr7%2BT54FrqjZJTJEyQQl%2F1l62g2tnOFI2%2FnnBEBDqE3ZIE6OY8jqvz%2BQnL6DOXPE%2B1rBXYqixrwBDDhiIvUBjqkAbGMIOLgGJ7m8%2BZzbaGa5OCTFLqAafI7dLuxevO9raKQpL69t3c%2B201xCS4PqdL25CrV2b42mKvFYwEUyBO6jwg9KfI7J%2BF8RvpSB3mAITZE%2BFKaZ0UnFsW1DRMEXdQ4e%2Fds3zqhLV92FAKJEBsUnSMN%2Fc6ObNDOU%2FSmnudNxkUWUqZoBWmELSPQRdblCsILRDRJdCNLd5PFz5iT0657S8Z0Sl3v&X-Amz-Signature=a917025d82dd6a6a6c60b67adda5cd4353de78cf7248c31775c690214d6b9c05&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
