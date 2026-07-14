---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UFHT5XP6%2F20260714%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260714T130242Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEgaCXVzLXdlc3QtMiJGMEQCID17Xo%2BmEF4ZsjyLR44bIpVSB93%2FZjDABsEodBuvRa%2B0AiBksy9mOBQ4jxnNX8V4kN%2FQLY4S%2Fb4LYVhWrMenqCsDBir%2FAwgREAAaDDYzNzQyMzE4MzgwNSIMRZu6kthGi9xm8TWkKtwDLHUa04bwvs2Im7gYId13cu3Nc332mllmCamCko8T9FrAqF5x3BlO0R5HLUnhdSio3Z0rISzsU2M%2FV5mIGzpPV46S91TmpNQEODQzkl5kcBlh97Of92AYqgCnwaopFeJ62bm73GGOD8hgeXwOn9NMjLC48xXoUq91Wu65yeeUvv6AfCrhuoYgwa%2Fm3Qw39bTr5409EurFSIsGICDOLy%2BVtOHvm0bCpn16je0y%2BsyXjbhZD%2F%2BUDizzEb7lQFDL1Z1pRbMLJDliefnlB1L3SjtglMf6bDR0CGbe3JY9%2B5EcDXtE%2BDArXRtZdsDGr14RF7%2BAol2gAM1ZqBK3Qhqaqrnv3qSbdzaW3%2FMWTwGacfCOVnBNfTs3Vs9%2B5TskHwHvovevIGVbuXn45e6FfXvKP9FscFR%2Bz49d5NJn8Fkfb%2BitekA3H7KX6XDjiIq1eGQ6mSVUIT0wicw9TbIGN%2BWb%2FLP2f16nxuQHoE6aojph75%2F4U8gqxNSlZfDDIwMcCujIRVNw951ViHSBy6e9S1q4aUg%2B5XT2iUJq067SeDiciMyOgRDByPzHWHIbivHgriF%2BEVW438ZiTK6bA8FrbbXOh%2B%2FVT7CenlrRklvU4Onr3hFiDcZMwL8I2ieMZDL2eqYw6szX0gY6pgEZZLy1tq4RhtuVdrCnWfoqBKBNloRzeeO9d7bHqwXEF6w021vLM7M6DqX1VpJl%2F6myT9p9nVqLKoM9AAdUGE0CPWxhgqNtRYcgX6P4Jcrva0D3xq%2Fu4LvFLt0QXjIWmDuuWNVq9%2FKVepgRH5bln%2FJ%2F6nikMdMkeRfSaCPGeO4RWr15kCMoSap1TT9fnYIxhNxQhMUShNha3iPc8aSjmglUS7cRdt3K&X-Amz-Signature=77cf912f966df7f9e5559ef484574b70e5371fe52649aba69d4f4cecf81b02a5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
