---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665LDCNVS3%2F20260514%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260514T114343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFZUzLCZ71aG9q7Ovmkn1COWywp9QCpNkF8wwK4eC7h1AiEA9YkUyDAwCoPz5aqj3RdMtcHqiQ4ziBk8SI66v3etxGIq%2FwMIXBAAGgw2Mzc0MjMxODM4MDUiDNqOhl2kVaHo%2BOoXSSrcA6iCc86BrmnOmU6H8QHvMCI6cIyX1oYbKlHtF7zOoKSKT8uO6B79hhHiW8yPcX7B9c8uTvcZj%2FW5r2n%2FmfyHZoMDd8%2Bn%2Fb6Bi3WbqGyLQMIy81%2BhwUfcsKUlMtSfOopvoHwm7UTAX4emfeSjFkw0D0IWsWrwCV0V7VGy3dOvD%2FpGY69jUUDaoU0dH6ViptX0TT%2BypEriHwtKDKan0anzvOTO0mlG3bZ0QGukfjtL75il%2BJi8IB%2F9zaaZ2fZSlRfrR2XwWtlvsQRNjxw6CkVFxJ%2F9vhjubsLefJWb58YJTE1iyJGNNn8gkMLt4sQcp549QZYMUNjZ0vnK2j%2BSFm%2FNlzFRuVPTA3pFrvJyXkr9ZrYtPdrCw0fldc2VFfxlgJN6LGaa1n6iURXbrzxOsf8kUsza%2BvIlp5hCSCiNgh5kjGEvK4EeuwVBCbtLMXF8%2FnkCEvEcTZgOLCXE4p%2Bo0af449ZZtkAHdUMrLGuTAdFIuhdBKOWB2uEUivCYTiSdKcfv6STaeUx%2Bf2eSRJqOpG%2FzLGdN3pipV0bL9n3Y1o8WHTvwQXc%2FYAKkuDL%2BvA5YQYq40rEZNNs2AEDKz%2Bn5a0SVJaS%2FPEp15K0hIFzE6oB7%2BdATWJjl7PI8k12Gd9VyMJbXltAGOqUBv%2FH86UbtoQMsM2w7qX6ptF9s%2BB0bDevl8RNoP9cUBr5H7koHOppV1UNyIlZAOwhRCLTj74HA7H5FUKl4zR1wz5DdxwtQbUwVWVhQl0tN6Br4aMwUSlAegByjRrfH2051TmAqWdWL3E26QDUuhmTVzEylx4zNE6x03d5gkp560XewqfpuURkCueSlCRAxfD8qBO1Dm4g6g8hX%2FiL7ygRSMoFhcEad&X-Amz-Signature=8e008d8ddbdd3f35ac85cb68d5b246997d374419c230ac95ef04155b22634140&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
