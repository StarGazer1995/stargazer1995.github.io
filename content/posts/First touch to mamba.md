---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662YERMFSO%2F20260731%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260731T052314Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCH%2FFXDxRLMP5Kxe0kvI%2BbF2cgWHw0w%2FVLcxDiCTYcF6wIgerWHwgl0Tp2y8MLNhrKTqwUs18Wj1eKe7fD5uO8wg4UqiAQIpf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIV2pgBNmj%2FzMrQ1NSrcA1kyUvQOcJom%2B1NK5uMv%2FxpiZcZ9F28HKSTKZZiwvRkc7XaHcTRZwDGrHqKqkLbJM0jlN8YFjfNqLWhjiSA3F5H5bXr5AnAqcPVKzmbun6o5SzJC%2FU1FcGfBWOscA8zwreuv7ajcct%2B2dm67OrGVT5XLPvOW3TBUuQ4TXFYsvmOZ9IPwJw%2By9JDHrPX45Lg8ILxib3rkF4AKvvlmxHianwzLTThBni5QnocMSljexcsQZtMg4fmhYfhZJximkrE2RwsRKcoQ6i8j9BI0hVCan0MVzhOthZAahnQ%2BPfDwWeUrIqY3XraEFz9D32p9ktvUTnmSK1t8PC67xHPeeNovmCn9jlAw%2F29bVNeEA146IDhvHYPWZjc3QIfnDp0I57oWt%2FLP%2BTpMrDcFkkZy0eXR4JtemKs6nkV0HGr5QOi%2B0dnx37Zw1SpdgC4MI1tJ38F%2FrOiPn0Ek5F%2FFQChvdzDrN8dAL4hWMCGyOsY%2F8HjcK2QOCHGfBNy15xWWoRMfQqqcb0YFHgoTD%2F9X38KfBTebk1urNBKke69GkPo4e5yK%2BpxLhMruH9NcDtHBp%2BSrqx21yaUl3CGS8t9NEOfoFPIRSbO%2Bd4DIw%2FSeJgyGUN%2BfkWNsq31p6Yss8BRFpodUMIK%2FsNMGOqUBFPNUVdNcdO20%2Bk%2FMLoHtafWobNGW3M6PGVynofPlwDidnrjUkomcDvq0HQil0oZBTg3Zeh8CNvlob%2BW24CuhH4ZtWot7UyEo2Mjh3AUPRNfQ81AfvJdRSsejb3w%2B6CtiEkeQVC0uQnJ1QKMiJcu6JxFsOVJOnjDYsWgBkuoxs7sKpn24UYO7lPOnYw8nQh2DRhf6NOpnoILg4AJcDaIpBY5siE1z&X-Amz-Signature=c1edfba4ab3e66987a0f4303f935b5480d18038218d6402ebe13f87d1e5d3206&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
