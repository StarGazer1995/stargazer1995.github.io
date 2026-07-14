---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VOINLMHR%2F20260714%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260714T111703Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEgaCXVzLXdlc3QtMiJHMEUCIF92%2Bw3nj%2B8LII9okpvEuJIUw1Fjb3tUUCerVUUDPRhQAiEA22w9kB6wXhinB5TS1jSHR%2BEvU%2BTsaUagYrnCTQU%2BGbAq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDGAyim9%2BQD6ZkwzowSrcA96yS%2FtB7OywczOoylzSGDdREHWsLqq1Kemiv%2BisvuA1SzogimSq4pEbFTARleaXZt%2B3NwfK68JdduyRDhILmb8HPgn%2FM2bK5eBOXfF7F4wnHhgTDS1KiusOZdstoQ98o87cndS0Cmq8ClV1pjtMYkVKOKSz%2B5bkE9qT3LxZtGSEkRJr6UJUZWUfBQ52329om0xqA2cyoeUyCsrOZGiLe95rvCR1Dc2fjQJelQHk%2Bt3eHGZnSRaSBh67rJkhf6frdaTr%2B%2FV6BdgBOHHba6M2AQVXwJLwfB8djrMOumwEUuDmJgLwiwZ%2Fdb4TW8skKjwQnXjV67SIDnjG6DTfdn5bq2Nb8NcWdaZc8w3%2FifzGp5QGApiBjjuI%2F%2Fb5jdHuGweSYyzcLdrRIqBCtOATV6ujPBkKgyf4HklgFsbbcu9FgnCXD%2FusvxTnLWyFFRDG2m8jFeJ2oxmz%2Bd%2BXdEYC7I0vPOhwh6C9aNSd5qGcj6cIvlqTQ8FW1Hv%2BnnAfpSs%2Fi6%2F2vB6fHrPqh4CFbCiuLRrlZW2Cy%2Bvyw3v8Jv9iKypr9sP%2F5uPENEFbRsP8gwzBQJgo1WDBIzvzJMIKnk5LJRl7CG0tbJyK6X6lVxHc0TLq9BjTJnC7Z7UpzkJvMm%2BAMNnN19IGOqUBXbsN1tyR3uVSYw196pdSW2Q7S8UkgFXjdNd7P7EtnAh74L6m5I7an1ozirNsgO9n9GcVAWIP89Sy%2Bgndywq%2B4MnfD6nbLQr6hX7QKVpN0WXV0iJDuALWLjROX0O9dksaVKjUBolewRUIdTMtvpH6%2BmWWyVimgFm7OrdYNb0RygAIeP3ZWie40eWVbLlcTo9guhi%2FlMkaZ5tB3a47YIWmS3L366Wd&X-Amz-Signature=3596d6b0f1127717ea62e2e8f726dcccf6bd8897f2e8771b3673c135185ba276&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
