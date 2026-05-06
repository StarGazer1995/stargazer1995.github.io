---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662EF3NGIL%2F20260506%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260506T132707Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBH8M7%2Bsv8Z1xCGgKcZgftg33o7tvmysW%2BDVNxT2QO8OAiBa2lJeCxZhAlKBjaAurlCsd7JKr87ET2Kims3Dob8H1iqIBAie%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM29Tum0t9vEHXL8flKtwDOz5BnvmV%2FQJuHCoJ38rD9hwAdl3i5d0VjxiM5baMS6tg3GU%2FdfZ7larmgqp4xQihxtxiSbI%2FeR4kaeihetknbUVBITOdwlLGd9nuBVGvNgyGOKAl7DULSBIsK33R1XJSWre%2FMTAqRfPTIFaThAZxwnyshBwjoetg9ywA3FLB%2FBKResz5WFdIc0jXQDZMtm72JhIX%2F98AwWAqESjR4OFiZB4tpGXw3yzEY9tkX41w1qblR%2Fmy8jU8uY%2Fut2EHpLOO5NlxsJDzhwNoA1RuXTDx909er%2FizBP%2Bn76qXT%2Fr5oDA%2FWvlbqtxccb7znkpbKsdYTaeXwkZ925qii9nAjXLPEyz6wvhJzrB%2B5GidDNi3z2PVH0bF1E1AFyTB0AKt05cF%2B3DA7%2Be9Np88U7tAkWKfZFZnBOhb7oFYcse1YbHWmHTpYL%2BYWi%2FRyCIqFV3iiD%2B%2FOEp1K4BggB9jLpG5hk2pFTH14sHSq7Ua7t7ikofiw8jCsvBDScD0WVXNl60z29I2dTNzs1n4eTMOXAg73LwJlWtJiWujJNkBjEAdsGykpVPSxvyqc1RaBbx7xdzKK6FmgvmdXb%2F7gq7%2F2ouK3QNd0zrRWXJg5EmN5wPuSpdjP6sNfjBnAkWmE8PsvhUw4efszwY6pgEdypN6xEmkH5qfIiakvgyuzRUTAA66fKt2mKykqmdpCdnS0HIVOBD5Sl78H059PU02aYZuc90ANJxLhcJbNSBc4%2BVCHmDYxzRbqLpQ2ND01KwrJcf96FSl7xaqcCZgBOBYlf%2BGkWAnLyiIjqmWELPfKQnQMIexaFEdRKmQk2W7oFojvbsKdWCJ8H748GDRB8wdEp3zs2COi%2B39xmUHDiutnDmQGffZ&X-Amz-Signature=7117d3d33d2aa51c07b2aeda7a3ec9476fec730941ee09fa8478a2e32652277f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
