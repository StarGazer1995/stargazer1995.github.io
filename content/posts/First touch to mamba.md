---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662ELIFSTQ%2F20260818%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260818T182005Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCmS6IQ%2FG5Jyz1B0ToeKIYfrZbCI43sd8N832mibYAI6wIgQ1oTDl7A8xjA5k22yD1jCodZOWGUqHQd4VQuks%2BI5Ecq%2FwMIYxAAGgw2Mzc0MjMxODM4MDUiDGIJK3vLZzagq3hKJCrcA74rjNe56kz6BYZgvF17rTdjpM5t5MkgeLBpCN5zEKuZ%2BNfnqR2Xz275QRNDvMcYyVA4c6JQ7NLTZ0uBqWGWor%2FIwCz3vMvXv842pxSS6g6jQNyln%2FgxjlGrbW9D98Kz5%2FLQOHfijxwC7X6FhEg9XRft0rKdjsWZxqPD8KxplMEK%2B4qmWrVSh%2BGVAdGUSrjT9rDJl9RZQLYsEwblly%2FDoSRRjLhQNt9q40k6fyq9vCan1V8k%2BDWEgt27P8UEkE3jsqMgrWZw%2BpBT85TS4iz%2BtVykqEuMa01%2F108MZw%2B1cUht64ubS4GIaemgmi%2B8qGql7uuwHqdCXs6U0zJgP58WD6NI28p3BJ7yUDLuaEMNZzPUhUeHIDRTCXyjX3QarOQ3k9H4VRiNBf6RbzrzHGt96QkFD01NMbQM1aNb4Vick2j4qTm1Wa%2B%2FJ8NEczuEUaQDpf0%2FeUJHHKpgkJ%2BQsKSS1%2FTdbg3pU0YLpPHWM1PvY5XUPsCpVyJhlAO3hcSCnBY0moP7lhQbb9kofTq3JgTslqqXdtD0MpiSY1L6u0HvFq%2FmMxhB6vhdXw%2F1bZ1SAoM%2FCoh3GBi6O5JZl6bILn4JI%2F5c0CJmC116gKD9Pb2YDmNXTeV53upGVW3FSoV5MPS7ktQGOqUBXFZky0%2B5ifE5vkfRgMdWAqe%2BTVBt9hfrcQOAZ1nQX%2FPMnzE0vr5c6XkM2fuykTCzc40GxrQ8OGeKB0IO1PPWI6XfBQyU0RtbyTes3T1d0BWzar%2FgdVQi87xLN9199wygG6nCfGVULc%2BU7aLVn6lBOGCuXzka%2Fj8V0%2BeDZralAz7YtlWfvMdx818PpDGLE5cO0REoRB7BqCwK92VSNLsDXRozMwSv&X-Amz-Signature=0cef0c833d4acdf5df7872736f1c35c602d2c159594f9f4803ea29a3dc4a0109&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
