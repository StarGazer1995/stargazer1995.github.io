---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YJRVVTPU%2F20260816%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260816T062018Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJIMEYCIQCKZvuw8THd6h6UBKOvUlm5tMVpobwrCfQAl9S0KwyBMQIhAKHbsRcic2q9Bug0edcgALh12C9bg0UXlewjd%2BINGqVLKv8DCCYQABoMNjM3NDIzMTgzODA1IgyxmZGzIj04Wi3zNV8q3ANAvMdG92aVi%2FM1uMhnDALgx4oQwKvevSsW2CtrEOOSQdnyytbozJJH3X69spAJe51CIXoaH5oNUO7%2BZyJKeScgDKbFobbr%2BblfCnMEhLM0ybZ0rMQUvP1MiC16V3R4J%2FVWJkSmWEn63aavpfKw5xNJLh1bvjsDMeWBOTOS%2Fz3Oaf6uYmOKnO2gPacR2HJCUBVIAJdu0XSMmuyBYPFG8TbSzEQNLfcFsCeZBa1IrOXYRXbDIolSj%2F5CeohN1aFzQ5R9K9pmzQ7XtAp9nngW34UIh0N8ipA4h3IDe55pUrKA775FKc9MKw59okC7R0myRIpzHTLBLlUFImvTPnDi1wCp3q6g05Zl5E6Z3WrgMXVJi88%2BrnWTw0fHI6hh1EukyelvAyFnjSrJtyCS6r2G5UwD%2BMM0sTcjxtDDL7dISxzB8bm5x1tf1H86tdB0vhIS1LhS2EPkSjNogcJ64Yv9aZMvVxCkIXhyo4OsKSVkwZ4%2BnyQbRohqnGcVrEdh74z62JWqbqu%2BkKLd%2Bce9xm3lx3LBYU%2BX%2BwINtbYCS%2FHTgT4JBWCF3ugsynTBmNPLca17OtW0k9YKp7pCD%2BeuXg8GJqDOhABGtnb6NF06nbbomNWbW8ajuBl1O6rEos2AHTCOg4XUBjqkAebIpYMpAcUC0ijbmB43EUHaFKFadNb%2FvQFnb8SMQT36Wl06EZ3l63NC%2FhpfB%2FsJiwMPIcooESO%2BCpXlmRAdC5zamLDTubQhL5WCJMpPRcQ200PgqBFvSUmpjwxq4HL89SdC6mfS7GqOPQbtU0fD471dCnfgyQjArjtRkmrBAHXswQsibxSEruQSvd3k6r0glBaDwhcmOdFaoFjY4RhPYx46VjBJ&X-Amz-Signature=ea1e114899de82c906d771e3d565cb868c4f84a97a22379854e596eac56e13c9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
