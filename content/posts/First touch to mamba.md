---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TVOD6T64%2F20260729%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260729T134145Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIC1l5dowtAVwDKA%2BZg516h2OQw5aCmoZrHCpYdEdMlSVAiBrzNHhg8ySIBR%2FtGVFta%2FA%2BLI8Gd24AZdseXEYI8YMPir%2FAwh%2FEAAaDDYzNzQyMzE4MzgwNSIMBGROOwzGeQhXxvOsKtwDsrvwpNzkCJjOYTtFEr1XWx2g4Hz9Fnw%2B%2F0PTKpWe9ZdwmtnYZXp86XpDgdlkKDtB4BytBIkMsimbilRwMabwKtqY3sH2Fh5bO2%2B2bAZdE%2Blj%2FJc2BCpH8mEFy8Oed1xe9ZZwctug3Fq1EHR5qHHPTYtYjod%2FqX5l27yqIxw5LzftNeHklLNrHlfutkTYTCgoqG1z7H3FbMPuRBWzceswQC2jS2PVrqRUzwZe0UohXjSfjNG%2Ftxw7Y6awt1A%2B%2FLPvZA22v%2Bc%2FhnRm0PxMFsyJEclfol%2BheJ3jWBTQuIS0Gl1wFBAmpg3dms9j9NuBoSlLaMU3xqm3HGeFERvb3g9ywAruW52p%2FyUzYScf493d92GM3sNi8IQZ7bgAqSgVUSIdMspghrhvUZivxmRMvAxDos7rTR3lrB%2BNSJVoxN2YwYdATHYAcnfBo7CeRKdKB0ngdowOuKMMmoixORKW7RDH6m4%2BRpygLnsbqOL7ieSez0awaDqp5wN00D3GQp7Bq%2FfcCo%2F0rl5qbqOjEgFFCZ1haDwQGwYxIizjCw%2ByzeRN4599Oo%2BwFsWahYUOzXSSpmMl4MMPMnmbqs7kHFZJmDogH5%2FAOIFMMPhLPb1hN7dU1A%2BueCpaLsWnAJcufpMwoIOo0wY6pgGMil4nmStFTGkvim1dGX9shOg4E3bphAwdE2rfb8M8lpI22vUtIxrz%2BseOlMs4qFwTMDMvtVr19RLkeNrjIxhjbuNFNzXPb7Cwy70fN4BUawv9P7AR8xBEJB00ffzzs3daZcykRJ83EQHlqQbTPKr%2Fc3NSmW0ruj7lEVu4p%2FvKObDLtbRnee8I2lqPpG836fexfVRGatYdYvLn%2Fo3hx3HT9yIQZamp&X-Amz-Signature=7daf5e9774299e7aa35a757527499070221a4231df96d72b975cd522ac844af7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
