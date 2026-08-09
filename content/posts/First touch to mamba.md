---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RVN2STJF%2F20260809%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260809T221850Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGpIZjFopYaHT8tvL55ZnBUp7M9l1JSVIAGKyekh%2FKt2AiBO1Rmiz7efkMsZULO4qKjk2VaMpmxet52zYFhqasawKyqIBAiO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMk0j%2BL16hNxdG6PxZKtwDSUGKhWLIb37SLKOq0zcaHcbMCpaJPUOU4hIUEmZDEVdqDZkpar6KGDTtm1rngofPJFHvRxSkN8772tueYIjWz0wi8C%2FVNNKAQY9n21IOJ%2FyogoscOI52kF72xVn%2Bu92Mj97A766P1VtM%2FuJG0T6D826kIVBSKdU9g41DAgEu8LUEsUlhGV5l%2FUPG3DpAg3vgCMa2%2BMP%2FjbnEzY3NpJcIocNoMlSyvkIWTHqXJq%2F1dJdi5HXrns6DaTrdcdOhp%2Bgj5yUlAc9HJVH3CjrbnX%2BsKz9n10N4SZF92Iwnl4UjcUSGZRGL6GJ%2BiKvYrOzIwRB4bYrCCGiIUsc%2B9Nw%2BcytVGvYyLkuCX8%2FOmDPni%2Fiobos7agH8kOik5o%2F4zjnrIdZaXcpiBmfkqtzwcAukElNGKQ1KREM0jW2cksGhTlpNwxmc6fSy7pUzfIwO39ScsO8YxqtqqTMSnP4tCgRi05J8WWY%2Ba4DKpVlIGXLENbuUMSUmkAKv5zQS2XOFRdZnF8UWr9qrw6cWaWdrhjth0sKvMwr92KiBj0IQuR9H6d7PKud%2FrQF3S1wYrHAealMWk2MVLAFPZx4O3c1Yw0I%2FSrfKkXIOhl%2BYZT2IFP5bdtSJBvFBQ82%2B4uAqcYiWEDIw5cjj0wY6pgGX0yDhhPW2NQqJ4yiLTCZp1dRfzQS%2B0PHX4Uk3PCuVIo5PPqY1bSmiBcuT%2FqSAZsxFSS5fOexwe9vApvzcARheRJn6o06Yl0zzxoBPwmo1tU5B29w3mGJQciWNe57KIVWtFGkUs%2Bdjyr8WR33iv8WJeG1LYhzxsfsKyO3jICCIPmvYxvQsjzlkOqYSC1tPmXowLI24twoU04Bp9OL0DYc%2BkRbYbljP&X-Amz-Signature=8c8b19a0998a78e0030e4ddd6fa67fa6a2ffa01dbf138d24c84d6cc4185fe2f6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
