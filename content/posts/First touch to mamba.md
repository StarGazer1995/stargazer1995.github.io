---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665KDHI53I%2F20260531%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260531T204739Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDUaCXVzLXdlc3QtMiJHMEUCIQCq889z6kxVfuckD9kOqZflFwhqI5GHr78Jr7Te0gmcbAIgWagCqB9xgu0ODyBhPCh6gzBlI0Ov%2F1JnTe9TtW5zIt4qiAQI%2Fv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDN9wqawpiRAvKl7PhCrcA0Xe8Rub003c2v0JDjSiWcCR8hpT3pX5vPAGrSTDqtTkhabSBrvB4UoR5YQQYIzdxxyP3E6B4ijlwYinvOk%2FsdDrTUF3%2FcRiyDEtt%2BZhFQsFdd6K9tCciiYSfZhs%2FouqTaGXpmigIRx2SC4T84AbMuqR6BE98fvC4TbyIn%2B1IcczNm1PkdGtdhWVwFTWnoqbxh0Pk3eVIPzBfN23H7UYOxzmryNBBhTt1agp3X4i%2BTSb0p9hp4S6GdH9f1UaMK0xa16DTjM1g5OXtnNkYUlD57J0OyXaqiMiO%2BO06BY8JTXNZkP07YoN1OjxWkPS9WwLZyWF7WYwsOfTcEJXLcyzgq7UqrVQc3%2FVJLCcHFWHRpjuRMHHDyZClB%2F5E2WXaQ3Pw8tes8l%2FBYo05P8J4IThWZziCK4E7QbxqdvBcAqZcTZg9gRxAFjDjNVg9MaVx66VNcEOsRxRjvqLUaCADMj4J7PMERIw2kBNmc656PQVlUh3iJclYamEJHZJOjaM3hvAFwPM%2FJCnN7WNiPS4VivIR%2Fj0Zd1bhkZjTgaDX8KQoc%2BBqp88JHhoHkyrgv%2F9JbjrP6XKHMlfocpbrqGjOSY5RxMwDwdbFV9PzGV7G56y1knboznpeIGFvlaxVOMtMLa38tAGOqUBZwWAjO9azKD0qrFKpdK2DNElrw2Dn%2BZP9ZL%2FuP4gcv8PNIiWgPdsNa5yikZjPm2PjWD8YxvVrFZe8bZIQcEQtih7mc8mw3nZG08UktuODFyhJOkaUMdDw47gDqEkFZTixjWOr2%2BbTtPqSmAF4bjEU%2FTf0w8RflMYItGKzp6oTyj7%2FS%2FOxphOH4Agao9fDXLfIE3zm1DXDx8zTvXmPoMAqI%2BfymM%2F&X-Amz-Signature=cf27818357c701b11b3351042a07455e161ce48f3c9af788ae13c660385071e8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
