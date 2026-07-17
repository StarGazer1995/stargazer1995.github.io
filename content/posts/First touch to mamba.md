---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665MSK4DOS%2F20260717%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260717T204138Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD%2FRKcC0ekjcb7gVyvde5zvvUEaOlpQqELtOUp%2FEGv8AAIgJ9nMM7XhjLC9c%2F7FbXQYPLFJchBjl0tILuPwGUox5cYq%2FwMIZRAAGgw2Mzc0MjMxODM4MDUiDEBMennTT%2BKihLploCrcA3967pVQSVIsLqlyxbPHx6sZ4ac7VXNVF%2ByXLV%2FAYhA%2FiZjp7Iq7%2BXGLpx1HOsyh9Q2LkRudosIj2Pz4Oqdmmd9TOsogn5%2BHiQTNtDuF083YDfKRJ3jY2hYQVWYCekeKWOELFThIBoNDO3wB%2FZb4O04A5a%2FJjjNO%2BbbY5C3gfquhiSpWwFwS%2FxaOH8E%2FIaehAMjrkXo6nUDcp692Uw3ZV0t99pouUzd8aMQYKr7azLcy1aLuV36%2Bjoyg1c8gazxQxtat1yj5TYOBKPorCXCxSiH5lXddu5AopNFO%2FEqatd5OJVcKiXunnLbykA7yw2xYS8INDBaMwXkEnJVRSTnXAg02c5dBWCXHhWOAtBBWyD%2FuGGz%2B5wI2Ebwjmhlu%2FCjUFYiYWccmTX7PADETxP7kyqgpWsnIP20L29y%2Fou8DU2hK9ugIqOVgqXd7KQtggZlV4W09yN6u1PxcxG5Y45N5OfrIJmG5LLaO3%2BAENtamKNZpYGJ2gx2Gq%2BMxQZKxnxEJiCGi3vQPfGyMHdROx2gcQg0UbtXKpNHLM0rTw9VLKEpbNWu5hgoujAZSy34Ld6PFA6iXc%2Ftq4sm5x2cVZnFss2kE%2BUecdbV03bA8OY6nVpkl5Dcf8nspupOOyMWpMLaF6tIGOqUB1WVK1Brg87KalGkyfrygd437zUVDhIPdxeiInlZ%2BDutaZRb46rGKZLG64eHEZbLdOAXglS7WeHMPnKmWtZO%2BH6251ZdxH5Ue88azxtcaMnYpkT%2FM3PbSAEwwlzc0%2FQA%2FI1B1dKRERD%2BONfSI4GO0cWRF5u4SMlw%2B01Cmu3FQpj7%2BsoF8WVpYG8LHymjO2UcUqeiAbW5AZyuLffP7Pz7MmAJlntoq&X-Amz-Signature=1661a511f68c31eaeedbbee196a9ab3813677cdc1a09441005a57f8a5018f5a6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
