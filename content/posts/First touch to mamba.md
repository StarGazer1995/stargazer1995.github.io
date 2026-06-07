---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TAGVGMWZ%2F20260607%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260607T225430Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD5VDl4If3bYZJYV3Ioz8G64rij46aRDjGLtIyEejH8zAIhAOh7QIBT%2Fdlodf7NidCP1m0vCMkqtiScB8x5buG1CCrrKogECKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwuhoCA%2FljKKQURj%2Bsq3AN%2Fq%2FYHqv%2FZLO5PqtlHhAo630IZR5fjDvSgdoqLvjm%2Fd2p7UC8aGQYtVyGmqaJ9rlCbBr7NfoDGOAw9V2JCW4fHyN5Wxi348RyMqbosBNCA0DMTidjy%2FWYL42FxlaukBDl%2FNe5%2FxYAxF4lWTQQURn14YFNVCNMZsCbV1JOvlzBlxKntDlQ77PYS9oSvsMB6lwg0cWX8q9sBB3OaRmalrSnLDvy9ucBrGizGNm%2B3wOU9iull9kZlj8euAiK%2FSeo8Z5lT%2FWZnh4osLIB1Me9mJgon9RyZqjcRvtMnbkZet3CjmC%2BhuqW0Q3UkZo7q%2Fgcip3SaRtqUYTb%2B1oawqmuH2stDSjUmy2BsOmelxm5k%2Fina43tCamTetpoQFkpyJ%2Be3ahMdMu7%2BsQvDAaSTWxMUbZHRxWo3NK%2FJbnZHxz%2FXWxNVbIRJw%2FqYB8l87hKXY2srBGce3ckN86MydB94urHnTdtdvHdFat92CIZV07MKwvaljB2%2Fvzq7nE%2FZ42RVu6qEZ7e4wJVdsO9wX2VqR8mImMOWVtoEzc3CZTL%2FY7LQss%2BDfibQLCAPXWAf5NjBK3GIuvuIoOQFcIKmbEKicVLlola6a8GSYK0YBZYw4TnWpd0w9%2BXlBsIpSroVfUam3zDCzpfRBjqkAR%2Bcz6WZfGLZ74odE0ilm14zoLPatsDkHnGbvbi3IkSgnkYg3yBv5kS96u3h3LXR%2BARt8lD%2FfjRc7xAlBpJFPxR0wdiM7KfdGodSZed1yTUQu4JyHwlin5SA489GICkBvLv1rruba%2B2tBQOMr8h9U5%2FyzLLkgzyraGryhk%2Fje580EO9cjo1dLLnJ40oH1Ahf47nIlFXn0QdW9D3aMSXF79cQvJeW&X-Amz-Signature=ed405ca5fe58dcc2d79a31df6f20a44b31ced1562414fe84f87dbf42300fca24&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
