---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665G2FE33U%2F20260523%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260523T224243Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJGMEQCIELqXUWDAABo5ZFzvHKsU%2Ft1enY0Gu4Gj9cQzbURIUiQAiApo4lp376u6Hk7SdU3iJaav90UqvSEHmfvxRT8DMq4GSr%2FAwg%2FEAAaDDYzNzQyMzE4MzgwNSIMHvXSnsmWWFL1ey1IKtwDGLxpF0bmXjPwsnT3GKneTOxYMfXDnyNaAhgv8LRRAK%2BRyd6uXzEm6s%2BiQ%2B8W1yYDFwIrJsiPqjgnYCD0%2BYtPPys9sR7fvkOtcZv08BE9Fs6TcldGsNMj0fRCzr%2FBJ4v%2FH1o3T8ov7%2B5KXELmctrKctkNNSVlsm5n5lHnw16byTyYy5n51b7RSggenx%2BZEgvwwhJ8EzHGEiOMcuEguHdDn61Kbb6bHvbKJpvPSBp%2BCbf%2BeRBIZEEiF8eaYNnXpLU04dWEkt4QmkskcihvM8PKQZDH0odsAWaHMdNAmoahbTQLdDg%2BKwni5CD7WFrH3JsDJ1QBpee80lskFzuS9eJ8JclwvihI2Fm79ZNu3S%2BDJvjrqn261rNC0MSmxuQqvC%2FRY%2F5Avm8zRXKtG5sjgk3VVkIUbLc8XF%2F3jlFhmBZHgC161B6pAUoVFkmAFkHItZCqy0mkvmK%2Bdm4zzTBrb4HUbZdlKGQoMoWtMrYyyZ9D7pTaim%2BNMOrntXrvua5UV0av2H8PcNFjWLq6xq1wzMOZ%2FQFFIWCfY%2FiObw6ootWJGXP1p75pyyLFD2P1Amo7gE4hQs4TB46YZGKXY0DWjnixaLxILNmUuR%2FXC8dnTzhbPhkDpNTE%2FkS46wn59x8w57bI0AY6pgFqU1HT%2BsTYTZ1EBOi%2FfTvNNH4tS5ZZGC4KXFtFbJ%2BBfk%2FIeXN%2Foddx3sidMT3V4E9RwxEGJs3ArIp%2FWCNqsZxR7p5N05PtC248JPqVaaTkRMv9fJF30%2Fj6AAxDG4JOphjPIt%2BQTNJtpbfZlW%2BTgKlbChyEOL8FlNKCE4m%2FAuVJpJGTwMHkk7VRZH6XylF8fTNZSo2b3K2bxXvkgWDCowU2rzovAJpv&X-Amz-Signature=46a22749c54b078e864950332132946dace86ec4335cf29b9323dfae2e455453&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
