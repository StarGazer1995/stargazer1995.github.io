---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QJACJW56%2F20260709%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260709T211029Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEdwmLA26F5ZjZlvdUH2IiWRgS8mDL81xdMjSQl8AHtyAiEA%2BTpv3QXI2JvyuDUtedzsmapPYxu9sZyAyB4zFzuTmyAqiAQIpv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNJvsRhzkn75LcwMVircA2GK3iBy3WSUqCUV7FgbKAgX2N2I%2FdPC7n%2FVucT%2FNnG712zrJb085bzXAIW5S0DGzXov4axghFO64r86iI8yFKIck4HghsapbBE%2BM%2B5y9Ukr%2B3E9NgJtdeyZGaVd053RdLsnT5N7JZUOa9g%2BT8UkcnQaQJmwNLw7%2FJY1X95Z805zaL9VpxufoxmoGJcFPRKx9nHYhFjzHxx7ITLtKYaW95JPelMVqfUGmU6ye5kDbYEJ3BS6zxrgPK8TXYM%2BMieWOXJ1bn36XrLgqzM8WNTRylRVElUYvHgy%2FkaLQbdmtJtix%2B59Be%2FkPTBDfLTzaNRn0jogahWdxCL3yBhP7UHFrNBzWiTjsmyZR5Qld1S18fBJ9oERndIE4ynkPYeST%2BJNIH1FucZL%2FgxL4qZBtjsQm0VlwxKBNjv4QAKN%2FnjeNNTKroBQVHecMNVNnbzzfNZSar8Bh8o%2Bdxh%2FtycUa7buxBPcY5aDzjwuTKogMjQdXl06At5txXW6YoRrW8BS43iHyul7iRbm1rhm3dx4f8kHeF%2FubCygQrYOegb%2FfoISQCY1ae8sJayO3wd%2BTAY9AavE6ZPvUf20EmOpYfxHmZvYuR%2BirpMn1x3jnQ%2Fs3S8BeOQXoKnP38x2BXjI5ON%2BMOmOwNIGOqUBJCK%2BG7D69ynV8ThRh%2FEYdtFK6JkpU9smUGJ%2BCHoSXWOTvJjryhJ1lWEsprvExa5b7gj1NiFHbtNGdrPZcwnsvG6fHttxSKGw%2FnJPgRJWMPPoOe9yzKeCtyV7W4KOk063c3OjuQblficjQrgQ6U%2FBKajc%2Fz1Emq3tQC7q5qNiOnJipJXKjYeQ6ku8XgEBFKUy6vOrwrLLLtM9m%2F7q%2Fqjs5NyRBwEp&X-Amz-Signature=35a3cd32a9ffab234d4eacccc3d879be1bb05b118bcdfa6e193d4fadcf779377&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
