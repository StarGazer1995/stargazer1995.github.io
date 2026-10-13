---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666TID2UIQ%2F20261013%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261013T171314Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFHewRoMyQ6%2BDzcevalUJDKLfOqcMgS%2Bvoa0OBZ8g9qpAiASY8DpKnm%2BVEMVZ2UT9ZL0AK6p75Ww4VS1ipBec1vnNSqIBAih%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMNy0iEd2Y%2FALkWQ9UKtwDS4fvnh7NUmMCvPvPt0jGskiEEnH73jPkACHOk0o7qzTjWY7QS0%2BiohXG0jTSktueTJZb%2BqywJ63XjNTVGzEYWEYTY1p5gqMLzZqPcOxN7wYkt1JLSy2frgXw7Co3TPv5OOrs4chTVD3sbpgG4IikGyDcOH73XqWewbu%2BCV%2FceEIvRmYrait74%2Bi2VrYG2Tl5CZ%2F2tBvF6sDW89pioj91JGOOhssA8lRNZcn520nF%2BvGQ%2Fa3spHgVFutO5boqjXmYJIgVdMHRIl7ZgqfxWjS3I4CWC2fk%2F6K1Urlf9iyvSrDQ%2FO4HanLrYVWx0kywuarNk0yBYvGoqmR%2FS0rJ7xo0ED9j07L%2FJhddsAcLKHhKKjPJBf0BOFCoZeMEyhm2Y8RgiFEsd6KVNYL6kisUvpN7sCBOlQAqlUQuiPgxMr%2BBx5o6r5HUFWA24og80XXVjyx1buVTuegfYMkaqo%2FQWdntM3keswDEbd87iFQ36kI0yz5YKj7G7%2Bcqx4TNd0a%2FkTthDLRiW%2BlZyICxIN9DzcA3RM1ty%2FE9PqscgB6ItlX4%2BseZOKU2tfeQNPYtMwbLPzxE7C2lD9l1RY5vZEL7kLtoVWM02TZAPYLcq0Yr5G9Z3xSKX%2BK7NcYSP5ATMRww1J651gY6pgHt4wrrtgE1u%2FJwvoGKPgSS%2BPGqkUj8aRITxgsmjOU6LZWhqO2cN2vTSmMpsqaT9H%2BqlGnzlJ87QeRtH5aGTijMhBcPiWR042destJ5BbBB5p1u7HXKY22D464Izb0KmRUAHWSeer%2F6S1rlz2VFcOQswdISCPZBQqBeuK6DUvNyZTH%2FgpxdgIfVDpdktSVcTGpqhVzMGo5k3vWd3jZ3nz7ZWrmCX0II&X-Amz-Signature=fca009eb3524fc47c0096b1c06f0c3d887f5318510b3dee99b81450be2fa6990&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
