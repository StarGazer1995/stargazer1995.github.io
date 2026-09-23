---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46667TLD2AI%2F20260923%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260923T191831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICAu%2FtNStBC2pe5q8aJuoVkg6HgWMk5RhwUOEJNpCOeRAiBqZuqHVSYmCuUVo44ch%2B5UMHEU3vCl%2F0Kc68MeJJBMYiqIBAjD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMT3PJHlLCwhxokY%2F7KtwDWIqfucTad7XHsVAD%2FJddinPCIZAq9NMKXA0HklfC9rH93fCnCTrUida7j170GTov7wKoyDJzkzltflgplTeITCzI40GjLI0sHwKTG7P9gylamX4iNeeNSHtRJ4yNae8Zp1Ho6IcZr28E%2FnqcVGTdO3m85efqxFAZLWmlNDihuhrWcyy3qupCvXTFpYl6sii%2BcmIMiNV1JOES26pIg1XkdtKYghaE5HWf%2B%2F8%2F%2FToOsofbzEr8WxjA%2BouZj8Yh1b419MMOrhSzb0H8kUJwveYUO%2BQqAWPmcTvLMkCCm56ty%2FUgxXSm1Jr9FaXyEwyHRaNYYZVcoo2xpX%2FSF%2BitjZbDIeAVW75HGmSpCmpBJ37zC10gg2Zb0uWajYuNQHDQxW%2BVH85EJ7vo%2Fj3Y2jtEnG%2FraWfxWcUUtEde%2BPt0dBtw3FgKVosC3tggKD%2FYxzpO%2BPsDlMPmXYAS1xxiUWidvI8jKDRLwqnkkNO4r1PdCFIYd2HWNB8wLHhSVDn%2BV17AWJMZ%2BnjdLhrLKuqwEM5%2FhOOLvCzzkhyirX5Io%2FIlhE%2BJM6euE2Sz%2F7mHI2wxoPo6Y4%2FWR7VF5mCE2vj2fck%2FYCve6MUJZX%2B7jlxDDBFjlkikLVewyUwI82FVKSXDTmowmrHQ1QY6pgGW%2B5uUUhJjQEud%2FFUufIuZgX3GLw3FvWuELvyEa%2BMWD95Kajd73Q2R%2FRQcU4EaoxHxYFCG%2Biz31m%2BbURE%2BsQuw3gAQDRR8TrkCab2gdq5URyuk%2BFvTY9TLoHBS%2F7N2hePHz9NqSS%2B%2BvOuPf%2BDWkV0I9antxI2Q0fLYZcwFLhK3VBLxnWBuLvJf9m2Ao8joFcp1tal8R0iGlFb4bgvxjRKvhl4zzl9Y&X-Amz-Signature=a52b87d800a2d3772d7841cb4877ff5679e10cb7d87d002e7c52422353ce743b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
