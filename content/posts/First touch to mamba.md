---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RNPHZPEB%2F20260622%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260622T231146Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJHMEUCIQCW8OGCf8vJx0HFVyLW%2BfUM5cnXlvmm6YPPl%2BsS5xfzUwIgZg3pGq1I2FEhpwXNLCLjI9cFK8NJzM7Ki5D16EqbDLYq%2FwMIDBAAGgw2Mzc0MjMxODM4MDUiDCzKsV1SCaRx9GqrZircA260qsDiLL7rLucNVvgpnIhOqlMfQ5N%2B%2FsSAETlLkPz9wesVkYbrmNg5kKwdjjzp8ZeCL%2BuL7aNhWZ2rS%2B8eLBzoETBsvytMDSjwQ7nTP0swBBhL1HYFan%2BZPIcq4SWo9JAhuBw%2FcwqNyxTin%2BHQBaxocJUckSyr3zT7kBV2UISxbEQrsIddpQWY07G4XhDjhJphgSAQRBgam85AMAAu1Op%2Fw231lJcVBip9sPjwQ63n0T%2FnpQpTXNfMfELljOkw%2BoYwPLlVYHURGJpuqf7taaDftS03kjWlg5Qiq6ImDEbQ2booYYCisf4sVwY8pv2%2F5xjVOt91pLfjqftZ0XvM9rjz9%2BouBMvTZK%2FAWmjaJCcHACEWJ5C03TcXORqjTYFkMWemPGz49GHlgx9A3mv8X8gjR%2BM7%2F0MRsF65ka9j4GK3omBdbMNVvWVZhspZ3bg2mC8ilTb0B55stlMHEeauV5XMDx2BUmO1L%2B9ZhyTHZQXCOrIoGzSdXhDjG01pEAJJBREJOPj1sOetjKBLTEU5CDC964ODTNw0koTFJH6KQxzNVAsMzJXh4rlLMejaT2Ja2OwwMzKlIMuzs76gtpbgT78lZUoBFWpZJYj4utlBQkvZysqvJNYw45cjRF9oMKWN5tEGOqUBMfMScGL3NnYx6ZfV2f1a%2BuIg2id2jHRdMzahio3TizGfr1zy9DOcNMBVdVTb%2BBxL4ABlFlWVXbjVzSrg%2FKXFgMvA3xyKRWO0LlOSD62eoWlt3BLx4Vwdy0QnVzauH6795mdUWIgkjbyvB8XhSll0cfZIzVITqgb51hZ97p4kJhuaKCBuwz3P%2FjROKAcnoo6OjJSdj7bNIgt3U6EY9vDAE3IKukqh&X-Amz-Signature=69449372e994e93c9114a294e9b524530ae0f456aa006b72528dc0ff1c77d088&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
