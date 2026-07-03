---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664ZBJOZ5G%2F20260703%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260703T205148Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJGMEQCIFWA7wXPSTcGvp3MMIsfsxODWazOF1%2Fg3E5lUpCtXJZIAiBm1NgTcsi4Hr1uU3ePHa9sya%2F15E2qE3hm7mL46PokDSr%2FAwgWEAAaDDYzNzQyMzE4MzgwNSIMQFl9kpy4XhwWtT3wKtwDsGY9UNDKIIGyzwKX5x2P09knErowyCFzvB1oc3ZTwM%2BnNFGoTmAmvE9CcEDN543MeYfzAQIS8UhhYqOxWee0vc0fR5nsE864QHL%2BXEJWZox0OIzWn0t39XfODDGIZA2hlI61nwbVijWnU57PeM77NcaobUNsDWmrrbMzELfiZf2no2GEhUKUP5VzLUVNTP3IfvHqZLpC%2F1IVy05nURWhngRx0R5Gmz6ZP9IZqK4Kz9MNzF5%2FW0BlljZ4Eqb%2F62m57qTpprM2S9wMMpLUCrXp3zXPGsQBhQ%2F7zltmILwqMF7ljgBxE3WieMhyjvTz7UuoqYfhw%2BJkJ2dJ6NGcA1x7o9DR3%2FiRAIIodnNRpxplFVMihiccEDXV2%2FODT6JjKJQ9Kk11irqk1bi%2BcWYllkFiCCXfhz9JA5EB3ySimYp%2BM%2BSYn35Xj%2F5o42EEORkgHlcSN4uWuUOFVNxAgwDfal7nyFt8hQnhC32%2BDUu4R4iu0iwx3Ulo4WmTHdOwUyoBiAeSJ%2BGYmmGTg%2FB2LEFfVz3Z1Z4EBJ2a118vWcePwbz1vzPNX0%2F5ngTbb4fdRBWQYCNFuglROPXEme8YtcSya%2B%2FnnDVy4w8ezLimh7EP7rKgIMsBTYTerA2PdWUV9ucwyLWg0gY6pgFy99Nls2BWOKgeb6uNQ%2BZh5A8lGOlmALS3IhkwP3MPrWrahOKA4sinyLLv%2F8sba2skFrM4n2IHhGxLOMZGP0UKN8vtaoxnnx0t%2FTJf5ijNUtajdlqDgC4g2TXiXu%2FK443sLRRNyHMURoPXk8l6%2BiF56vV7GXZvxCgIzHaBr%2F%2FPOSZj8WmRM4B3D8zI8rVtnLi0eSi82XQuSB8%2BYVRCiE7iIeJqzIyJ&X-Amz-Signature=5c000b84931515ec2f9c013992293557f20c3488009b8d68d2b7e69c76d48520&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
