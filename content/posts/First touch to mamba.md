---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R7F3EZIF%2F20260727%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260727T014646Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHoaCXVzLXdlc3QtMiJIMEYCIQCp%2B4HJXj7d1ptvCz0zMHrF6G%2BRbytXTsFTiLXMvctCYwIhANLRqxr0zPYAHc3GzWyqhQJ0Znr3tKBjYfMyEdKYObpOKv8DCEMQABoMNjM3NDIzMTgzODA1IgzfgF7jdKA85g%2F6nb0q3ANpv73UV%2FVpFDMYmeNqMSi6Wicirmx9vgbP8R5NBdd5hC7rbQskArUiKWF7z4MSGxXGWJzcW%2Fb396PadXngarlk4QgTl75rOLcyPzSBnr82q0Ow72%2F%2BFqd9CP4ON0h7wBUJs%2FEAptyZpGGrfZjq%2BMlt8FQKGFta7J7Kun4xD43IsptIS2i8d7S39YSW8u%2F8OfVNI1JBMx8%2Bd0uaOcaTFUdKE1cSalhJViBAo8OrB96x2CT3oQIKwIhy62NDiM1Ej74YYoP0JZtN5eG5KoTMSpknXsvxzDY3cPp0OKpHCkWPR%2Fv09V7Io9sBFoOh9nxoFwDeV76JM84zB8bjc%2B6DlfC1LW7V85SqHhapGrACJwW4RS6Lygph4vPBJgTnQfCMt2B5Y%2FXCXPUuzVkvxaBAwmWz2Dwe4L7%2B5XGqPtrm4oK2klFhePtNn8CM6HCWc9RWlLyqMB2p0hhxjbTWXNrguzxnyGbCZFHNQWY%2BKQZ31GqvcnWPaasa95PdMy%2Bz5FFG%2B1OxrkQwbOHgqSTCrvodp7%2BOG9oPYGxVOCenuNdXDu%2Fr681d%2BoVObx%2F7hzJ9mdok%2Fa5Jk0ngZqZbRPn8clUJuLl0t2nZRKwd%2FUgVrXhfn3skASG7q%2BHiixEoDO5AkTCt65rTBjqkAUuflki4rve%2B9hQmEuxemM170ulW1r7PaVls0HrSadBldbnfqDAOv9JCs8T9uz2QLJl%2B9LZeKjPOvt4Lj7%2BEeDoM3jGga1QdKaScSU4u3kdugpvNq5E%2FWNnC8195%2B%2B%2B8KHAmdtsD9LQgJsBq8C9WFwDruiI0UBpM0%2F7EPd7JG8rP%2BEeq5y%2BRGYPRpvV1lGPislpXv2%2FN6HfwilgSViRM%2B5ztRweY&X-Amz-Signature=7f04fb837de4f139fc28672cd3ba45134cd1b7db17d680cc0a761718562d687b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
