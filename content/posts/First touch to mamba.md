---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U2LABY2K%2F20260623%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260623T020049Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJHMEUCIQCC370oxoH%2FHxmdoROVeuokJOsfY%2FV8bIWjxePNJuY0OAIgM7eyHDaZpCcgVC4oYm3%2Ffw9AMdCQUhG%2BgfNmza%2BGTp8q%2FwMIExAAGgw2Mzc0MjMxODM4MDUiDHozKi%2BbUa%2B6yVmfsSrcA1n53WoZJIMKEKsHDCB5UpHGnZJFQHycyU62nJlbliMkPlwGRVgQSdK%2B5G6h7pPfWp1jX3BNSqRIups9aLRCtdru1z%2BRKOmSC9JNFbkGuH2qQfbZKxshejlHczy%2FAKT11MwaY%2BEqLlZvoFEWS4ZnZF1LVgl2gan0ATrdO0OHlB2sHzGIi7g1X%2BcjTdQoFLEMiHlZyn1gzaY8ds%2BsLtqkQh0a8HoU5NVkO8NHAoWZBRbnGFOND5UkT6Y904YCO7Xkj%2B8l6x7TFDAzhpfnz%2Bt12GNFrjdIkmtcKBPL70d8vSHD5cKZaDFXTGB5z6RRZdFGL%2BwfeQ%2BIMlRJVIsfwqF7IvBIqchMnulpFy%2F3VFL%2BUfVk3GRXt8f9K2Szd7oEFlztsvZUk%2F4T%2BFWhuuh%2BL5D1nBZbMUSvc2E4Rdw%2BLgvsQsCsEKWPIWWr2VQ5oEROWxp1Dr5G%2Fz%2BeMxR0BQ3RMN0SCI34e3hBSV5UtwcAQwCUnohkG4gTlH7976inoCxQ5wVePyV%2BlHoTjdvKzcbDSMQzjqzIkz6sw2WBbuUHaywOHDRjMIXZIrBfTa%2BTeu%2B%2FNxwIL%2B6k%2F7dsYnDVKTTCTNQf%2F4P6YGf1NJQ%2BaQhUM6NURF7rqr5p%2BbLqxuJ%2F0I6iMPzG59EGOqUBpSNy2DQeTVQTKut50fJA7MHBKkWJot0nwP9SqM4mSNQ%2ByNfCVp%2BcDnK5nT5vbiaiuNP4TY8CzVfP4h4axWWO4rgvDrNv87v2enInjlNyWrSmD6%2Bsw7w5%2B0UBQ%2BWxnDdG1TPr7MKUicDxuCJKPC7V1rrGX03SuwWhHz%2B9NYQuLdseR0rZkuqAV2qXcx5erch2H9VfhFAD5UbYxbs1MSvtJlwvxd78&X-Amz-Signature=bc090e8c5a4cb36a52f7714df5b68a1a7dd2856bccf04608007471016885e7f7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
