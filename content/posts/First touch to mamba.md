---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QWGDC7S2%2F20260506%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260506T210206Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCWV38OK8BDYK5S8X0h1i51YiRe4LMOHDuG6i0DiRqpuAIhAKYHm80VpfyhMUMx6SbE1jGgcSbSVHKWDmpGpFW6nw%2FVKogECKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy1O8yPAo3DRzE6NiQq3AOlF6TjsfzScPPDAeDffPcS%2BcWWCsSqvFVo0Fsx8yW33ZdtXc6tALf6CBe4u8DbNzQlEqq3LwG3m3RvOtpx%2BiryBiz79w%2BuNrUc0%2FrXxGvbV3Hhuc5XphJcTIeUdWcrS8wICAWcAC9cu0OpZqhQd%2Bkb45I%2Fh6O69fG0MK%2BhZa9jz1KoWqkna9Ek9fagikF5uyJBskfK5fmeViN8ZmpAAQdZK%2Fsapp4MCUxxQTkAo3UPG%2F%2B7XnjxTu0i7Ehyie1m6Kw3HmOPQfo%2FYcAOjneZ%2B6LwwYgQ2VqzbG6abOz8Ui%2FIkkDDw8Wfr5hN20moaxGrznpiaf5WB71bMuR2%2BtGPpSEkg5WxatW4lics4TN4XeFNLmH9A9ac4rNxG%2BWRMe0WwI1lt7uQgQ6a1OmW2QKxU6jIqs%2FG9SpbchNMC2HdHfUy93w3Kl%2BMD55Pz4nQFTRnu2GfOM3Jn9tDeRIRm6tYdMtojJ9gT9jBe%2FS908b2ER0gJr97tKh4FsOLdt5yaWVEwZPPam3L0ISegIImIqyBf0dbW%2BQDdpbNq0S2OYCZyUOaj1TCK8cxmFvDzswpGmkg6Zc7K81LpYrh%2FLBNlQ6WSnVDk%2Ff1rzsbmB12zMoKjELNFu8cppa2NgMN7yFVnzDjyO7PBjqkAUzBXPc9tEDVZ69iOwEIu94leVqVlV1ralPWHUo44rtXo10oN74a7zKOvCsE7HUFD0gOwEOpStX5rmeAZVpJrN7C8VruwWCIA7bXXhpr3Cew%2F%2BQIExJ7LoPNETKArECKzfHxiAhYhU5ZB922uv14g9%2Bz0HJRrL1RE86mWRYlMV4Y8sfx8bBZwaTikJU9dGN0SBRCrFpGpmzsYR7BAvAqirNzCLvB&X-Amz-Signature=34aac4c520e134779e63a3252c46cd87e2cc5b1ff940858761f4bc340bd7cfcd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
