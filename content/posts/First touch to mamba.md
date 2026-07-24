---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662JPO5QPE%2F20260724%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260724T012457Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIQC0gdZKeTE3ls0tFgMFxIOLySQjIn%2FZJWk9zr0PJJ31bgIgERCLhDzT9U%2BsyvNMZGRyeKwVdSKXBqDF%2B0cYeBSI6v8qiAQI%2Bv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBdgIi9JQclcJnkMCircA%2FYywyalmI%2Fp8KGnnPOszg8MS8yL%2BO1DUSaFSEJn26Mcyi9JVmKfqNL3gEGN5XUCWns%2Fwnn%2Fm2%2BMPXQtKj8u93FCDqb18nmflQDqAzVIfjH2SRIc655KFLaocXg3Zg6DHdUSJScusGyFMVi0%2BeoaP5ScVTHKljmHbWWDIsVF7vTy7Fl5E9zVLAC4it7QaiodaZToa42OsJvPUGV2RVH0ASU2QZXb7407ie3vW9uEH8txPhzTsgmCtCfP1k9vXz1GkvUlV6MFTIT%2B39ASVQl%2FZrdR3pbfvPpNQVg6DC7Be2kur3mPiKkojdT8VlSC1Ox0er8TxWOcSjRwV9dZRXdeOi%2BCWgZe2WmAkCpTPC45t8S5yWOhPDKSGaZ2fWSWs8ellhBFclg52u%2BaprSlHACWbUhUIrYAeUf%2FceChDjDkafvSiJM%2BwRzPq9a9eMyqEaKhrvREFUQblv1HlNr30IjijHcYicOvNPuj3pLWVKSsSxCrGXHwl1FRjXMjHld7jCBRM4O4BDtpBhwafeLUGullNVfZ4UqfK8QqYi9YvZvivztZ62XL0MBih4xOyEZu89prJygmTbDn1v4QZIoaKZkwyRcb%2BIaGo6Y74kZw07g8g8d1AZ0aXEmhJyUYzbK%2FMOTritMGOqUB%2FFhNK8koyyCvWW2Zcp18uI%2BP6F21hN4gWtNtespW4bvW10ZtCki%2BSds8KyBP89vZ6uUPwzTzTsPq7a7MpDWMHvrVjxStvlezeCv8ZFU3XywUr%2FekilgDD18Z6Xu3SY1T5eb%2BJcVCXftvAxi1BU%2BqIRyexeEey8XuPL06RZs473LXRvSFRtlG%2FcbxkINuKqDGrLVz%2Fl5PAjeDJlS41VKPHGcvi5Ck&X-Amz-Signature=e9da58d558b182e3c2c299830eb4463cb8bafb78fb7a52a6e7f73415df417fce&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
