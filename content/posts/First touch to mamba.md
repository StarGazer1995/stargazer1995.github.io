---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667GDOUE7V%2F20260626%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260626T192731Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDcXcubAbCTRQ4A2pC7zT45vx4c8aKCy40JgFWj31GN9AiBLEHEhTAqG4A7frwC9h0AANv%2B4jbdaAsFupc6%2Ff4wrcir%2FAwhsEAAaDDYzNzQyMzE4MzgwNSIMjFPRkpeRP1accTs%2BKtwDH%2BX29X2CaRh%2BkxiTmMmV0vw7vrNPmr3qzeIUHexiOYVcKTibj4bi9gd0kVQUpT1fNem7ootbg8bVLnBph021vtmf7FjGl5Wd4fsiT9747vAOT8ZvItu2ymR9Tzfy9cmyARnJ4cW94EKeRkNu5GjWoFXOJY5MHTGSQbgwYwuywiHzJkT1l4u%2Bdmg4zYmKgDmAvi%2BBpnNUkrdQYKw1Z7LgELYMoUvj1zvcGhyjvMCdTKkZgo5MprLbKkp3RSjfXwmUd5i0C%2F7J3vDvlsiWfi5L640qJL365D0GgZTi1mWxN6BtMl1fBHPsdIu3ibtuPWaYp9RTs%2BUfrwv21F%2F%2Ff01m1Z6m%2BU%2Fi1dsdbIOz%2BvXxxX6cdJhTbHzYkojTXMWQrEewS9sTsP%2BcWa%2F8LaWjzRtk08GCQVzmm%2F1NZdCA75lI0cP%2BBMO2fOufJQrKLMOkQouzs6rSBbINumOkc5BQItr%2FhKXU5BBhDKvXKOSerQMtvlMHdgIXKoGOECia%2BUlGlSYitWobcBubBbuTG66ggJ%2BIUnge7vdxYFx5ty32a1Cz8Vui7qmQ6ECZPCkhel5nHDDHJy%2FlCJ5XHZugrDweQGvA8n4ht7lE3U2x8kZH1MpaPcI8vPGDO7rYvK8Ergkw3Zz70QY6pgGbctKgR3bjXmFAHdKExa9Uu0pNrzzSsTAIZtPEAaALCllWhQIxQQizuzZdcRSCIFlzowQX4bmrfX2Xsp%2FAsE7eOC9ZhMUnXuMJq%2BaOH9rCwmGxF%2BjD6LC3UbBB%2Bm%2BTQ9FkZkTmwLhKfmMR9u8L3zdkCo19brtbggRMru7y92mzCqI4gGr6yo%2BveXTXQzYScPyDfl1DRwQGsim5hi3RBaTNUMES%2BmAm&X-Amz-Signature=f21feba2e311a29fef544b1d136077c90bb7eeb70defa85c415821007d2ba93e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
