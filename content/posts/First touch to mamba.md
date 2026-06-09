---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662VA3XQ6D%2F20260609%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260609T195502Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAsaCXVzLXdlc3QtMiJHMEUCIGA0kKWR8gQI8cEQI8kQ%2BnnChTNBm1nV%2B%2FHQJ%2B7T7L6mAiEAxXEouhgAJyI2SW0atLHRDuLftaOjx5A%2FIQKE7JHqQB0qiAQI1P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF3xTpYxW7RVKDPOqyrcA670lM1SRjrlOnE7NeeZuhaob%2FKYbU3wKmL8funGBqOUDknpy5kWbmHrTyiWKQPml3lUDDSECu7%2FbKM7HePETNUzXfkA8nTBjktngJlSWbpCRwrfQiwB8kHIT9qGyOUpKpeLwv1iCGY54jFtG7YSyhZKvclmXMdXOLmYcLRdwiwXsB%2BpAx9jLoQXVnMtCPvOB%2BYLiXIvT3%2BGR1svK9k0xAtHDII3hCP9TVVbyRXDcwFS9O1EhFXT7%2BTEvC2zP3jMPSH3vvtVMUsQohA4kxriZ7gPWW%2FyxK2FSQlor1291bdqSvDYFmRXh4brt5%2FE8Nl8HeolPPMtBP5SnXiG8QJizNGjmpAkObNxM%2BA8qVr8D6XNxaaFrVbEBxWed1fZwLOBVQnNGHsMnlELK2JfdKsXRVaQRiD5t8ZhELRgCZ6Ig9tAQN%2F1MG4gFTfFKHgKfGRtDhpWJl2wR7fP2X%2Frji5ionkeOIFvD7l0t8FoARHKIezuDLzlGFP8B9Wc2vmD%2BMgUe7jdH4QjrGCYY7ii6J4UN1DQheBcKOEqpwsOnKZkkfqmyrw9jw2vwWErSc3lbT58WX0L7H%2BSuO3%2B2z7kgKRqvjJJojiqf5kGUXUTsltHxr%2F8NG4GIlaQFvPsBb%2FAMJrModEGOqUBMNhRx4go1qT4wBrz9gPsj7WmIAcoNC5RUeEIc4%2FbFavQpDF1pfap3FVd%2BgDIJAMgwGd6HuHq%2BengI6XFP1LI%2FO36mQCSfE0JxJBHdqUS63CnQlPWYGq8MnO48G5kgJNBQa0idzMD%2FwPohDDUwhGB2DRoHAc5zc%2B3%2BN37siwiIvoWW6M8tgOHZLrnArlVqFlkaaRRwjpI6uul%2FwU55VvLKPC8azzh&X-Amz-Signature=d0283b4dc7aa4cf1379f9bb782926c8720178c8bae3766c5a50d36f3fc4506df&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
