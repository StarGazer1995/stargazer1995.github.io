---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667OUSDFWX%2F20260909%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260909T233752Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCdmzcubZZAatW1PcXM7UnqTtbeaBXX9B1mRws9RzNtYgIhAKxKo3Wan4J%2F2GwBPOeV4Ihya%2FBd0dVImlJ69sEIyEAtKv8DCHcQABoMNjM3NDIzMTgzODA1IgwkXML84%2BsGdBZR7isq3AP0Au9%2FEDDh6d5%2FCehMxzKU5tbkgvp%2BKlZCIY9YfKq7hFxMcL894fc5F1jOmF%2FpRrBnpHhWcciMBKRmXZIRkVqC%2Bo8TQmi6%2F5m3I5D4XerjPYDXJlZsVxj2vzdewMlHkXv%2B%2BE3aIJJ3q1FLljJQNdVahKg6nJ%2BkVvcIllDMxUjKNAobz%2FWqfbTt%2F9bgU3Wmyk%2BK8yMxFKWGSSgT909XNAzKqJaoPHSEWKusMTlevUVOraPi0KiP34S3n4CGTpaYUr38uxpRSMeWeTRe4hjnUo%2BRNqI4drWSSCfFdJPTEeHQ3A29jlH7%2BSlb3pnUU1KXrWMhXR1iY3Bfx46AxYzTwkRyVVICCdZj3BOmrOsMYUvoThh%2Fb4IBxqyTQnTZUb78rR8V%2FB71nGK89u2PiuxPjOt03vh72KSRyTjP3LCLfKAhFmvJsyzcuri2O6u0%2Fd4PmQXN%2FtBDDjCxq03qOAwJB36AynqmG4W3p4wm%2BexzbGw1OfUcY%2B%2FgdiN5kgEPMgDr4kipnGK2lHnN3d4K%2FyNhkl4GoJ6IESLzHPh3dveZmzsTcoN%2BhzpaSbnJuTzFgMW1qyKCmfaAabSBX2o9Ii8ce2CUBt%2FDeRwwdOUL%2BU479bwyAe99Ok1F5TG%2F5sQcKzDKsofVBjqkAQxLAAyQznZHsykK61QQnRr%2FCfeRgGHe7eP8G7y%2BW6jnSp52zpSLwa0uPuAZijdT2Cuyhic8UOTTmHdx08atXnfXCPctV0G6af%2BB3gANdM3iwjYPnS3KOEhX3KXwo4c7woJyY%2BYKp5y7ZBvjKDXxyu9%2FTPFPBycQ6DlbJVoc7%2FOXTY6JxpynGxJXoV3OpW%2BhP9EpjHbmO0uJuCCHkO9OvxEFIv2D&X-Amz-Signature=43bca5b1702dbe9839ab863c43e45d299e7c9b36227e064646b2db9debdc34a6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
