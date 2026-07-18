---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QXAA2DJE%2F20260718%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260718T144407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBFDVhSLznUu6ayssN%2F3P38VLSoKQtzKIDCTw4vjyOtiAiEA7XNZay56F6pKlkjHMj7BSO%2FH9InZytotHr32OTgEqmQq%2FwMIdxAAGgw2Mzc0MjMxODM4MDUiDDQ4fCFh0q3Fa7ZP3yrcA3NutUbscBzdM90XudZAIXvfEgy4%2BtpcCiXUSCyHY6pG%2FX2fh%2FM%2BOPYY3mfJTcpFbtmji5To9y2Eml%2F3TAZEHu4Gv6la41DQ05o%2FqVsaQODdr5W53d4HtKJv65NqnEuv9v%2FNK7he1XeGxuvrHaIR%2BDK5KrT4Yn6Dy7jN5zQySpG%2BbK1jpUXbPSza4lEmQQNPJb3Q4X51q1ols87O2I%2F7T9ilKY%2F6EOiCIY0BLCRmmXRH%2FoT6UHvTMKcZKdvoUqIW8lRUIUxEg%2Fs5hEZTQ5jCTXiywQLn21tU3TV3kTGffO3IGYiBMD5tDUF7AOJIymmsT1klfRwMQdH%2BQjJNRbXUuNYHJMYyzsyYG38TE%2F8y8R6d7uVw4XSE9LC8XAYgC4QFpHi3BQ3f5KOoR%2Bv61Y8B7RAo3%2Fiphk%2BUV5HTxQ%2FfZzwpzKA0QKDmIvvqgK9GcJrp%2BYKaGMBHvT8rlSEFzvhW6fRri%2F5s1A%2BLL%2F7CsQ%2BAptdXZQu%2Bd%2FFSvLp8OvyPrfeQfoF43afoedVColLGX44Bmxd6F%2BV9ssPhAH%2BiAbvdTuxrLl9jRlNefbdbDoiDE8kgxq8n34sKplO4%2F6euanYLEOX3EaTC3RvY6LCarAW6Yc5IRqpOEdTOGn7Ohpi%2FMPv%2B7dIGOqUB%2BI6aRRZwxHob8cfTarAHRgLUDoORksFrGeAd%2BkxI8tSthvKziEHi%2BhZbF6nMT04ofWjfr%2FiLc42LQaNtJbeZyCBnDEZIA3c4P5J%2BJqtFQ7xVnG6F9v6oPv2mfZWVvd6Iz6On5ZHyWUh5YnmBD6w9Fy6W4bzp%2FISrIVjDz8gdg%2FVuwoevy6axSuXw6%2BzK%2BaISRS9svO4%2BV1%2BTP6L%2Bk3IdcI3QXAGl&X-Amz-Signature=c09948b51a999e237d1e64ee77d4633d96a84b02f51f051d20ace18055dbd059&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
