---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QPIOHSDV%2F20260720%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260720T205926Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHCfqOxbVrte1%2FUWLCA7VF94N%2BWSGoWqQ7LQwZ3hBeFZAiEAtn8JLYC29U06HTXPYobwMUWcOSUQw5GlvG3bih%2Fwn2AqiAQIrv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFZDMNR%2FPWW%2Fe8Q4YCrcAzsd35FhkjhmpHPXE0gqLPQ9ZzlG%2BITUPSmONd5yiUG8yxC6GhlPCjN7ndJae7Ilfz7DLJHJL3bfEr7YFtq%2BZd%2FQ1aJDk1mpSeu5gSwIhC3IYcrHVeY%2FPQdUlh2dLEyVyzteoyCaXVr7pv4Cf20VSscVkZzw8u%2FfVDgyBWPCPzkV0TV4NmSkCOnkkunfZ9sEC6L1K24ftTgKg59AZkINCKi8WamOOgL3G29%2FuHbTakVYSCindJpMMBU%2BMT9XzCrZ3ruugrihjXHOQWHBAko3YbhO99rlkCRMuZb99ZanwzsvLJBA18iJXRVl7vtLaWzivKCmLcUMq0D3rRUWEjX1F6AtyNPv4Ea4fKHl2m3kyuiI%2FB31M1BjLaIJTElJjDMzxbXDz%2BLz%2F0h4tuBk2rGnqVSUkwK7rCFltmmtNycy2io4a%2FUFPP63JrFWqJPJBQHQpMIBrtGx05ukVvp4EJjvyrFmB6UI5NkX5kkBTfWt1gHu4QK6AQg6785CMPskk0mzswbLW9t50gUZOaPncSx32%2Bi%2FkQmuYx5dqTCFA4s6%2FoPPOB6vkbddTzB1fW5PNRU9c2nJ%2FtmpafDizsD4tM7eHYnsFL3s%2F98Dxy8z9kChScAG9SkQGGTmrqO6COVEMI%2BP%2BtIGOqUBPRXhW2eHIA1TVbBEyBuo98zLAOGD3Kz5WwYoxtjFI0ubNGJw9IadPgaI%2BrwLiIUqwu6ybeOAWinnJlYUJot%2BbJj%2FuEOT9hQ0W%2B8gDEWFTYp2c50qYc4Xla45%2Fp9Azb1wyWUGUAepJ9fzPNcZwgaAVz844TjMflKaPqAESeqflldInuXLl4k%2FP1jyFN0ZrZZoVd%2FY7rh%2Fi4cdC5uTUAdD22oDo4sj&X-Amz-Signature=78a373321b148983ed87061de8dc5030fedf410739ece4f3c70a608a3693e050&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
