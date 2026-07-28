---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664STTMHKJ%2F20260728%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260728T172145Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICTwDkQfkR7xGh7yGir3iR6yIpxhKB6vrIHHixPYDcmPAiEAlnSAz7bjl7tJ7QirS7tDJYvRwCZwm1QA%2BB9QT%2F1ONBAq%2FwMIahAAGgw2Mzc0MjMxODM4MDUiDHq7%2FwS2wJOQQrh9oSrcA81eFgV4kIosLXhk%2Bnorz%2F6bLz%2BwPdFV208su3RT%2BnT1vT0NHd1t2Uk2lQQYSMLtZfw4fwMY9483QGVxN1s8f9otSPbGwcbbg%2B4QsCxHPEG7ColeFY6W1mcTyObtvDbVyd7ESfEnS2tY8FCmZuwO1qCEbG0CH0%2BOlApnE1BnyCDttWzmgg82%2F6S9Q8wB84kau2wRDLmaQ4Q8EhHqk8JJiOoIyijmBP7UtaKcEw3Hin5eKgkY8E%2B3M%2FCLVr5yxACNwplTTBbpNsdGANG%2FQH8wRbJKqid0ji8rSF7%2Fh2X4tCd5vCPnTNcQqw46Ol5nH5EzpHM%2FfgBDK856pU8Kwfhaf%2BtABiCp9lAb4%2FKyPGV5mS3O%2B6KH%2FlMlgw3hUqTXi33JpURCTA%2BBVDOtmhEXxpmbLa%2FW4ggOz4cEhcE%2BoBLqwgTr99NjGqDUt8XnuV847%2B8vfLON0jBJFp%2F9C1SgLHkEKqrfCu%2BrfJsdrloxRkl7touXUBrZopsQfXM1I95zz3vYpiXwBCVfaqF8XLCFHm%2B8OG0CtWJzG9fN1mPQxix%2BCynidAuYAqSUsR5YchC1AZnOFkX0bfIVZUVAX%2BtEb6V6OpYRLBrKaU8xIvRxVnozpM14YuUTAsSwmL3lnNuYMKi0o9MGOqUBHrHalKQSZt5hgJDmmBIha7uSNXzDzHKu06Bp5tZWLNV5XnZATmdWhPkZnja02%2FZSd4Qv2abuiRExhzZCFZkt28XZu0pgi42LN2c1u0l7aLROiJB%2BFsUNlmtfjpXQPmWfh5G%2Bi21%2BqZKWxcfSks5r%2F3oWPP4vqMv6nECHgya8JmYqD9ocCtolbEHG%2FVb216%2FBMjCE1A8e7yKP%2FK2KMIk3YQqFZruX&X-Amz-Signature=a3e9bf70b6ef7f2431ba523fc09878ea6977947549969c40e67cc2727b969786&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
