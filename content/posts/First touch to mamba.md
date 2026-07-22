---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663X4DA4SO%2F20260722%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260722T131758Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJIMEYCIQDa8tEwwccGSVJmhqxxWBVQzxfP%2FTmk%2Bd75xss3JLCjcwIhALmu8iEwfNEe3B567NJMm6ECC7DUYvGwDDNySE3itbxAKogECNX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy7f1mc6hZQNelOdT4q3APsTMy1LKEOPdaC%2FUkL8kJkLtIPT3FHCkAyEJcs3jsPHeKAeD0SCUtNC9bq%2F4YNazGEed%2FSh431FyBQ7Ft%2BdTisWY8%2Fxmdxa3xTbHpekCd5Ng39%2BQ6PinTWLjNVU0iWBqTL7HSlKzdAGUjVcuzV4Ey6Ye1RyS41kcPPfwp8g5cYujyxptfc20xYOmSo6Aw2dZif2qRAR0j8uWdjEdv1PtVLQa7EIzux69huEvYMbcmokISAGnbdzoyh7Hp2idX7xHlbgUIio9c%2FBJbjR7KEeX5uQ0qiY6UbFtEeJlCLWRg8%2BLnyqPmyXOgEtnpnPTKVqOjwcwlvk22OjKfcc58eu173S7Z8FSCWXTZnh4qP%2B5k1dZfmNw5JkdNd31ZnUi401Lh2kqHXMpdbXUFqzsLiFQUFw16IM%2BqvCBe9jRW93DsOxvYURsZThcyYtl2LVK%2FbRNPOM69CE880mknF%2FH5Cy1RVRLNap7TaNCbM%2FQox2JRuwo5eJVQELRg%2FPc7WTpqCagdaxt8OMAVQsMrtP7cXD0Dnti4Bj3IKq5CHI5F5tNwGLYFhomICV3hydpel7Q1y7Lg46MDlhROB8jFICjAWX8hflwVqiunuI%2Fb20H%2BvET1Dr6%2BxP2Y9HnJBGXQ73jDs5ILTBjqkAaiwjs%2FPQXVNGBDqnaIWHV7UQJgxKHZihgeZ%2BKI1LR6ITVIjlWSV6Y1Jhn5jLdI0EFzR7fcrMw20AmbVrzNrrug8tAup6k0X%2FBeRJHMQCOBv9K1w%2BvwYr7LQ96z4APSHHRKr78im4pofKAPH%2FnvxeJdu4ZNlvnmPqFcnooWh7BcMNfEMybuHlAgQT44fgT6j48jLaseSIzR24BXAFM7xIk94lXLp&X-Amz-Signature=e3b863506c9d83df711695cdc9f9b54de343dc8adbdfe44d6ad0c87b5854708d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
