---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664MTB5DTJ%2F20260529%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260529T182646Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJGMEQCIHiaELncOikcwIzGxTzoxx5zqqGdIcVlkEXS2l2VvWUaAiAf9D9dqTg9yTAsqv1gBrru8FTxSzgoyccq2uCEn0PO7yqIBAjL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMfVvHlgqtIMy8ROcoKtwDaaRURbu6D48JbwBROVZN%2B0n0NUIMhb8bQNLkGB9iHJg2Kw4JP5cYRxZ9eHVAj7l8mDBJGdf9oG8CQeDVCWqxRu%2BJAB2gVQREBODUOT591%2BcUTVv7wzhAOYDU7n2ZG%2B4jLpv2YfeofXNDa%2B4pi9SdTUY6QD27vDA8NKIFYMjPePfMUy8n%2Fd3s2em5SEAKFUPTSNyBGDHjCcdX9T35NWOkZWoBy6S6Wl3PcRQh7s5fk3zdtTvnrL8VL%2BSmDPBO5dXvVYBbjJ0czLVCX93ALBZMTdEal7hR3sC4Cu6OckGk9JLIljoYwVhnH9ivIy9C%2FNFh4lk76Ekg4%2Fu9J7VsldAQRlegljKwlzHDi3TaEc8KJoTwe3hUnB24SrpwcNzRyDrnFSBZTw8H45CWvo582ZeuNEABWyI3OzKWqZrZZrOKfqpO6BZsrN8XCNnGyExtxPGnl32yw945MYxTuZWcGVV0WmYo4yld1qvSxHi4aI3VkHAXwewIq9UapilZBqqxwyA7FVz%2FQkHURkwkr%2Bi3e1xSnuEH66S3X4NmcNAXFlrkDHnGcDrQvKcLQ3j10LPhyiFkK16dqLGdn52uCip0UOn8XTCx5qVDTP3RcyvPMIfBBT%2FfepfJKeDr2VrVdMEwha3n0AY6pgG66Fw9Wkmxctvgs9%2BSaPoLnoEq2TAVDwI6sJFDFL0n9UK%2BndLqttMRTLxJqJuyovooK4on1sYmrOsc8XYxvy%2FWYVLJzeJKdQ87wTCwrHnyK9sb1UTvqWLaBS763DZCd3RH5CxkRJlj2oz3yFSDbX%2F8v22iU1bIK%2F7ycIPNf%2FF5U4GHCD2rbwxVtZ%2FRe%2FLQAUzQa6L%2F%2FRR4b2SNbp5EAgfnosLhlhPS&X-Amz-Signature=407999f843250918be3eec2978904cb157ec9ba2223ad970d644ec56446d258b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
