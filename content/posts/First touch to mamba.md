---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UUU53UUE%2F20260525%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260525T205746Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIG0Pbh%2B8AhG1vt7%2FwbRJbE%2BYt3ofwf6R9ur%2BFPMF1xLUAiADaDQetAFMq1szXfRL%2FbdGxsZz%2FmXvxe0LbqOcQM8O2ir%2FAwhrEAAaDDYzNzQyMzE4MzgwNSIMdFuNnTdkDvGxNCd5KtwDhdaVbkt4OY%2FIpZiDUFCCM0YKDlwb3lddQI4pqhnlSdGlz65YWFxrFSPI%2BT0ndtk2%2FPjDjpZT%2BlrZpu8rFMqrhpo1ity5ygIpWY7Wms%2BZ1zotA3NDyklHo6EpBwcmTd9%2FjpkxSFkrGrVHoZ652ZA5VaL57R5ap9AFjxMW81qJ0gQ4lauzGro6VsNvX8iUXO8UxBk1VOxVwapSpfMqZQX2jMAkVHjzKu3dkJM1f%2B%2BBhOtFsH4M1S5OS%2FJ9K1o5rpL%2FkGWA4jnoY2lbQnl9GaegTfnN7PSaNrWV3zjcC0JoHkTODTINSVJrYujYTxp%2Fgmh12Gpdcqxk3ou6f8VqtyMjZ6VSGGy%2BfOV%2Br3n2mSMS8tTAn1RK5rjnTTHR9y9xK2plgKxZQ54IG%2B5KrAlDLBfg1kLz%2F9jt6gW6PvFA0zEi0XJD%2FOp0G6lPrp6k0ounJ5Z6q7JFJQwLtZPyztWChySejZSdTY7uIVntx3cN3i5GSRQ7jeUcgmB6Oo5V4cYNR8w62htAytQrb%2BWAh1%2BSR4UqZm2VFzLmjrVpbb0mlf4sGVwQWyVb25sWBAnfGSeSqk%2BAr25XEwXjYcIubFGgrhR6Yt4%2BiaExeQKOmYEJwY7IcPRsv9XMvs8nizcIskkw8KbS0AY6pgGz8uLtMihS6Kfrniu7kHtfDJcmO0b0T1TAdMmGUCCNxZxdIBf40zL%2BBU4UVd%2FJYXOvz4lmhVFb6AK83fGJw0zbYsy%2F3Ik8KnlcDxBiwjLGWTzcP2DQCIj8M3hTzIHOhDdwElW4RvuuRrGTYhfMqfTiF1z4Ngr8P5Syt4HA5NvHEbl096NBB4RULjiC4KYX5qB1Tc9c%2FJuKywewvju0etud66tXjyIr&X-Amz-Signature=6df89a250425e67835e10b9fa9ea05e24998a8eca7d72e15db33e0d150a9469e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
